import { AnimatedValue } from "@/components/ui/motion";

type StatBoxProps = {
  value: string;
  label: string;
};

export function StatBox({ value, label }: StatBoxProps) {
  return (
    <div className="panel-light rounded-card px-6 py-7 text-center">
      <AnimatedValue
        value={value}
        className="block text-3xl font-bold tracking-[-0.04em] text-brand-black"
      />
      <span className="mt-2 block text-sm font-semibold uppercase tracking-[0.14em] text-brand-muted">
        {label}
      </span>
    </div>
  );
}
