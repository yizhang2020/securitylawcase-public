# Audit Packet Checklist (48-hour evidence readiness) — Yahoo MDL (2018)

If examined (regulator, auditor, litigation), you should be able to produce the following within **48 hours**.

## A) Architecture + boundaries
- Legacy identity-store and account-service architecture diagrams (current + incident-era versions).
- Internet-facing authentication, recovery, and account-management service inventory with ownership.
- Boundary-control baselines for account data environments, including exception register with approvals and expiry.

## B) Change control proof
- Change tickets and approval records for authentication, session, and account-recovery control updates.
- Emergency-change logs tied to disclosed incident-response windows plus post-implementation reviews.
- PR approvals for high-risk security configuration changes affecting account data paths.

## C) IAM least privilege proof
- Privileged-access inventory for account and identity data stores.
- Quarterly access-review attestations with remediation tickets for stale/high-risk privileges.
- MFA-enforcement evidence and break-glass access logs with reviewer sign-off.

## D) Logging + monitoring proof
- Log-source matrix (auth events, account changes, admin actions, data-access events).
- Retention policy evidence and immutable storage configuration for incident-relevant logs.
- Alert rules and investigation-ticket samples for credential abuse and suspicious account activity.

## E) Risk management & governance
- Risk-register entries mapped to MDL allegations and remediation commitments.
- Governance committee minutes and executive reporting packets covering remediation status.
- Independent assessment or audit findings with closure evidence and target dates.

## F) Incident response readiness
- Incident-response plan and runbooks for account compromise and large-scale credential abuse.
- Forensic evidence index and chain-of-custody records for preserved incident artifacts.
- Tabletop-exercise records and lessons-learned tracker tied to MDL-relevant scenarios.
