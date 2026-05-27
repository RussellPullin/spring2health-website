# Deploying Spring 2 Health to Vercel

The **live site** is the green static HTML at the **repository root** (`index.html`, `referral.html`, `gallery.html`, etc.). Preview locally with:

```bash
cd "/Users/pristinelifestylesolutions/Desktop/S2H website"
python3 -m http.server 3456
```

Open [http://localhost:3456](http://localhost:3456).

The `spring2health/` folder is an unused Next.js prototype — **do not** set it as the Vercel root directory.

## 1. GitHub

Repository: [github.com/RussellPullin/spring2health-website](https://github.com/RussellPullin/spring2health-website)

Push changes to `main` to trigger a deploy (after Vercel is configured as below).

## 2. Vercel project settings

In Vercel → Project → **Settings → General**:

| Setting | Value |
|---------|--------|
| **Root Directory** | *(empty — use repo root)* |
| **Framework Preset** | Other |
| **Build Command** | *(leave empty)* |
| **Output Directory** | *(leave empty)* |
| **Install Command** | `npm install` *(optional; installs `resend` for `/api/submit`)* |

If Root Directory is still set to `spring2health`, clear it, save, then redeploy.

## 3. Environment variables

In Vercel → **Settings → Environment Variables**:

| Variable | Required | Notes |
|----------|----------|--------|
| `RESEND_API_KEY` | Yes | From [resend.com](https://resend.com) → API Keys |

Apply to **Production**, **Preview**, and **Development**.

`RESEND_TO_EMAIL` and `RESEND_FROM_EMAIL` are **not** used by the static site. The API at [`api/submit.js`](api/submit.js) sends to `info@spring2health.com.au` from `noreply@spring2health.com.au`.

## 4. Resend (email)

1. Verify the domain `spring2health.com.au` in Resend (DNS records from Resend dashboard).
2. Use `noreply@spring2health.com.au` as the from address (already set in `api/submit.js`).
3. Do not use `onboarding@resend.dev` in production.

## 5. Custom domain and DNS

1. Vercel → **Settings → Domains** — add `spring2health.com.au` and `www.spring2health.com.au`.
2. In **GoDaddy DNS** (not GoDaddy Website Builder):
   - **A** `@` → `76.76.21.21` (or the IP Vercel shows)
   - **CNAME** `www` → `cname.vercel-dns.com`
   - Keep **MX** records for email
3. Disconnect or unpublish any **GoDaddy Website** attached to this domain.
4. Wait for DNS propagation, then click **Refresh** in Vercel Domains.

## 6. Deploy

Push to `main` or click **Redeploy** in Vercel.

## 7. Verify after deploy

- [ ] `https://spring2health.com.au` — green forest theme, logo image, not black/gold Next.js
- [ ] `/referral` or `/referral.html` — referral form with participant fields
- [ ] `/gallery` — gallery page loads
- [ ] Contact and referral forms send email (test with `RESEND_API_KEY` set)
- [ ] No `/_next/static/` assets in page source (that indicates the wrong Next.js deploy)

## Local development

```bash
cd "/Users/pristinelifestylesolutions/Desktop/S2H website"
python3 -m http.server 3456
```

Forms POST to `/api/submit`, which only works on Vercel (or with a local serverless stub). For local form testing, deploy to a Vercel preview branch.
