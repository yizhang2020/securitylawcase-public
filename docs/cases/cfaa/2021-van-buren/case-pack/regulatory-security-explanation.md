# Regulatory Security Explanation (*Van Buren v. United States* — CFAA program alignment)

> Use this to explain access controls and insider-threat programs where “authorization” under the CFAA is a live issue for cooperation with criminal authorities and civil oversight.

---

## Purpose

This explanation frames the organization’s security posture for regulator, examiner, or counsel review in light of *Van Buren v. United States*, 593 U.S. 327 (2021). It connects governance, technical controls, and evidence practices to the relevant legal or enforcement context so external stakeholders can assess control reasonableness and implementation maturity.

## Hallucinated writing examples

**Scenario:** In an illustrative period after the Supreme Court’s June 3, 2021 decision **(time)**, a financial services firm — Chief Information Security Officer **(role)** prepares a regulatory security explanation **(type)** for federal law enforcement cyber liaison staff **(audience)** (illustrative cooperation context).

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Federal Bureau of Investigation — Cyber Division (Liaison) (Illustrative)<br>
<strong>From: </strong>Regional Commerce Bank, N.A. — Chief Information Security Officer<br>
<strong>Date: </strong>September 10, 2021<br>
<strong>Re: </strong>IT Access Controls and Insider Threat Program — Alignment With <em>Van Buren</em> “Authorized Access” Framework</p>
</div>

<p><strong>Introduction: </strong>This submission describes the organization’s technical and administrative controls for defining and enforcing <em>authorized access</em> to computers and sensitive data in environments subject to the Computer Fraud and Abuse Act (CFAA). The Supreme Court held in <em>Van Buren v. United States</em>, 593 U.S. 327 (2021), that “exceeds authorized access” under the CFAA is limited and does not cover mere violation of use policies where access for a purpose is otherwise authorized—shaping how employers and investigators evaluate misuse cases. The scope of this letter includes governance of access policies, technical enforcement, monitoring, insider threat response, and evidence practices for investigations and referrals. It is intended to support structured dialogue with criminal authorities and internal stakeholders; it is not a legal opinion.</p>

<p><strong>Governance: </strong>Access policies distinguish <em>authentication</em> (who may log in) from <em>purpose limitations and handling rules</em> (what may be done with information). Legal, HR, and security jointly maintain role definitions, acceptable use, and escalation for suspected misuse. The CISO approves technical controls and monitoring scope consistent with policy and law.</p>

<p><strong>Risk Management: </strong>Priority risks include <em>insider access to sensitive databases for non-business purposes</em>, <em>service account misuse</em>, <em>elevated credential theft</em>, and <em>ambiguous “business purpose” justifications</em>. Risk treatment ties technical controls to documented employment and contractor terms and to investigation playbooks.</p>

<p><strong>Control Environment and Evidence Of Operation: </strong>Key controls by domain: (1) <em>Role-based access and least privilege.</em> Provisioning tied to job function; periodic recertification; separation of duties for sensitive queries. Evidence: IAM exports, recertification tickets, SoD matrices. (2) <em>Purpose logging and business justification.</em> Where systems support it, query logging with business context fields for high-risk data sets. Evidence: application logs, sample investigations, policy mapping. (3) <em>Monitoring and insider threat.</em> UEBA or rules-based alerting for anomalous access volumes, off-hours access, and bulk exports. Evidence: detection logic documentation, alert tickets, tuning records. (4) <em>Investigation readiness.</em> Preserved chain-of-custody for logs and exports provided to counsel or law enforcement. Evidence: forensic SOPs, evidence lockers, sample preservation records. (5) <em>Training and sanctions alignment.</em> Workforce training on authorized use; HR coordination for policy violations. Evidence: training completions, disciplinary process descriptions (high level).</p>

<p><strong>Incidents and Remediation: </strong>Where misuse is suspected, the organization follows coordinated legal, HR, and security procedures—recognizing <em>Van Buren</em>’s guidance on CFAA “authorization” analysis versus employment and contract remedies for policy breaches. This response is submitted for liaison review and is supported by the attached evidence index.</p>

</div>

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
