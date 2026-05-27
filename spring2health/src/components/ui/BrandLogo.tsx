import Link from "next/link";

import { company } from "@/lib/site-data";
import { cn } from "@/lib/utils";

type BrandLogoProps = {
  className?: string;
  imageClassName?: string;
  showTagline?: boolean;
  priority?: boolean;
};

export function BrandLogo({
  className,
  showTagline = true,
  imageClassName
}: BrandLogoProps) {
  return (
    <Link
      href="/"
      className={cn("inline-flex items-center gap-3 text-left", className)}
      aria-label={`${company.name} home`}
    >
      <span
        className={cn(
          "inline-flex h-11 w-11 items-center justify-center rounded-full border border-brand-gold/35 bg-brand-gold/10 text-brand-gold shadow-gold",
          imageClassName
        )}
        aria-hidden
      >
        <svg viewBox="0 0 64 64" className="h-6 w-6 fill-current">
          <path d="M35.2 9.4c-7.7 3.2-13.1 10.5-13.1 19.1 0 7.4 3.9 13.8 9.8 17.5-1.8-7.5 3.3-12.2 8-16.5 4.2-3.9 8.2-7.6 6.4-13.7-1.1-3.7-4.1-6.1-7.8-6.4-1.2-.1-2.3-.1-3.3 0Z" />
          <path d="M20.4 20.8C13.6 24 9 30.9 9 38.8 9 49.4 17.6 58 28.2 58c9.1 0 16.8-6.4 18.7-15-3.9 2.7-9.1 3.8-13.8 2.6-7.8-2-13.1-9.1-12.7-17.8Z" />
        </svg>
      </span>
      <span>
        <span className="block font-heading text-xl font-semibold tracking-[-0.04em] text-white">
          Spring 2 Health
        </span>
        <span className="block text-[0.62rem] font-semibold uppercase tracking-[0.28em] text-brand-gold/80">
          NDIS Registered Provider
        </span>
      </span>
      {showTagline ? (
        <span className="hidden text-[0.58rem] font-semibold uppercase tracking-[0.28em] text-white/40 sm:block">
          Disability Support · Queensland
        </span>
      ) : null}
    </Link>
  );
}
