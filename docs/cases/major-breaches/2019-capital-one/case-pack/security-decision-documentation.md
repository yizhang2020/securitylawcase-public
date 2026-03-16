# Security Decision Documentation (Capital One 2019)

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Hallucinated writing examples

**Scenario.** In September 2020, one month after the OCC Consent Order (August 6, 2020) **(time)**, the Security Director **(role)** is required to document a material security decision: the adoption of config-as-code and drift detection as mandatory controls for cloud perimeter assets. The security decision record **(type)** will be shared with the Board, the OCC, and potentially counsel **(audience)** in connection with the Consent Order and litigation. The record must state what was decided, who participated, what options were considered, and what evidence or inputs were relied on.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision:</strong> Adoption of config-as-code and automated drift detection as mandatory control for cloud perimeter assets<br>
<strong>Date:</strong> September 10, 2020<br>
<strong>Participants:</strong> Security Director (Technology Risk), CISO, CTO, Chief Risk Officer, [Board designate]</p>
</div>

<p><strong>Context.</strong> Following the July 2019 cybersecurity incident—in which an external actor exploited a misconfiguration in our AWS-hosted web application firewall (WAF) to gain access to customer data—and the Consent Order and $80 million civil money penalty issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC NR 2020-98), the Bank was required to strengthen cloud configuration governance. The Consent Order mandates improved risk management, board reporting, and cloud security. This decision formalizes the control approach for perimeter and boundary configuration so that we meet regulatory expectations and reduce the likelihood of repeat exposure.</p>

<p><strong>Options considered.</strong> (1) Mandate config-as-code and automated drift detection for all designated perimeter controls (selected). This option directly addresses the root cause of the 2019 incident and provides auditable evidence for the OCC and for any litigation or disclosure. (2) Manual baseline reviews only—rejected as insufficient to meet Consent Order expectations and residual risk. (3) Full outsourcing of configuration management—evaluated; rejected to retain control and evidence ownership for regulatory and legal purposes.</p>

<p><strong>Rationale.</strong> Config-as-code with peer review and drift detection directly addresses the configuration weakness that allowed the July 2019 incident. It aligns with Consent Order requirements and supports defensibility in regulatory and legal process. Evidence or inputs relied on: internal risk assessment post-incident; Consent Order requirements (OCC NR 2020-98); internal architecture review; cost and timeline estimates from Technology.</p>

<p><strong>Commitments.</strong> Rollout per approved roadmap; Phase 1 completion Q1 2021; quarterly reporting to the Board and to the OCC per the Consent Order. Exceptions require CISO approval and documented revisit date. This decision is acknowledged by the participants above and is maintained as a formal record for audit and regulatory review.</p>

</div>

---

## Official document (decisions in enforcement and settlement)

Post-breach, Capital One made material decisions that were later scrutinized: consent order commitments, settlement terms, and program changes. **OCC consent orders** and **settlement agreements** often reference board and management decisions; internal decision documentation supports defensibility.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — required actions imply decisions (e.g., risk management, board reporting, cloud security) that should be documented internally.
- **Settlement:** [In re Capital One Consumer Data Security Breach Litigation](https://www.capitalonesettlement.com) — class settlement reflects decisions on remediation, notification, and compensation.
- **SEC guidance:** Material cybersecurity decisions (e.g., risk acceptance, control changes) may need to be reflected in disclosure; decision records support accuracy and consistency.

*Decision documentation is internal; consent orders and settlements show that “what was decided and why” can be requested by regulators and counsel.*

---

## Writing analysis

**How security decision documentation is typically structured**

- **Decision** — Clear statement of what was decided.
- **Date and participants** — When and who (individuals or roles).
- **Context** — What triggered the decision (incident, finding, project).
- **Options** — Alternatives considered.
- **Rationale** — Why this option; key factors (risk, cost, compliance).
- **Evidence or inputs** — Documents, assessments, or advice relied on.
- **Commitments** — Follow-up actions, review dates, or conditions.
- **Approval** — Sign-off or acknowledgment.

**What to emulate**

- One document per significant decision; link to supporting artifacts (risk assessment, architecture doc, legal advice).
- Clear “rationale” and “evidence or inputs” so the record shows informed, documented decision-making.
- Revisit dates and commitments so follow-through is trackable.

**What to improve**

- Avoid undocumented oral decisions for material risk or control changes; capture in writing promptly.
- Use a standard template so auditors and regulators see consistent structure.

