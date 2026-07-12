# Schema Recommendations — AI Pulse

> **Generated:** 2026-07-12
> **Domain:** aipulse-landing.vercel.app

---

## Current Schema Status

### Existing Schema: SoftwareApplication ✅

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "AI Pulse — Model Radar",
  "description": "Track AI models from 170+ companies in one clean, zero-build dashboard.",
  "url": "https://aipulse-landing.vercel.app/",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": [
    {
      "@type": "Offer",
      "name": "Personal Edition",
      "price": "29",
      "priceCurrency": "USD",
      "url": "https://tachyon80.gumroad.com/l/aipulse-personal"
    },
    {
      "@type": "Offer",
      "name": "Team Edition",
      "price": "99",
      "priceCurrency": "USD",
      "url": "https://tachyon80.gumroad.com/l/aipulse-team"
    }
  ]
}
```

---

## Recommended Schemas

### 1. FAQPage Schema (High Priority)

**Impact:** +15% AI visibility, featured snippet eligibility

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

### 2. Organization Schema (High Priority)

**Impact:** Brand authority, knowledge panel eligibility

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

### 3. WebSite Schema (Medium Priority)

**Impact:** Sitelinks, search functionality

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

### 4. BreadcrumbList Schema (Medium Priority)

**Impact:** Navigation context, rich results

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

### 5. Article Schema (For Blog Content)

**Impact:** Topical authority, news results

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

## Implementation Guide

### Step 1: Add to index.html

Place all JSON-LD scripts in the `<head>` section:

```html
<head>
  <!-- Existing SoftwareApplication schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    ...
  }
  </script>
  
  <!-- New FAQPage schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    ...
  }
  </script>
  
  <!-- New Organization schema -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    ...
  }
  </script>
</head>
```

### Step 2: Validate

Use Google Rich Results Test:
- https://search.google.com/test/rich-results

### Step 3: Monitor

Check Google Search Console for:
- Rich result impressions
- Click-through rates
- Index coverage

---

## Priority Matrix

| Schema | Priority | Effort | Impact |
|--------|----------|--------|--------|
| FAQPage | High | Low | +15% visibility |
| Organization | High | Low | Brand authority |
| WebSite | Medium | Low | Sitelinks |
| BreadcrumbList | Medium | Low | Navigation |
| Article | Low | Medium | Blog content |

---

## Validation Checklist

- [ ] All schemas pass Google Rich Results Test
- [ ] No duplicate schema types
- [ ] All required fields included
- [ ] URLs are absolute and correct
- [ ] Dates in ISO 8601 format
- [ ] Prices as strings, not numbers

---

**Next Review:** 2026-08-12
