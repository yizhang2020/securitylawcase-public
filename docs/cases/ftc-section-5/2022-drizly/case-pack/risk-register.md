# Risk Register (FTC v. Drizly 2022)

## Purpose

An incident-grounded register of the material security risks revealed by the Drizly breach and FTC enforcement action, so security, engineering, and compliance teams can prioritize remediation and demonstrate control effectiveness against order requirements.
The entries below are prepared for copy and paste into `executive-security-risk-summary.md`, `security-program-status-report.md`, `compliance-justification-document.md`, and `security-governance-memo.md` (either in the main body where risk posture is discussed or as an appendix for detailed risk records).

## Risk Register

### IAM-CRED-01 — Credential Reuse and Missing MFA on Source Code Access
- **Severity:** Critical
- **Description:** Executive GitHub access relied on weak/reused credentials and lacked mandatory MFA, enabling account takeover.
- **Impact:** Unauthorized repository access and compromise of credentials with downstream production exposure.
- **Mitigation:** Enforce MFA for all source-code and privileged accounts, credential hygiene controls, and periodic access recertification.
- **Evidence:** MFA enforcement reports, identity policy settings, access review records, deprovisioning logs.

### SECRET-02 — Secrets Exposure in Repositories
- **Severity:** Critical
- **Description:** AWS/database credentials were present in source repositories accessible to compromised accounts.
- **Impact:** Rapid privilege escalation from code access to infrastructure and data-store access.
- **Mitigation:** Secrets manager adoption, repository secret scanning with blocking controls, rotation playbooks, and secure SDLC checks.
- **Evidence:** Secret-scan findings and closure history, key rotation records, pipeline policy checks, exception register.

### DET-RESP-03 — Insufficient Detection of Exfiltration Activity
- **Severity:** High
- **Description:** Monitoring controls did not detect malicious access and data exfiltration promptly; discovery came from external reporting.
- **Impact:** Longer attacker dwell time and larger data-loss window.
- **Mitigation:** Centralized telemetry, anomaly detections for privileged access/exfiltration, alert triage standards, and incident runbook testing.
- **Evidence:** SIEM coverage metrics, detection rule catalog, alert handling SLAs, incident timeline evidence.

### DATA-RET-04 — Excessive Data Retention and Minimization Gaps
- **Severity:** High
- **Description:** Personal data retention exceeded strict necessity, increasing breach impact and regulatory exposure.
- **Impact:** Expanded consumer harm potential and FTC compliance risk.
- **Mitigation:** Published retention schedule, deletion/de-identification workflows, purpose-based data inventory, and periodic retention audits.
- **Evidence:** Retention policy artifacts, deletion logs, inventory snapshots, audit findings and closure status.

### GOV-PROG-05 — Program Governance and Assurance Maturity Risk
- **Severity:** Medium
- **Description:** Security program governance, ownership formalization, and independent assurance were insufficiently mature pre-order.
- **Impact:** Compliance execution risk and weak evidentiary posture during regulatory review.
- **Mitigation:** Designated coordinator, documented security program, board-level reporting cadence, and biennial independent assessments.
- **Evidence:** Governance charters, reporting packs, assessor engagement and reports, remediation tracking.

**Document-type guide:** [Executive Security Risk Summary](../../../../document-types/executive-board/executive-security-risk-summary.md)

**Writing tips:** [Writing best practices — Executive Security Risk Summary](../../../../studio/writing-best-practices.md#executive-security-risk-summary)
