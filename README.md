# Spring 2 Health Website

Green static site (forest green + amber theme) for [spring2health.com.au](https://spring2health.com.au).

## Local preview

```bash
python3 -m http.server 3456
```

Open [http://localhost:3456](http://localhost:3456).

## Pages

- `index.html` — Home
- `about.html` — About
- `services.html` — Services
- `gallery.html` — Gallery
- `contact.html` — Contact
- `referral.html` — Referral form
- `privacy-policy.html` — Privacy policy

## Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) and [GODADDY_DNS_FIX.md](GODADDY_DNS_FIX.md).

Forms use `/api/submit` (Resend). Set `RESEND_API_KEY` in Vercel.
