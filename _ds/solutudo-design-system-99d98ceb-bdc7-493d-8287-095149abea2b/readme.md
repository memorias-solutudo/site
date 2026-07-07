# Solutudo — Design System

> _"O maior guia de empresas do Brasil."_ — The largest business guide in Brazil.

This repository is the brand & product design system for **Solutudo®** (Solutudo
Produtos e Serviços Ltda, est. ~2005). It contains the visual foundations,
reusable React components, and high-fidelity UI-kit recreations needed to design
on-brand Solutudo interfaces and assets.

---

## 1. What Solutudo is

Solutudo is a Brazilian **local business directory & discovery platform** — a
modern evolution of the classic "guia de empresas" (yellow-pages-style city
guide). Two audiences meet on the platform:

- **Consumers / the population** search for local businesses, jobs ("Empregos"),
  bus lines ("Ônibus"), useful phone numbers and city information, city by city
  (e.g. Botucatu, Sorocaba, São Manuel).
- **Business owners ("Empresários")** register their company — free or on a paid
  plan — to get a professional Solutudo profile, a shareable personal link, and
  **greater odds of being found on Google, Bing, ChatGPT, Gemini, Claude and
  other AI assistants**. AI-era discoverability is a central, repeated promise.

Solutudo positions itself as **"a ponte entre a população e as empresas"** (the
bridge between people and businesses) and **"um guia"** — a trustworthy, curated,
validated source, present in ~hundreds of Brazilian cities, with "20 anos de
história."

### Products / surfaces represented in this system

| Surface | Portuguese name | Notes |
|---|---|---|
| Consumer search home | *Home / Buscar* | City hero + big search bar + facility tiles + live "Movimento" feed |
| City activity feed | *Movimento* | Real-time timeline of registrations, jobs, products in a city |
| Business marketing site | *LP / Cadastre grátis* | White landing pages that sell the free + paid registration |
| Business dashboard | *Área do Empresário* | Internal dashboard (gray bg, white cards): profile, results, community |
| Plans & pricing | *Planos e Preços* | 5 tiers: Gratuito · Essencial · Destaque · Destaque Exponencial (+ Social Media / Completo) |
| Mobile app | *App Solutudo* | iOS + Android; Menu, Área do cliente / Área do empresário |
| Onboarding | *Wizard 1–5* | Multi-step company registration |
| Checkout | *Checkout 1–6* | Plan purchase flow |

### Plan tiers (for reference)
`Gratuito` (R$0, ink/black) · `Essencial` (R$29,90, green) · `Destaque`
(R$189,90, purple) · `Destaque Exponencial + Social Media` (R$499,90, pink) ·
`Destaque Exponencial + Social Media Completo` (R$1299,90, orange). Each tier owns
a brand color; copy is always "Tudo do plano anterior, mais:".

---

## 2. Sources

- **Figma:** *"Solutudo - Base Design System no Claude.fig"* — 1 page, 42 frames
  (consumer home, Movimento, LP desktop V1/V3, Área do Empresário, Planos e Preços
  V1/V2, mobile Menu/Área, Onboarding Wizard, Checkout 1–6, Comunidade). The Figma
  had **no defined components** (all raw frames) and used **Poppins** throughout.
- This system is built from that Figma's visual values (colors, gradients,
  layouts, copy) re-expressed in the brand's chosen production type stack.

> ⚠️ **Type substitution flagged:** The Figma uses **Poppins**. Per brand
> direction this system standardizes on **DM Sans** (UI/body) + **Playfair
> Display** (italic display accents). If Poppins is in fact the canonical face,
> swap `--font-sans` in `tokens/typography.css`. Fonts load from Google Fonts;
> provide self-hosted `.woff2` files if you need offline/locked builds.

---

## 3. Content fundamentals — how Solutudo writes

**Language:** Brazilian Portuguese (pt-BR), always. UI, marketing and microcopy.

**Voice:** Warm, encouraging, plain-spoken and benefit-first. Solutudo talks like
a helpful local ally, not a corporation. It is optimistic and a little proud
("20 anos de história", "o maior guia").

**Person & address:** Speaks to the reader as **"você"** (informal singular) and
refers to itself as **"a Solutudo"** (feminine, the brand-as-entity) or **"nós"**.
E.g. *"Já ajudamos você com 212 buscas"*, *"Seu negócio na Solutudo"*.

**Casing:** Sentence case everywhere — headlines, buttons, nav. Marketing nav
labels can be ALL-CAPS small tracking (`COMECE`, `COMO FUNCIONA`, `BENEFÍCIOS`,
`CADASTRO`). Avoid Title Case Like This.

**Tone devices**
- **Free-first:** the word **"grátis" / "gratuito"** is the hero of almost every
  CTA, and it is the word most often rendered in the Playfair gradient accent.
  *"Cadastre **grátis** sua empresa"*, *"O cadastro é **gratuito**"*.
- **Concrete numbers:** "205.890 usam a Solutudo em Botucatu", "7.540 empresas",
  "780 vagas", "Leva menos de 1 minuto!".
- **Imperative CTAs:** *Cadastrar empresa, Saiba mais, Buscar, Mudar para este
  plano, Ver movimento, Ver detalhes, Convidar, Chamar no WhatsApp*.
- **City-personalized:** copy bends to the current city — *"A Solutudo movimenta
  Botucatu"*, *"Conheça a cidade"*.
- **AI-era proof:** repeatedly names Google, Bing, ChatGPT, Gemini, Claude, Manus
  as places the business will appear.

**Punctuation & symbols:** Uses the **®** on the wordmark in formal contexts.
Prices as `R$ 29,90/mês` (comma decimal, "/mês" or "/Anual"). Em-dash sparingly.

**Emoji:** Not used in product UI. Brand expression is carried by the gradient
heart-mark and color, not emoji.

---

## 4. Visual foundations

### Color & vibe
A **black-and-white base** lit up by a **full-spectrum gradient**. The neutral
system is genuinely neutral (true grays, ink `#151515`, white) so the rainbow
brand gradient and the saturated accents pop. The mood is friendly, energetic,
contemporary-Brazilian, optimistic.

- **Primary brand:** electric purple `#A701FD`.
- **Secondary:** coral-orange `#FF6849`, plus pink `#FC0097`, cyan `#20CCEF`,
  green `#00FFAD`, yellow `#FFC700`.
- **Signature gradient:** a warm→cool diagonal sweep **yellow → orange → pink →
  purple** (`--grad-brand`) and a full rainbow rule (`--grad-rainbow`,
  "Linha de Cores") used as a 4px divider/accent line.
- **Headings:** near-black `#151515` in most areas; a deep slate-purple
  `#58476C` is used for large hero/feed headings on the consumer side.
- **Body / descriptions:** medium-dark gray `#656565`; captions `#888888`;
  placeholders/muted `#ACACAC`.

### Backgrounds (per product, by direction)
- **Sites & landing pages → white** `#FFFFFF`, with light-gray `#F2F2F2`
  section bands for rhythm.
- **Internal dashboards → light gray** `#F2F2F2` page, **white cards** on top.
- **Consumer search hero →** a soft **mesh gradient wash** (`--grad-hero-mesh`):
  a low-opacity version of the brand sweep blooming from a corner over white.
- **Tinted tiles:** pastel surfaces (lavender, mint, peach, soft-yellow) for
  facility tiles and stat cards — each pairs a saturated icon/number with its
  own pale wash.

### Type
- **DM Sans** for all UI, set with **reduced letter-spacing** (`-0.03em` default).
  Weights 400–800; headings bold/extrabold, body 400–500.
- **Playfair Display, italic** for one or two **accent words** inside a headline,
  almost always clipped with the brand gradient (`.sol-display.sol-gradient-text`).
  This serif/sans + gradient contrast is the single most recognizable type move.
- Big, confident display sizes (hero city name ~64px+). Minimum body 14px.

### Shape, corners, cards
- **Everything is rounded.** Pills (`999px`) for buttons, chips, the search bar
  and nav; `16–25px` radii for cards and large surfaces.
- **Cards:** white, generously padded, **soft low-contrast shadow**
  (`--shadow-card: 0 8px 28px rgba(21,21,21,0.06)`), usually borderless or a
  faint `#E3E3E3` hairline. No colored left-border accents.
- **Glass:** the search bar / floating nav use translucent white
  (`rgba(255,255,255,0.86)`) + `backdrop-filter: blur(20px)` + an inset hairline.

### Shadows
Soft, vertical, low-alpha. A dedicated **brand glow** (`--shadow-brand`,
purple-tinted) sits under primary gradient CTAs. No hard/black drop shadows.

### Buttons & states
- **Primary:** brand gradient fill, white text, pill, subtle purple glow.
- **Dark:** solid `#151515` pill, white text (used for "Mudar para este plano",
  "Convidar").
- **Secondary:** white pill, ink text, hairline border.
- **WhatsApp green** is used literally for "Chamar no WhatsApp" actions.
- **Hover:** slight brightness lift + shadow grow; **press:** scale down ~0.97.
  Motion is gentle — `--ease-out`, 140–360ms, fades & small slides. No bounces,
  no infinite decorative loops.

### Layout
Centered, airy, generous whitespace. Fixed floating top nav (pill, glass) on
marketing/consumer; standard top bar on dashboard. Content max-width centered.
Imagery is bright, warm, real-people/real-city photography (not illustration).

---

## 5. Iconography

- **Style:** **outline / line icons**, ~1.5–2px stroke, rounded joins/caps,
  frequently **tinted in the brand purple** (or the local tile color). Examples
  seen: search (magnifier), briefcase (Empregos), bus (Ônibus), storefront
  (empresa), package (produto), edit, list, logout, share, plus, microphone.
- **Brand mark as icon:** the **rainbow heart-knot** (from the wordmark) is used
  on its own as a brand bullet/avatar/favicon.
- **Third-party logos** appear full-color and recognizable: Google, ChatGPT,
  Gemini, WhatsApp, Bing, Claude, Manus (the "appear everywhere" section); press
  logos Estadão, Exame, Gazeta do Povo, Empresas&Negócios; Google Play / App
  Store badges.
- **No emoji** in product UI. No decorative unicode glyphs as icons.

> The Figma defined no exported icon set, so this system uses **Lucide**
> (outline, rounded, ~1.75px) from CDN as the closest match to Solutudo's line
> style. **Flagged substitution** — replace with Solutudo's own SVG icon set when
> available. Brand/press/partner logos referenced in UI kits are copied into
> `assets/` as raster from the Figma.

---

## 6. Index / manifest

**Root**
- `readme.md` — this guide.
- `SKILL.md` — Agent-Skill manifest for downloadable use.
- `styles.css` — global entry point (imports every token + font file).

**`tokens/`** — `fonts.css` (DM Sans + Playfair Display via Google Fonts),
`colors.css`, `gradients.css`, `typography.css`, `spacing.css` (spacing, radii,
shadows, motion, glass).

**`assets/`** — `logo-solutudo.png` (primary wordmark), `mark-heart.png`
(rainbow heart mark, standalone), `photo-person.jpg` (team photo),
`photo-crowd.png`, `avatar-a/b.png`.

**`components/`** — reusable React primitives (each: `.jsx` + `.d.ts` +
`.prompt.md`, one card per dir):
- `buttons/` — **Button** (primary · dark · secondary · ghost · whatsapp).
- `forms/` — **Input**, **SearchBar**, **SegmentedToggle**.
- `display/` — **Card**, **Badge**, **Avatar**, **StatTile**.
- `marketing/` — **PlanCard**, **FeedItem**.

**`ui_kits/`** — full product recreations (self-contained React+Babel pages):
- `consumer-search/` — Home · Results · Business profile · Movimento feed.
- `business/` — Cadastre-grátis landing · Área do Empresário (Início ·
  Resultados · Planos e Preços).
- `shared/` — `primitives.jsx` + `icons.jsx` (window-global, no-bundle versions
  used by the kit pages).

**`guidelines/`** — foundation specimen cards (Design System tab): brand &
neutral colors, tints, gradients, type display + scale, radii, shadows, logo.

> Starting points (for consuming projects): both UI kits, plus the `Button`,
> `SearchBar`, `StatTile` and `PlanCard` components.
