# Risk Register (In re Target Corp. MDL)

## Purpose

This register captures material risks highlighted by In re Target Corp. MDL with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### POS-SEG-01 — POS and store network segmentation drift
- **Severity:** Critical
- **Description:** Retail store environments can deviate from approved segmentation baselines.
- **Impact:** Lateral movement risk and payment-card data exposure.
- **Mitigation:** Gold-image enforcement, segmentation audits, and drift remediation windows.
- **Evidence:** Segmentation audit reports, gold-image compliance metrics, remediation tickets.

### VENDOR-REM-02 — Vendor remote access control weakness
- **Severity:** High
- **Description:** Third-party remote pathways can bypass intended trust boundaries if not tightly governed.
- **Impact:** Expanded attack surface and forensic complexity.
- **Mitigation:** Managed jump hosts, MFA, session recording, and vendor entitlement recertification.
- **Evidence:** Vendor access inventory, MFA compliance reports, session logs, review attestations.

### LOG-FOREN-03 — Forensic reconstruction limitations
- **Severity:** High
- **Description:** Fragmented logging across stores and corporate tiers impairs incident timeline reconstruction.
- **Impact:** Higher litigation and response cost due to evidence gaps.
- **Mitigation:** Centralized retention standards and legal-hold evidence indexing.
- **Evidence:** Log-retention attestations, SIEM coverage maps, evidence request response logs.

### REMED-BACK-04 — Critical remediation backlog accumulation
- **Severity:** Medium
- **Description:** Open high-risk findings persisting across quarters indicate delivery bottlenecks.
- **Impact:** Sustained residual risk and adverse litigation optics.
- **Mitigation:** Quarterly closure targets with board-visible escalation for aged items.
- **Evidence:** Backlog aging dashboard, governance minutes, closure verification reports.

### COMMS-ALIGN-05 — Technical-to-legal narrative misalignment
- **Severity:** Medium
- **Description:** Inconsistent technical facts and legal communications can undermine defense posture.
- **Impact:** Disclosure risk and reduced trust with court and counterparties.
- **Mitigation:** Joint legal/security review workflow for incident and remediation narratives.
- **Evidence:** Joint review checklist, approved statements archive, issue tracker.

