import Link from "next/link";

import { BrandLogo } from "@/components/ui/BrandLogo";
import { company, footerServices, navigationLinks } from "@/lib/site-data";

export function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="border-t border-brand-gold/15 bg-[#080808]">
      <div className="container-shell py-16">
        <div className="grid gap-12 border-b border-white/5 pb-10 md:grid-cols-[1.7fr_1fr_1fr]">
          <div>
            <BrandLogo showTagline={false} />
            <p className="mt-5 max-w-sm text-sm leading-8 text-white/38">
              A disability support provider based in Queensland, dedicated to
              improving the quality of life of our participants through holistic,
              person-centred care.
            </p>
            <div className="mt-6 space-y-2 text-sm text-white/45">
              <p>
                <Link href={company.phoneHref} className="transition hover:text-brand-gold">
                  {company.phone}
                </Link>
              </p>
              <p>
                <Link href={company.emailHref} className="transition hover:text-brand-gold">
                  {company.email}
                </Link>
              </p>
              <p>{company.address}</p>
            </div>
          </div>

          <div>
            <p className="mb-4 text-[0.7rem] font-bold uppercase tracking-[0.18em] text-brand-gold/60">
              Site Links
            </p>
            <div className="flex flex-col gap-3">
              {navigationLinks.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="text-sm text-white/45 transition hover:text-brand-gold"
                >
                  {item.label}
                </Link>
              ))}
              <Link
                href="/referral"
                className="text-sm font-semibold text-white/65 transition hover:text-brand-gold"
              >
                Make a Referral
              </Link>
            </div>
          </div>

          <div>
            <p className="mb-4 text-[0.7rem] font-bold uppercase tracking-[0.18em] text-brand-gold/60">
              Support Services
            </p>
            <div className="flex flex-col gap-3">
              {footerServices.map((item, index) => (
                <Link
                  key={`${item.label}-${index}`}
                  href={item.href}
                  className="text-sm text-white/45 transition hover:text-brand-gold"
                >
                  {item.label}
                </Link>
              ))}
            </div>
          </div>
        </div>

        <div className="flex flex-col justify-between gap-3 pt-6 text-xs text-white/20 sm:flex-row">
          <p>{year} Spring 2 Health. All rights reserved.</p>
          <p>{company.ndisStatus}</p>
        </div>
      </div>
    </footer>
  );
}
