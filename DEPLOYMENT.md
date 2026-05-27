# Deploying Spring 2 Health to Vercel

The live site is the **Next.js app** in the `spring2health/` folder. The HTML files in the project root are an older static version and are not used for deployment.

## 1. Push the project to GitHub

Vercel deploys from Git. From the project folder:

```bash
cd "/Users/pristinelifestylesolutions/Desktop/S2H website"
git init
git add .
git commit -m "Prepare Spring 2 Health site for Vercel"
```

Create a new repository on GitHub, then:

```bash
git remote add origin https://github.com/YOUR_ORG/spring2health-website.git
git branch -M main
git push -u origin main
```

## 2. Import the project in Vercel

1. Go to [vercel.com/new](https://vercel.com/new) and import your GitHub repository.
2. Set **Root Directory** to `spring2health` (important — the Next.js app is not at the repo root).
3. Framework Preset should auto-detect as **Next.js**.
4. Build Command: `npm run build` (default)
5. Output Directory: leave default (`.next`)

## 3. Add environment variables

In Vercel → Project → **Settings** → **Environment Variables**, add:

| Variable | Example | Notes |
|----------|---------|-------|
| `RESEND_API_KEY` | `re_...` | From [resend.com](https://resend.com) → API Keys |
| `RESEND_TO_EMAIL` | `info@spring2health.com.au` | Inbox for form submissions |
| `RESEND_FROM_EMAIL` | `Spring 2 Health <noreply@spring2health.com.au>` | Must use a **verified domain** in Resend |

Apply to **Production**, **Preview**, and **Development**.

Without these variables, forms still submit but emails are not sent.

## 4. Configure Resend (email)

1. In Resend, add and verify the domain `spring2health.com.au` (DNS records from Resend dashboard).
2. Use a from address on that domain, e.g. `noreply@spring2health.com.au`.
3. Do **not** use `onboarding@resend.dev` in production — it only works for testing.

## 5. Connect your custom domain

1. Vercel → Project → **Settings** → **Domains**
2. Add `spring2health.com.au` and `www.spring2health.com.au`
3. Update DNS at your domain registrar with the records Vercel provides.
4. Set the apex domain (`spring2health.com.au`) as the **primary** domain and redirect `www` if desired.

## 6. Deploy

Click **Deploy** (or push to `main` — Vercel redeploys automatically).

After deploy, verify:

- [ ] Home, About, Services, Contact, Referral pages load
- [ ] Contact form sends email to `RESEND_TO_EMAIL`
- [ ] Referral form sends email
- [ ] `https://spring2health.com.au/sitemap.xml` and `/robots.txt` are reachable

## Local development

```bash
cd spring2health
cp .env.example .env.local
# Edit .env.local with your Resend keys
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).
