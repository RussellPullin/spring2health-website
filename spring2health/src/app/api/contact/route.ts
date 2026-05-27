import { NextResponse } from "next/server";

import { sendSiteEmail } from "@/lib/email";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type ContactPayload = {
  firstName?: string;
  lastName?: string;
  phone?: string;
  email?: string;
  message?: string;
};

export async function POST(request: Request) {
  const body = (await request.json()) as ContactPayload;

  if (
    !body.firstName ||
    !body.lastName ||
    !body.phone ||
    !body.email ||
    !body.message
  ) {
    return NextResponse.json(
      { message: "Please complete all required fields." },
      { status: 400 }
    );
  }

  if (!isValidPhone(body.phone) || !isValidEmail(body.email)) {
    return NextResponse.json(
      { message: "Please provide a valid phone number and email address." },
      { status: 400 }
    );
  }

  const result = await sendSiteEmail(
    "New Spring 2 Health contact enquiry",
    `
      <h2>Contact enquiry</h2>
      <p><strong>Name:</strong> ${body.firstName} ${body.lastName}</p>
      <p><strong>Phone:</strong> ${body.phone}</p>
      <p><strong>Email:</strong> ${body.email}</p>
      <p><strong>Message:</strong></p>
      <p>${body.message.replace(/\n/g, "<br />")}</p>
    `,
    { replyTo: body.email }
  );

  return NextResponse.json({
    message: result.delivered
      ? "Thanks. Your message has been sent."
      : "Thanks. Your message was recorded and email delivery is currently not configured."
  });
}
