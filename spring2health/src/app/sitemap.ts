import type { MetadataRoute } from "next";

const siteUrl = "https://spring2health.com.au";

const routes = ["/", "/about", "/services", "/contact", "/referral"];

export default function sitemap(): MetadataRoute.Sitemap {
  return routes.map((path) => ({
    url: new URL(path, siteUrl).toString(),
    lastModified: new Date(),
    changeFrequency: path === "/" ? "weekly" : "monthly",
    priority: path === "/" ? 1 : 0.8
  }));
}
