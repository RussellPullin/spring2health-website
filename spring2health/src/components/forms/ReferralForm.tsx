"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";

import { FormField } from "@/components/forms/FormField";
import { company } from "@/lib/site-data";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type ReferralFormValues = {
  referrerName: string;
  referrerPhone: string;
  referrerEmail: string;
  relationship: string;
  participantName: string;
  participantPhone: string;
  participantEmail: string;
  fundManagement: string;
  additionalInformation: string;
};

export function ReferralForm() {
  const [status, setStatus] = useState<{
    type: "idle" | "success" | "error";
    message?: string;
  }>({ type: "idle" });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting }
  } = useForm<ReferralFormValues>({
    defaultValues: {
      referrerName: "",
      referrerPhone: "",
      referrerEmail: "",
      relationship: "",
      participantName: "",
      participantPhone: "",
      participantEmail: "",
      fundManagement: "",
      additionalInformation: ""
    }
  });

  async function onSubmit(values: ReferralFormValues) {
    setStatus({ type: "idle" });

    const response = await fetch("/api/referral", {
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
      message: data.message ?? "Thanks. Your referral has been submitted."
    });
  }

  return (
    <div className="panel-light rounded-[18px] p-8 sm:p-10">
      <h3 className="text-2xl font-bold tracking-[-0.03em] text-brand-black">
        Submit a referral
      </h3>
      <p className="mt-2 text-sm leading-7 text-brand-muted">
        Share the details below and our team will be in touch to discuss the
        next steps.
      </p>

      <form onSubmit={handleSubmit(onSubmit)} className="mt-8 space-y-8">
        <div>
          <p className="mb-4 text-xs font-bold uppercase tracking-[0.18em] text-brand-goldDeep">
            Referrer Details
          </p>
          <div className="grid gap-5 md:grid-cols-2">
            <FormField label="Referrer Name" error={errors.referrerName?.message} required>
              <input
                {...register("referrerName", {
                  required: "Referrer name is required."
                })}
                className="input-control"
                placeholder="Your full name"
                aria-invalid={errors.referrerName ? "true" : "false"}
              />
            </FormField>

            <FormField
              label="Contact Number"
              error={errors.referrerPhone?.message}
              required
            >
              <input
                {...register("referrerPhone", {
                  required: "Contact number is required.",
                  validate: (value) =>
                    isValidPhone(value) || "Please enter a valid phone number."
                })}
                className="input-control"
                placeholder="Your phone number"
                aria-invalid={errors.referrerPhone ? "true" : "false"}
              />
            </FormField>

            <FormField
              label="Email Address"
              error={errors.referrerEmail?.message}
              required
            >
              <input
                {...register("referrerEmail", {
                  required: "Email address is required.",
                  validate: (value) =>
                    isValidEmail(value) || "Please enter a valid email address."
                })}
                className="input-control"
                placeholder="Your email address"
                aria-invalid={errors.referrerEmail ? "true" : "false"}
              />
            </FormField>

            <FormField
              label="Relationship to Participant"
              error={errors.relationship?.message}
              required
            >
              <input
                {...register("relationship", {
                  required: "Please describe your relationship to the participant."
                })}
                className="input-control"
                placeholder="e.g. Guardian, Case Worker"
                aria-invalid={errors.relationship ? "true" : "false"}
              />
            </FormField>
          </div>
        </div>

        <div>
          <p className="mb-4 text-xs font-bold uppercase tracking-[0.18em] text-brand-goldDeep">
            Participant Details
          </p>
          <div className="grid gap-5 md:grid-cols-2">
            <FormField
              label="Participant Name"
              error={errors.participantName?.message}
              required
            >
              <input
                {...register("participantName", {
                  required: "Participant name is required."
                })}
                className="input-control"
                placeholder="Participant's full name"
                aria-invalid={errors.participantName ? "true" : "false"}
              />
            </FormField>

            <FormField
              label="Contact Number"
              error={errors.participantPhone?.message}
              required
            >
              <input
                {...register("participantPhone", {
                  required: "Participant phone number is required.",
                  validate: (value) =>
                    isValidPhone(value) || "Please enter a valid phone number."
                })}
                className="input-control"
                placeholder="Participant's phone"
                aria-invalid={errors.participantPhone ? "true" : "false"}
              />
            </FormField>

            <div className="md:col-span-2">
              <FormField
                label="Participant Email"
                error={errors.participantEmail?.message}
                required
              >
                <input
                  {...register("participantEmail", {
                    required: "Participant email is required.",
                    validate: (value) =>
                      isValidEmail(value) || "Please enter a valid email address."
                  })}
                  className="input-control"
                  placeholder="Participant's email address"
                  aria-invalid={errors.participantEmail ? "true" : "false"}
                />
              </FormField>
            </div>

            <div className="md:col-span-2">
              <FormField
                label="Fund Management"
                error={errors.fundManagement?.message}
                required
              >
                <select
                  {...register("fundManagement", {
                    required: "Please select a fund management option."
                  })}
                  className="input-control"
                  aria-invalid={errors.fundManagement ? "true" : "false"}
                >
                  <option value="">Select fund management type</option>
                  {company.fundManagement.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </FormField>
            </div>

            <div className="md:col-span-2">
              <FormField
                label="Additional Information"
                error={errors.additionalInformation?.message}
                required
              >
                <textarea
                  {...register("additionalInformation", {
                    required: "Please provide some background information."
                  })}
                  className="input-control min-h-[150px]"
                  placeholder="Tell us about the participant's goals, support needs, or any relevant background..."
                  aria-invalid={errors.additionalInformation ? "true" : "false"}
                />
              </FormField>
            </div>
          </div>
        </div>

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
          {isSubmitting ? "Submitting..." : "Submit Referral"}
        </button>
      </form>
    </div>
  );
}
