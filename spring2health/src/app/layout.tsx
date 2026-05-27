import type { Metadata } from "next";
import { Nunito, Playfair_Display } from "next/font/google";

import { Footer } from "@/components/layout/Footer";
import { Nav } from "@/components/layout/Nav";
import { createMetadata } from "@/lib/metadata";
import "../styles/globals.css";

const nunito = Nunito({
  subsets: ["latin"],
  variable: "--font-nunito",
  display: "swap"
});

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  display: "swap"
});

export const metadata: Metadata = createMetadata({
  title: "Spring 2 Health | Disability Support Queensland",
  description:
    "Spring 2 Health is an NDIS registered disability support provider offering person-centred support across Queensland."
});

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${nunito.variable} ${playfair.variable}`}>
      <body className="bg-brand-cream text-brand-ink antialiased">
        <Nav />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
