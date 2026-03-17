# Internal Security Directive (FTC v. Drizly 2022)

> Directive or mandate from leadership on access control, credential management, and data retention following the FTC order.

---

## Purpose

An internal directive that mandates: (1) multifactor authentication for all accounts with access to source code or production credentials; (2) prohibition on storing credentials in source repositories and requirement for repository scanning; (3) adherence to the data retention schedule and deletion of unnecessary personal information; (4) completion of the written information security program and biennial assessment per the FTC order. Issued by CEO or CISO; sets expectations and accountability for consent order compliance.

---

## Hallucinated writing examples

**Scenario.** In November 2022, after the FTC accepted the consent order **(time)**, the CISO **(role)** issues an internal security directive **(type)** to the Senior Lead Security Engineer **(audience)** to mandate specific control changes and evidence collection required for compliance.

<div class="writing-example-formal">

<p><strong>INTERNAL SECURITY DIRECTIVE</strong></p>

<div class="doc-meta">
<p><strong>To:</strong> Senior Lead Security Engineer<br>
<strong>From:</strong> Chief Information Security Officer<br>
<strong>Date:</strong> November 16, 2022<br>
<strong>Subject:</strong> Mandatory Controls — MFA, Secrets Handling, Monitoring, and Data Retention (FTC Docket No. 2023185)</p>
</div>

<p>This directive implements immediate control requirements aligned with the FTC Decision and Order accepted on October 24, 2022. The scenario is illustrative; the obligations reflected below are derived from the Order.</p>

<p><strong>1) MFA and access governance (effective immediately).</strong><br>
- Enforce MFA for all accounts with access to source code repositories and for any account capable of retrieving or deploying production credentials.<br>
- Complete an access review for privileged access; revoke stale access within five business days; document evidence.</p>

<p><strong>2) Secrets management (effective immediately).</strong><br>
- No credentials, tokens, or keys may be stored in source code or repositories.<br>
- Enable continuous secrets scanning; remediate findings through rotation and documented closure; maintain a “zero critical secrets” target.</p>

<p><strong>3) Monitoring and evidence readiness (30 days).</strong><br>
- Confirm logging coverage for authentication events, repository access, privileged cloud changes, and database access.<br>
- Implement detection for anomalous access and data exfiltration; maintain investigation tickets and outcomes.</p>

<p><strong>4) Data retention and minimization (30–60 days).</strong><br>
- Implement the data retention schedule and produce deletion or de-identification evidence for personal information no longer necessary for specified purposes.</p>

<p><strong>Reporting.</strong> Provide weekly written updates on completion status and evidence artifacts required for FTC requests and independent assessment readiness.</p>

</div>

## Primary sources

- **FTC Decision and Order:** [Decision and Order — Drizly, LLC, and James Cory Rellas](https://www.ftc.gov/system/files/ftc_gov/pdf/2023185-drizly-combined-consent.pdf), FTC Docket No. 2023185 (Oct. 24, 2022).
