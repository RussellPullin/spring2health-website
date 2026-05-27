import Link from "next/link";

import { QuoteCard } from "@/components/ui/QuoteCard";
import { Reveal, Stagger, StaggerItem } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";
import { ServiceCard } from "@/components/ui/ServiceCard";
import { StatBox } from "@/components/ui/StatBox";
import { ValueItem } from "@/components/ui/ValueItem";
import { createMetadata } from "@/lib/metadata";
import { homeHero, quote, services, stats, values } from "@/lib/site-data";

export const metadata = createMetadata({
  title: "Spring 2 Health | NDIS Support In Queensland",
  description:
    "Discover person-centred disability support, social work, respite, counselling, community access, and referral pathways with Spring 2 Health.",
  path: "/"
});

export default function HomePage() {
  return (
    <>
      <section className="hero-surface relative overflow-hidden pt-32 sm:pt-36">
        <div className="grid-dots absolute inset-0 opacity-60" aria-hidden />
        <div
          className="absolute right-[-120px] top-[-120px] h-[420px] w-[420px] rounded-full bg-brand-gold/10 blur-3xl"
          aria-hidden
        />
        <div className="container-shell relative z-10 grid gap-12 py-16 lg:grid-cols-[1.08fr_0.92fr] lg:items-center lg:py-24">
          <div>
            <Reveal>
              <PillLabel className="mb-6">{homeHero.pill}</PillLabel>
            </Reveal>
            <Reveal delay={0.08}>
              <h1 className="text-balance text-[clamp(2.8rem,5vw,5rem)] font-bold leading-[1.02] tracking-[-0.05em] text-white">
                {homeHero.title}
                <span className="block font-heading text-brand-gold italic">
                  {homeHero.accent}
                </span>
              </h1>
            </Reveal>
            <Reveal delay={0.16}>
              <p className="mt-5 max-w-xl text-lg font-light leading-8 text-white/60">
                {homeHero.subtitle}
              </p>
            </Reveal>

            <Stagger className="mt-8 space-y-3">
              {homeHero.highlights.map((item) => (
                <StaggerItem key={item}>
                  <div className="flex items-center gap-3 text-sm text-white/80 sm:text-base">
                    <span className="flex h-6 w-6 items-center justify-center rounded-full border border-brand-gold bg-brand-gold/15 text-xs text-brand-gold">
                      ✓
                    </span>
                    <span>{item}</span>
                  </div>
                </StaggerItem>
              ))}
            </Stagger>

            <Reveal delay={0.24} className="mt-10 flex flex-wrap gap-4">
              <Link href="/referral" className="btn-primary">
                Make a Referral
              </Link>
              <Link href="/services" className="btn-secondary">
                Explore Our Services
              </Link>
            </Reveal>
          </div>

          <Stagger className="grid gap-4">
            {homeHero.floatingCards.map((card, index) => (
              <StaggerItem key={card.title}>
                <div
                  className={`panel-dark rounded-card p-6 transition duration-200 hover:translate-x-1 ${
                    index === 0 ? "bg-brand-gold/10" : ""
                  }`}
                >
                  <div className="flex items-start gap-4">
                    <div className="flex h-11 w-11 items-center justify-center rounded-xl border border-brand-gold/25 bg-brand-gold/10 text-xl">
                      {card.icon}
                    </div>
                    <div>
                      <h2 className="text-base font-bold text-white">{card.title}</h2>
                      <p className="mt-2 text-sm leading-7 text-white/50">
                        {card.description}
                      </p>
                    </div>
                  </div>
                </div>
              </StaggerItem>
            ))}
          </Stagger>
        </div>
      </section>

      <section className="bg-[#0d0d0d] py-8">
        <div className="container-shell grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          {stats.map((item) => (
            <StatBox key={item.label} value={item.value} label={item.label} />
          ))}
        </div>
      </section>

      <section className="section-pad">
        <div className="container-shell grid gap-12 lg:grid-cols-[1fr_0.95fr] lg:items-center">
          <Reveal>
            <PillLabel className="mb-5">About Spring 2 Health</PillLabel>
            <h2 className="section-heading">
              We are <em>curious</em> to get to know you
            </h2>
            <p className="section-copy mt-5">
              At Spring 2 Health, we want to get to know all about you as the
              expert in your own life. We take a person-centred approach to
              understanding who you are at a deeper level so we can provide
              individualised disability support that speaks to exactly who you are.
            </p>
            <p className="section-copy mt-4">
              Our focus is improving your quality of life through working in close
              partnership with yourself, your family, and your support network.
            </p>
            <Link href="/about" className="btn-primary mt-8">
              Learn More About Us
            </Link>

            <div className="mt-8 grid gap-4">
              {values.map((value) => (
                <ValueItem
                  key={value.title}
                  icon={value.icon}
                  title={value.title}
                  description={value.description}
                />
              ))}
            </div>
          </Reveal>

          <Reveal delay={0.1}>
            <QuoteCard text={quote.text} attribution={quote.attribution} />
          </Reveal>
        </div>
      </section>

      <section className="bg-brand-black py-20">
        <div className="container-shell">
          <Reveal className="mx-auto mb-12 max-w-2xl text-center">
            <PillLabel className="mb-5">Our Support Services</PillLabel>
            <h2 className="section-heading text-white">
              Improving your <em>quality of life</em>
            </h2>
          </Reveal>

          <Stagger className="grid gap-5 md:grid-cols-2 xl:grid-cols-3">
            {services.slice(0, 6).map((service) => (
              <StaggerItem key={service.slug}>
                <ServiceCard
                  icon={service.icon}
                  title={service.title}
                  description={service.shortDescription}
                  href="/services"
                />
              </StaggerItem>
            ))}
          </Stagger>

          <Reveal className="mt-10 text-center">
            <Link href="/services" className="btn-primary">
              View All Services
            </Link>
          </Reveal>
        </div>
      </section>

      <section className="bg-brand-gold py-20 text-center">
        <div className="container-shell max-w-3xl">
          <Reveal>
            <h2 className="text-balance text-[clamp(2.1rem,4vw,3.2rem)] font-bold tracking-[-0.04em] text-brand-black">
              Ready to get started?
            </h2>
            <p className="mx-auto mt-4 max-w-xl text-base leading-8 text-black/65">
              Our team are here to support you. Make a referral today and we will
              be in touch to discuss how we can help.
            </p>
            <Link href="/referral" className="btn-dark mt-8">
              Make a Referral
            </Link>
          </Reveal>
        </div>
      </section>
    </>
  );
}
