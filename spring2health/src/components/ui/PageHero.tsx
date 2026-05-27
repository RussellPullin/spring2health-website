import { Reveal } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";

type PageHeroProps = {
  pill: string;
  title: React.ReactNode;
  subtitle: string;
};

export function PageHero({ pill, title, subtitle }: PageHeroProps) {
  return (
    <section className="hero-surface relative overflow-hidden pt-36 pb-20 sm:pt-40 sm:pb-24">
      <div className="grid-dots absolute inset-0 opacity-60" aria-hidden />
      <div className="container-shell relative z-10">
        <Reveal className="max-w-3xl">
          <PillLabel className="mb-6">{pill}</PillLabel>
          <h1 className="text-balance text-[clamp(2.7rem,5vw,5rem)] font-bold leading-[1.02] tracking-[-0.04em] text-white">
            {title}
          </h1>
          <p className="mt-5 max-w-2xl text-lg font-light leading-8 text-white/60">
            {subtitle}
          </p>
        </Reveal>
      </div>
    </section>
  );
}
