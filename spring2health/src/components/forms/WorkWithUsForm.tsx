"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";

import { FormField } from "@/components/forms/FormField";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type WorkWithUsFormValues = {
  name: string;
  phone: string;
  email: string;
  message: string;
};

export function WorkWithUsForm() {
  const [status, setStatus] = useState<{
    type: "idle" | "success" | "error";
    message?: string;
  }>({ type: "idle" });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting }
  } = useForm<WorkWithUsFormValues>({
    defaultValues: {
      name: "",
      phone: "",
      email: "",
      message: ""
    }
  });

  async function onSubmit(values: WorkWithUsFormValues) {
    setStatus({ type: "idle" });

    const response = await fetch("/api/work-with-us", {
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
      message: data.message ?? "Thanks. Your application has been sent."
    });
  }

  return (
    <div className="panel-light rounded-[18px] p-8 sm:p-10">
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
        <div className="grid gap-5 md:grid-cols-2">
          <FormField label="Your Name" error={errors.name?.message} required>
            <input
              {...register("name", {
                required: "Your name is required."
              })}
              className="input-control"
              placeholder="Full name"
              aria-invalid={errors.name ? "true" : "false"}
            />
          </FormField>

          <FormField label="Contact Number" error={errors.phone?.message} required>
            <input
              {...register("phone", {
                required: "Contact number is required.",
                validate: (value) =>
                  isValidPhone(value) || "Please enter a valid phone number."
              })}
              className="input-control"
              placeholder="Phone number"
              aria-invalid={errors.phone ? "true" : "false"}
            />
          </FormField>
        </div>

        <FormField label="Email Address" error={errors.email?.message} required>
          <input
            {...register("email", {
              required: "Email address is required.",
              validate: (value) =>
                isValidEmail(value) || "Please enter a valid email address."
            })}
            className="input-control"
            placeholder="Email address"
            aria-invalid={errors.email ? "true" : "false"}
          />
        </FormField>

        <FormField
          label="Why do you want to work for us?"
          error={errors.message?.message}
          required
        >
          <textarea
            {...register("message", {
              required: "Please tell us a little about yourself."
            })}
            className="input-control min-h-[140px]"
            placeholder="Tell us about yourself..."
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
          {isSubmitting ? "Sending..." : "Send Application"}
        </button>
      </form>
    </div>
  );
}
