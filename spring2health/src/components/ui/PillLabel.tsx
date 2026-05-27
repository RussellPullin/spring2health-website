import { cn } from "@/lib/utils";

type PillLabelProps = {
  children: React.ReactNode;
  className?: string;
};

export function PillLabel({ children, className }: PillLabelProps) {
  return (
    <span
      className={cn(
        "inline-flex items-center gap-2 rounded-pill border border-brand-gold/30 bg-brand-gold/10 px-4 py-1.5 text-[0.68rem] font-bold uppercase tracking-[0.18em] text-brand-gold",
        className
      )}
    >
      <span className="h-1.5 w-1.5 rounded-full bg-brand-gold" aria-hidden />
      {children}
    </span>
  );
}
