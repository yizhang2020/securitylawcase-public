# Security Program Status Report (SEC v. SolarWinds Corp. et al.)

> Use this to report program health, key metrics, and progress to leadership; supports secure SDLC, build integrity, and disclosure alignment after a supply-chain incident.

---

## Purpose

This status report translates post–SUNBURST remediation and securities-enforcement scrutiny into measurable program execution: build pipeline controls, developer environment access, detection, and evidence for disclosures. It gives leadership a consistent view of whether remediation is on track and where escalation or resourcing is required.

## Hallucinated writing examples

**Scenario:** In an illustrative period after public disclosure of the SUNBURST campaign and SEC enforcement filings **(time)**, the Lead Security Engineer, Secure SDLC **(role)** prepares a security program status report **(type)** for Security Director, Chief Information Security Officer **(audience)**.

<div class="writing-example-formal">

<p><strong>SECURITY PROGRAM STATUS REPORT</strong></p>

<div class="doc-meta">
<p><strong>To: </strong>Security Director, Chief Information Security Officer<br>
<strong>From: </strong>Lead Security Engineer, Secure SDLC<br>
<strong>Date: </strong>January 15, 2024<br>
<strong>Reporting period: </strong>Post–SUNBURST remediation emphasis (July 2023–January 2024)</p>
</div>

<p><strong>Overview: </strong>This report summarizes security program status following December 2020 public disclosure of the SUNBURST supply-chain compromise affecting Orion customers and subsequent SEC civil enforcement (see Commission complaint filed October 30, 2023, and related materials). Executive and engineering attention focuses on build integrity, signing, developer environment access, and alignment between internal security assessments and public statements. This report covers pipeline hardening, artifact provenance, privileged access to build systems, customer-facing incident coordination metrics, and disclosure control testing support.</p>

<p><strong>Incident Context: </strong>Remediation has prioritized segregated build and signing, tamper detection on release artifacts, monitoring of development environments, and coordinated customer communications under counsel guidance.</p>

<p><strong>Metrics and Progress: </strong>During the reporting period we have: (1) Achieved build attestation coverage for approximately 73% of production release artifacts (target 90%). (2) Enforced MFA and PAM on roughly 88% of administrative paths to build infrastructure (target 98%). (3) Reduced mean time to patch build-system CVEs from 14 days to 6 days. (4) Onboarded additional detection content for anomalous commits and unusual publishing activity; 76% of developer workstations in scope under updated EDR posture. (5) Completed two disclosure-control test cycles with Finance and Legal; remediated 11 of 18 exceptions.</p>

<p><strong>Issues and Next Period: </strong>Residual gaps include phased rollout constraints on legacy pipeline stages and backlog of penetration findings touching the build. Priorities: raise attestation coverage, complete PAM scope, finish SBOM linkage for releases, and sustain cross-functional disclosure review cadence. This report supports internal oversight and multi-year legal process readiness.</p>

</div>

**Document-type guide:** [Security Program Status Report](../../../../document-types/executive-board/security-program-status-report.md)

**Writing tips:** [Writing best practices — Security Program Status Report](../../../../studio/writing-best-practices.md#security-program-status-report)
