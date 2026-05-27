import { Resend } from "resend";

const resendApiKey = process.env.RESEND_API_KEY;
const resendToEmail = process.env.RESEND_TO_EMAIL;
const resendFromEmail =
  process.env.RESEND_FROM_EMAIL ??
  "Spring 2 Health <noreply@spring2health.com.au>";

export function canSendEmail() {
  return Boolean(resendApiKey && resendToEmail);
}

type SendSiteEmailOptions = {
  replyTo?: string;
};

export async function sendSiteEmail(
  subject: string,
  html: string,
  options: SendSiteEmailOptions = {}
) {
  if (!canSendEmail()) {
    return {
      delivered: false,
      reason:
        "Email delivery skipped because RESEND_API_KEY or RESEND_TO_EMAIL is not configured."
    };
  }

  const resend = new Resend(resendApiKey);

  await resend.emails.send({
    from: resendFromEmail,
    to: resendToEmail as string,
    replyTo: options.replyTo,
    subject,
    html
  });

  return { delivered: true };
}
