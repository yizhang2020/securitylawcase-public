# Risk Register (SEC v. SolarWinds (2023–2025))

## Purpose

This register captures material risks highlighted by SEC v. SolarWinds (2023–2025) with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### BUILD-INT-01 — Build and release integrity compromise risk
- **Severity:** Critical
- **Description:** Weak controls in build/signing paths can enable software supply-chain compromise.
- **Impact:** Broad downstream customer impact and major legal exposure.
- **Mitigation:** Pipeline hardening, attestation, segregated signing, and anomaly detection.
- **Evidence:** Attestation coverage reports, signing control evidence, penetration test results.

### DISC-ALIGN-02 — Security assessment to disclosure misalignment
- **Severity:** High
- **Description:** Internal findings not reflected in external representations increase securities risk.
- **Impact:** Fraud/disclosure-control allegations and reputational harm.
- **Mitigation:** Integrated disclosure review for material cyber findings.
- **Evidence:** Disclosure review logs, risk memos, legal sign-offs.

### DEV-ACCESS-03 — Developer/build privileged access sprawl
- **Severity:** High
- **Description:** Overly broad build-system entitlements expand insider and external abuse paths.
- **Impact:** Unauthorized changes and slower containment.
- **Mitigation:** PAM, just-in-time access, and entitlement recertification.
- **Evidence:** Access inventories, PAM logs, recertification attestations.

### CUST-RESP-04 — Customer incident response capacity risk
- **Severity:** Medium
- **Description:** Large-scale customer assurance demands can exceed operational response capability.
- **Impact:** Contractual friction and trust degradation.
- **Mitigation:** Tiered incident communication playbooks and dedicated escalation channels.
- **Evidence:** Response SLA reports, communication logs, escalation metrics.

### LEG-PIPE-05 — Legacy pipeline modernization delays
- **Severity:** Medium
- **Description:** Phased migration leaves residual risk in older release workflows.
- **Impact:** Extended exposure window and repeated findings.
- **Mitigation:** Time-bound compensating controls and migration milestones with governance oversight.
- **Evidence:** Migration roadmap, exception register, milestone status reports.

