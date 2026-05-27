import { ReferralForm } from "@/components/forms/ReferralForm";
import { ContactItem } from "@/components/ui/ContactItem";
import { PageHero } from "@/components/ui/PageHero";
import { Reveal } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";
import { createMetadata } from "@/lib/metadata";
import { contactItems } from "@/lib/site-data";

export const metadata = createMetadata({
  title: "Make a Referral | Spring 2 Health",
  description:
    "Submit a referral to Spring 2 Health for person-centred disability support services in Queensland.",
  path: "/referral"
});

export default function ReferralPage() {
  return (
    <>
      <PageHero
        pill="Make A Referral"
        title={
          <>
            Refer with <em className="font-heading text-brand-gold italic">confidence</em>
          </>
        }
        subtitle="Share the referral details below and our team will review the information and contact you about the next steps."
      />

      <section className="section-pad">
        <div className="container-shell grid gap-12 lg:grid-cols-[0.88fr_1.12fr]">
          <Reveal>
            <PillLabel className="mb-5">Referral Pathway</PillLabel>
            <h2 className="section-heading">
              A clear and supportive <em>referral process</em>
            </h2>
            <p className="section-copy mt-5 max-w-xl">
              We work collaboratively with referrers, participants, families, and
              support teams to make the intake process as straightforward as
              possible. If you are unsure about any details, submit what you can
              and our team will follow up.
            </p>

            <div className="mt-8 grid gap-4">
              {contactItems.map((item) => (
                <ContactItem
                  key={item.label}
                  icon={item.icon}
                  label={item.label}
                  value={item.value}
                  href={"href" in item ? item.href : undefined}
                />
              ))}
            </div>
          </Reveal>

          <Reveal delay={0.08}>
            <ReferralForm />
          </Reveal>
        </div>
      </section>
    </>
  );
}
