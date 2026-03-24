# Writing best practices

**Tips and patterns for Studio document types.**

This page collects **writing analysis** guidance moved from case-pack writing examples (Capital One, Drizly). Use it together with each type’s [guide page](../document-types/executive-board/board-security-brief.md) and the [Document types](document-types.md) catalog. Case-pack files keep scenarios, samples, official sources, **One-slide summary**, **Talk track**, and **Decisions requested** where applicable.

---

## Executive and board communication

### Board Security Brief

**How board-level security disclosure is typically structured (e.g. 10-K Item 1C)**

- **Risk management and strategy** — How the company identifies, assesses, and manages material cyber risks; use of frameworks (e.g. NIST); third-party and incident response programs.
- **Governance** — Board oversight (e.g. audit committee); who in management is responsible (CISO/CIO); frequency of reporting.
- **Material incidents** — If applicable, description of significant incidents, impact, and remediation.
- **Program elements** — Defense in depth, monitoring, identity/access, business continuity, third-party reviews, testing.

**Board communication tips**

- Present a concise, one-page summary covering the incident, its impact, key control gaps, remediation actions, metrics, and required decisions.
- Use a consistent talk track to ensure clarity and alignment during presentation.
- Clearly articulate decisions requested to support effective board oversight and approval.
- Define measurable outcomes for all remediation actions (e.g., “percentage of changes peer-reviewed”), rather than relying on technical descriptions alone.

**Structure to emulate (brief narrative flow)** — Incident summary → regulatory outcome → root causes and control gaps → remediation and consent order compliance → decisions requested. Keep the brief to one to two pages; provide a clear list of decisions or approvals requested so the board knows what is being asked.

**References (example — FTC matter):** FTC Complaint and Decision and Order, Docket No. 2023185 (Oct. 24, 2022), as linked from the case primary sources.

---

### Executive Security Risk Summary

**How executive risk summaries are typically structured**

- **Executive summary** — Overall risk posture and trend.
- **Risk landscape** — Categories (e.g., cyber, third-party, resilience) and severity.
- **Top risks** — Key risks with impact, likelihood, and mitigation status.
- **Gaps and initiatives** — What is being done and what is planned.
- **Decisions / approvals** — Risk acceptances or resource requests.
- **Appendix** — Optional detail (e.g., risk criteria, heat map).

**What to emulate**

- One-page or short deck: trend, top 5–7 risks, mitigation status, and clear “asks” (approval, budget, acceptance).
- Trace each risk to the risk register; each mitigation to control evidence or project status.
- Use plain language; avoid jargon so non-security executives can act.

**What to improve**

- Avoid listing controls without tying them to risk reduction or evidence.
- Include “risks of inaction” and revisit dates for accepted risks so accountability is clear.

---

### Security Program Status Report

**How program status reports are typically structured**

- **Overview** — Program mission and scope; reporting period.
- **Metrics** — KPIs/KRIs (e.g., incidents, vulnerabilities, control coverage, training).
- **Progress** — Initiatives completed, in progress, and planned.
- **Issues and blockers** — What is at risk and what is needed.
- **Next period** — Priorities and milestones.
- **Appendix** — Optional charts, framework alignment, or roadmap.

**What to emulate**

- Tie every metric to a data source (ticketing, assessments, audits) so the report is defensible.
- Show trend over time (e.g., open findings, control coverage) so leadership sees direction.
- Call out decisions needed (resources, scope, timeline) so the report drives action.

**What to improve**

- Avoid vanity metrics; prefer metrics that reflect control effectiveness and evidence readiness.
- Link “progress” to risk register and audit findings so regulators and counsel see a clear thread.

---

### Strategic Security Initiative Justification

**How initiative justifications are typically structured**

- **Initiative summary** — What, why, and high-level scope.
- **Business context** — Risk or compliance driver; strategic alignment.
- **Options considered** — Alternatives and why this path.
- **Benefits** — Risk reduction, compliance, efficiency, or other outcomes.
- **Resources and timeline** — Cost, headcount, and milestones.
- **Risks of inaction** — What happens if we do nothing.
- **Recommendation and ask** — Clear ask (approval, budget, authority).

**What to emulate**

- Reference risk assessments, regulatory expectations, or audit findings so the ask is evidence-based.
- One-page summary plus appendix; decision-makers need a clear “recommendation and ask.”
- Spell out risks of inaction so the cost of delay is explicit.

**What to improve**

- Avoid technical deep-dives in the main summary; keep benefits and trade-offs in business language.
- Tie approved initiatives to program status and risk register so execution is tracked.

---

## Regulatory and compliance documentation

### Regulatory Security Explanation

**How regulatory security explanations are typically structured**

- **Introduction** — Scope, period, and context of the response.
- **Governance** — Oversight, roles, and accountability for security.
- **Risk management** — How risks are identified, assessed, and mitigated.
- **Control environment** — Key controls by domain (e.g., access, logging, IR, third-party).
- **Evidence of operation** — How controls are tested, monitored, and evidenced.
- **Incidents and remediation** — Relevant incidents and lessons applied.
- **Conclusion** — Summary of posture and any commitments.

**What to emulate**

- Every assertion supportable by policies, assessments, logs, and testing results.
- Align language with regulatory guidance (e.g., OCC, FTC, SEC) so examiners see expected concepts.
- Clear “evidence of operation” section so the document bridges artifacts and expectations.

**What to improve**

- Avoid generic statements; cite specific controls, metrics, and review cadences.
- If an incident is in scope, describe cause, impact, and remediation so the regulator sees accountability.

---

### Compliance Justification Document

**How compliance justification documents are typically structured**

- **Requirement** — Citation (regulation, standard, or control).
- **Interpretation** — What the requirement means in practice.
- **Implementation** — How the organization meets it (process and controls).
- **Evidence** — Artifacts that demonstrate compliance (policies, logs, reviews, tests).
- **Gaps and exceptions** — Any shortfalls, compensating controls, or risk acceptance.
- **Owner and review** — Accountability and last review date.

**What to emulate**

- One row or section per requirement; each with implementation + evidence so auditors can verify.
- Use the same citation format as the framework or regulator (e.g., NIST ID, CIS control number).
- Document gaps and risk acceptance explicitly so there are no surprises.

**What to improve**

- Avoid “we have a policy” without pointing to evidence of operation (testing, reviews, logs).
- Keep owner and review date current so the document is a living control-to-evidence map.

---

### Governance Response Memo

**How governance response memos are typically structured**

- **Context** — Request or finding being addressed.
- **Governance model** — Board and committee structure; reporting lines.
- **Security ownership** — CISO/security leadership role and authority.
- **Risk and control oversight** — How risk and controls are reviewed and escalated.
- **Policies and standards** — How they are set, maintained, and enforced.
- **Evidence** — Minutes, charters, org charts, and policy approval records.
- **Conclusion** — Summary of governance and any commitments.

**What to emulate**

- Back every governance claim with an artifact (charter, org design, minutes, policy approval).
- Use clear reporting lines and escalation paths so “who decides what” is unambiguous.
- Align with regulatory language (e.g., “board oversight,” “management accountability”) so the memo speaks the examiner’s language.

**What to improve**

- Avoid vague “tone at the top” statements; cite specific committees, cadence, and deliverables.
- Include a short evidence index (charter, last meeting date, policy version) so the auditor can verify quickly.

---

## Legal-technical analysis

### Security Architecture Explanation for Legal Review

**How architecture explanations for legal review are typically structured**

- **Scope** — Systems, data, or transactions in scope.
- **Architecture overview** — High-level design (diagrams and narrative).
- **Security controls** — How critical controls are implemented (access, encryption, monitoring).
- **Data flows and boundaries** — Where data lives and how it is protected.
- **Risks and mitigations** — Known risks and how they are addressed.
- **Assumptions and limitations** — What the architecture does and does not guarantee.
- **Appendix** — Glossary, acronyms, or detailed diagrams.

**What to emulate**

- Plain-language summary first; technical detail in appendices so counsel can opine without becoming an engineer.
- Align narrative with actual configs and assessments so legal opinions and disclosures are accurate.
- Explicit “assumptions and limitations” so counsel knows what is not guaranteed.

**What to improve**

- Avoid jargon in the main narrative; define acronyms and critical terms.
- Tie each control to evidence (config, log, test) so the document supports defensibility.

---

### Security Decision Documentation

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

---

## Policy and governance writing

### Security Policy Draft

**How security policy drafts are typically structured**

- **Purpose and scope** — Why the policy exists; who and what it covers.
- **Policy statement** — High-level requirements (what must be true).
- **Roles and responsibilities** — Who owns the policy; who implements and enforces.
- **Requirements** — Specific, testable requirements (can be in policy or linked standards).
- **Exceptions** — How exceptions are requested, approved, and documented.
- **Review and enforcement** — How often reviewed; consequences of non-compliance.
- **Related documents** — Standards, procedures, and guidelines.
- **Revision history** — Version, date, and change summary.

**What to emulate**

- Policy as the top-level artifact; standards and procedures implement it. Keep policy concise; put detail in standards.
- Each requirement testable or auditable so “policy in practice” can be evidenced (training, exceptions, reviews).
- Clear exception process so risk acceptance is documented, not implicit.

**What to improve**

- Avoid policy that cannot be enforced or evidenced; tie to controls and metrics.
- Align with regulatory and framework language (e.g., OCC, NIST) so auditors see expected concepts.

---

### Security Governance Memo

**How security governance memos are typically structured**

- **Purpose** — Why governance is being defined or updated.
- **Governance model** — Board/committee structure; reporting lines.
- **Roles** — CISO, security leadership, risk owners, and their authority.
- **Committees** — Security/risk committee charter, membership, and cadence.
- **Escalation** — When and how issues escalate (incidents, risk, exceptions).
- **Policies and standards** — How they are set, approved, and updated.
- **Review cycle** — How often governance is reviewed and by whom.

**What to emulate**

- Align with charters, org design, and policy approval records so the memo is evidence of oversight.
- Clear escalation paths (incident, risk acceptance, exception) so “who decides what” is unambiguous.
- One-page summary plus appendix (charters, org chart) so leadership and auditors can use it quickly.

**What to improve**

- Avoid vague “committee oversees security”; name the committee, cadence, and deliverables.
- Tie governance to evidence (minutes, charters, approval dates) so “tone at the top” is demonstrable.

---

### Security Program Justification

**How security program justifications are typically structured**

- **Program mission** — What the security program exists to achieve.
- **Scope** — What is in scope (systems, data, business units).
- **Current state** — Structure, headcount, and key capabilities.
- **Gap analysis** — What is missing relative to risk and expectations.
- **Options** — Alternative structures or resource levels.
- **Recommendation** — Proposed scope, structure, and resources.
- **Evidence** — Risk assessments, benchmarks, regulatory expectations.
- **Conclusion** — Ask (approval, budget, headcount).

**What to emulate**

- Reference risk register, regulatory guidance, and industry norms so the ask is evidence-based.
- Clear “recommendation and ask” so decision-makers know exactly what is being requested.
- Once approved, track execution in program status and risk register.

**What to improve**

- Avoid justifying by headcount alone; tie to risk reduction, control coverage, and evidence readiness.
- Include “risks of inaction” so the cost of under-investment is explicit.

---

### Internal Security Directive

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
- Include a single owner or escalation path so “who is responsible” is clear.

---

## Public communication support

### Security Public Statement Draft (public breach or incident statements)

**How the official statement is built**

- **Lead** — What happened and when, in one sentence; perpetrator arrested (reassurance).
- **CEO quote** — Apology and commitment; humanizes the response.
- **Scope** — Approximate numbers (e.g., regional counts); what was and was *not* compromised.
- **Data categories** — Clear bullets: application data, customer data, exceptions (e.g., SSNs, bank accounts).
- **Actions** — Fixed vulnerability, working with law enforcement, notifying affected individuals, free credit monitoring.
- **Contact / next steps** — URL for more information; “investigation ongoing.”
- **FAQ** — Optional but effective: vulnerability, discovery, timing, encryption, cloud, financial impact. Reduces repeat inquiries and shows control of narrative.
- **Forward-looking / legal** — Cost range, insurance, efficiency guidance; cautionary language for investors.

**What works well**

- Factual, sequenced, and scoped; avoids speculation.
- Clear “what was not compromised” to reduce fear.
- Single CEO voice; commitment and next steps explicit.
- SEC exhibit version includes investor-oriented detail (costs, insurance) and safe-harbor language.

**What to improve**

- “Configuration vulnerability” is vague; a later FAQ adds a bit of detail but still may omit technical root cause. For a technical audience, a short, plain-language technical sentence can help without undermining legal posture.
- “Highly sophisticated individual” may age poorly once the threat actor was publicly identified; neutral wording (“external actor,” “unauthorized individual”) is more durable.
- Explicit “what you can do” (e.g., enroll in credit monitoring, watch for phishing) can be one short bullet block for affected individuals.

---

### Customer Security Explanation

**How customer security explanations are typically structured**

- **What happened** — Simple description of the event or topic.
- **What information was involved** — Types of data (e.g., name, email) and whether exposed or not.
- **What we are doing** — Steps taken to protect data and prevent recurrence.
- **What you can do** — Practical steps (check statements, enable MFA, watch for phishing).
- **How to get help** — Contact, FAQ, or support channel.
- **Additional resources** — Links to credit monitoring, identity protection, or more detail.

**What to emulate**

- Plain language; avoid jargon and legalese so customers can act.
- Align with internal facts and legal/compliance requirements so the message is accurate and consistent across channels.
- Clear “what you can do” and “how to get help” so customers have a path forward.

**What to improve**

- Avoid minimizing impact or over-promising; stick to facts and committed actions.
- Ensure one source of truth (e.g., one page or FAQ) so support and legal stay aligned.

---

### Security Transparency Report Section

**How security transparency report sections are typically structured**

- **Reporting period** — Date range and scope.
- **Overview** — Security mission and approach (brief).
- **Metrics** — Incidents, requests (e.g., law enforcement), or other disclosed metrics.
- **Notable events** — Significant incidents or changes (as appropriate to disclose).
- **Program highlights** — Investments, certifications, or improvements.
- **Commitments** — What the organization commits to going forward.
- **References** — Link to full report, policy, or contact.

**What to emulate**

- Metrics and events accurate and consistent with internal records; review by legal and leadership before publication.
- Balance transparency with legal and competitive constraints; do not promise more disclosure than you can sustain.
- Clear “reporting period” and “references” so readers know scope and where to go for more.

**What to improve**

- Avoid vague “we take security seriously”; use concrete metrics or commitments.
- Align with 10-K and other disclosures so the section does not contradict formal filings.

---

## How to use this page

1. Pick your [document type](document-types.md) and open its guide for structure and audience.
2. Use the matching section here for **patterns, emulate/improve lists**, and disclosure tips.
3. In case packs, use the **hallucinated example**, **official document**, and remaining sections (e.g., one-slide, talk track) for application to a specific matter.
