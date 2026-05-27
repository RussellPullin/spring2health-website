"use client";

import {
  animate,
  motion,
  useInView,
  useReducedMotion
} from "framer-motion";
import { useEffect, useMemo, useRef, useState } from "react";

const fadeUpVariants = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0 }
};

export function Reveal({
  children,
  className,
  delay = 0
}: {
  children: React.ReactNode;
  className?: string;
  delay?: number;
}) {
  const prefersReducedMotion = useReducedMotion();

  if (prefersReducedMotion) {
    return <div className={className}>{children}</div>;
  }

  return (
    <motion.div
      className={className}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.2 }}
      variants={fadeUpVariants}
      transition={{ duration: 0.6, ease: "easeOut", delay }}
    >
      {children}
    </motion.div>
  );
}

export function Stagger({
  children,
  className
}: {
  children: React.ReactNode;
  className?: string;
}) {
  const prefersReducedMotion = useReducedMotion();

  if (prefersReducedMotion) {
    return <div className={className}>{children}</div>;
  }

  return (
    <motion.div
      className={className}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.2 }}
      variants={{
        hidden: {},
        visible: {
          transition: {
            staggerChildren: 0.13
          }
        }
      }}
    >
      {children}
    </motion.div>
  );
}

export function StaggerItem({
  children,
  className
}: {
  children: React.ReactNode;
  className?: string;
}) {
  const prefersReducedMotion = useReducedMotion();

  if (prefersReducedMotion) {
    return <div className={className}>{children}</div>;
  }

  return (
    <motion.div
      className={className}
      variants={fadeUpVariants}
      transition={{ duration: 0.6, ease: "easeOut" }}
    >
      {children}
    </motion.div>
  );
}

export function AnimatedValue({
  value,
  className
}: {
  value: string;
  className?: string;
}) {
  const ref = useRef<HTMLSpanElement | null>(null);
  const inView = useInView(ref, { once: true, amount: 0.6 });
  const prefersReducedMotion = useReducedMotion();
  const [displayValue, setDisplayValue] = useState(value);

  const parsed = useMemo(() => {
    const match = value.match(/^(\D*)(\d+)(.*)$/);

    if (!match) {
      return null;
    }

    return {
      prefix: match[1],
      number: Number(match[2]),
      suffix: match[3]
    };
  }, [value]);

  const renderedValue =
    !parsed || prefersReducedMotion || !inView ? value : displayValue;

  useEffect(() => {
    if (!parsed || prefersReducedMotion || !inView) {
      return;
    }

    const controls = animate(0, parsed.number, {
      duration: 1.1,
      ease: "easeOut",
      onUpdate(latest) {
        setDisplayValue(
          `${parsed.prefix}${Math.round(latest)}${parsed.suffix}`
        );
      }
    });

    return () => controls.stop();
  }, [inView, parsed, prefersReducedMotion, value]);

  return (
    <span ref={ref} className={className}>
      {renderedValue}
    </span>
  );
}
