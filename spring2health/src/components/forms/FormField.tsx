type FormFieldProps = {
  label: string;
  error?: string;
  hint?: string;
  children: React.ReactNode;
  required?: boolean;
};

export function FormField({
  label,
  error,
  hint,
  children,
  required = false
}: FormFieldProps) {
  return (
    <label className="block">
      <span className="mb-2 block text-sm font-bold text-brand-black">
        {label}
        {required ? <span className="ml-1 text-brand-goldDeep">*</span> : null}
      </span>
      {children}
      {hint ? <span className="mt-2 block text-xs text-brand-muted">{hint}</span> : null}
      {error ? <span className="mt-2 block text-sm text-[#a64d39]">{error}</span> : null}
    </label>
  );
}
