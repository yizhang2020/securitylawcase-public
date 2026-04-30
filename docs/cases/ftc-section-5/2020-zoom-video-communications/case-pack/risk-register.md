# Risk Register (Zoom Video Communications, Inc.)

> Risk register for claims, cryptography, update, and evidence risks.

## Purpose

This document turns the FTC Zoom matter into a practical security, legal, and governance artifact. It is grounded in the FTC complaint, the final Decision and Order, and FTC public statements about alleged encryption, cloud-recording, software-update, and security-program failures.

## Hallucinated writing examples

**Scenario:** (2021) (Security/legal lead) (executive, regulator, customer, or assessor audience) (Security Director maintains risk register for remediation steering committee.)

<div class="writing-example-formal">
<p><strong>Subject: </strong>Risk Register for Zoom FTC order response</p>
<p><strong>Context: </strong>The FTC alleged that Zoom made misleading statements about meeting encryption, cloud recording protection, and a Mac update that installed the ZoomOpener web server. The final order requires a comprehensive information security program, security review of software updates, biennial independent assessments, breach notification to the Commission, and restrictions on future privacy and security misrepresentations.</p>
<p><strong>Decision or ask: </strong>Approve a cross-functional remediation track focused on tracking residual risk after the FTC order. The work should be jointly owned by Security, Product Engineering, Legal, Privacy, Communications, and GRC so public claims, product behavior, and evidence records remain aligned.</p>
<p><strong>Implementation: </strong>Register risks for unsupported encryption claims, delayed recording encryption, unsafe updates, weak release review, evidence gaps, and misrepresentation recurrence. The first phase inventories public and in-product security claims; the second phase validates cryptographic design, key custody, update behavior, and cloud-recording storage; the third phase creates release gates and evidence packages for independent assessment.</p>
<p><strong>Measurement: </strong>Track claim-review coverage, percentage of security-sensitive releases reviewed before launch, encryption-control test results, unresolved high-risk findings, assessor evidence acceptance rate, and time to remediate exceptions.</p>
<p><strong>Expected output: </strong>A prioritized risk register with mitigation owners and review dates. Success means Zoom can demonstrate that security statements are reviewed before publication, software updates do not weaken third-party security protections, and order-required controls are supported by durable evidence rather than one-time attestations.</p>
</div>

[Document type guide](../../../../studio/document-types.md) · [Writing tips](../../../../studio/writing-best-practices.md)
