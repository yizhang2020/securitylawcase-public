# Security Policy Draft (FTC v. Drizly 2022)

> Use this to draft or update an enterprise security policy; defines required behavior and controls in policy language and supports consistency and auditability.

---

## Purpose

This draft policy converts lessons and obligations from FTC v. Drizly 2022 into enforceable internal requirements, control expectations, and governance responsibilities. It is structured for review by security leadership, legal, and affected business owners before formal adoption.

## Hallucinated writing examples

**Scenario:** In an illustrative period following the FTC October 2022 consent order after the July 2020 Drizly breach **(time)**, the Security Director **(role)** prepares a security policy draft **(type)** for Engineering and security operations staff **(audience)**.

<div class="writing-example-formal">

<p><strong>ENTERPRISE SECURITY POLICY — DRAFT</strong></p>

<div class="doc-meta">
<p><strong>Policy title: </strong>Identity, Secrets, and Data Retention Security Policy<br>
<strong>Version: </strong>1.0 (Draft)<br>
<strong>Owner: </strong>Chief Information Security Officer<br>
<strong>Effective date: </strong>Upon approval<br>
<strong>Last reviewed: </strong>December 2022<br>
<strong>Context: </strong>FTC Docket No. 2023185 program implementation requirements</p>
</div>

<p><strong>Purpose and Scope: </strong>This policy establishes enforceable requirements for privileged identity controls, secret-management practices, monitoring, and retention governance aligned to FTC order obligations following the 2020 incident. It applies to all personnel managing source code, cloud administration, and consumer data systems.</p>

<p><strong>Policy Statement: </strong>The organization shall enforce MFA on privileged paths, prevent credentials in repositories, implement monitoring and retention controls, and govern exceptions under formal approval and review.</p>

<p><strong>Roles and Responsibilities: </strong>The CISO owns policy governance. Engineering managers implement control standards; security operations maintain monitoring and evidence; compliance/legal review adherence to order obligations.</p>

<p><strong>Requirements: </strong>(1) Privileged and sensitive access shall require MFA and periodic recertification. (2) Secrets in source repositories are prohibited; violations require immediate remediation. (3) Logging and retention for designated systems shall meet order and legal requirements. (4) Data retention/deletion controls shall follow approved schedules. (5) Exceptions require risk acceptance with revisit date and quarterly review.</p>

</div>

**Document-type guide:** [Security Policy Draft](../../../../document-types/policy-governance/security-policy-draft.md)

**Writing tips:** [Writing best practices — Security Policy Draft](../../../../studio/writing-best-practices.md#security-policy-draft)
