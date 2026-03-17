# Controls → Evidence Map (FTC v. Drizly 2022)

Maps **required control state** to **evidence artifacts** and **verification signals** for FTC consent order compliance and audit readiness.

---

## 1) Access control and credential management

**Required control state:** Multifactor authentication for all accounts with access to source code or production credentials; no credentials stored in source repositories; role-based access and timely offboarding; strong password or equivalent policy.

**Evidence artifacts:** MFA enrollment and enforcement logs; access review records; repository scanning results (no secrets); offboarding checklist and timestamps.

**Verification signals:** Percentage of privileged accounts with MFA; number of credentials found in repos (target zero); time from offboarding to access revocation.

---

## 2) Monitoring and detection

**Required control state:** Logging and monitoring for anomalous access and exfiltration; regular assessments of protection measures; detection and response capability.

**Evidence artifacts:** Log source inventory; retention policy; detection rules and alert thresholds; sample investigation tickets with outcomes.

**Verification signals:** Log coverage; mean time to detect anomalous access; assessment report dates and remediation closure.

---

## 3) Data minimization and retention

**Required control state:** Published data retention schedule; process to delete or de-identify personal information when no longer necessary; no collection or use beyond necessity.

**Evidence artifacts:** Data retention schedule (public or internal); deletion logs or de-identification records; data inventory by purpose and retention period.

**Verification signals:** Retention schedule compliance; volume of data deleted or de-identified per period.

---

## 4) Program governance and assessment

**Required control state:** Written information security program; designated coordinator; risk assessment; training; testing; service provider oversight; biennial independent third-party assessment.

**Evidence artifacts:** Program document; risk register; training records; test and assessment reports; third-party assessment report (biennial).

**Verification signals:** Program update date; risk review cadence; assessment report date and scope.

---

## Primary sources

- **FTC Decision and Order:** [Decision and Order — Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
- **FTC Complaint:** [Complaint](https://www.ftc.gov/system/files/ftc_gov/pdf/202-3185-Drizly-Complaint.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
