# Fix: Vercel shows "No active branches" or "NOT_FOUND"

GitHub **does** have a `main` branch with your green site:  
https://github.com/RussellPullin/spring2health-website/tree/main

If Vercel shows **no active branches**, the Git link is broken or the project still points at the old `spring2health` folder (removed from the repo).

---

## Step 1 — Reconnect GitHub in Vercel

1. Open [vercel.com/dashboard](https://vercel.com/dashboard)
2. Open project **spring2health-website**
3. **Settings** → **Git**
4. If you see a warning or no branches:
   - Click **Disconnect** (or **Edit**)
   - Click **Connect Git Repository**
   - Choose **GitHub** → **RussellPullin/spring2health-website**
5. If GitHub asks for access, approve Vercel for that repo:
   - GitHub → **Settings** → **Applications** → **Vercel** → configure access to `spring2health-website`

---

## Step 2 — Fix build settings (critical)

**Settings** → **General**:

| Setting | Value |
|---------|--------|
| **Production Branch** | `main` |
| **Root Directory** | *(completely empty — delete `spring2health` if it is there)* |
| **Framework Preset** | Other |
| **Build Command** | *(empty, Override ON)* |
| **Output Directory** | `.` |
| **Install Command** | `npm install` *(or empty)* |

Save.

---

## Step 3 — Redeploy

1. **Deployments** tab
2. Click **⋯** on latest → **Redeploy**
3. Or push any commit to `main` on GitHub (triggers auto-deploy)

Success looks like: deployment **Ready**, no error about missing root directory.

---

## Step 4 — Turn off deployment protection

**Settings** → **Deployment Protection** → set **Production** to **None** (public).

Otherwise preview URLs show "Authentication Required" / not found.

---

## Step 5 — Custom domain (GoDaddy)

Even when Vercel works, `spring2health.com.au` may still show GoDaddy until DNS is fixed. See [GODADDY_DNS_FIX.md](GODADDY_DNS_FIX.md).

---

## Confirm GitHub has files

Open: https://github.com/RussellPullin/spring2health-website

You should see: `index.html`, `referral.html`, `logo.png`, `vercel.json`, `api/submit.js`

If that page is empty, tell us — otherwise the fix is only in Vercel settings above.
