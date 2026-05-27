import type { Metadata } from "next";

const siteUrl = "https://spring2health.com.au";
const siteName = "Spring 2 Health";

type MetadataInput = {
  title: string;
  description: string;
  path?: string;
};

export function createMetadata({
  title,
  description,
  path = "/"
}: MetadataInput): Metadata {
  const url = new URL(path, siteUrl).toString();

  return {
    metadataBase: new URL(siteUrl),
    title,
    description,
    alternates: {
      canonical: url
    },
    openGraph: {
      title,
      description,
      url,
      siteName,
      type: "website"
    },
    twitter: {
      card: "summary_large_image",
      title,
      description
    }
  };
}
