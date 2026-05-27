import Link from "next/link";

import { WorkWithUsForm } from "@/components/forms/WorkWithUsForm";
import { PageHero } from "@/components/ui/PageHero";
import { QuoteCard } from "@/components/ui/QuoteCard";
import { Reveal, Stagger, StaggerItem } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";
import { StatBox } from "@/components/ui/StatBox";
import { ValueItem } from "@/components/ui/ValueItem";
import { createMetadata } from "@/lib/metadata";
import { quote, stats, values, whyPoints, workWithUsIntro } from "@/lib/site-data";

export const metadata = createMetadata({
  title: "About Spring 2 Health",
  description:
    "Learn about Spring 2 Health's person-centred philosophy, collaborative care model, and disability support approach in Queensland.",
  path: "/about"
});

export default function AboutPage() {
  return (
    <>
      <PageHero
        pill="About Us"
        title={
          <>
            Who we <em className="font-heading text-brand-gold italic">are</em>
          </>
        }
        subtitle="A disability support provider that puts people first, always curious, always collaborative, always person-centred."
      />

      <section className="section-pad">
        <div className="container-shell grid gap-12 lg:grid-cols-[1fr_0.95fr]">
          <Reveal>
            <PillLabel className="mb-5">Our Philosophy</PillLabel>
            <h2 className="section-heading">
              We are <em>curious</em> to get to know you
            </h2>
            <p className="section-copy mt-5">
              At Spring 2 Health, we want to get to know all about you as the
              expert in your own life. We take a person-centred approach to
              understanding who you are at a deeper level so that we can provide
              individualised disability support that speaks to exactly who you are
              and the type of support you need.
            </p>
            <p className="section-copy mt-4">
              We operate from a curiosity standpoint and are constantly seeking to
              learn more about our participants and their unique situations. Our
              approach is strength-based, meaning we focus on our participants
              abilities and potential rather than their limitations.
            </p>
            <p className="section-copy mt-4">
              We recognise that our participants are experts in their own lives,
              and we work to empower them to make their own decisions and live
              their lives to the fullest. We operate from a place of diversity and
              inclusion, ensuring that everyone feels valued and respected.
            </p>

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
            <QuoteCard
              text="We provide support differently. Most organisations think of their bottom line. We are in this for our participants, putting you first in everything we do."
              attribution={quote.attribution}
            />
            <Link href="/referral" className="btn-primary mt-8">
              Make a Referral
            </Link>
          </Reveal>
        </div>
      </section>

      <section className="bg-brand-black py-20">
        <div className="container-shell grid gap-12 lg:grid-cols-[1fr_0.95fr] lg:items-center">
          <Reveal>
            <PillLabel className="mb-5">Why Spring 2 Health</PillLabel>
            <h2 className="section-heading text-white">
              We provide support <em>differently</em>
            </h2>
            <p className="dark-copy mt-5 max-w-xl text-base leading-8">
              Through providing a tailored service unique to you, your obstacles,
              and your aspirations, we deliver care that supports you as an
              individual.
            </p>

            <Stagger className="mt-8 space-y-4">
              {whyPoints.map((point) => (
                <StaggerItem key={point.number}>
                  <div className="panel-dark rounded-card border-l-4 border-l-brand-gold p-6">
                    <div className="flex gap-4">
                      <div className="font-heading text-3xl text-brand-gold/35">
                        {point.number}
                      </div>
                      <div>
                        <h3 className="text-lg font-bold text-white">{point.title}</h3>
                        <p className="mt-2 text-sm leading-7 text-white/50">
                          {point.description}
                        </p>
                      </div>
                    </div>
                  </div>
                </StaggerItem>
              ))}
            </Stagger>
          </Reveal>

          <Reveal delay={0.12}>
            <div className="grid gap-4 sm:grid-cols-2">
              <div className="panel-dark rounded-card border-brand-gold/25 bg-brand-gold/8 p-8 sm:col-span-2">
                <p className="text-xl font-bold text-white">
                  Strength-Based &amp; Person-Centred
                </p>
                <p className="mt-3 text-sm leading-7 text-white/55">
                  Our philosophy puts you at the centre of everything, recognising
                  you as the expert in your own life.
                </p>
              </div>
              {stats.map((item) => (
                <StatBox key={item.label} value={item.value} label={item.label} />
              ))}
            </div>
          </Reveal>
        </div>
      </section>

      <section className="bg-[#faf7f0] py-20">
        <div className="container-shell grid gap-12 lg:grid-cols-[0.95fr_1.05fr] lg:items-center">
          <Reveal>
            <PillLabel className="mb-5">Join Our Team</PillLabel>
            <h2 className="section-heading">
              Want to work with <em>Spring 2 Health?</em>
            </h2>
            <p className="section-copy mt-5">{workWithUsIntro}</p>
          </Reveal>
          <Reveal delay={0.08}>
            <WorkWithUsForm />
          </Reveal>
        </div>
      </section>
    </>
  );
}
