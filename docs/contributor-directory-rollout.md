# Contributor Directory rollout

Beta-tester acknowledgements were added separately from catalogue submission
credits at Scott Jarmusch's explicit request on 11 September 2026: Daniel Otto
and Morgane Mauduit, with the ORCID identifiers supplied by the maintainer.
These acknowledgements do not create fictitious Tool submissions or consent
records. Removal requests use the same Privacy contact form.

The contribution landing pages now credit only published catalogue records with
`provenance.public_attribution_consent: true`. Existing names and ORCIDs are not
backfilled into the directory. Credits are deduplicated by ORCID, then normalized
name, with ambiguous shared names kept separate when they have different ORCIDs.

Both new-entry forms collect a required name, optional ORCID and a separate
required public-attribution consent checkbox. Both issue converters enforce this
consent before creating a draft. The optional boolean schema field defaults to
false, so older catalogue records remain valid.

The Privacy page identifies Scott Jarmusch as controller/contact and uses the
maintainer-supplied Formspree endpoint. The recipient address is managed only in
Formspree; it is not embedded in site assets or repository configuration.
Ordinary public enquiries still use GitHub issues. Private requests do not.

## Handling withdrawal

On a valid withdrawal request, set consent to false for all affected records and
remove the name and ORCID as appropriate. Rebuild and check both contribution
routes. Review any public provenance exports and repository history separately;
changing the directory alone does not erase GitHub issues or old commits. Never
copy the private request into a public issue or commit message.

## Validation

- Strict static build, schema validation and submission-vocabulary sync.
- Contributor consent, identity, ORCID, escaping, schema compatibility, routes,
  sitemap, footer and privacy form regression tests.
- Existing editorial, terminology, branding, catalogue and local-link checks.
- Browser QA at 375, 768 and 1440 px; required fields and form POST checked using
  a locally intercepted request. No live form message was sent.

## Next

Confirm a real request arrives in the configured inbox and review spam controls
in Formspree. Resume the specialist Tool population checkpoint, then review
relationships before implementing Ask Navigator recommendations.
