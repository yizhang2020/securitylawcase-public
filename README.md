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

### 7. “Monday Morning” Translation

What a security lead should do in practice after reading the case.

---

## Taxonomy

Cases are organized by:

* **Regime**

  * FTC Section 5
  * SEC cyber disclosure enforcement
  * HIPAA / HITECH
  * GLBA
  * NYDFS 500
  * CFAA
  * State privacy enforcement

* **Incident Type**

  * Ransomware
  * Credential stuffing
  * Cloud misconfiguration
  * Third-party breach
  * Business Email Compromise
  * DDoS

* **Legal Issue**

  * Standing
  * Unfairness
  * Deception
  * Reasonable security
  * Materiality
  * Class certification


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
  cases/
  taxonomy/
  playbooks/
mkdocs.yml
.github/workflows/deploy.yml
```

Built with:

* MkDocs + Material for MkDocs
* GitHub Actions
* GitHub Pages

---

## Public vs Premium

This repository contains the **public research layer**.

The premium version of SecurityLawCase (separate private repository and gated site) expands on:

* Detailed control mappings
* Evidence artifact templates
* Risk register examples
* Board-ready summaries
* Operational compliance toolkits

The public site establishes authority and shared knowledge.
The premium site provides structured implementation support.


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
