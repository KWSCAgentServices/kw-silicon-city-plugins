"""Read-only roster lookup. Requires openpyxl; never executes workbook macros."""
import argparse
import json
import re
import unicodedata

# Internal verification metadata is never part of the public contact projection.
INTERNAL_FIELDS = ('name', 'email', 'phone', 'license', 'expiration', 'role', 'category', 'sheet', 'row')
PUBLIC_FIELDS = ('name', 'email', 'phone', 'license')


def public_contact_result(result):
    """Project a lookup result onto contact-only fields; never return raw records."""
    output = {'status': result['status']}
    if result['status'] == 'matched':
        output['record'] = {key: result['record'][key] for key in PUBLIC_FIELDS
                            if result['record'].get(key) is not None}
    elif 'candidates' in result:
        output['candidates'] = [{'name': item['name']} for item in result['candidates']]
    return output


def normalize(value):
    text = unicodedata.normalize('NFKD', str(value or '')).casefold()
    return ' '.join(re.sub(r'[^a-z0-9]+', ' ', text).split())


def digits(value):
    return re.sub(r'\D', '', str(value or ''))


def rows_from_workbook(path):
    import openpyxl
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    result = []
    try:
        for sheet in workbook:
            iterator = sheet.iter_rows(values_only=True)
            headers = [normalize(v) for v in next(iterator, [])]
            def get(row, *names):
                for name in names:
                    if name in headers:
                        index = headers.index(name)
                        value = row[index] if index < len(row) else None
                        if value is not None and str(value).strip().upper() not in ('NONE', 'N/A'):
                            return str(value).strip()
                return None
            sheet_key = normalize(sheet.title)
            category = ('former' if any(s in sheet_key for s in ('left', 'inactive', 'former')) else
                        'staff' if 'staff' in sheet_key else
                        'other' if any(s in sheet_key for s in ('assistant', 'mortgage')) else
                        'agent_candidate' if any(s in sheet_key for s in ('roster', 'agent')) else 'unknown')
            for number, row in enumerate(iterator, 2):
                first, last = get(row, 'first name'), get(row, 'last name')
                full = get(row, 'full name', 'display name', 'name', 'agent name', 'associate name')
                if not full and not first and not last:
                    continue
                combined = ' '.join(v for v in (first, last) if v)
                result.append({'name': full or combined, 'aliases': list(set(v for v in (full, combined) if v)),
                               'email': get(row, 'kw email', 'email'),
                               'phone': get(row, 'phone', 'phone number'),
                               'license': get(row, 'dre', 'dre number', 'license number'),
                               'expiration': get(row, 'dre expiration', 'expiration'),
                               'role': get(row, 'title', 'role'), 'category': category,
                               'sheet': sheet.title, 'row': number})
    finally:
        workbook.close()
    return result


def resolve(records, query):
    query = str(query).strip()
    key = normalize(query)
    numeric = digits(query)
    if '@' in query:
        matches = [r for r in records if (r.get('email') or '').casefold() == query.casefold()]
        evidence = 'exact email'
    elif len(numeric) == 8 and re.fullmatch(r'[\d\s-]+', query):
        matches = [r for r in records if digits(r.get('license')) and
                   digits(r.get('license')).zfill(8) == numeric and numeric != '00000000']
        evidence = 'exact DRE'
    elif len(numeric) in (10, 11) and re.fullmatch(r'[\d\s()+.-]+', query):
        matches = [r for r in records if digits(r.get('phone'))[-10:] == numeric[-10:]]
        evidence = 'exact phone'
    else:
        matches = [r for r in records if any(normalize(v) == key for v in r.get('aliases', [r['name']]))]
        evidence = 'exact normalized name'
        if not matches:
            matches = [r for r in records if any(key and key in normalize(v).split() for v in r.get('aliases', [r['name']]))]
            # Partial names can suggest candidates but never establish identity.
            return {'status': 'needs_identifier' if matches else 'not_found', 'candidates':
                    [{'name': r['name'], 'category': r['category']} for r in matches]}
    if len(matches) != 1:
        return {'status': 'ambiguous' if matches else 'not_found', 'candidates':
                [{'name': r['name'], 'category': r['category']} for r in matches]}
    record = {key: matches[0][key] for key in INTERNAL_FIELDS if key in matches[0]}
    return {'status': 'matched', 'evidence': evidence, 'record': record,
            'eligibility': 'verify_license_and_affiliation' if record['category'] == 'agent_candidate'
            else 'not_established_as_current_agent'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('workbook')
    parser.add_argument('query')
    parser.add_argument('--public', action='store_true', help='Return only identifying name, business contacts and DRE.')
    args = parser.parse_args()
    result = resolve(rows_from_workbook(args.workbook), args.query)
    print(json.dumps(public_contact_result(result) if args.public else result, ensure_ascii=False))
