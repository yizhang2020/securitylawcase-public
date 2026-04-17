# Executive Security Risk Summary (SEC v. SolarWinds Corp. et al.)

> Use this to present a consolidated view of security risks and mitigation to executives; supports risk acceptance and resource decisions under securities enforcement and supply-chain scrutiny.

---

## Purpose

This executive summary consolidates the highest-priority security and legal risks arising from the SUNBURST supply-chain campaign and SEC enforcement action against SolarWinds and related developments, with impact framing, mitigation status, and near-term decision points for senior leadership. It supports cross-functional alignment among security, legal, finance, and operations on risk treatment and accountability.

## Hallucinated writing examples

**Scenario:** In an illustrative period after the SEC filed its October 2023 complaint **(time)**, the Security Director, Technology Risk **(role)** prepares an executive security risk summary **(type)** for Chief Executive Officer, Chief Risk Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>EXECUTIVE SECURITY RISK SUMMARY</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Chief Executive Officer, Chief Risk Officer<br>
<strong>From: </strong>Security Director, Technology Risk<br>
<strong>Date: </strong>January 15, 2024<br>
<strong>Subject: </strong>Consolidated Security Risk Summary — SEC Civil Action (S.D.N.Y.); Press Release 2023-227; Post–SUNBURST Disclosure</p>
</div>

<p><strong>Executive Summary: </strong>Cyber and securities risk are intertwined after December 2020 public disclosure of the SUNBURST supply-chain compromise affecting Orion customers and parallel scrutiny of prior public statements about cybersecurity and internal assessments. On October 30, 2023, the SEC filed a civil complaint (see SEC Press Release 2023-227 and the filed complaint) alleging fraud, internal accounting control, and disclosure control failures tied to cyber disclosures—creating executive exposure beyond traditional incident-response metrics. Later motion practice (e.g., district court decision reported at 741 F. Supp. 3d 37) and stipulated dismissal with prejudice (Litigation Release LR-26423, 2025) affect ongoing governance lessons but do not diminish the program imperatives below.</p>

<p><strong>Risk Landscape: </strong>(1) Secure SDLC and build integrity—pipeline protections, signing, and tamper detection. (2) Developer and build environment access—least privilege, MFA, monitoring. (3) Customer trust and incident coordination—supply-chain response at scale. (4) Disclosure controls—alignment of engineering facts with investor communications. (5) Regulatory and civil overhang—multi-year legal cost and reputational drag.</p>

<p><strong>Top Risks (Abbreviated): </strong>(1) <em>Build/pipeline compromise recurrence.</em> Catastrophic impact class-wide. Mitigation: SLSA-style controls, segregated signing, anomaly detection on build outputs; quarterly third-party tests. (2) <em>Weakness in vulnerability management messaging.</em> High securities-law exposure if public statements diverge from internal assessments. Mitigation: unified disclosure review with Legal and Finance; documentation discipline. (3) <em>Customer forensic and contractual demands.</em> High operational load. Mitigation: customer success war-room, prioritized hotline for critical sectors. (4) <em>Executive and CISO personal exposure narratives.</em> Medium–high in enforcement climate. Mitigation: independent board oversight of security program funding and independence.</p>

<p><strong>Gaps and Initiatives: </strong>Key gaps: end-to-end SBOM and artifact provenance for releases; closed-loop remediation for penetration findings touching the build. Initiatives: executive dashboard for pipeline controls and customer-facing incident SLAs. We request risk acceptance for phased rollout constraints with revisit June 2024, budget for pipeline security engineering and disclosure controls testing, and metrics (build attestation coverage percent, mean time to patch build systems, disclosure control test exceptions) for the next executive review.</p>

</div>

**Document-type guide:** [Executive Security Risk Summary](../../../../document-types/executive-board/executive-security-risk-summary.md)

**Writing tips:** [Writing best practices — Executive Security Risk Summary](../../../../studio/writing-best-practices.md#executive-security-risk-summary)
