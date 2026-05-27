import Link from "next/link";

import { cn } from "@/lib/utils";

type ServiceCardProps = {
  icon: string;
  title: string;
  description: string;
  href?: string;
  className?: string;
};

export function ServiceCard({
  icon,
  title,
  description,
  href = "/services",
  className
}: ServiceCardProps) {
  return (
    <Link
      href={href}
      className={cn(
        "group panel-dark relative block overflow-hidden rounded-card p-7 transition duration-200 hover:-translate-y-1 hover:border-brand-gold/35 hover:bg-brand-gold/5",
        className
      )}
    >
      <div className="absolute inset-x-0 bottom-0 h-[3px] origin-left scale-x-0 bg-gradient-to-r from-brand-goldDeep to-brand-gold transition-transform duration-300 group-hover:scale-x-100" />
      <div className="mb-5 flex h-12 w-12 items-center justify-center rounded-xl border border-brand-gold/25 bg-brand-gold/10 text-2xl">
        {icon}
      </div>
      <h3 className="text-lg font-bold text-white">{title}</h3>
      <p className="mt-3 text-sm leading-7 text-white/55">{description}</p>
    </Link>
  );
}
