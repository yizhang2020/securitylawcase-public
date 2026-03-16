# SecurityLawCase (Public)

**Engineer-first analysis of cybersecurity and privacy case law.**

SecurityLawCase is a public research platform examining cybersecurity enforcement actions and court decisions through a technical and compliance-focused lens.

Most legal resources answer:

> *“What did the court or regulator decide?”*

SecurityLawCase also answers:

> *“What would a reasonable security program have looked like — and what evidence would prove it?”*

---

## Mission

To translate cybersecurity case law into actionable insight for:

* Security engineers
* Security architects
* GRC professionals
* Security directors aspiring to CISO roles
* Lawyers seeking technical clarity

This repository hosts the **public research layer** of SecurityLawCase.


## What This Site Contains

Each case analysis includes:

### 1. Executive Summary

What happened, what was decided, and why it matters.

### 2. Primary Sources

Links to official complaints, opinions, consent orders, and enforcement documents.

### 3. Procedural Timeline

Filing → litigation → resolution → remedies.

### 4. Legal Analysis

Issues, standards applied (e.g., unfairness, deception, materiality), holdings, and penalties.

### 5. Technical Deep Dive

* Likely attack path
* Security control failures
* Compliance expectations at the time

### 6. Compliance → Controls → Evidence Mapping

* Mapping to NIST CSF / CIS Controls (high-level in public version)
* Types of artifacts regulators rely on
* Evidence that security leaders should retain

### 7. Action checklist

What a security lead should do in practice after reading the case.

---

## Taxonomy

Cases are organized by:

* **Regime** (`taxonomy/regimes.md`) — Federal regulators (OCC, Federal Reserve, FTC, SEC, HHS OCR), federal laws and regulations (FTC Act § 5, CFAA, GLBA, HIPAA, HITECH, SEC disclosure, interagency guidance), state/sector (e.g. NYDFS 500), and executive orders affecting cybersecurity.

* **Incident type** (`taxonomy/incident-types.md`) — What happened technically (e.g. cloud misconfiguration, SSRF, credential stuffing, third-party breach, ransomware, BEC, web app vulnerability, insider threat, payment card/skimming, logging/monitoring failures), each with a short explanation and a linked representative case.

* **Legal issue** (`taxonomy/legal-issues.md`) — What mattered legally (reasonable security, governance & oversight, disclosure/materiality, unfairness/deception, causation & damages, standing, class certification, remedies/injunctive terms), each with a short explanation and a linked representative case.


## Differentiation

SecurityLawCase is **not** a legal database.

Existing resources provide:

* Court opinions
* Docket access
* Legal summaries

SecurityLawCase provides:

* Technical reconstruction
* Control-failure analysis
* Compliance mapping
* Engineering-to-lawyer translation
* Operational security insights

The goal is to bridge **law and implementation**.


## Sources

All case pages rely on:

* Official court opinions
* Agency complaints and orders
* Public enforcement announcements
* Public-domain legal materials

This site does **not** reproduce copyrighted legal commentary.


## Repository Structure

```
docs/
  index.md                 # Home
  browse/
    index.md               # Start here — case tables (live + incoming), taxonomy links
  cases/
    major-breaches/
      2019-capital-one/    # Capital One case + case-pack documents
    ftc-section-5/
      2022-drizly/         # Drizly FTC case
    sec-disclosure/        # SEC disclosure placeholder
    _template/             # Case template
  taxonomy/
    regimes.md             # Federal regulators, laws, executive orders
    incident-types.md      # Incident types + representative cases
    legal-issues.md        # Legal issues + representative cases
  studio/
    index.md               # Writing Studio overview
    workflows.md
    document-types.md
  document-types/          # Reference docs by category (executive-board, regulatory-compliance, etc.)
  methodology.md
  research/
    2026-03-14-curated-starter-set.md
  assets/
    stylesheets/
    javascripts/
mkdocs.yml
.github/workflows/deploy.yml
```

Built with:

* MkDocs + Material for MkDocs
* GitHub Actions
* GitHub Pages

---

## Status

This project is in active development.
Initial focus areas include:

* FTC data security enforcement (Section 5)
* SEC cyber disclosure cases
* Key CFAA decisions


## Contributing

This repository currently serves as a curated research project.

Future contributions and collaboration may be considered as the taxonomy and methodology mature.


## License

Content is original analysis unless otherwise cited.
Primary legal documents remain the property of their respective issuing authorities.
