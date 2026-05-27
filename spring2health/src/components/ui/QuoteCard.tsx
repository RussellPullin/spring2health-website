type QuoteCardProps = {
  text: string;
  attribution: string;
};

export function QuoteCard({ text, attribution }: QuoteCardProps) {
  return (
    <blockquote className="panel-dark rounded-card p-8 sm:p-10">
      <p className="font-heading text-2xl italic leading-10 text-white sm:text-3xl">
        &ldquo;{text}&rdquo;
      </p>
      <footer className="mt-6 text-sm font-semibold uppercase tracking-[0.16em] text-brand-gold">
        {attribution}
      </footer>
    </blockquote>
  );
}
