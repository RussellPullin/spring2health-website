# Spring 2 Health — Cursor AI Prompt
## Full Website Build Brief

Paste this entire prompt into Cursor to build the Spring 2 Health website as a production-ready Next.js application.

---

## PROJECT OVERVIEW

Build a complete multi-page website for **Spring 2 Health**, an NDIS-registered disability support provider based in Sanctuary Cove, Queensland, Australia. The business was formerly known as Pristine Lifestyle Solutions.

---

## TECH STACK

- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **Fonts:** Google Fonts — `Playfair Display` (serif/headings italic) + `Nunito` (sans body)
- **Animations:** Framer Motion for scroll reveals and hero animations
- **Forms:** React Hook Form + basic email via Resend (or Nodemailer)
- **Language:** TypeScript

---

## BRAND & DESIGN SYSTEM

### Colours
```css
--gold:        #C9A84C   /* Primary accent — buttons, highlights, icons */
--gold-dark:   #A8893A   /* Hover states */
--gold-pale:   #F5EDD6   /* Light gold backgrounds */
--gold-frost:  #FAF7F0   /* Page section backgrounds */
--black:       #0A0A0A   /* Hero / dark section backgrounds */
--black-mid:   #111111   /* Dark cards */
--black-soft:  #1A1A1A   /* Secondary dark */
--cream:       #F8F5EF   /* Light page backgrounds */
--white:       #FFFFFF
--mid:         #4A4A4A   /* Body text on light */
--soft:        #7A7A7A   /* Muted text */
--border:      rgba(201,168,76,0.18)
```

### Typography
- **Display headings:** `Playfair Display`, italic weight, for `<em>` styled words in headings
- **All other text:** `Nunito`, weights 300/400/600/700
- **Heading sizes:** clamp(2rem, 3.2vw, 3.25rem) for section titles; clamp(2.75rem, 4.5vw, 4.75rem) for hero
- **Body:** 1rem, line-height 1.9, color `--mid`

### Logo
- The logo file is `spring2health-logo.png` (placed in `/public/images/`)
- The logo has a **black circle** with a **gold S-path** through it, and the text "Spring**2**Health" where the "2" is gold
- On dark/black backgrounds: use logo as-is (it has transparent background)
- The logo was recoloured from the original blue/green to black/gold

### Design Language
- **Dark hero sections** with subtle gold dot-grid overlay and radial gold glow
- **Light cream sections** for content areas
- **Gold accent borders** (not blue, not green — always gold)
- Cards with `rgba(201,168,76,0.1)` background and `rgba(201,168,76,0.12-0.25)` border
- Hover: cards lift with `translateY(-4px)` and gold border intensifies
- Bottom border reveal on service cards on hover: gold gradient line slides in from left
- Border radius: 10-14px for cards, 8px for inputs, 100px for pill labels
- Consistent gold shadow: `0 6px 24px rgba(201,168,76,0.3)`

---

## SITE STRUCTURE (5 Pages)

```
/               → Home (index)
/about          → About Us
/services       → Our Services
/contact        → Contact Us
/referral       → Make a Referral
```

---

## COMPONENTS TO BUILD

### `<Nav />`
- Fixed top, full width
- Background: `rgba(10,10,10,0.97)` with `backdrop-filter: blur(20px)`
- Bottom border: `1px solid rgba(201,168,76,0.15)`
- Left: Logo image + tagline "Disability Support · Queensland" (tiny, muted)
- Right: Links → Home, About, Services, Contact + gold CTA button "Make a Referral"
- Active page link styled with gold colour + subtle gold background
- Mobile: hamburger menu, links slide in from right

### `<Footer />`
- Background: `#080808`
- Top border: `1px solid rgba(201,168,76,0.15)`
- 3-column grid: Brand + tagline | Navigation links | Services links + Policies
- Logo shown full colour (black/gold) — it works on dark background
- Link hover: gold colour
- Bottom row: copyright + privacy/terms links

### `<PageHero />` (reusable for inner pages)
- Full-width dark hero with black gradient background
- Radial gold glow in top-right corner
- Pill label + large heading with italic gold `<em>` word + subtitle
- Props: `pill`, `title`, `subtitle`

### `<PillLabel />`
- Small rounded tag: gold border, gold text, gold dot
- `background: rgba(201,168,76,0.1)`

### `<ServiceCard />` (used on Home + Services page)
- Dark card with gold icon box, title, description
- Hover: lift + gold border + bottom gold gradient reveal

### `<StatBox />`
- Used in About/Why Us sections
- White on light backgrounds, dark on dark backgrounds
- Large gold number, small muted label

### `<QuoteCard />`
- Dark gradient card with large italic serif quote
- Oversized gold opening quote mark
- Gold horizontal rule + attribution text
- Used on Home and About pages

### `<ValueItem />` (`av` in CSS)
- Horizontal row: gold icon box + bold title + muted description
- Used in About section with cream background + gold bottom border
- Hover: gold-pale background

### `<ContactItem />`
- Small card with gold icon circle, label, value
- Used on Contact + Referral pages

### `<FormField />`
- Label (tiny uppercase gold-dark) + input/select/textarea
- Border: `1.5px solid rgba(201,168,76,0.2)`
- Focus: gold border + `box-shadow: 0 0 0 3px rgba(201,168,76,0.15)`
- Background: cream, turns white on focus

---

## PAGE SPECIFICATIONS

---

### HOME PAGE (`/`)

**1. Hero Section** (full viewport, dark)
- Background: `linear-gradient(145deg, #000 0%, #1A1A1A 60%, #0D0D0D 100%)`
- Radial gold blobs (top-right + bottom-center)
- Dot grid overlay: `radial-gradient(rgba(255,255,255,0.05) 1px, transparent 1px)` at 36px
- 2-column layout: left content + right floating cards
- **Left content:**
  - Gold pill badge: "NDIS Registered Provider — Queensland"
  - H1: "Providing you with the support you truly deserve" — "truly deserve" in italic Playfair gold
  - Subtitle paragraph
  - 4 checkmark pills (gold circle with ✓):
    - Specialists in Mental Health & Psychosocial Disability
    - Supported Independent Living & Respite
    - Social Work & Therapeutic Services
    - Adventure Therapy & Community Access
  - Two buttons: "Make a Referral" (gold) + "Explore Our Services" (ghost/outline)
- **Right floating cards** (hidden on mobile): 4 dark semi-transparent cards with gold borders showing key services with emoji icons
- **Animation:** staggered fadeUp on hero left content items (Framer Motion)

**2. Stats Band**
- Dark background `#0D0D0D`
- Gold top/bottom borders
- 4 stats: `6+` Services | `24/7` Support | `NDIS` Registered | `QLD` Based
- Gold numbers, muted white labels, vertical dividers between

**3. About Preview Section** (cream background)
- 2-column: left text + right quote card
- Left: pill + h2 with italic gold em + 2 body paragraphs + CTA button + 3 value items
- Right: Dark QuoteCard ("We provide support differently...") with floating gold badge (100% / Participant Centred) bottom-right

**4. Services Preview** (dark gradient background)
- Centred header: pill + h2
- 3-column grid of 6 ServiceCards (linked to /services)
- Centred CTA button below

**5. CTA Banner** (solid gold background `#C9A84C`)
- Centred: large heading + paragraph + dark button "Make a Referral"
- Text colour: `#1A1A1A`

---

### ABOUT PAGE (`/about`)

**1. PageHero** — "Who we are" / "About Us"

**2. Main About Section** (cream background, 2-column)
- Left: philosophy text (4 paragraphs) + 4 ValueItems
- Right: QuoteCard + referral CTA button below

**3. Why Us Section** (dark background, 2-column)
- Left: pill + h2 + subtitle + 4 numbered Why Points (left gold border cards)
  - 01: Individualised Care Plans
  - 02: Holistic, Collaborative Approach
  - 03: Mental Health Specialists
  - 04: Innovation & Adventure
- Right: 2-column stats grid:
  - Wide card: "Strength-Based & Person-Centred" text
  - 4 stat boxes: 24/7 | NDIS | 6+ | QLD

**4. Work With Us Section** (gold-frost background, 2-column)
- Left: pill + h2 + paragraph
- Right: White card form with fields: Name, Phone, Email, Why do you want to work for us? (textarea), Submit button

---

### SERVICES PAGE (`/services`)

**1. PageHero** — "Our Support Services"

**2. Services Detail Section** (dark gradient background)
- 7 full-width alternating service blocks (flip layout every other one):
  - Each block: 2-column — left: icon + title + description + referral CTA | right: dark card with bullet points
  - Alternating columns flip for visual rhythm
  - Services:
    1. 🏠 Supported Independent Living
    2. 🤝 Social Work Services
    3. 🌿 Respite Care
    4. 🌐 Community Access
    5. 💬 Counselling Services
    6. ⛺ Adventure Therapy
    7. 📋 Positive Behaviour Support Plans

---

### CONTACT PAGE (`/contact`)

**1. PageHero** — "Let's Connect"

**2. Contact Section** (cream background, 2-column)
- Left: pill + h2 + subtitle + 4 ContactItems (Phone, Email, Location, Fund Management)
- Right: White form card (shadow, gold border)
  - Fields: First Name, Last Name, Phone, Email, Message (textarea)
  - Gold submit button

---

### REFERRAL PAGE (`/referral`)

**1. PageHero** — "Make a Referral"

**2. Referral Section** (gold-frost background, 2-column — 1fr / 1.5fr)
- Left: pill + h2 + subtitle + 4 ContactItems
- Right: Large white form card
  - Section heading "Referrer Details" (gold, uppercase, gold bottom border)
    - Referrer Name, Contact Number (2-col)
    - Email Address, Relationship to Participant (2-col)
  - Section heading "Participant Details"
    - Participant Name, Contact Number (2-col)
    - Participant Email (full width)
    - Fund Management select: NDIA Managed / Plan Managed / Self Managed (full width)
    - Additional Information textarea (full width)
  - Gold submit button "Submit Referral"

---

## CONTENT — COMPANY DETAILS

```
Business Name:    Spring 2 Health
Former Name:      Pristine Lifestyle Solutions
Phone:            0468 404 865
Email:            info@spring2health.com.au
Address:          PO Box 460, Sanctuary Cove QLD 4212
NDIS Status:      Registered Provider
Fund Management:  NDIA Managed, Plan Managed, Self Managed
```

---

## SERVICES DETAIL CONTENT

### Supported Independent Living
Help with daily living tasks, meal preparation, personal care, and community access. Personalised care plans reviewed regularly. 24/7 availability. Safe and supportive environment.

### Social Work Services
Individual and family counselling, advocacy and rights support, referrals to community services, personalised support plan development, collaborative work with full care team, NDIS plan guidance.

### Respite Care
In-home, centre-based, and community-based care. Short and medium-term accommodation available. Flexible scheduling. Experienced and compassionate care team.

### Community Access
Attendance at community events, access to local services and programs, building meaningful relationships, transport and accompaniment support, tailored to individual interests.

### Counselling Services
Individual and group counselling, CBT, trauma-informed therapy, anxiety and depression management, resilience and coping strategy development. Tailored to NDIS plan.

### Adventure Therapy
Hiking, rock climbing, camping and more. Personalised program for your needs. Resilience and self-esteem building. Mental health through outdoor engagement. Fully supported and safe.

### Positive Behaviour Support Plans
Comprehensive PBS plans. Proactive rather than reactive strategies. Collaborative with full care network. Practical coping tools. Regular review and adaptation.

---

## ANIMATIONS (Framer Motion)

- **Hero content:** staggered `fadeUp` (opacity 0→1, y 24→0) with 0.13s delays between children
- **Section headings:** fade up on scroll into view (`whileInView`, `once: true`)
- **Cards:** fade up with slight delay stagger on scroll
- **Service cards:** lift on hover with `whileHover: { y: -4 }`
- **Why points:** slide right on hover `whileHover: { x: 4 }`
- **Stats band numbers:** count-up animation when scrolled into view

---

## RESPONSIVE BREAKPOINTS

- **Desktop:** 1100px+ — full multi-column layouts
- **Tablet:** 700–1100px — 2-column → 1-column, hide hero right panel
- **Mobile:** <700px — single column, hamburger nav, 1-col form grid

---

## FORM HANDLING

- Use **React Hook Form** for validation
- On submit: POST to `/api/contact` or `/api/referral` Next.js API routes
- Send email via **Resend** (recommended) or Nodemailer
- Show success/error state inline (no page reload)
- Basic validation: required fields, email format, phone format

---

## SEO & METADATA

Each page should have:
```tsx
export const metadata: Metadata = {
  title: "Page Title | Spring 2 Health",
  description: "Page-specific description",
  openGraph: { ... }
}
```

- Home: "Spring 2 Health | NDIS Disability Support Queensland"
- About: "About Us | Spring 2 Health"
- Services: "Support Services | Spring 2 Health"
- Contact: "Contact Us | Spring 2 Health"
- Referral: "Make a Referral | Spring 2 Health"

---

## FILE STRUCTURE

```
spring2health/
├── public/
│   └── images/
│       └── spring2health-logo.png      ← Place logo here
├── src/
│   ├── app/
│   │   ├── layout.tsx                   ← Root layout (Nav + Footer)
│   │   ├── page.tsx                     ← Home page
│   │   ├── about/page.tsx
│   │   ├── services/page.tsx
│   │   ├── contact/page.tsx
│   │   ├── referral/page.tsx
│   │   └── api/
│   │       ├── contact/route.ts
│   │       └── referral/route.ts
│   ├── components/
│   │   ├── layout/
│   │   │   ├── Nav.tsx
│   │   │   └── Footer.tsx
│   │   ├── ui/
│   │   │   ├── PillLabel.tsx
│   │   │   ├── ServiceCard.tsx
│   │   │   ├── QuoteCard.tsx
│   │   │   ├── StatBox.tsx
│   │   │   ├── ValueItem.tsx
│   │   │   ├── ContactItem.tsx
│   │   │   ├── FormField.tsx
│   │   │   └── PageHero.tsx
│   │   └── sections/
│   │       ├── home/
│   │       │   ├── Hero.tsx
│   │       │   ├── StatsBand.tsx
│   │       │   ├── AboutPreview.tsx
│   │       │   ├── ServicesPreview.tsx
│   │       │   └── CtaBanner.tsx
│   │       ├── about/
│   │       │   ├── AboutMain.tsx
│   │       │   ├── WhyUs.tsx
│   │       │   └── WorkWithUs.tsx
│   │       ├── services/
│   │       │   └── ServicesDetail.tsx
│   │       ├── contact/
│   │       │   └── ContactSection.tsx
│   │       └── referral/
│   │           └── ReferralSection.tsx
│   └── styles/
│       └── globals.css                  ← Tailwind + CSS variables
```

---

## TAILWIND CONFIG

```js
// tailwind.config.ts
module.exports = {
  theme: {
    extend: {
      colors: {
        gold: { DEFAULT: '#C9A84C', dark: '#A8893A', pale: '#F5EDD6', frost: '#FAF7F0' },
        black: { DEFAULT: '#0A0A0A', mid: '#111111', soft: '#1A1A1A' },
        cream: '#F8F5EF',
      },
      fontFamily: {
        sans: ['Nunito', 'sans-serif'],
        serif: ['Playfair Display', 'Georgia', 'serif'],
      },
      borderRadius: { card: '14px', pill: '100px' },
      boxShadow: {
        gold: '0 6px 24px rgba(201,168,76,0.3)',
        'gold-lg': '0 16px 60px rgba(201,168,76,0.2)',
        dark: '0 16px 60px rgba(0,0,0,0.28)',
      },
    },
  },
}
```

---

## GETTING STARTED COMMANDS

```bash
npx create-next-app@latest spring2health --typescript --tailwind --app
cd spring2health
npm install framer-motion react-hook-form resend
npm run dev
```

Place the Spring 2 Health logo at `public/images/spring2health-logo.png` before running.

---

## NOTES FOR CURSOR

- Build one page at a time, starting with the shared `Nav` and `Footer` components
- Use Tailwind utility classes throughout — avoid inline styles except for dynamic values
- All gold coloured interactive elements should have smooth `transition-all duration-200`
- Ensure all forms are accessible with proper labels and ARIA attributes
- The site should score 90+ on Lighthouse for Performance, Accessibility, and SEO
- Make all animations respect `prefers-reduced-motion`
- Images should use Next.js `<Image />` component with proper alt text
