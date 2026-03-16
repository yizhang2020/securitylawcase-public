# Methodology

SecurityLawCase focuses on **primary sources + technical translation**.

The goal is to make cybersecurity case law usable for security practitioners by connecting:

**Legal standards → security controls → evidence artifacts**



## What counts as a “case” here

A “case” may include:

- court opinions and litigation filings
- regulator enforcement actions (FTC, SEC, state AGs)
- consent orders, administrative complaints, settlements, orders
- official press releases only as context (never as the main authority)

This site is not trying to be a complete legal database. It is a curated analysis library focused on decisions that shape **“reasonable security”** expectations.



## Source policy (primary-first)

### Primary sources (preferred)

We prioritize official and authoritative sources, such as:
- court opinions (official court sites when possible)
- dockets/filings via public repositories (e.g., CourtListener/RECAP)
- agency documents (FTC, SEC, state regulators)
- published consent orders and administrative decisions

### Secondary sources (limited use)
Secondary sources (news, blogs, commentary) may be used only for:

- timeline context
- industry background
- public impact narrative

They are never treated as the definitive authority for legal holdings.



## How technical facts are handled

Many legal records do **not** fully describe the technical root cause. When technical details are incomplete:

- We clearly label inferences as **“likely,” “plausible,” or “unknown.”**
- We distinguish between:
  - **allegations** (complaint)
  - **findings** (order/opinion)
  - **public reporting** (media)
- We avoid claiming certainty beyond the record.

If the record lacks technical specificity, the site still provides:

- control areas implicated (e.g., IAM, logging, secure SDLC)
- evidence artifacts that matter in enforcement and litigation
- “what a defensible program would show”



## Case page structure (standard template)

Each public case page uses a repeatable layout aligned with the [Writing Studio](studio/index.md) and evidence-ready governance:

1. **Executive Summary**
2. **Primary Sources**
3. **Procedural Timeline**
4. **Background**
5. **Legal Analysis**
    - issues / standards / holding / remedy
6. **Technical Deep Dive**
    - attack path (as known)
    - control failures
    - engineering translation
7. **Compliance → Controls → Evidence**
    - framework mapping (start: NIST CSF + optionally CIS)
    - evidence artifacts counsel/regulators rely on
8. **Action checklist**
9. **Impact**
10. **References (indexed)**



## Framework mapping approach

SecurityLawCase maps legal expectations into a small number of widely used security frameworks.

**Default mappings:**

- **NIST CSF** functions/categories (clear, broadly understood)
- **CIS Controls** (implementation-oriented)

We start with high-level mappings and add detail over time as patterns stabilize.



## “Compliance → Controls → Evidence”

For each case, we ask:

1. What security expectations were implied?

    Examples:

    - MFA on privileged paths
    - monitoring and detection for suspicious access
    - vulnerability and patch management
    - vendor risk management
    - incident response preparedness

2. What control failures were central?

    We identify the control areas that the record implies were missing, ineffective, or not evidenced.

3. What evidence would have helped?

    Examples:

    - policies/standards and training records
    - risk assessments and remediation tracking
    - audit logs and retention
    - access reviews and MFA enforcement proof
    - incident response plans + tabletop documentation
    - vendor due diligence records

This "evidence layer" is what security leaders need to defend reasonableness and demonstrate program maturity.



## Quality bar / editorial principles

- Cite primary sources first
- Separate allegations from findings
- Mark uncertainty explicitly
- Avoid copying copyrighted summaries
- Use consistent structure and terminology
- Write for engineers, but keep it board/counsel readable



## Disclaimer

This site is for educational purposes and **does not provide legal advice**. Consult qualified counsel for legal interpretation and strategy.
