export const company = {
  name: "Spring 2 Health",
  formerName: "Pristine Lifestyle Solutions",
  phone: "0468 404 865",
  phoneHref: "tel:0468404865",
  email: "info@spring2health.com.au",
  emailHref: "mailto:info@spring2health.com.au",
  address: "PO Box 460, Sanctuary Cove QLD 4212",
  locationLabel: "Sanctuary Cove, Queensland",
  ndisStatus: "NDIS Registered Provider",
  fundManagement: ["NDIA Managed", "Plan Managed", "Self Managed"]
} as const;

export const navigationLinks = [
  { href: "/", label: "Home" },
  { href: "/about", label: "About" },
  { href: "/services", label: "Services" },
  { href: "/contact", label: "Contact" }
] as const;

export const homeHero = {
  pill: "NDIS Registered Provider - Queensland",
  title: "Providing you with the support you",
  accent: "truly deserve",
  subtitle:
    "We take a holistic, strength-based, person-centred approach, working in close partnership with you, your family, and your support network.",
  highlights: [
    "Specialists in Mental Health & Psychosocial Disability",
    "Supported Independent Living & Respite",
    "Social Work & Therapeutic Services",
    "Adventure Therapy & Community Access"
  ],
  floatingCards: [
    {
      icon: "🏠",
      title: "Supported Independent Living",
      description:
        "Personalised 24/7 care plans supporting people to live independently."
    },
    {
      icon: "🌿",
      title: "Adventure Therapy",
      description:
        "Innovative outdoor programs designed to build resilience and wellbeing."
    },
    {
      icon: "🤝",
      title: "Social Work & Counselling",
      description:
        "Qualified practitioners guiding participants and families through complex needs."
    },
    {
      icon: "🌐",
      title: "Community Access",
      description:
        "Support to engage, participate, and build meaningful community connections."
    }
  ]
} as const;

export const stats = [
  { value: "6+", label: "Support Services" },
  { value: "24/7", label: "Support Available" },
  { value: "NDIS", label: "Registered Provider" },
  { value: "QLD", label: "Queensland Based" }
] as const;

export const values = [
  {
    icon: "🎯",
    title: "Uniquely Tailored to You",
    description:
      "Support designed around individual needs, goals, and aspirations."
  },
  {
    icon: "🤝",
    title: "Collaborative by Nature",
    description:
      "Working alongside participants, families, and the wider support network."
  },
  {
    icon: "💡",
    title: "Deeper Understanding",
    description:
      "Operating from curiosity to understand strengths, challenges, and aspirations."
  },
  {
    icon: "⚖️",
    title: "Fairness & Transparency",
    description:
      "Providing honest, professional support built on trust and integrity."
  }
] as const;

export const quote = {
  text:
    "We provide support differently. Most organisations think of their bottom line. We're in this for our participants.",
  attribution: "Spring 2 Health - Our Promise"
} as const;

export const whyPoints = [
  {
    number: "01",
    title: "Individualised Care Plans",
    description:
      "Every participant receives a personalised plan built around their needs, goals, and aspirations."
  },
  {
    number: "02",
    title: "Holistic, Collaborative Approach",
    description:
      "Support is delivered in partnership with participants, families, carers, and the full care network."
  },
  {
    number: "03",
    title: "Mental Health Specialists",
    description:
      "We bring deep experience in psychosocial disability and mental health-informed support."
  },
  {
    number: "04",
    title: "Innovation & Adventure",
    description:
      "From community access to outdoor therapeutic experiences, we use creative and practical supports."
  }
] as const;

export const services = [
  {
    slug: "supported-independent-living",
    icon: "🏠",
    title: "Supported Independent Living",
    shortDescription:
      "24/7 personalised support helping participants live independently with dignity.",
    description:
      "We support daily living, personal care, meal preparation, and community access through personalised care plans that are reviewed regularly and shaped around each participant.",
    bullets: [
      "Help with daily living tasks and personal care",
      "Meal preparation and household management",
      "Community access support and accompaniment",
      "Personalised care plans reviewed regularly",
      "24/7 availability where required",
      "Safe and supportive living environment"
    ]
  },
  {
    slug: "social-work-services",
    icon: "🤝",
    title: "Social Work Services",
    shortDescription:
      "Qualified social workers providing advocacy, counselling, and practical support.",
    description:
      "Our social work team helps participants and families navigate complex challenges, build strong support plans, and access the right services and advocacy when they need it most.",
    bullets: [
      "Individual and family counselling",
      "Advocacy and rights support",
      "Referrals to community services",
      "Support plan development",
      "Collaboration with the full care team",
      "NDIS guidance and coordination support"
    ]
  },
  {
    slug: "respite-care",
    icon: "🌿",
    title: "Respite Care",
    shortDescription:
      "Flexible respite options that give participants and caregivers room to recharge.",
    description:
      "We offer in-home, centre-based, and community-based respite support with flexible arrangements that provide high-quality care while giving carers and families time to rest.",
    bullets: [
      "In-home respite support",
      "Centre-based and community-based options",
      "Short and medium term accommodation",
      "Flexible scheduling around participant needs",
      "Experienced and compassionate care team",
      "Safe and reliable support environments"
    ]
  },
  {
    slug: "community-access",
    icon: "🌐",
    title: "Community Access",
    shortDescription:
      "Helping participants build confidence, connection, and belonging in the community.",
    description:
      "We support participants to engage with local events, services, and activities that match their interests, build relationships, and strengthen independence and inclusion.",
    bullets: [
      "Attendance at community events and activities",
      "Access to local services and programs",
      "Building meaningful social connections",
      "Transport and accompaniment support",
      "Plans tailored to individual interests",
      "Support to reduce barriers to participation"
    ]
  },
  {
    slug: "counselling-services",
    icon: "💬",
    title: "Counselling Services",
    shortDescription:
      "Evidence-based therapeutic support focused on wellbeing, resilience, and coping.",
    description:
      "Our counselling services support participants with mental health, trauma, anxiety, depression, and emotional wellbeing through practical, person-centred therapeutic approaches.",
    bullets: [
      "Individual and group counselling",
      "Cognitive behavioural therapy informed support",
      "Trauma-informed therapeutic approaches",
      "Anxiety and depression management",
      "Resilience and coping strategy development",
      "Support aligned with participant goals and plans"
    ]
  },
  {
    slug: "adventure-therapy",
    icon: "⛺",
    title: "Adventure Therapy",
    shortDescription:
      "Outdoor experiences that support growth, resilience, confidence, and wellbeing.",
    description:
      "Adventure therapy creates safe, supported opportunities for participants to challenge themselves outdoors while building resilience, self-esteem, emotional regulation, and connection.",
    bullets: [
      "Hiking, camping, climbing, and outdoor activities",
      "Programs tailored to individual needs",
      "Resilience and confidence building",
      "Mental health support through outdoor engagement",
      "Fully supported and safe participation",
      "Experienced staff guiding each activity"
    ]
  },
  {
    slug: "positive-behaviour-support-plans",
    icon: "📋",
    title: "Positive Behaviour Support Plans",
    shortDescription:
      "Proactive plans that build safety, understanding, and long-term positive outcomes.",
    description:
      "We develop practical, person-centred PBS plans that focus on proactive strategies, collaboration, and long-term support for participants and their wider care team.",
    bullets: [
      "Comprehensive Positive Behaviour Support Plans",
      "Proactive rather than reactive strategies",
      "Collaboration with the full support network",
      "Practical coping tools and strategies",
      "Plans tailored to unique participant needs",
      "Regular review and adaptation"
    ]
  }
] as const;

export const contactItems = [
  { icon: "📞", label: "Phone", value: company.phone, href: company.phoneHref },
  { icon: "✉️", label: "Email", value: company.email, href: company.emailHref },
  { icon: "📍", label: "Location", value: company.address },
  {
    icon: "💳",
    label: "Fund Management",
    value: company.fundManagement.join(" - ")
  }
] as const;

export const footerServices = services.slice(0, 6).map((service) => ({
  label: service.title,
  href: "/services"
}));

export const workWithUsIntro =
  "We'd love to hear from passionate people who share our values and approach to support. If you want to work with Spring 2 Health, send us your details and tell us why this work matters to you.";
