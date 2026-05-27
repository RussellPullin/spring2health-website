import { NextResponse } from "next/server";

import { sendSiteEmail } from "@/lib/email";
import { isValidEmail, isValidPhone } from "@/lib/utils";

type WorkPayload = {
  name?: string;
  phone?: string;
  email?: string;
  message?: string;
};

export async function POST(request: Request) {
  const body = (await request.json()) as WorkPayload;

  if (!body.name || !body.phone || !body.email || !body.message) {
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
    "New Spring 2 Health work with us enquiry",
    `
      <h2>Work with us enquiry</h2>
      <p><strong>Name:</strong> ${body.name}</p>
      <p><strong>Phone:</strong> ${body.phone}</p>
      <p><strong>Email:</strong> ${body.email}</p>
      <p><strong>Why they want to work with us:</strong></p>
      <p>${body.message.replace(/\n/g, "<br />")}</p>
    `,
    { replyTo: body.email }
  );

  return NextResponse.json({
    message: result.delivered
      ? "Thanks. Your application has been sent."
      : "Thanks. Your application was recorded and email delivery is currently not configured."
  });
}
