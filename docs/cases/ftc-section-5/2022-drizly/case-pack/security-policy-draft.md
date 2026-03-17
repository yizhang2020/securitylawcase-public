# Security Policy Draft (FTC v. Drizly 2022)

> Draft or update enterprise security policy to support FTC consent order and program maturity.

---

## Purpose

Policies that support the consent order and address FTC findings: (1) **Information security program policy** — scope, coordinator, risk assessment, safeguards, training, testing, service provider oversight. (2) **Access control and authentication policy** — MFA requirements, password standards, role-based access, offboarding. (3) **Secure development and credential management** — no credentials in source code; repository scanning; change review. (4) **Data retention and minimization policy** — retention schedule, deletion or de-identification of unnecessary personal information. Policies should be written, approved, and available for examiner review.

---

## Hallucinated writing examples

**Scenario.** In November 2022, after the FTC accepted the consent order **(time)**, the Security Director **(role)** submits a security policy draft **(type)** to the CISO **(audience)** for approval and rollout to support information security program and retention obligations.

<div class="writing-example-formal">

<p><strong>SECURITY POLICY DRAFT — SUMMARY FOR APPROVAL</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Chief Information Security Officer<br>
<strong>From:</strong> Security Director<br>
<strong>Date:</strong> November 22, 2022<br>
<strong>Re:</strong> Policy Package — Information Security Program, IAM, Secure Development, and Data Retention</p>
</div>

<p>This package summarizes the core policies required to operate the information security program and data minimization obligations reflected in the FTC Decision and Order (FTC Docket No. 2023185). The scenario is illustrative; the obligations and topics are grounded in the Order and the FTC’s complaint allegations.</p>

<p><strong>1) Information Security Program Policy (Program Governance).</strong><br>
Defines program scope, designated coordinator, risk assessment cadence, safeguards, training, testing and monitoring, service provider oversight, and documentation and evidence requirements.</p>

<p><strong>2) Access Control and Authentication Policy (IAM).</strong><br>
Requires MFA for accounts with access to source code or production credentials; defines role-based access, access reviews, account lifecycle controls, and password and session standards where applicable.</p>

<p><strong>3) Secure Development and Credential Management Policy (Secrets).</strong><br>
Prohibits secrets in source code or repositories; requires automated secret scanning, credential rotation workflows, change review for high-risk settings, and incident handling for credential exposure.</p>

<p><strong>4) Data Minimization and Retention Policy (Data Security).</strong><br>
Implements a retention schedule; requires deletion or de-identification when data is no longer necessary; limits collection and use to what is necessary for specified purposes; defines evidence and auditability.</p>

<p><strong>Requested approval.</strong> Approve the policy package for publication and enforcement, including policy ownership, effective dates, and quarterly compliance reporting.</p>

</div>

## Primary sources

- **FTC Decision and Order:** [Decision and Order — Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **FTC Complaint:** [Complaint](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
