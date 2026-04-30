# Implementation Checklist (TikTok Inc. v. Garland)

> 0-30 / 30-60 / 60-90 day execution checklist.

## Purpose

This document converts *TikTok Inc. v. Garland* into a practical security, legal, and governance artifact. It is grounded in the Supreme Court's narrow First Amendment holding and the opinion's discussion of data collection, recommendation algorithms, source code, foreign-adversary control, and qualified divestiture.

## Hallucinated writing examples

**Scenario:** (2025) (Security/legal lead) (executive, regulator, customer, or assessor audience) (Program owner drives implementation after board approval.)

<div class="writing-example-formal">
<p><strong>Subject: </strong>Implementation Checklist for TikTok platform-control risk governance</p>
<p><strong>Context: </strong>The Supreme Court affirmed the D.C. Circuit in a case involving a foreign-adversary controlled application statute, TikTok's U.S. user scale, sensitive data collection, recommendation algorithms, and ByteDance control. The opinion emphasized that the holding is narrow, but it treats data collection and platform control as concrete national-security issues when a foreign adversary can influence access, code, or operations.</p>
<p><strong>Decision or ask: </strong>Approve a cross-functional workstream focused on sequencing platform-control remediation. The work should be led jointly by Security, Product Engineering, Privacy, Legal, Government Affairs, GRC, and Communications so technical facts, legal positions, and external statements remain consistent.</p>
<p><strong>Implementation: </strong>Sequence data inventory, access restrictions, algorithm ownership review, source-code dependency mapping, evidence automation, and board reporting. Phase one inventories sensitive data, user-scale exposure, privileged access, source-code custody, and recommendation-system dependencies. Phase two validates whether controls are technically enforceable through logging, segmentation, change approval, and independent evidence. Phase three converts the evidence into board reporting, customer explanations, and regulator-ready documentation.</p>
<p><strong>Measurement: </strong>Track data-inventory coverage, percentage of privileged access reviewed, cross-border transfer exceptions, recommendation-system changes with complete approval records, source-code dependency findings, unresolved high-risk issues, and evidence accepted without rework during review.</p>
<p><strong>Expected output: </strong>A 0-30 / 30-60 / 60-90 day execution checklist. Success means leadership can explain who controls the platform, what data is exposed, how algorithmic and code changes are governed, what residual foreign-control risks remain, and which evidence proves the controls are operating.</p>
</div>

[Document type guide](../../../../studio/document-types.md) · [Writing tips](../../../../studio/writing-best-practices.md)
