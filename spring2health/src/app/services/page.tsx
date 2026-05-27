import Link from "next/link";

import { PageHero } from "@/components/ui/PageHero";
import { Reveal, Stagger, StaggerItem } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";
import { createMetadata } from "@/lib/metadata";
import { services } from "@/lib/site-data";

export const metadata = createMetadata({
  title: "Services | Spring 2 Health",
  description:
    "Explore Spring 2 Health services including supported independent living, respite, social work, counselling, community access, adventure therapy, and PBS plans.",
  path: "/services"
});

export default function ServicesPage() {
  return (
    <>
      <PageHero
        pill="Our Services"
        title={
          <>
            Support tailored to <em className="font-heading text-brand-gold italic">you</em>
          </>
        }
        subtitle="We provide practical, therapeutic, and person-centred support designed around each participant's individual needs, aspirations, and care network."
      />

      <section className="section-pad">
        <div className="container-shell">
          <Reveal className="max-w-3xl">
            <PillLabel className="mb-5">Support Streams</PillLabel>
            <h2 className="section-heading">
              Improving your <em>quality of life</em>
            </h2>
            <p className="section-copy mt-5">
              Every service is delivered through a collaborative, strengths-based
              lens. We take the time to understand the person behind the plan so
              the support feels meaningful, practical, and genuinely individual.
            </p>
          </Reveal>

          <Stagger className="mt-12 space-y-6">
            {services.map((service, index) => (
              <StaggerItem key={service.slug}>
                <article className="panel-light rounded-[18px] p-8 sm:p-10">
                  <div className="grid gap-8 lg:grid-cols-[0.85fr_1.15fr] lg:items-start">
                    <div>
                      <div className="mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-brand-gold/15 text-3xl">
                        {service.icon}
                      </div>
                      <p className="text-xs font-bold uppercase tracking-[0.18em] text-brand-goldDeep">
                        Service {String(index + 1).padStart(2, "0")}
                      </p>
                      <h2 className="mt-3 text-3xl font-bold tracking-[-0.04em] text-brand-black">
                        {service.title}
                      </h2>
                      <p className="mt-4 text-base leading-8 text-brand-muted">
                        {service.description}
                      </p>
                    </div>

                    <div className="rounded-card border border-brand-gold/15 bg-brand-cream px-6 py-6">
                      <p className="text-sm font-bold uppercase tracking-[0.18em] text-brand-goldDeep">
                        What this can include
                      </p>
                      <ul className="mt-5 grid gap-3 sm:grid-cols-2">
                        {service.bullets.map((bullet) => (
                          <li
                            key={bullet}
                            className="flex gap-3 text-sm leading-7 text-brand-ink"
                          >
                            <span className="mt-2 h-2 w-2 rounded-full bg-brand-gold" />
                            <span>{bullet}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </article>
              </StaggerItem>
            ))}
          </Stagger>

          <Reveal className="mt-12 text-center">
            <Link href="/referral" className="btn-primary">
              Make a Referral
            </Link>
          </Reveal>
        </div>
      </section>
    </>
  );
}
