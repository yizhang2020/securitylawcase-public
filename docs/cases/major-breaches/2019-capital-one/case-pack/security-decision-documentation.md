# Security Decision Documentation (Capital One 2019)

> Use this to record a significant security-related decision: what was decided, why, who was involved, and what evidence or inputs were used; supports accountability and audit.

---

## Purpose

This document standardizes how significant security and disclosure decisions related to Capital One 2019 are recorded, including rationale, approvers, assumptions, and follow-up actions. It supports legal defensibility, internal accountability, and post-incident learning.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Security Director **(role)** prepares a security decision documentation **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY DECISION RECORD</strong></p>

<div class="doc-meta">
<p><strong>Decision: </strong>Adoption of config-as-code and automated drift detection as mandatory control for cloud perimeter assets<br>
<strong>Date: </strong>September 10, 2020<br>
<strong>Participants: </strong>Security Director (Technology Risk), CISO, CTO, Chief Risk Officer, [Board designate]</p>
</div>

<p><strong>Context: </strong>Following the July 2019 cybersecurity incident—in which an external actor exploited a misconfiguration in our AWS-hosted web application firewall (WAF) to gain access to customer data—and the Consent Order and $80 million civil money penalty issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC NR 2020-98), the Bank was required to strengthen cloud configuration governance. The Consent Order mandates improved risk management, board reporting, and cloud security. This decision formalizes the control approach for perimeter and boundary configuration so that we meet regulatory expectations and reduce the likelihood of repeat exposure.</p>

<p><strong>Options Considered: </strong>(1) Mandate config-as-code and automated drift detection for all designated perimeter controls (selected). This option directly addresses the root cause of the 2019 incident and provides auditable evidence for the OCC and for any litigation or disclosure. (2) Manual baseline reviews only—rejected as insufficient to meet Consent Order expectations and residual risk. (3) Full outsourcing of configuration management—evaluated; rejected to retain control and evidence ownership for regulatory and legal purposes.</p>

<p><strong>Rationale: </strong>Config-as-code with peer review and drift detection directly addresses the configuration weakness that allowed the July 2019 incident. It aligns with Consent Order requirements and supports defensibility in regulatory and legal process. Evidence or inputs relied on: internal risk assessment post-incident; Consent Order requirements (OCC NR 2020-98); internal architecture review; cost and timeline estimates from Technology.</p>

<p><strong>Commitments: </strong>Rollout per approved roadmap; Phase 1 completion Q1 2021; quarterly reporting to the Board and to the OCC per the Consent Order. Exceptions require CISO approval and documented revisit date. This decision is acknowledged by the participants above and is maintained as a formal record for audit and regulatory review.</p>

</div>

**Document-type guide:** [Security Decision Documentation](../../../../document-types/legal-technical/security-decision-documentation.md)

**Writing tips:** [Writing best practices — Security Decision Documentation](../../../../studio/writing-best-practices.md#security-decision-documentation)
