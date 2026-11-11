# Project template

This template gives you one place to write down everything the rules ask you to record for a project: your intake answers, the rules that apply, your risks, your data, your plans and your release history.

## How to use it

1. Copy the template below into a new file in your project, for example `HUMANE.md`, or into your planning doc.
2. Fill in sections 1 to 4 before you start designing. They take about half an hour.
3. Fill in the rest as you build. You don't need everything on day one.
4. Keep it up to date. Come back to it before every release and whenever the product gets a big new feature.

Write "n/a" for anything that doesn't apply, so it's clear you checked rather than forgot.

## The template

```markdown
# Humane Dev Rules: [project name]

Owner: [name]
Started: [date]
Last reviewed: [date]

## 1. Intake questions (rule 1)

Answer yes or no. If you're not sure, say yes for now.

1. Does it collect or store personal data? yes / no
   - If yes, is any of it health, biometric or payment data? yes / no
2. Will people in the EU or UK use it? yes / no
3. Will people in the US use it? yes / no
4. Could children use it? yes / no
5. Does it use AI? yes / no
   - If yes, does the AI chat with users or write replies they read? yes / no
   - Does it have a human name, face or voice? yes / no
   - Does it make images, audio or video? yes / no
   - Can it take actions, like sending, buying or deleting? yes / no
   - Does it affect money, health, jobs or legal matters? yes / no
6. Does it take payments or subscriptions? yes / no
7. Can users post content, images or messages? yes / no
   - If yes, do you rank or recommend posts? yes / no
8. Does it use optional cookies, pixels or tracking? yes / no
   - If yes, do you sell or share data or run targeted ads? yes / no
9. Is it a mobile app or software people install? yes / no
10. Do users log in? yes / no

Also check:
- Does it send notifications? yes / no
- Does it play video or audio? yes / no
- Does it have a feed? yes / no
- Does it have rewards, points or badges? yes / no
- Can users invite other people? yes / no
- Will people use it regularly, like every day or every week? yes / no
- Does it show numbers or reviews, like stock levels or ratings? yes / no
- Is this a big launch? yes / no

## 2. Rules that apply

All "Always" rules, plus these "Only if" rules:

| Rule | What it means for this project |
|---|---|
| [number] | [for example: rule 31, payments go through Stripe Checkout] |

## 3. Consequence Scan (rule 2)

Date: [date]   Time spent: [minutes]   Who took part: [names]

| Who could be harmed | How | What we'll do about it |
|---|---|---|
| | | |
| | | |
| | | |

## 4. Threat model (rule 4)

| What an attacker might want | How they might try to get it | How we'll stop them |
|---|---|---|
| | | |
| | | |

## 5. Privacy risk assessment (rule 3)

Needed? yes / no
If yes, the main privacy risks and how we'll reduce them, or a link to the full assessment:

## 6. Data we collect (rules 12 and 14)

| Data | Why we need it | Where it's stored | Deleted after |
|---|---|---|---|
| | | | |

How people can see, download and delete their data: [link or steps]

## 7. Cookies and tracking (rules 15 to 20)

| Cookie or tag | What it does | Optional? | Waits for consent? |
|---|---|---|---|
| | | | |

- "Reject all" next to "Accept all", looking the same: yes / no / n/a
- Cookie settings link in the footer: yes / no / n/a
- "Do Not Sell or Share" link and GPC respected (US): yes / no / n/a
- Last cookie check: [date]   Next one due: [date]

## 8. Security basics (rules 21 to 31)

- Security level we're aiming for: ASVS level 1 / level 2, plus MASVS for mobile apps (rule 22)
- Accounts protected with passkeys or security keys: [code hosting, cloud, domain, package accounts] (rule 24)
- Where secrets are kept: [secrets manager] (rule 25)
- Automatic scans set up for code, packages, secrets and settings: yes / no (rule 32)
- Who approves releases to production: [name] (rule 30)

## 9. Wellbeing measure (rules 5 and 52)

- What we measure: [for example: bookings completed without needing to call]
- How we measure it: [where the number comes from]
- What good looks like: [target]
- Checked every month by: [name]

## 10. AI (rules 36a to 42), if the product uses AI

- How AI is labelled: [description] (rules 36a, 36b and 37)
- What the AI can and can't do on its own: [list] (rule 39)
- Who checks AI decisions about money, health, jobs or legal matters: [name or n/a] (rule 40)
- Red-team test done: [date and short result] (rule 42)

## 11. Pages to publish (rules 45 to 47)

- Accessibility statement: [link]
- Privacy notice: [link or n/a]
- Cookie policy: [link or n/a]
- Terms that explain how to cancel: [link or n/a]
- security.txt and how to report security problems: [link]
- Security updates provided until: [date or n/a]

## 12. People and plans (rules 50 and 51)

- Who handles security incidents: [name and contact]
- Incident plan: [link]
- Data breach plan: [link or n/a]
- Who answers people's data requests: [name] (reply within a month)
- Who handles takedown reports: [name or n/a]

## 13. After-launch calendar (rules 49, 52 and 53)

| How often | What | Who | Next date |
|---|---|---|---|
| Every month | Check the wellbeing measure | | |
| Every three months | Remove old accounts and keys; cookie check | | |
| Every year | Update risks and threat model, practise the incident plan, check for new laws | | |
| When a security problem is found | Fix it in time: 72 hours if attacked, 7 days critical, 30 days high, 90 days medium | | |

## 14. Releases (rule 48)

| Version | Date | Checklist saved at | Signed off by | Second check |
|---|---|---|---|---|
| | | | | |

## 15. Exceptions and decisions (rule 35)

Anything you decided not to do, or to do differently, and why.

| Rule | What we decided | Why | Review or expiry date |
|---|---|---|---|
| | | | |
```
