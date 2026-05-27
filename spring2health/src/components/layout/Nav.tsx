"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { BrandLogo } from "@/components/ui/BrandLogo";
import { navigationLinks } from "@/lib/site-data";
import { cn } from "@/lib/utils";

export function Nav() {
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="fixed inset-x-0 top-0 z-50 border-b border-brand-gold/15 bg-black/95 backdrop-blur-xl">
      <div className="container-shell flex min-h-[84px] items-center justify-between gap-6 py-4">
        <BrandLogo priority className="shrink-0" />

        <nav className="hidden items-center gap-1 lg:flex">
          {navigationLinks.map((item) => {
            const isActive = pathname === item.href;

            return (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  "rounded-lg px-4 py-2 text-sm font-semibold text-white/65 transition hover:bg-brand-gold/10 hover:text-brand-gold",
                  isActive && "bg-brand-gold/8 text-brand-gold"
                )}
              >
                {item.label}
              </Link>
            );
          })}

          <Link href="/referral" className="btn-primary ml-2 px-5 py-3 text-sm">
            Make a Referral
          </Link>
        </nav>

        <button
          type="button"
          onClick={() => setIsOpen((value) => !value)}
          aria-expanded={isOpen}
          aria-label="Toggle navigation menu"
          className="inline-flex h-11 w-11 items-center justify-center rounded-xl border border-brand-gold/25 bg-brand-gold/10 text-brand-gold lg:hidden"
        >
          <span className="relative h-4 w-5">
            <span
              className={cn(
                "absolute left-0 top-0 h-0.5 w-5 bg-current transition",
                isOpen && "top-[7px] rotate-45"
              )}
            />
            <span
              className={cn(
                "absolute left-0 top-[7px] h-0.5 w-5 bg-current transition",
                isOpen && "opacity-0"
              )}
            />
            <span
              className={cn(
                "absolute left-0 top-[14px] h-0.5 w-5 bg-current transition",
                isOpen && "top-[7px] -rotate-45"
              )}
            />
          </span>
        </button>
      </div>

      {isOpen ? (
        <div className="border-t border-brand-gold/10 bg-black/95 lg:hidden">
          <div className="container-shell flex flex-col gap-2 py-4">
            {navigationLinks.map((item) => {
              const isActive = pathname === item.href;

              return (
                <Link
                  key={item.href}
                  href={item.href}
                  onClick={() => setIsOpen(false)}
                  className={cn(
                    "rounded-xl px-4 py-3 text-sm font-semibold text-white/70 transition hover:bg-brand-gold/10 hover:text-brand-gold",
                    isActive && "bg-brand-gold/10 text-brand-gold"
                  )}
                >
                  {item.label}
                </Link>
              );
            })}
            <Link
              href="/referral"
              onClick={() => setIsOpen(false)}
              className="btn-primary mt-2 w-full"
            >
              Make a Referral
            </Link>
          </div>
        </div>
      ) : null}
    </header>
  );
}
