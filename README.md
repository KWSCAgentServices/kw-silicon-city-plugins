# KW Silicon City Plugins

A skills-only Agent Plugins 1.0 package for KW Silicon City real estate marketing.

## What it does

- Looks up the user-designated KWSC host or promoting agent in the current Drive roster.
- Retrieves that agent's original headshot and branding from the connected Drive library.
- Extracts public property details and listing attribution from a supplied listing URL.
- Generates the visual marketing design with GPT Image.
- Places the original headshot unchanged in the finished layout.
- Includes the brokerage logo and accurate Listed by credit for another agent's listing.

## Example request

Use $kw-silicon-city-plugins to create an open-house flyer.

Listing URL: [public MLS/listing URL]

Hosting agent: [full KWSC agent name]

Open house: [date and time]

Generate the design with GPT Image, use the original Drive headshot without changing the face, include the KW Silicon City logo, and credit the actual listing agent.

## Required connections

The host must provide GPT Image generation, authorized Google Drive access to the roster and headshot library, listing-page access, and original-image compositing/export capability. This package provides instructions and assets; it does not deploy an MLS scraper, image service, or MCP server.

Drive URLs are references, not access grants. Each user needs the appropriate Drive permissions. Private agent records and portraits are not bundled in this repository. Do not commit credentials or downloaded roster/headshot files.

## Package layout

The root plugin.json is the portable manifest. The reusable skill, references, and supplied brokerage logo are under skills/kw-silicon-city-plugins/.

For later plugin import, use a ZIP containing the single kw-silicon-city-plugins directory. GitHub storage alone does not install the plugin or connect its required services. Import/install it through the plugin workflow supported by your host.

## Verification status

The skill passed its structural validator. The package manifest and referenced resources were checked locally. End-to-end generation with a live listing remains to be tested in a connected host.
