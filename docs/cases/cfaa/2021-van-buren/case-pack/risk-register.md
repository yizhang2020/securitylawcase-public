# Risk Register (Van Buren v. United States (2021))

## Purpose

This register captures material risks highlighted by Van Buren v. United States (2021) with severity, impact pathway, mitigation plan, and evidence expectations. It is intended for ongoing governance and audit use so risk acceptance, remediation progress, and accountability remain explicit over time.

## Risk Register

### AUTH-MISUSE-01 — Misuse of authorized access
- **Severity:** High
- **Description:** Users with valid access can still misuse sensitive information for improper purposes.
- **Impact:** Insider harm and legal response complexity.
- **Mitigation:** Purpose-aware monitoring, approvals on sensitive queries, and separation of duties.
- **Evidence:** Query audit logs, monitoring alerts, approval records.

### ENTITLE-02 — Over-broad role entitlements
- **Severity:** High
- **Description:** Static, broad access roles increase opportunity for unauthorized data use.
- **Impact:** Expanded insider and compromise impact.
- **Mitigation:** Least-privilege redesign with recurring recertification.
- **Evidence:** Entitlement inventories, recertification attestations, access diffs.

### PLAYBOOK-03 — Outdated incident playbooks
- **Severity:** Medium
- **Description:** Playbooks relying solely on CFAA theories may be insufficient post-Van Buren.
- **Impact:** Delayed or ineffective legal/HR response.
- **Mitigation:** Counsel-reviewed runbooks covering alternative legal remedies and response paths.
- **Evidence:** Runbook versions, legal review sign-offs, tabletop outcomes.

### LOG-04 — Insufficient immutable audit trails
- **Severity:** Medium
- **Description:** Weak logging can impede investigation quality and evidentiary reliability.
- **Impact:** Longer investigations and weaker disciplinary outcomes.
- **Mitigation:** Immutable logging controls and retention standards for sensitive systems.
- **Evidence:** Log integrity reports, retention attestations, chain-of-custody records.

### JIT-05 — Break-glass governance risk
- **Severity:** Medium
- **Description:** Emergency access paths may remain overused without strict controls.
- **Impact:** Untracked privileged activity risk.
- **Mitigation:** Time-bound break-glass with mandatory post-use review and approval.
- **Evidence:** Break-glass usage logs, review approvals, exception register.

