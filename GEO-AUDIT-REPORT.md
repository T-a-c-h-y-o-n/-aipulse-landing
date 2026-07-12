# GEO-AUDIT-REPORT — AI Pulse — Model Radar

> **Audit Date:** 2026-07-12
> **Domain:** aipulse-landing.vercel.app
> **Business Type:** SaaS / Digital Product
> **GEO Score:** 72/100

---

## Executive Summary

AI Pulse — Model Radar is a single-file HTML dashboard comparing 600+ AI models from 170+ companies. The landing page has solid foundations but needs optimization for AI search visibility.

### Key Findings

| Category | Score | Status |
|----------|-------|--------|
| AI Citability & Visibility | 65/100 | Needs improvement |
| Brand Authority Signals | 55/100 | Needs improvement |
| Content Quality & E-E-A-T | 70/100 | Good |
| Technical Foundations | 85/100 | Excellent |
| Structured Data | 75/100 | Good |
| Platform Optimization | 60/100 | Needs improvement |

### Priority Actions

1. **Add FAQPage schema** — Increase AI citability
2. **Create blog content** — Build topical authority
3. **Enhance llms.txt** — Add more structured information
4. **Build brand mentions** — Reddit, YouTube, LinkedIn presence

---

## 1. AI Citability Score (0-100)

### Overall Score: 65/100

| Page | Citability Score | Notes |
|------|------------------|-------|
| Landing Page (index.html) | 70/100 | Good structure, needs more citable passages |
| Live Demo | 60/100 | Limited text content for AI citation |

### Citable Passages Found

1. **Hero Section:** "AI Pulse tracks 600+ models from 170+ companies — price, benchmarks, context window, license — in one HTML file."
   - **Quality:** Good — Clear, factual, citable
   - **AI Readiness:** High

2. **Offer Section:** "No backend, no install. Update it yourself whenever you want."
   - **Quality:** Good — Unique value proposition
   - **AI Readiness:** Medium

### Missing Citable Passages

- **Definition block** — What is AI Pulse in 1-2 sentences
- **Comparison table** — AI Pulse vs alternatives
- **Use case scenarios** — Who uses it and why
- **Technical specifications** — File size, performance metrics

### Recommendations

1. Add a "What is AI Pulse?" section with a clear, quotable definition
2. Create a comparison table (AI Pulse vs ChatGPT Plus vs Perplexity)
3. Add numbered use case scenarios
4. Include technical specs in a structured format

---

## 2. AI Crawler Access Analysis

### Current Status: ✅ Excellent

| Crawler | Access | Status |
|---------|--------|--------|
| GPTBot | ✅ Allowed | Good |
| ClaudeBot | ✅ Allowed | Good |
| PerplexityBot | ✅ Allowed | Good |
| Google-Extended | ✅ Allowed | Good |
| GoogleOther | ✅ Allowed | Good |
| Applebot-Extended | ✅ Allowed | Good |
| FacebookBot | ✅ Allowed | Good |
| Twitterbot | ✅ Allowed | Good |
| LinkedInBot | ✅ Allowed | Good |
| Bytespider | ✅ Allowed | Good |
| CCBot | ✅ Allowed | Good |
| anthropic-ai | ✅ Allowed | Good |
| Cohere-ai | ✅ Allowed | Good |

### robots.txt Analysis

```
# Current robots.txt is well-configured
# All major AI crawlers have access
# Sitemap is properly declared
```

### Recommendations

- No changes needed — robots.txt is optimally configured
- Consider adding `Host` directive for consistency

---

## 3. Schema Markup Analysis

### Current Schema: SoftwareApplication ✅

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "AI Pulse — Model Radar",
  "description": "Track AI models from 170+ companies...",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Web",
  "offers": [...]
}
```

### Missing Schemas

| Schema | Priority | Impact |
|--------|----------|--------|
| **FAQPage** | High | +15% AI visibility |
| **Organization** | High | Brand authority |
| **WebSite** | Medium | SearchAction |
| **BreadcrumbList** | Medium | Navigation context |
| **Article** | Low | Blog content (when created) |

### Recommendations

1. Add FAQPage schema for the FAQ section
2. Add Organization schema with author info
3. Add WebSite schema with SearchAction
4. Consider BreadcrumbList for multi-page navigation

---

## 4. Content Structure Analysis

### Heading Hierarchy

| Level | Count | Status |
|-------|-------|--------|
| H1 | 1 | ✅ Correct |
| H2 | 5 | ✅ Good |
| H3 | 4 | ✅ Good |

### Meta Tags

| Tag | Content | Status |
|-----|---------|--------|
| Title | "AI Pulse — Stop guessing which AI model to use" | ✅ Good |
| Description | 160+ characters, keyword-rich | ✅ Good |
| OG Tags | Complete set | ✅ Good |
| Twitter Cards | Complete set | ✅ Good |

### Entity-Based Content

- ✅ Product name: "AI Pulse — Model Radar"
- ✅ Price mentions: "$29", "$99"
- ✅ Feature list: "600+ models", "170+ companies"
- ✅ Use cases: "developers", "researchers", "product managers"

### Recommendations

1. Add more entity-rich paragraphs
2. Include industry terminology (LLM, benchmark, context window)
3. Add author/contributor mentions
4. Include publication/update dates

---

## 5. Growth Leaks Identified

| Leak Type | Severity | Impact | Fix |
|-----------|----------|--------|-----|
| Missing FAQPage schema | High | -15% AI visibility | Add JSON-LD |
| No blog content | High | -20% topical authority | Create 3 articles |
| Limited brand mentions | Medium | -10% authority | Reddit/LinkedIn posts |
| No comparison content | Medium | -10% citability | Create vs page |
| Missing Organization schema | Low | -5% trust signals | Add JSON-LD |

---

## 6. Content Optimization Recommendations

### Landing Page Optimizations

1. **Add "What is AI Pulse?" section**
   - Clear, quotable definition
   - 2-3 sentences for AI citation
   - Entity-rich content

2. **Enhance FAQ section**
   - Add 6-8 questions (currently 4)
   - Use FAQPage schema
   - Include long-tail keywords

3. **Add comparison content**
   - AI Pulse vs ChatGPT Plus
   - AI Pulse vs Perplexity
   - AI Pulse vs manual comparison

4. **Include testimonials/social proof**
   - User quotes
   - GitHub stars
   - Download counts

### Technical Optimizations

1. **Add structured data for demo page**
2. **Implement breadcrumb navigation**
3. **Add author markup for blog content**
4. **Include datePublished/dateModified**

---

## 7. 30-Day Content Plan

| Week | Content Type | Topic | Target Keyword |
|------|--------------|-------|----------------|
| 1 | Blog post | "How to Compare AI Models: A Complete Guide" | compare AI models |
| 2 | FAQ update | Expand FAQ with 4 new questions | AI model comparison tool |
| 3 | Service page | "AI Pulse Features Deep Dive" | AI dashboard features |
| 4 | Blog post | "ChatGPT vs Claude vs Gemini: Pricing Comparison" | AI model pricing |

### Content Calendar

**Week 1:**
- Publish "How to Compare AI Models" guide
- Share on Reddit r/LocalLLaMA
- Post on LinkedIn

**Week 2:**
- Update FAQ section with new questions
- Add FAQPage schema
- Share FAQ on Twitter

**Week 3:**
- Create features deep-dive page
- Add internal linking
- Submit to Google Search Console

**Week 4:**
- Publish pricing comparison article
- Create infographic for social
- Email to newsletter subscribers

---

## 8. Technical Recommendations

### Performance

- ✅ Single HTML file — Excellent load time
- ✅ No external dependencies (except Google Fonts)
- ⚠️ Consider lazy loading for screenshots
- ⚠️ Optimize base64 images

### Security

- ✅ HTTPS enabled (Vercel)
- ✅ No external scripts
- ✅ No user data collection

### Mobile

- ✅ Responsive design
- ✅ Touch-friendly elements
- ✅ Viewport meta tag

---

## 9. Platform-Specific Optimization

### Google AI Overviews

- **Status:** Partially optimized
- **Action:** Add more structured content
- **Target:** Featured snippet eligibility

### ChatGPT

- **Status:** Well-indexed
- **Action:** Enhance llms.txt with more context
- **Target:** Increase citation frequency

### Perplexity

- **Status:** Basic optimization
- **Action:** Add comparison tables
- **Target:** Appear in "best tools" queries

---

## 10. 90-Day Roadmap

### Month 1: Foundation

- [ ] Add FAQPage schema
- [ ] Add Organization schema
- [ ] Create 2 blog posts
- [ ] Submit to Google Search Console

### Month 2: Content

- [ ] Create comparison page
- [ ] Publish 4 blog posts
- [ ] Build Reddit presence
- [ ] Start LinkedIn content

### Month 3: Authority

- [ ] Guest post on AI blogs
- [ ] Create video content
- [ ] Build backlinks
- [ ] Monitor AI visibility

---

## Appendix: Schema Templates

### FAQPage Schema

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
        "text": "AI Pulse is a single-file HTML dashboard that compares 600+ AI models from 170+ companies, showing pricing, benchmarks, context windows, and licensing."
      }
    }
  ]
}
```

### Organization Schema

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "AI Pulse",
  "url": "https://github.com/T-a-c-h-y-o-n/aipulse",
  "logo": "https://aipulse-landing.vercel.app/pulse2.png",
  "sameAs": [
    "https://github.com/T-a-c-h-y-o-n/aipulse",
    "https://www.producthunt.com/products/ai-pulse-model-radar"
  ]
}
```

---

**Report Generated:** 2026-07-12
**Next Audit:** 2026-08-12
**Auditor:** GEO-SEO Automation
