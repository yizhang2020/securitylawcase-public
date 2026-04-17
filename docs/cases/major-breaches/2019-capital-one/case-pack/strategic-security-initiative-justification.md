# Strategic Security Initiative Justification (Capital One 2019)

> Use this to build a business case for a major security initiative (e.g., IAM overhaul, zero trust, SOC upgrade); supports approval, budget, and prioritization.

---

## Purpose

This document provides the strategic and financial rationale for major security investments required after Capital One 2019, linking legal exposure and operational risk to concrete program outcomes. It is intended to support budget and prioritization decisions with a clear cost-risk-benefit narrative.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Chief Information Security Officer **(role)** prepares a strategic security initiative justification **(type)** for Executive Leadership, Board Finance Committee **(audience)**.

<div class="writing-example-formal">

<p><strong>STRATEGIC SECURITY INITIATIVE JUSTIFICATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Executive Leadership, Board Finance Committee<br>
<strong>From: </strong>Chief Information Security Officer<br>
<strong>Date: </strong>November 15, 2020<br>
<strong>Subject: </strong>Business Case — Cloud Configuration Governance and Drift Detection Initiative (Post–July 2019 Incident; OCC Consent Order)</p>
</div>

<p><strong>Initiative Summary: </strong>This document requests approval and budget for an enterprise-wide initiative to implement config-as-code and automated drift detection for cloud perimeter and critical infrastructure controls. The initiative is required under the Consent Order issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC NR 2020-98) and directly addresses the root cause of the July 2019 cybersecurity incident, in which an external actor exploited a misconfiguration in our AWS-hosted WAF to gain access to customer data. Scope: AWS WAF, routing, and boundary policies; phased rollout over 12 months with Phase 1 completion Q1 2021.</p>

<p><strong>Business and Regulatory Context: </strong>The 2019 incident resulted in unauthorized access to approximately 106 million individuals’ data, the arrest of the threat actor (<em>United States v. Paige A. Thompson</em>), an $80 million civil money penalty and Consent Order from the OCC, and consumer class-action litigation (later settled). The OCC found that our cloud security and risk management did not meet heightened standards and required the Bank to strengthen configuration governance and control effectiveness. This initiative implements that requirement and reduces the risk of repeat exposure from configuration drift or human error.</p>

<p><strong>Options Considered: </strong>(1) Full config-as-code and drift detection (recommended): all designated perimeter changes via version control and peer review; automated drift detection with remediation or documented exception. (2) Manual baselines and periodic review only: rejected as insufficient to meet Consent Order expectations and residual risk. (3) Third-party managed service: evaluated; we recommend a hybrid approach with internal ownership to retain control and evidence for regulators and counsel.</p>

<p><strong>Benefits, Resources, and Risks Of Inaction: </strong>Benefits include reduced risk of boundary drift, demonstrable control operation for the OCC and auditors, and faster evidence production for exams and litigation. Estimated cost [X]; headcount [Y]; milestones tied to Consent Order reporting. Risks of inaction: Consent Order deadlines may be missed; likelihood of repeat configuration-related exposure remains elevated; additional regulatory or audit findings. We recommend approval of scope, budget, and timeline and authorize the CISO to execute and report progress quarterly to the Board and OCC.</p>

</div>

**Document-type guide:** [Strategic Security Initiative Justification](../../../../document-types/executive-board/strategic-security-initiative-justification.md)

**Writing tips:** [Writing best practices — Strategic Security Initiative Justification](../../../../studio/writing-best-practices.md#strategic-security-initiative-justification)
