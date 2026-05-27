"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";

import { FormField } from "@/components/forms/FormField";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type ContactFormValues = {
  firstName: string;
  lastName: string;
  phone: string;
  email: string;
  message: string;
};

type ContactFormProps = {
  title?: string;
  subtitle?: string;
  endpoint?: string;
  submitLabel?: string;
};

export function ContactForm({
  title = "Send us a message",
  subtitle = "We'll get back to you as soon as possible.",
  endpoint = "/api/contact",
  submitLabel = "Send Message"
}: ContactFormProps) {
  const [status, setStatus] = useState<{
    type: "idle" | "success" | "error";
    message?: string;
  }>({ type: "idle" });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting }
  } = useForm<ContactFormValues>({
    defaultValues: {
      firstName: "",
      lastName: "",
      phone: "",
      email: "",
      message: ""
    }
  });

  async function onSubmit(values: ContactFormValues) {
    setStatus({ type: "idle" });

    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values)
    });

    const data = (await response.json()) as { message?: string };

    if (!response.ok) {
      setStatus({
        type: "error",
        message: data.message ?? "Something went wrong. Please try again."
      });
      return;
    }

    reset();
    setStatus({
      type: "success",
      message: data.message ?? "Thanks. Your message has been sent."
    });
  }

  return (
    <div className="panel-light rounded-[18px] p-8 sm:p-10">
      <h3 className="text-2xl font-bold tracking-[-0.03em] text-brand-black">
        {title}
      </h3>
      <p className="mt-2 text-sm leading-7 text-brand-muted">{subtitle}</p>

      <form onSubmit={handleSubmit(onSubmit)} className="mt-8 space-y-5">
        <div className="grid gap-5 md:grid-cols-2">
          <FormField label="First Name" error={errors.firstName?.message} required>
            <input
              {...register("firstName", {
                required: "First name is required."
              })}
              className="input-control"
              placeholder="First name"
              aria-invalid={errors.firstName ? "true" : "false"}
            />
          </FormField>

          <FormField label="Last Name" error={errors.lastName?.message} required>
            <input
              {...register("lastName", {
                required: "Last name is required."
              })}
              className="input-control"
              placeholder="Last name"
              aria-invalid={errors.lastName ? "true" : "false"}
            />
          </FormField>
        </div>

        <FormField label="Contact Number" error={errors.phone?.message} required>
          <input
            {...register("phone", {
              required: "Phone number is required.",
              validate: (value) =>
                isValidPhone(value) || "Please enter a valid phone number."
            })}
            className="input-control"
            placeholder="Your phone number"
            aria-invalid={errors.phone ? "true" : "false"}
          />
        </FormField>

        <FormField label="Email Address" error={errors.email?.message} required>
          <input
            {...register("email", {
              required: "Email address is required.",
              validate: (value) =>
                isValidEmail(value) || "Please enter a valid email address."
            })}
            className="input-control"
            placeholder="Your email address"
            aria-invalid={errors.email ? "true" : "false"}
          />
        </FormField>

        <FormField label="Your Message" error={errors.message?.message} required>
          <textarea
            {...register("message", {
              required: "Please add a message."
            })}
            className="input-control min-h-[140px]"
            placeholder="How can we help you?"
            aria-invalid={errors.message ? "true" : "false"}
          />
        </FormField>

        {status.message ? (
          <p
            className={
              status.type === "success"
                ? "text-sm text-[#1f6d43]"
                : "text-sm text-[#a64d39]"
            }
          >
            {status.message}
          </p>
        ) : null}

        <button type="submit" disabled={isSubmitting} className="btn-primary w-full">
          {isSubmitting ? "Sending..." : submitLabel}
        </button>
      </form>
    </div>
  );
}
