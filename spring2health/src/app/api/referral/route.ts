import { NextResponse } from "next/server";

import { sendSiteEmail } from "@/lib/email";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type ReferralPayload = {
  referrerName?: string;
  referrerPhone?: string;
  referrerEmail?: string;
  relationship?: string;
  participantName?: string;
  participantPhone?: string;
  participantEmail?: string;
  fundManagement?: string;
  additionalInformation?: string;
};

export async function POST(request: Request) {
  const body = (await request.json()) as ReferralPayload;

  const requiredFields = [
    body.referrerName,
    body.referrerPhone,
    body.referrerEmail,
    body.relationship,
    body.participantName,
    body.participantPhone,
    body.participantEmail,
    body.fundManagement,
    body.additionalInformation
  ];

  if (requiredFields.some((field) => !field)) {
    return NextResponse.json(
      { message: "Please complete all required fields before submitting." },
      { status: 400 }
    );
  }

  if (
    !isValidPhone(body.referrerPhone as string) ||
    !isValidPhone(body.participantPhone as string) ||
    !isValidEmail(body.referrerEmail as string) ||
    !isValidEmail(body.participantEmail as string)
  ) {
    return NextResponse.json(
      { message: "Please provide valid phone numbers and email addresses." },
      { status: 400 }
    );
  }

  const result = await sendSiteEmail(
    "New Spring 2 Health referral",
    `
      <h2>Referral submission</h2>
      <h3>Referrer details</h3>
      <p><strong>Name:</strong> ${body.referrerName}</p>
      <p><strong>Phone:</strong> ${body.referrerPhone}</p>
      <p><strong>Email:</strong> ${body.referrerEmail}</p>
      <p><strong>Relationship:</strong> ${body.relationship}</p>
      <h3>Participant details</h3>
      <p><strong>Name:</strong> ${body.participantName}</p>
      <p><strong>Phone:</strong> ${body.participantPhone}</p>
      <p><strong>Email:</strong> ${body.participantEmail}</p>
      <p><strong>Fund management:</strong> ${body.fundManagement}</p>
      <p><strong>Additional information:</strong></p>
      <p>${(body.additionalInformation as string).replace(/\n/g, "<br />")}</p>
    `,
    { replyTo: body.referrerEmail }
  );

  return NextResponse.json({
    message: result.delivered
      ? "Thanks. Your referral has been submitted."
      : "Thanks. Your referral was recorded and email delivery is currently not configured."
  });
}
