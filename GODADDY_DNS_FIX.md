# Fix: Domain shows GoDaddy instead of your website

**Your domain does not point to Vercel yet.** Traffic goes to GoDaddy’s servers, so you see the GoDaddy template no matter what Vercel deploys.

Current DNS (wrong for Vercel):

| Type | Name | Value (delete these) |
|------|------|----------------------|
| A | @ | `76.223.105.230` |
| A | @ | `13.248.243.5` |
| A | @ | `216.198.79.1` |

---

## Step 1 — Turn off GoDaddy Website (do this first)

1. Go to [godaddy.com](https://godaddy.com) → **My Products**
2. Under **Websites**, open any site linked to `spring2health.com.au`
3. **Unpublish** or **Delete** the site, or **disconnect** the domain
4. **Domains** → `spring2health.com.au` → **Forwarding** → turn **Off**

Until this is done, GoDaddy can keep showing its template.

---

## Step 2 — Fix DNS in GoDaddy

1. **Domains** → `spring2health.com.au` → **DNS** → **Manage DNS**
2. **Delete every A record** for `@` (all three IPs above)
3. **Add one A record:**

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | `76.76.21.21` | Default |

(Vercel may show a different IP in **Domains** — use the value Vercel gives you if it differs.)

4. **www subdomain:**

| Action | Type | Name | Value |
|--------|------|------|--------|
| Delete | CNAME | www | if it points to `@` or GoDaddy |
| Add | CNAME | www | `cname.vercel-dns.com` |

5. **Keep** your **MX** record (email) — do not delete it.

6. Save and wait **15–60 minutes** (sometimes up to a few hours).

---

## Step 3 — Fix Vercel (green static site)

In [vercel.com](https://vercel.com) → your project → **Settings → General**:

| Setting | Must be |
|---------|---------|
| Root Directory | **Empty** (not `spring2health`) |
| Framework Preset | **Other** |
| Build Command | **Empty** (override on) |
| Output Directory | **`.`** or empty |

Then **Deployments** → **Redeploy** latest on `main`.

Environment variable: `RESEND_API_KEY` (for contact/referral forms).

---

## Step 4 — Confirm it worked

Open an **incognito** window:

- `https://spring2health.com.au` → green forest theme, **logo image**, not GoDaddy cookie banner
- Page source should **not** contain `layout-layout` (GoDaddy) or `_next/static` (old Next.js)

In Vercel → **Domains**, status should be **Valid Configuration**.

---

## Quick test: is it DNS or Vercel?

| URL | What you should see |
|-----|---------------------|
| `http://localhost:3456` | Green site (correct) |
| Vercel preview URL (in Vercel dashboard) | Green site after Step 3 |
| `https://spring2health.com.au` | Green site only after Steps 1–2 |

If the Vercel preview URL looks correct but the custom domain does not, the problem is **DNS (Step 2)**.
