import { ContactForm } from "@/components/forms/ContactForm";
import { ContactItem } from "@/components/ui/ContactItem";
import { PageHero } from "@/components/ui/PageHero";
import { Reveal } from "@/components/ui/motion";
import { PillLabel } from "@/components/ui/PillLabel";
import { createMetadata } from "@/lib/metadata";
import { contactItems } from "@/lib/site-data";

export const metadata = createMetadata({
  title: "Contact Spring 2 Health",
  description:
    "Contact Spring 2 Health for disability support enquiries, referrals, and service information across Queensland.",
  path: "/contact"
});

export default function ContactPage() {
  return (
    <>
      <PageHero
        pill="Contact Us"
        title={
          <>
            Let&apos;s start the <em className="font-heading text-brand-gold italic">conversation</em>
          </>
        }
        subtitle="Whether you are looking for support, guidance, or more information about our services, our team is here to help."
      />

      <section className="section-pad">
        <div className="container-shell grid gap-12 lg:grid-cols-[0.9fr_1.1fr]">
          <Reveal>
            <PillLabel className="mb-5">Get In Touch</PillLabel>
            <h2 className="section-heading">
              Support starts with a <em>simple conversation</em>
            </h2>
            <p className="section-copy mt-5 max-w-xl">
              Reach out to our team and we will get back to you as soon as
              possible. We are happy to discuss current supports, service
              suitability, referrals, and next steps.
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
            <ContactForm />
          </Reveal>
        </div>
      </section>
    </>
  );
}
