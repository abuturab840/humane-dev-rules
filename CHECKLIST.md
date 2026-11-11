# Release checklist

Go through this list before every release (rule 48 in the [rules](RULES.md)).

1. Copy the list into your release notes, pull request or a note you keep with the release.
2. Tick each item that's done.
3. Write "n/a" next to anything that doesn't apply to your project, for example the AI items on a site with no AI.
4. If an item applies and isn't done, fix it before you ship. If you really can't, write down why and the date you'll fix it by (rule 35).

Working alone? Run it again the next day with fresh eyes before a big launch.

## Humane

- [ ] A Consequence Scan is done, and the biggest risks are dealt with.
- [ ] Success is measured by how much the product helps people, not by time spent.
- [ ] Non-essential notifications are off by default, nothing plays automatically, and feeds have stopping points.
- [ ] The product passes the Manipulation Matrix and the regret test.
- [ ] Where they apply: rewards are earned and predictable, people choose who to invite, users have controls like quiet hours, and every number and review shown is real.

## Private

- [ ] Only the data you need is collected, and each type has a delete date.
- [ ] The cookie check is clean. "Reject all" works and looks the same as "Accept all". The browser's "don't sell my data" signal (GPC) is respected where the law requires it.
- [ ] People can see, download and delete their data.
- [ ] A privacy notice and a cookie policy are published.

## Secure

- [ ] The right OWASP security level is met (ASVS, or MASVS for mobile apps), with no known critical or high problems left.
- [ ] The automatic scans have passed: code, packages, secrets and settings.
- [ ] Access has been tested for every type of user.
- [ ] The release has a list of what's inside it (SBOM) and a digital signature.
- [ ] security.txt is live, and the incident and data breach plans are ready.
- [ ] For a big launch, a penetration test is done.

## Fair and accessible

- [ ] There are no dark patterns. Cancelling and deleting are as easy as signing up.
- [ ] The WCAG 2.2 AA accessibility check has passed, including tests with a keyboard and a screen reader.
- [ ] If children might use it, the safest settings are on by default.

## Accountable

- [ ] AI is labelled where rules 36a and 36b apply, and images, audio and video made by AI are labelled.
- [ ] The AI security checks (OWASP LLM Top 10) and red-teaming have passed.
- [ ] A person checks AI decisions about money, health, jobs or legal matters.
- [ ] There's a working way for people to report illegal content and ask for takedowns.
- [ ] You've said how long you'll provide security updates.
- [ ] The person doing the release has signed it off (plus a second reviewer for big launches), and the result is saved with the release.
