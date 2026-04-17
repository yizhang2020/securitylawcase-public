# Security Policy Draft (Capital One 2019)

> Use this to draft or update an enterprise security policy; defines required behavior and controls in policy language and supports consistency and auditability.

---

## Purpose

This draft policy converts lessons and obligations from Capital One 2019 into enforceable internal requirements, control expectations, and governance responsibilities. It is structured for review by security leadership, legal, and affected business owners before formal adoption.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the 2019 Capital One cloud breach and related enforcement and litigation tracks **(time)**, the Security Director **(role)** prepares a security policy draft **(type)** for leadership stakeholders **(audience)**.

<div class="writing-example-formal">

<p><strong>ENTERPRISE SECURITY POLICY — DRAFT</strong></p>

<div class="doc-meta">
<p><strong>Policy title: </strong>Cloud Configuration and Boundary Security<br>
<strong>Version: </strong>1.0 (Draft)<br>
<strong>Owner: </strong>Chief Information Security Officer<br>
<strong>Effective date: </strong>Upon approval<br>
<strong>Last reviewed: </strong>November 2020<br>
<strong>Context: </strong>Post–July 2019 incident; OCC Consent Order (OCC NR 2020-98)</p>
</div>

<p><strong>Purpose and Scope: </strong>This policy establishes requirements for the design, change, and monitoring of cloud perimeter and boundary controls to reduce the risk of unauthorized access and to support audit and regulatory expectations, including those set forth in the Consent Order issued by the Office of the Comptroller of the Currency on August 6, 2020. The July 2019 cybersecurity incident involved exploitation of a misconfiguration in our AWS-hosted web application firewall (WAF); this policy is intended to prevent recurrence and to demonstrate control effectiveness to the OCC and other stakeholders. It applies to all business units and technology teams responsible for cloud-hosted systems that process [designated data].</p>

<p><strong>Policy Statement: </strong>The organization shall manage cloud perimeter and boundary controls (including WAF, routing, and exposure rules) using config-as-code with mandatory peer review. Changes shall be authorized, documented, and monitored for drift. Exceptions shall be requested, approved, and documented with rationale, mitigation, and revisit date. This approach aligns with the Consent Order's requirement for strengthened cloud security and risk management.</p>

<p><strong>Roles and Responsibilities: </strong>The CISO owns this policy and approves exceptions within defined criteria. Technology owners implement and operate controls per supporting standards. Risk owners acknowledge risk acceptances. Audit may verify compliance. The Security Director is responsible for maintaining supporting standards and evidence of implementation.</p>

<p><strong>Requirements: </strong>(1) Designated perimeter controls shall be defined in version-controlled configuration. (2) All changes shall follow the approved change workflow (e.g., pull request, review, approval). (3) Drift detection shall be enabled; exceptions remediated or formally accepted with revisit date. (4) Baselines and exceptions shall be documented and reviewed per [cadence]. Related documents: [Cloud Configuration Standard]; [Change Management Procedure]; [Risk Acceptance Procedure]. This policy shall be reviewed annually. Non-compliance shall be reported and remediated; repeated or material non-compliance may result in [consequences per HR/governance]. Revision history: [Version, date, summary.]</p>

</div>

**Document-type guide:** [Security Policy Draft](../../../../document-types/policy-governance/security-policy-draft.md)

**Writing tips:** [Writing best practices — Security Policy Draft](../../../../studio/writing-best-practices.md#security-policy-draft)
