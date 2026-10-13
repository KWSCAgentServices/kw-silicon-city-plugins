# Keller Williams design and GPT Image

Research checked October 8, 2026. These public sources establish palette and resource access; they do not establish every current typography, logo-size, or local Market Center rule.

## Official sources and template priority

- [KW standard color palette](https://answers.kw.com/hc/en-us/articles/360011998334-What-are-the-standard-color-codes-for-KW-red-and-the-KW-color-palette): digital KW Red #CE011F, Main Gray #828282, Light Gray #CCCCCC, Medium Gray #4D4D4D, Black #000000. For print, KW identifies Pantone 200 / CMYK 0,100,66,13 for red and Pantone 424 / CMYK 0,0,0,60 for Main Gray. Apply these to surrounding design elements; preserve the supplied logo pixels.
- [KW Identity & Style Guide access](https://answers.kw.com/hc/en-us/articles/360012098693-Access-the-KW-Identity-Style-Guide): the current guide is accessed through authenticated KW Connect, New Associates Essentials, Logos and Branding. An older public PDF link returned 404 during research; do not claim its contents were verified.
- [KW Brand Templates in Canva](https://answers.kw.com/hc/en-us/articles/44040516783251-Access-KW-Brand-Templates-in-Canva): current KW templates are available through Canva.kw.com, Brand, All Brand Templates. They include postcard and social formats and still require appropriate local/MLS adaptations and asset rights.

Prefer a user-supplied approved KW template or one accessible through the user's authenticated KW Canva account. Inspect the actual template before following its layout, typography, and proportions. Use it as a design reference for GPT Image; do not replace the requested image-generation workflow with Canva authoring.

If no approved template is accessible, use the verified palette plus the recommendations below and describe the result as KW-aligned, not an official KW-approved template or a fully certified brand-compliant design. Do not invent official font names or numeric logo clear-space rules. If the user later supplies the current guide, apply its actual requirements.

## Recommended layout defaults

These are design recommendations, not quoted KW requirements:

- Make the property the unmistakable visual hero. Use the strongest verified listing photo as the largest focal point and include additional useful property photos when the format and available sources allow. Do not let the agent portrait, name, or branding dominate.
- Establish a clear hierarchy: verified attention headline, property imagery, address and event/price information, 3–5 concise feature bullets, calm call to action, then a smaller supporting agent/contact block and listing attribution.
- Follow an accessible approved template's fonts when known. Otherwise use a high-impact, readable editorial headline with clean supporting typography; a warm serif headline is welcome for the user's preferred home-first direction.
- Reserve distinct areas for the KWSC host's smaller portrait/contact block, complete brokerage logo, and readable listing-agent credit. The agent must remain noticeable but secondary to the property.
- For an open house, make the event date/time prominent and label the host explicitly. For another agent's listing, do not imply ownership through headlines or logo placement.
- Adapt each requested size deliberately; keep credit and branding inside the visible safe area rather than relying on automatic crops.

## Required image generation

Generate the entire finished marketing design with the built-in GPT Image workflow. The image model—not HTML, CSS, SVG, canvas, scripts, programmatic drawing, or a later compositing step—must perform the layout, typography treatment, photo integration, portrait placement, logo placement, and overall visual polish.

Do not generate an empty template for later assembly. Do not add the property photo, agent headshot, logo, text, boxes, or corrections afterward with code or non-generative design tools. Non-generative utilities may only inspect source files or perform a final format conversion or proportional export that does not rebuild or alter the design.

Use the strongest GPT Image model exposed by the host. If the host does not disclose an exact backend version, describe it simply as built-in GPT Image and proceed. For an explicitly selected API/CLI workflow with configured credentials, use a supported GPT Image model such as gpt-image-2.5-sunburst; do not invent model names or start API work merely to update this skill.

## Complete source packet gate

Before invoking GPT Image, finish collecting and verifying all inputs:

- original listing photos that are visually confirmed to belong to the supplied listing;
- the matched KWSC agent's original Drive headshot, unless the user explicitly authorized a no-portrait draft after disclosure;
- the complete supplied KW Silicon City logo and any verified agent/team branding;
- exact address, price, status, beds, baths, property type, MLS number, and selected public features, with every square-foot value individually formatted as "Approx. [number] sq. ft.";
- exact event date and time;
- exact KWSC host/promoter name, role, phone, email, website, and license details needed for the piece;
- exact listing-agent name(s), listing brokerage, and the required "Listed by" line;
- required disclosures, intended dimensions, platform, and approved template or style reference.
- finalized property-first copy: one verified attention headline, at most one brief hook, 3–5 short feature bullets, and a calm buyer-focused call to action. Reject dense paragraphs and one-sentence fact dumps before generation.

If any required source is unavailable, ambiguous, or unverified, stop and ask the user. Do not send an incomplete packet and ask GPT Image to fill gaps.

Apply the [status-specific price and date rules](property-first-copy-and-layout.md#status-specific-price-and-date-rules) before generation. Keep verified source values internally, but send only approved display fields as final copy: no price for In Contract, and no dates for Just Listed or Just Closed unless explicitly requested. An intentionally omitted price or date is not a missing prerequisite and must not trigger a follow-up question.

## Generate the complete design

Attach the verified listing photos, original headshot, complete logo, and any approved template directly to the GPT Image request as clearly labeled visual inputs. Include the verified source record and exact final copy in the same request. Ask GPT Image to create one complete, polished, publication-ready KW-aligned composition using those supplied assets.

The prompt must explicitly require:

- use the supplied listing photos as the actual property imagery; do not synthesize a house from the address or description;
- make the property the star of the composition, with the strongest real listing photo as the largest visual and additional useful real property photos when the format and verified source set allow;
- keep the agent portrait, name, and contact block smaller and visually secondary while still noticeable and readable;
- make the phone number slightly larger than the surrounding contact text (roughly 10–20% larger than email, website, role, and license text), with clear contrast and spacing so it stands out within the compact contact block;
- use the supplied agent headshot for the named host/promoter and preserve identity, facial features, age, expression, skin tone, hair, and overall appearance;
- use the complete supplied brokerage logo without redrawing, cropping, recoloring, stretching, rearranging, or replacing it;
- reproduce the exact verified names, roles, contact details, license number, address, permitted price and requested event details, property facts, listing attribution, and disclosures from approved display copy; never restore amounts or dates omitted under the status-specific rules;
- put "Approx." directly with every individual square-foot measurement, including living area, lot size, rooms, garages, ADUs, patios, and parcels; never rely only on a general disclaimer;
- keep "Hosted by" or "Presented by" separate from "Listed by";
- open with the supplied verified attention headline; keep the body short, use the supplied 3–5 feature bullets, and use a calm value-first call to action. Do not turn the copy into a paragraph, data dump, hype, or pushy sales language;
- use the requested dimensions, safe margins, hierarchy, KW palette, and approved template guidance;
- do not add invented features, people, houses, rooms, logos, initials badges, placeholders, or unverified text.

Provide the most useful real listing photos rather than flooding the model with near-duplicates. Label every input so the property photos, agent headshot, brokerage logo, listing agent, and host/promoter cannot be confused.

## Correct through GPT Image only

Inspect the complete generated result at full size. Compare the property, face, logo, and every material text field against the source packet. Search the visual and accompanying copy for every square-foot value and confirm each one has an adjacent "Approx." qualifier.

If anything is wrong—including a missing or weak headline, dense body copy, facts collapsed into a paragraph, too few useful property photos, or an agent block that competes with the property—send the generated draft back through GPT Image together with the original source assets and focused correction instructions. Reattach the originals on every correction pass so the model does not drift. Corrections must remain inside GPT Image; never patch text, replace photos, insert the headshot, rebuild the logo, or repair the layout with HTML, CSS, SVG, canvas, scripts, or code-based compositing.

Use a small number of focused correction attempts. If GPT Image still cannot preserve the correct property, agent identity, logo, required facts, or an "Approx." qualifier on every square-foot value, stop and tell the user what remains wrong rather than delivering or claiming a publication-ready flyer.

## Original-face release gate

The user's instruction is absolute: never change an agent's face. Treat the verified headshot as an original photographic insert, not inspiration for a generated person. Only proportional scaling and a clean crop are allowed; never crop away identity-critical facial details. Keep the original face, facial proportions, eyes, nose, mouth, teeth, expression, skin texture and tone, age, hairline and hair unchanged. No reconstruction, beautification, smoothing, relighting, expression changes, face swap or approximate likeness. A recognizable person is not enough.

Include this exact constraint in every complete-design and correction prompt: "Place the supplied original headshot as an unchanged photograph. Do not generate, redraw, retouch or modify the face. Crop and scale proportionally only. If exact preservation is not possible, do not substitute a similar face."

Reattach the original headshot on every attempt; never reuse a portrait extracted from a generated flyer. Inspect source and output side by side, with the face enlarged enough to compare individual features, not only as a tiny footer thumbnail. Record pass, fail or unverifiable for the portrait, property, logo and material copy. Any visible facial change is a failure, even when the person remains recognizable. If the portrait is too small to assess or preservation is uncertain, mark it unverifiable, not passed. Do not use face-recognition similarity or layout approval as evidence that the face is unchanged.

Make at most two focused correction attempts through GPT Image with the original assets. If face preservation still fails or cannot be verified, stop the affected visual and report the limitation in one consolidated message; do not call it ready to use or hide the problem behind a design-proof label. Ask for direction only when needed to change workflow or obtain explicit no-portrait authorization. Never bypass the user's complete-GPT-Image workflow with HTML or code compositing. Instructions cannot guarantee pixel-preserving insertion by a generative model; do not promise an absolute technical guarantee that has not been demonstrated.

Approval of a layout approves only its design direction, not a changed face, altered property, logo redraw, missing CTA or other failed release check. Do not bundle private portraits or listing photos into the reusable skill, plugin or GitHub repository.

## Property and portrait fidelity

The supplied listing photos are the only acceptable property references. The finished design may crop or scale them for layout, but it must not show a different property, reconstructed exterior or room, stock home, image from another listing, virtual staging, generated landscaping, or an artist's illustration.

The supplied headshot is the only acceptable portrait source. Do not request or accept a generated replacement, face swap, beauty retouch, altered age, altered expression, altered hair, initials badge, monogram, silhouette, generic avatar, or stock portrait. The face must remain unchanged from the verified original; mere recognizability is not sufficient. Apply the original-face release gate above.

A result that merely resembles the address or agent is not sufficient. Verify against the actual inputs, not plausibility. When fidelity fails, correct through GPT Image with the originals attached again.
