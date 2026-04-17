# Executive Security Risk Summary (Capital One 2019)

> Use this to present a consolidated view of security risks and mitigation to executives; supports risk acceptance and resource decisions.

---

## Purpose

This executive summary consolidates the highest-priority security and legal risks arising from Capital One 2019, with impact framing, mitigation status, and near-term decision points for senior leadership. It supports cross-functional alignment among security, legal, finance, and operations on risk treatment and accountability.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Security Director, Technology Risk **(role)** prepares a executive security risk summary **(type)** for Chief Executive Officer, Chief Risk Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>EXECUTIVE SECURITY RISK SUMMARY</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Executive Officer, Chief Risk Officer<br>
<strong>From: </strong>Security Director, Technology Risk<br>
<strong>Date: </strong>September 30, 2020<br>
<strong>Subject: </strong>Consolidated Security Risk Summary — Post–July 2019 Incident and OCC Consent Order; Q3 2020</p>
</div>

<p><strong>Executive Summary: </strong>Cyber risk posture remains elevated as a direct result of the July 2019 incident and the Consent Order and $80 million civil money penalty issued by the Office of the Comptroller of the Currency on August 6, 2020 (OCC NR 2020-98). Top risks are explicitly tied to the root causes identified by the OCC and our internal review: cloud configuration governance, identity and access management (IAM), logging and retention, and evidence readiness. Mitigation is driven by Consent Order commitments and our internal roadmap; all items below map to risk register entries and consent order milestones.</p>

<p><strong>Risk Landscape: </strong>The incident involved the exploitation of a WAF misconfiguration on AWS-hosted infrastructure and over-permissioned IAM roles, leading to access to customer data. The OCC Consent Order requires the Bank to strengthen risk management, board reporting, cloud security, and third-party risk. Our risk categories accordingly are: (1) Cloud and perimeter—configuration drift and unauthorized change. (2) Identity and access—over-permissioned roles and third-party access. (3) Detection and response—logging, retention, and forensic readiness. (4) Third-party and supply chain—vendor access and control evidence.</p>

<p><strong>Top Risks (Abbreviated): </strong>(1) <em>Cloud boundary and WAF configuration.</em> High impact; root cause of the 2019 incident. Mitigation: config-as-code and drift detection for designated perimeter controls; target completion Q4 2020 per consent order. (2) <em>IAM over-permissioning.</em> High impact; enabled lateral access in the incident. Least-privilege review in progress; we are tracking a reduction in wildcard and over-scoped roles. (3) <em>Log coverage and retention.</em> Medium–high; insufficient logging was cited in the OCC findings. Centralized logging and retention policy are being implemented; evidence package readiness is improving.</p>

<p><strong>Gaps and Initiatives: </strong>Key gaps relative to Consent Order and risk register: independent validation of control effectiveness; full alignment of risk register to board and OCC reporting. Initiatives in progress: PR-based change workflow for perimeter controls, drift detection rollout, audit packet, and control-to-evidence mapping. We request risk acceptance for [specific exception] with revisit date March 2021, budget approval for [initiative] per the approved plan, and acknowledgment of Q4 priorities and metrics for the next executive review.</p>

</div>

**Document-type guide:** [Executive Security Risk Summary](../../../../document-types/executive-board/executive-security-risk-summary.md)

**Writing tips:** [Writing best practices — Executive Security Risk Summary](../../../../studio/writing-best-practices.md#executive-security-risk-summary)
