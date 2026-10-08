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

- Use a strong property-photo focal point, ample white space, and restrained red accents.
- Establish a clear hierarchy: event/promotion heading, address, date/time or price, concise verified facts, then agent contact and attribution.
- Use readable sans-serif typography; follow the supplied approved template's fonts when known.
- Reserve distinct areas for the KWSC host's portrait/contact block, complete brokerage logo, and readable listing-agent credit.
- For an open house, make the event date/time prominent and label the host explicitly. For another agent's listing, do not imply ownership through headlines or logo placement.
- Adapt each requested size deliberately; keep credit and branding inside the visible safe area rather than relying on automatic crops.

## Required image generation

Generate every visual marketing design with the built-in GPT Image tool using the installed imagegen workflow. The user's clarified requirement is GPT Image generation, not proof of a particular backend version. If the tool does not expose its exact version, proceed normally; do not stop, request version confirmation, or fall back to HTML/CSS. Describe the workflow as GPT Image generation without asserting an unverified model version.

Do not use HTML/CSS, SVG, canvas, or programmatically drawn shapes and text to create the marketing layout in place of GPT Image. Non-generative tools may only assemble the generated design with original protected assets, resize/export it, or package it into a PDF. They must not redesign the generated composition. Deliver the actual generated marketing image, not merely an HTML preview or a promise to generate later.

For an explicitly selected API/CLI workflow with configured credentials, use an actual supported GPT Image 2.5 model. [OpenAI's Sunburst documentation](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) identifies `gpt-image-2.5-sunburst` for precise image generation/editing. Do not call an invented `gpt-images-2.5` alias or run live API work merely to update this skill.

Provide the source listing photos, complete supplied logo, and accessible KW template as labeled inputs. Inspect local inputs first. Reserve an empty portrait area for the matched host's original Drive headshot. Do not generate the agent's face as part of the design. Prompt with:

- intended format and dimensions;
- template-derived composition or recommended KW-aligned layout;
- exact verified property and event copy;
- exact KWSC host/promoter name, role, contact details, and license details when needed;
- exact "Listed by [verified name(s)]" line and actual listing brokerage when sourced;
- photo and logo preservation instructions, plus an empty portrait area for later placement of the original headshot;
- legible attribution and required branding on every independent output.

Do not ask the model to reconstruct the logo or invent a property photo. Image generation is for composing the marketing design while preserving supplied subjects and assets.

## Mandatory preservation of the agent's face

Use the exact matched headshot from the authorized Drive library as a separate image layer in the final artifact. GPT Image generates the surrounding design; the original portrait is inserted afterward with a non-generative layout/compositing operation. This assembly step is required to preserve the face and does not replace the requested GPT Image design generation.

Never synthesize, redraw, swap, beautify, smooth skin, change facial features, expression, age, hair, makeup, skin tone, lighting, or pose. Do not use AI upscaling or enhancement on the face. Allow proportional scaling and an ordinary rectangular or circular frame only when it leaves the face intact. Preserve the original image file.

After inserting the original headshot, do not pass the flattened result through image generation for further edits. Edit the surrounding design separately and reinsert the original portrait. If original-image placement is unavailable, deliver a clearly labeled draft with the portrait area empty and explain the limitation; do not substitute a generated face.

## Verify generated outputs

Compare rendered names, phone, email, address, price, dates, license numbers, listing-agent credit, logo, portrait, and property photos against the source record. Regenerate or edit the surrounding design with GPT Image and inspect again, then reinsert the unchanged headshot. An attractive result with a wrong host, omitted listing credit, altered logo, or invented property feature is not ready to deliver. If exact preservation cannot be achieved, report the unresolved issue instead of claiming it passed.

Verify portrait provenance by the selected Drive file and original-image layer, not by a claim that a generated face looks similar. Compare the placed portrait with the original to catch distortion, unwanted cropping, or edits. Correct portrait errors by reinserting the original file, never by regeneration.
