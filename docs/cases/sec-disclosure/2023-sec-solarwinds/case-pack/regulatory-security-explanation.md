# Regulatory Security Explanation (SEC v. SolarWinds Corp. et al. — disclosure and controls)

> Use this to explain security monitoring, SDLC controls, and disclosure alignment in SEC cyber enforcement contexts.

---

## Purpose

This explanation frames the organization’s security posture for regulator, examiner, or counsel review in light of SEC v. SolarWinds and related litigation developments. It connects governance, technical controls, and evidence practices to the relevant legal or enforcement context so external stakeholders can assess control reasonableness and implementation maturity.

## Hallucinated writing examples

**Scenario:** In an illustrative period after the SEC’s October 30, 2023 complaint and subsequent motion practice **(time)**, SolarWinds Corporation — Chief Information Security Officer **(role)** prepares a regulatory security explanation **(type)** for U.S. Securities and Exchange Commission — Enforcement staff **(audience)** (illustrative).

<div class="writing-example-formal">

<p><strong>REGULATORY SECURITY EXPLANATION</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>U.S. Securities and Exchange Commission — Enforcement Staff (Illustrative)<br>
<strong>From: </strong>SolarWinds Corporation — Chief Information Security Officer<br>
<strong>Date: </strong>January 15, 2024<br>
<strong>Re: </strong>Security Program, SDLC Controls, and Disclosure Support — SEC Litigation Release and Complaint (PR-2023-227)</p>
</div>

<p><strong>Introduction: </strong>This submission describes SolarWinds’ security program and controls relevant to software development, integrity of build and distribution, monitoring of intrusions affecting the development environment, and support for public disclosures following the Commission’s October 30, 2023 enforcement action (<em>SEC v. SolarWinds Corp.</em> et al., see Commission complaint and Litigation Release LR-26423 and related docket materials). The complaint’s theories (as alleged) concern fraud, internal accounting controls, and disclosure controls in connection with cybersecurity risks and the SUNBURST campaign. The scope of this letter includes governance, risk management, secure SDLC and code-signing controls, detection and incident response, and evidence practices for disclosure and regulatory inquiries. Assertions are supportable by the attached evidence index.</p>

<p><strong>Governance: </strong>Executive oversight of product security, secure development practices, and incident management is documented through defined roles, committees, and escalation to legal and finance for material incidents. The CISO coordinates cross-functional response where technical facts may affect investor communications.</p>

<p><strong>Risk Management: </strong>Priority risks include <em>compromise of build or update pipelines</em>, <em>supply-chain threats affecting customers</em>, <em>detection gaps for sophisticated intrusions</em>, and <em>coordination between engineering facts and disclosure obligations</em>. Risks are tracked with mitigation milestones and linkage to testing outputs.</p>

<p><strong>Control Environment and Evidence Of Operation: </strong>Key controls by domain: (1) <em>Secure SDLC and code integrity.</em> Code review, secrets management, signing processes, and build pipeline protections. Evidence: pipeline configs, signing records, change approvals. (2) <em>Environment segregation and access.</em> Least privilege for build systems; MFA; monitoring of administrative access. Evidence: IAM reviews, PAM artifacts, access logs (samples). (3) <em>Monitoring and threat detection.</em> EDR/SIEM coverage for corporate and development environments; hunting procedures. Evidence: detection engineering docs, alert samples, IR tickets. (4) <em>Incident response and customer coordination.</em> Playbooks for supply-chain scenarios; customer communications workflows with legal review. Evidence: IR summaries, comms approvals (samples). (5) <em>Disclosure controls support.</em> Processes ensuring material cybersecurity facts reach disclosure stakeholders. Evidence: disclosure control testing, issue remediation.</p>

<p><strong>Incidents and Remediation: </strong>The SUNBURST campaign involved compromise of software build processes and widespread customer impact. Remediation has emphasized pipeline security, detection, and governance of customer communications. Civil enforcement and motion practice continued on parallel tracks (including dismissal rulings in district court in the public record). This response is illustrative, submitted for staff review, and supported by the attached evidence index.</p>

</div>

**Document-type guide:** [Regulatory Security Explanation](../../../../document-types/regulatory-compliance/regulatory-security-explanation.md)

**Writing tips:** [Writing best practices — Regulatory Security Explanation](../../../../studio/writing-best-practices.md#regulatory-security-explanation)
