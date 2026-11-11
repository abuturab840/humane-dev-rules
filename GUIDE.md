# How to use these rules

This page is for anyone building a website, app or piece of software, with or without AI. You don't need to know the standards behind the rules. If a word is new to you, look it up in the [glossary](GLOSSARY.md).

The short version: answer ten questions, write down which rules apply, keep them in mind while you build, and run the checklist before you release.

## Step 1: Answer the intake questions

Open the [intake questions](INTAKE.md) and answer each one with yes or no. They ask things like "Do we collect personal data?" and "Could children use it?"

Every rule is marked "Always" or "Only if". The "Always" rules apply to every project. Your yes answers switch on the "Only if" rules. That way a small site doesn't have to follow the rules meant for AI chatbots or children's apps.

If you're not sure about an answer, say yes. You can drop the extra rules later.

## Step 2: Write down your list

Write your answers down somewhere you'll see them. The [project template](TEMPLATE.md) has a place for everything the rules ask you to record:

- your intake answers and the rules that apply
- your Consequence Scan, threat model and wellbeing measure
- the data you collect and when it's deleted
- your cookies, security set-up and the pages you need to publish
- who handles incidents and data requests
- an after-launch calendar, a release log and any exceptions

Copy it into a file in your project, such as `HUMANE.md`, or into your planning doc. Fill in the first four sections before you design anything, and the rest as you build.

## Step 3: Do the start-of-project rules

Section A of the rules happens before you design anything. None of it needs special tools.

- **Consequence Scan (rule 2).** Sit down for 15 minutes and ask: who could this product hurt, and how? Think about misuse, mistakes, people left out, and what happens if it's very popular. Write down the top three risks and what you'll do about each one.
- **Threat model (rule 4).** Ask: what would an attacker want from this, and how would they try to get it? Customer details, admin access, free use of your servers? Write down how you'll stop each one.
- **Wellbeing measure (rule 5).** Pick one number that shows the product is actually helping people. For a booking site it might be "bookings completed without needing to call us". Never use time spent as your goal.

## Step 4: Build with the rules open

Keep the rules next to you while you work and check the right section when you get to it:

- Designing screens, sign-up or cancel flows? Section B (humane design) and J (healthy engagement).
- Adding a form, analytics or a cookie banner? Section C (privacy and cookies).
- Setting up hosting, logins or plugins? Section D (security).
- Adding AI? Section F.

You don't need paid tools for most of it. Some free ones that help:

- **Accessibility:** try using your site with only the keyboard, then with a screen reader (VoiceOver on Mac and iPhone, NVDA on Windows). The WAVE and axe browser extensions catch common problems.
- **Security:** turn on GitHub's Dependabot and secret scanning, run Semgrep on your code, and check your live site with ZAP, securityheaders.com and SSL Labs.
- **Cookies:** open your browser's developer tools and look at what loads before anyone clicks "Accept". Nothing optional should.

On WordPress, every plugin counts as a dependency (rule 28). Fewer, well-maintained plugins are safer.

## Step 5: Run the checklist before every release

Copy the [release checklist](CHECKLIST.md) into your release notes or pull request. Tick what's done, write "n/a" next to what doesn't apply, and fix anything that's left before you ship.

If something can't be fixed in time, rule 35 says to write down why and the date it will be fixed by. A serious security problem (critical or high) should never ship.

## Step 6: Keep going after launch

Section I covers life after launch. Put these in your calendar so you don't forget:

- **Every month:** check your wellbeing measure (rule 52).
- **Every quarter:** remove old accounts and keys (rule 53) and, if you use optional cookies, run a cookie scan (rule 20).
- **Every year:** refresh your risk notes and threat model, and check if any laws have changed (rule 53).

## An example: a small booking site

Say you're building a booking site for a hair salon in the UK. Customers book online and pay a deposit. Staff log in to see the bookings.

The intake answers:

| # | Question | Answer |
|---|---|---|
| 1 | Personal data? | Yes: names, phone numbers, emails |
| 2 | EU or UK users? | Yes |
| 3 | US users? | No |
| 4 | Children? | No |
| 5 | AI? | No |
| 6 | Payments? | Yes: deposits through a payment provider |
| 7 | User posts? | No |
| 8 | Optional cookies or tracking? | Yes: the owner wants Google Analytics |
| 9 | Mobile app? | No |
| 10 | Users log in? | Yes: staff only |

So on top of the "Always" rules, the salon site also follows the extra points for personal data, UK visitors with cookies, payments and logins. If it shows customer reviews, rule 60 applies too.

What that means in practice:

- **Payments go through Stripe Checkout or similar**, so the site never sees card numbers (rule 31).
- **Old bookings are deleted after 12 months**, and customers can ask for their data or ask for it to be deleted (rules 12 and 14).
- **Analytics don't load until the visitor clicks "Accept"**, and "Reject all" sits right next to it, the same size (rules 15 and 16). Or the owner could switch to a cookie-free counter and skip the banner completely.
- **Cancelling a booking is as easy as making one** (rule 9). No phone call needed.
- **Staff accounts can only see what they need**, and the server checks it on every request (rule 23).
- **Appointment reminders are fine**, because they're essential. Marketing messages stay off unless the customer turns them on (rule 6).

## If you work alone

Most of this was written with small teams and solo developers in mind. A few tips:

- Start with the "Always" rules and the checklist. That covers most of the risk.
- Where a rule asks for a second person (rule 48), check it yourself the next day with fresh eyes.
- Don't let a perfect checklist stop you from shipping. But don't ship with a known serious security hole either.

## When a rule doesn't fit

The rules are a starting point, not a law. If one doesn't make sense for your project, write down why and move on. You're free to change them under the [licence](LICENSE). If you think a rule is wrong for everyone, please [open an issue](https://github.com/abuturab840/humane-dev-rules/issues) so it can be fixed.
