export function cn(...values: Array<string | false | null | undefined>) {
  return values.filter(Boolean).join(" ");
}

export function isValidEmail(value: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}

export function isValidPhone(value: string) {
  return /^[\d+\s()/-]{8,}$/.test(value);
}

export function formatPhoneHref(value: string) {
  return `tel:${value.replace(/[^\d+]/g, "")}`;
}
