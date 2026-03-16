# Internal Security Directive (Capital One 2019)

> Use this to issue a directive or mandate from leadership on security: required actions, deadlines, or standards; creates clear accountability and follow-up.

---

## Hallucinated writing examples

**Scenario.** In September 2019, approximately six weeks after the July 2019 breach disclosure and the arrest of the individual responsible **(time)**, the Chief Information Security Officer **(role)** issues an internal security directive **(type)** to the Board and Bank leadership **(audience)** mandating immediate controls for cloud perimeter configuration. The directive is issued during the incident response and regulatory scrutiny; it is intended to prevent recurrence and to demonstrate to the Board and future regulators that the Bank has mandated specific, measurable actions. The directive will be tracked for compliance and may be referenced in OCC or legal process.

<div class="writing-example-formal">

<p><strong>INTERNAL SECURITY DIRECTIVE</strong></p>

<div class="doc-meta">
<p><strong>Issuing authority:</strong> Chief Information Security Officer (with acknowledgment of Chief Executive Officer and General Counsel)<br>
<strong>Effective date:</strong> September 15, 2019<br>
<strong>Subject:</strong> Mandatory Control — Cloud Perimeter and Boundary Configuration; No Production Changes Without Peer Review and Documentation</p>
</div>

<p><strong>Context.</strong> On July 29, 2019, the Company publicly disclosed that an unauthorized individual had obtained access to customer data stored in our AWS-hosted infrastructure. The vulnerability has been secured and law enforcement was notified; the individual was arrested the same day. This directive is issued to prevent recurrence and to establish mandatory controls for cloud perimeter and boundary configuration. It applies to all business and technology units responsible for web application firewall (WAF), routing, exposure rules, and designated equivalent controls in our AWS and other cloud environments.</p>

<p><strong>Directive.</strong> Effective immediately, no production change to cloud perimeter or boundary controls (WAF, routing, exposure rules, and designated equivalent) shall be made outside an approved change workflow that includes (1) proposal and review in version control or equivalent, (2) peer review by a designated reviewer, and (3) approval before merge or deployment. All such changes must be documented and traceable. Exceptions require CISO approval and documented risk acceptance with a defined revisit date. In addition, all teams that administer perimeter or boundary configuration affecting [designated data or systems] shall, by December 31, 2019, document current baselines and establish a process for detecting and remediating unauthorized or unapproved changes (drift). Third-party managed components are in scope where the Bank controls or can influence configuration.</p>

<p><strong>Accountability and deadlines.</strong> Technology owners are responsible for implementation and for producing evidence of compliance (e.g., repository coverage, change tickets, baseline documentation). The CISO organization is responsible for defining the change workflow, approving exceptions, and reporting to the Board and to Risk. Compliance and progress shall be reported to the CISO and Risk per [cadence]. Failure to meet the requirements or deadlines may result in escalation to [executive] and reporting to the Audit Committee. Questions: Contact the CISO organization at [contact]. Supporting standards and procedures will be published by [date].</p>

</div>

---

## Official document (mandated actions in enforcement)

The **OCC consent order** required Capital One to take specific actions by specified timelines—in effect, a regulator-issued “directive” that the bank had to implement. Internal directives from leadership serve a similar purpose: mandatory actions with deadlines and accountability.

- **OCC Consent Order (2020):** [OCC Consent Order and Civil Money Penalty against Capital One](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html) — required actions (e.g., risk management, board reporting, cloud security) with compliance expectations and reporting to the OCC.
- **FFIEC / OCC:** Regulatory guidance often mandates specific controls or behaviors (e.g., MFA, encryption, incident reporting); internal directives implement and track them.
- **Post-incident practice:** After a breach or audit, leadership often issues directives to close gaps and demonstrate commitment.

*Internal directives are confidential; consent orders show how regulators mandate and track required actions.*

---

## Writing analysis

**How internal security directives are typically structured**

- **Issuing authority** — Who is issuing (e.g., CEO, CISO, board).
- **Effective date** — When it takes effect.
- **Directive** — Clear statement of what is required (actions, standards, or behavior).
- **Scope** — Who must comply (org, business unit, role).
- **Deadlines** — When actions must be completed.
- **Accountability** — Who is responsible for compliance and reporting.
- **Consequences** — What happens for non-compliance (if stated).
- **Questions** — Where to go for clarification.

**What to emulate**

- One-page, scannable; decision-makers and implementers need to see “what” and “by when” quickly.
- Track acknowledgment, completion evidence, and exceptions so the directive is part of the compliance trail.
- Align with policy and regulatory expectations so the directive implements a known standard.

**What to improve**

- Avoid directives that cannot be completed or measured; tie to concrete deliverables and evidence.

- Include a single owner or escalation path so "who is responsible" is clear.
