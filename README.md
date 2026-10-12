# KW Silicon City Marketing Agent

A skills-only Agent Plugins 1.0 package for KW Silicon City real estate marketing.

## What it does

- Looks up the user-designated KWSC host or promoting agent in the current Drive roster.
- Completes available roster, headshot, listing-photo, and current price/status verification steps before asking the user; it does not stop at a preliminary prerequisite checklist.
- When listing data is stale or dated, searches current authoritative sources by MLS number and address and resolves freshness before drafting distribution-ready copy.
- Retrieves that agent's original headshot and branding from the connected Drive library.
- Stops and asks the user when the original headshot cannot be confidently found or verified; it never substitutes initials, a monogram, avatar, silhouette, or generated portrait.
- Extracts public property details and listing attribution from a supplied listing URL.
- Requires at least one visually verified original listing photo and stops to ask when it cannot obtain one; it never generates, reconstructs, illustrates, or stock-substitutes the property.
- Sends the complete verified source packet—listing photos, headshot, logo, facts, attribution, and copy—to GPT Image to generate the entire finished design.
- Starts every marketing piece with a verified attention headline, then uses a short body, 3–5 scannable feature bullets, and a calm buyer-focused call to action instead of a dense paragraph.
- Makes the property the visual hero with the strongest real listing photo and additional useful property photos when available; keeps the agent portrait and contact block smaller and secondary.
- For a full campaign, produces six coordinated but distinct core deliverables: an announcement post, primary open-house or listing flyer, property-features carousel, property spotlight post, vertical story, and reminder or private-tour post.
- Supports requested campaign add-ons such as email, postcard, brochure, door hanger, feature sheet, extra carousel or story cards, reel/video scripts and covers, paid-ad variations, signs, QR handouts, landing-page copy, follow-up messages, and verified bilingual versions.
- Labels every individual square-foot measurement with an adjacent "Approx." qualifier in visuals and accompanying copy.
- Requires GPT Image to integrate the verified original headshot and preserve the agent's identity and appearance.
- Includes the brokerage logo and accurate Listed by credit for another agent's listing.
- Makes all design corrections through GPT Image; it never repairs or rebuilds the flyer with HTML, CSS, SVG, canvas, scripts, or code-based compositing.

## Example request

Use $kw-silicon-city-plugins to create an open-house flyer.

Listing URL: [public MLS/listing URL]

Hosting agent: [full KWSC agent name]

Open house: [date and time]

Generate the design with GPT Image, use the original Drive headshot without changing the face, include the KW Silicon City logo, and credit the actual listing agent.

## Required connections

The host must provide GPT Image generation with visual-reference inputs, authorized Google Drive access to the roster and headshot library, and listing-page access. This package provides instructions and assets; it does not deploy an MLS scraper, image service, or MCP server.

Drive URLs are references, not access grants. Each user needs the appropriate Drive permissions. Private agent records and portraits are not bundled in this repository. Do not commit credentials or downloaded roster/headshot files.

## Package layout

The root plugin.json is the portable manifest. The reusable skill, references, and supplied brokerage logo are under skills/kw-silicon-city-plugins/.

For later plugin import, use a ZIP containing the single kw-silicon-city-plugins directory. GitHub storage alone does not install the plugin or connect its required services. Import/install it through the plugin workflow supported by your host.

## Verification status

The skill structure, package manifest, referenced resources, and complete-generation rules were checked locally. End-to-end generation with a live listing remains to be tested in a connected host.
