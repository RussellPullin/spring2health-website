import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          gold: "#d8b36a",
          goldDeep: "#b88a34",
          black: "#121212",
          ink: "#1f1f1f",
          cream: "#f7f2e9",
          creamDark: "#efe5d4",
          sand: "#e6d6b7",
          muted: "#6f675b"
        }
      },
      fontFamily: {
        heading: ["var(--font-playfair)", "serif"],
        body: ["var(--font-nunito)", "sans-serif"]
      },
      boxShadow: {
        gold: "0 18px 40px rgba(184, 138, 52, 0.18)",
        soft: "0 14px 30px rgba(18, 18, 18, 0.08)"
      },
      borderRadius: {
        card: "14px",
        input: "8px",
        pill: "100px"
      },
      backgroundImage: {
        "hero-radial":
          "radial-gradient(circle at top, rgba(216, 179, 106, 0.28), transparent 46%)",
        "dot-grid":
          "radial-gradient(circle, rgba(216, 179, 106, 0.22) 1.2px, transparent 1.2px)"
      },
      backgroundSize: {
        dots: "24px 24px"
      },
      keyframes: {
        float: {
          "0%, 100%": { transform: "translateY(0px)" },
          "50%": { transform: "translateY(-8px)" }
        }
      },
      animation: {
        float: "float 6s ease-in-out infinite"
      }
    }
  },
  plugins: []
};

export default config;
