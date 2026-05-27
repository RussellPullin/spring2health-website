import Link from "next/link";

type ContactItemProps = {
  icon: string;
  label: string;
  value: string;
  href?: string;
};

export function ContactItem({ icon, label, value, href }: ContactItemProps) {
  const content = (
    <div className="panel-light rounded-card p-6">
      <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-xl bg-brand-gold/15 text-2xl">
        {icon}
      </div>
      <p className="text-xs font-bold uppercase tracking-[0.18em] text-brand-goldDeep">
        {label}
      </p>
      <p className="mt-3 text-base font-semibold leading-7 text-brand-black">
        {value}
      </p>
    </div>
  );

  if (!href) {
    return content;
  }

  return (
    <Link href={href} className="block transition duration-200 hover:-translate-y-1">
      {content}
    </Link>
  );
}
