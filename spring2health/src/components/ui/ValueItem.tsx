type ValueItemProps = {
  icon: string;
  title: string;
  description: string;
};

export function ValueItem({ icon, title, description }: ValueItemProps) {
  return (
    <article className="panel-light rounded-card p-7">
      <div className="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-brand-gold/15 text-2xl">
        {icon}
      </div>
      <h3 className="text-xl font-bold text-brand-black">{title}</h3>
      <p className="mt-3 text-sm leading-7 text-brand-muted">{description}</p>
    </article>
  );
}
