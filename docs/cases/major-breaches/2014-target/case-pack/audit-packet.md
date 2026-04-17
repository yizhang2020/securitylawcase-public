# Audit Packet Checklist (48-hour evidence readiness) — Target (2014 breach context)

If examined (regulator, auditor, litigation), you should be able to produce the following within **48 hours**.

## A) Architecture + boundaries
- Cardholder-data environment architecture diagrams and segmentation boundary maps.
- POS and payment-processing system inventory with security ownership and data-flow boundaries.
- Firewall/WAF baseline documentation and approved exception register.

## B) Change control proof
- Change approvals for payment-environment segmentation and hardening updates.
- Emergency change records from containment periods with retrospective approvals.
- Ticket-to-deployment evidence for high-risk control fixes in POS/payment systems.

## C) IAM least privilege proof
- Privileged account inventory for payment and store operations systems.
- Access-review attestations and stale-access remediation records.
- Service-account governance evidence, including key rotation and scope restrictions.

## D) Logging + monitoring proof
- Log-source inventory (POS, endpoint security, network, authentication, data access).
- Retention and integrity-control evidence for incident and fraud-investigation logs.
- Detection rule catalog and investigation-ticket samples for card data exfiltration indicators.

## E) Risk management & governance
- Risk-register entries for payment-card security, third-party access, and segmentation risk.
- Board/committee reporting artifacts and remediation program status updates.
- Independent audit and PCI-related findings with remediation closure evidence.

## F) Incident response readiness
- IR plan and playbooks for payment-card compromise and malware on store systems.
- Forensic collection indexes and custody documentation for relevant evidence.
- Tabletop records focused on payment-environment compromise and external coordination.
