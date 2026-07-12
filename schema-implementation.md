# Schema Implementation — AI Pulse

> **Generated:** 2026-07-12
> **Domain:** aipulse-landing.vercel.app

---

## Implemented Schemas

### 1. SoftwareApplication ✅

**Status:** Implemented
**Location:** index.html `<head>` section

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "AI Pulse — Model Radar",
  "description": "Track AI models from 170+ companies in one clean, zero-build dashboard. Compare parameters, context window, pricing, benchmarks, licensing, and community traction.",
  "url": "https://aipulse-landing.vercel.app/",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": [
    {
      "@type": "Offer",
      "name": "Personal Edition",
      "price": "29",
      "priceCurrency": "USD",
      "description": "Single user, lifetime access, one-time payment",
      "url": "https://tachyon80.gumroad.com/l/aipulse-personal",
      "availability": "https://schema.org/InStock"
    },
    {
      "@type": "Offer",
      "name": "Team Edition",
      "price": "99",
      "priceCurrency": "USD",
      "description": "Multiple users, lifetime access, one-time payment",
      "url": "https://tachyon80.gumroad.com/l/aipulse-team",
      "availability": "https://schema.org/InStock"
    }
  ],
  "featureList": [
    "600+ AI models from 170+ companies",
    "Side-by-side model comparison",
    "Export as PDF, PNG, CSV",
    "Provider Radar — free tier detection",
    "Cost analysis — pricing per 1K and 1M tokens",
    "10 interactive charts",
    "Instant search and smart filters",
    "Self-updating Python pipeline",
    "Dark/light themes",
    "Responsive layout"
  ],
  "screenshot": "https://aipulse-landing.vercel.app/dashboard-top.png",
  "softwareVersion": "3.0",
  "datePublished": "2026-01-01",
  "author": {
    "@type": "Person",
    "name": "Alp Erk",
    "url": "https://github.com/T-a-c-h-y-o-n"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AI Pulse",
    "url": "https://github.com/T-a-c-h-y-o-n/aipulse"
  },
  "sameAs": [
    "https://github.com/T-a-c-h-y-o-n/aipulse",
    "https://www.producthunt.com/products/ai-pulse-model-radar"
  ]
}
```

**Validation:** ✅ Passes Google Rich Results Test

---

### 2. Organization ✅

**Status:** Implemented
**Location:** index.html `<head>` section

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AI Pulse",
  "url": "https://aipulse-landing.vercel.app/",
  "logo": "https://aipulse-landing.vercel.app/pulse2.png",
  "description": "AI Pulse tracks 600+ AI models from 170+ companies in one HTML file.",
  "founder": {
    "@type": "Person",
    "name": "Alp Erk",
    "url": "https://github.com/T-a-c-h-y-o-n"
  },
  "sameAs": [
    "https://github.com/T-a-c-h-y-o-n/aipulse",
    "https://www.producthunt.com/products/ai-pulse-model-radar"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "Tachyonic@gmail.com",
    "contactType": "customer service"
  }
}
```

**Validation:** ✅ Passes Google Rich Results Test

---

### 3. WebSite ✅

**Status:** Implemented
**Location:** index.html `<head>` section

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "AI Pulse — Model Radar",
  "url": "https://aipulse-landing.vercel.app/",
  "description": "Compare 600+ AI models in one file",
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://aipulses.vercel.app/?search={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

**Validation:** ✅ Passes Google Rich Results Test

---

### 4. FAQPage ✅

**Status:** Implemented
**Location:** index.html `<head>` section

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is AI Pulse?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI Pulse is a single-file HTML dashboard that compares 600+ AI models from 170+ companies. It shows pricing, benchmarks, context windows, and licensing in one place. No backend, no install — just open and go."
      }
    },
    {
      "@type": "Question",
      "name": "How much does AI Pulse cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI Pulse Personal Edition costs $29 (one-time payment, single user, lifetime access). Team Edition costs $99 (one-time payment, multiple users). No subscription required."
      }
    },
    {
      "@type": "Question",
      "name": "How do I update AI Pulse with new models?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Run the included Python update script (tools/pipeline.py). It pulls new models from HuggingFace and OpenRouter automatically. No extra packages required — just Python 3.8+."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a free demo?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes! Try the free demo at https://aipulses.vercel.app/ — it includes ~50 models with full comparison features."
      }
    },
    {
      "@type": "Question",
      "name": "What data sources does AI Pulse use?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI Pulse pulls data from HuggingFace and OpenRouter, covering 600+ models from 170+ companies. Data includes pricing, benchmarks, context windows, and licensing."
      }
    },
    {
      "@type": "Question",
      "name": "Can I export comparison data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes! AI Pulse supports exporting as PDF, PNG, and CSV. You can also use 10 interactive charts for visual analysis."
      }
    }
  ]
}
```

**Validation:** ✅ Passes Google Rich Results Test

---

### 5. BreadcrumbList ✅

**Status:** Implemented
**Location:** index.html `<head>` section

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://aipulse-landing.vercel.app/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Features",
      "item": "https://aipulse-landing.vercel.app/#features"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Pricing",
      "item": "https://aipulse-landing.vercel.app/#pricing"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "FAQ",
      "item": "https://aipulse-landing.vercel.app/#faq"
    }
  ]
}
```

**Validation:** ✅ Passes Google Rich Results Test

---

## Blog Post Schemas

### Article Schema (For Blog Posts)

**Status:** Ready for implementation
**Location:** Blog post HTML files

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Compare AI Models: A Complete Guide",
  "description": "Learn how to compare AI models effectively using pricing, benchmarks, and context windows.",
  "author": {
    "@type": "Person",
    "name": "Alp Erk"
  },
  "publisher": {
    "@type": "Organization",
    "name": "AI Pulse",
    "logo": {
      "@type": "ImageObject",
      "url": "https://aipulse-landing.vercel.app/pulse2.png"
    }
  },
  "datePublished": "2026-07-12",
  "dateModified": "2026-07-12",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://aipulse-landing.vercel.app/blog/how-to-compare-ai-models"
  }
}
```

---

## Validation Checklist

- [x] All schemas pass Google Rich Results Test
- [x] No duplicate schema types
- [x] All required fields included
- [x] URLs are absolute and correct
- [x] Dates in ISO 8601 format
- [x] Prices as strings, not numbers
- [x] Contact information complete
- [x] Social media links included

---

## Monitoring

### Weekly

- Check Google Search Console for schema errors
- Monitor rich result impressions
- Review click-through rates

### Monthly

- Validate all schemas with Google Rich Results Test
- Check for new schema opportunities
- Update schemas as needed

### Quarterly

- Full schema audit
- Competitor schema analysis
- Strategy adjustment

---

## Next Steps

1. **Monitor Performance**
   - Track rich result impressions in Search Console
   - Monitor click-through rates
   - Review AI visibility

2. **Expand Schema Coverage**
   - Add Article schema for blog posts
   - Consider Product schema for detailed pricing
   - Add Review schema when available

3. **Stay Updated**
   - Follow Schema.org updates
   - Monitor Google's structured data guidelines
   - Adapt to new rich result types

---

**Last Updated:** 2026-07-12
**Next Review:** 2026-08-12
