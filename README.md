# KW Silicon City Assistant

A skills-only Agent Plugins 1.0 package for KW Silicon City real estate marketing.

## Everyday agent support with simple requests

The assistant also helps with property and market research, comparable analyses, neighborhood reports, client profiles, buyer/seller replies, follow-ups, lead organization, presentations, objection handling, personal branding, offer and contract summaries, transaction checklists, and an integrated weekly workflow. All 28 topics from the supplied task list are mapped in the skill's agent task playbook. Agents do not need a complex prompt.

Try: "Compare these homes", "Write a description for this listing", "Reply to this buyer", "Organize these leads", "Prepare my listing presentation", "Summarize this offer", or "Build a checklist for this escrow". Supply the relevant link, notes, or document; the assistant retrieves what it can and asks only for essential missing information.

These workflows provide evidence-based research and document support. Connected service access and artifact-generation capabilities depend on the host. The package does not itself provide an MLS feed, CRM integration, message delivery, professional appraisal, legal review, or accredited course certificate.

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

Version 0.2.1 adds role-aware roster resolution, an optional read-only Python/openpyxl helper, 16 synthetic regression tests, and channel-specific industry checks. Live checks on 2026-10-13 fetched the authoritative roster, matched six identity/ambiguity cases, retrieved and visually inspected an original agent headshot, and checked three agents plus the responsible brokerage against current California DRE records. Private roster records and portraits are not bundled.

Run the synthetic checks with `python tests/test_roster_resolution.py` in an environment with openpyxl. These tests validate the optional resolver, not autonomous behavior of every host/model. The skill remains instructions with host-dependent tools, not an independently deployed all-in-one app. Full GPT Image composition and a complete live campaign remain unverified until tested with a designated agent and authorized listing media. Do not represent the 28 task mappings as 28 end-to-end passed tests.
