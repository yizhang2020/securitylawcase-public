# Audit Packet Checklist (48-hour evidence readiness) — SolarWinds (SEC 2023 context)

If examined (regulator, auditor, litigation), you should be able to produce the following within **48 hours**.

## A) Architecture + boundaries
- Secure-build and software-release architecture diagrams with trust boundaries.
- Inventory of build/release infrastructure and ownership for security controls.
- Boundary-control documentation for environments handling signing and release artifacts.

## B) Change control proof
- Change approvals for secure-build, access, and pipeline-hardening controls.
- Emergency change logs during major remediation windows with after-action reviews.
- Traceable ticket evidence tying risk findings to implemented changes.

## C) IAM least privilege proof
- Privileged-access inventory for build systems, signing infrastructure, and production services.
- Access-review and recertification records with remediation for excess privileges.
- MFA/session-control evidence for high-risk engineering and admin roles.

## D) Logging + monitoring proof
- Log-source map for build pipelines, auth events, code-signing actions, and telemetry.
- Retention and integrity evidence for logs used in incident and disclosure support.
- Detection-rule documentation and investigation tickets for supply-chain abuse indicators.

## E) Risk management & governance
- Risk-register entries mapped to SEC allegations, litigation posture, and controls.
- Executive/board reporting artifacts on secure-development remediation progress.
- Independent assessments and closure records for high-priority control gaps.

## F) Incident response readiness
- IR runbooks for supply-chain compromise and software integrity events.
- Evidence collection and chain-of-custody documentation for forensic support.
- Tabletop outputs for coordinated legal, security, and disclosure response.
