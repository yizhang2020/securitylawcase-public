# Security Public Statement — Capital One (2019)

Public breach disclosure statement. This page links to the **official document**, provides a **writing analysis**, and a **sample rewrite** for the same incident type.

---

## Hallucinated writing examples

**Scenario.** On July 29, 2019, the same day the FBI arrests the individual responsible **(time)**, the Chief Information Security Officer **(role)** is required to draft the Company's public statement announcing the data security incident **(type)** for investors and the public **(audience)**. The statement will be issued that day and must be accurate, consistent with Legal and Communications guidance, and suitable for filing as an exhibit to SEC reports. The draft must cover what happened, what data was affected, what the Company is doing, and what customers can do—in a tone that is professional and appropriate for investors and the public.

<div class="writing-example-formal">

<p><strong>PRESS RELEASE — FOR IMMEDIATE RELEASE</strong></p>

<div class="doc-meta">
<p><strong>Subject:</strong> Capital One Announces Data Security Incident; Law Enforcement Notified<br>
<strong>Date:</strong> July 29, 2019<br>
<strong>Contact:</strong> [Media relations]</p>
</div>

<p>Capital One Financial Corporation (NYSE: COF) announced today that it has identified unauthorized access by an external actor to certain customer data stored in the Company's cloud infrastructure. The Company promptly fixed the vulnerability, notified federal law enforcement, and is cooperating with the investigation. An individual has been arrested in connection with the incident.</p>

<p><strong>What happened.</strong> On July 19, 2019, the Company learned of the incident through a responsible disclosure from a security researcher. The access involved data stored in infrastructure hosted on Amazon Web Services (AWS). The vulnerability has been secured and forensic evidence has been preserved for law enforcement and our investigation. The Company is not aware of any use or dissemination of the information for fraud; the investigation is ongoing.</p>

<p><strong>What was affected.</strong> The incident affects approximately 100 million individuals in the United States and approximately 6 million in Canada. Information involved includes data provided in connection with credit card and other consumer product applications, including names, addresses, dates of birth, and income. For a subset of individuals, Social Security numbers or bank account numbers were also accessed. Credit card account numbers and log-in credentials were not compromised. The Company has no evidence that the information has been used for fraud or disseminated.</p>

<p><strong>What we are doing.</strong> The Company has remediated the vulnerability, strengthened controls, and is notifying affected individuals. Free credit monitoring and identity protection services are being offered to affected customers. A dedicated webpage and phone line have been established for customer inquiries. We take our responsibility to protect customer information seriously and apologize for any concern this may cause.</p>

<p><strong>What you can do.</strong> Affected customers are encouraged to enroll in the offered credit monitoring, to monitor account and credit activity, and to be alert to phishing. The Company will not request full Social Security numbers or passwords by email or phone. For more information: [URL]. The Company is committed to protecting customer information and meeting its legal and regulatory obligations.</p>

</div>

---

## Official document

**Capital One press release (July 29, 2019)** — Data security incident announcement.

- **Primary (company):** [Capital One Announces Data Security Incident](https://www.capitalone.com/about/newsroom/capital-one-announces-data-security-incident/) (capitalone.com)
- **SEC exhibit (filed):** [Exhibit 99.1 — Press Release](https://www.sec.gov/Archives/edgar/data/927628/000092762819000262/exhibit991-pressrelease72919.htm) (sec.gov)

Read the original below (if your browser allows embedding), or open the links above in a new tab. Some hosts block iframe embedding; if the frame is empty, use the SEC link.

<div style="border:1px solid #ccc; border-radius:6px; overflow:hidden; margin:1em 0;">
<iframe src="https://www.sec.gov/Archives/edgar/data/927628/000092762819000262/exhibit991-pressrelease72919.htm" title="Capital One July 29 2019 press release (SEC exhibit)" width="100%" height="480" style="border:0;"></iframe>
</div>

*If the frame above does not load (e.g. due to SEC or browser restrictions), [open the SEC exhibit in a new tab](https://www.sec.gov/Archives/edgar/data/927628/000092762819000262/exhibit991-pressrelease72919.htm).*

---

## Writing analysis

**How the official statement is built**

- **Lead** — What happened and when, in one sentence; perpetrator arrested (reassurance).
- **CEO quote** — Apology and commitment; humanizes the response.
- **Scope** — Approximate numbers (100M US, 6M Canada); what was and was *not* compromised.
- **Data categories** — Clear bullets: application data, customer data, exceptions (140k SSNs, 80k bank accounts).
- **Actions** — Fixed vulnerability, working with law enforcement, notifying affected individuals, free credit monitoring.
- **Contact / next steps** — URL for more information; “investigation ongoing.”
- **FAQ** — Optional but effective: vulnerability, discovery, timing, encryption, cloud, financial impact. Reduces repeat inquiries and shows control of narrative.
- **Forward-looking / legal** — Cost range, insurance, efficiency guidance; cautionary language for investors.

**What works well**

- Factual, sequenced, and scoped; avoids speculation.
- Clear “what was not compromised” to reduce fear.
- Single CEO voice; commitment and next steps explicit.
- SEC exhibit version includes investor-oriented detail (costs, insurance) and safe-harbor language.

**What to improve**

- “Configuration vulnerability” is vague; a later FAQ adds a bit of detail but still no mention of SSRF/metadata. For a technical audience, a short, plain-language technical sentence would help without undermining legal posture.
- “Highly sophisticated individual” may age poorly once the threat actor was publicly identified; neutral wording (“external actor,” “unauthorized individual”) is more durable.
- Explicit “what you can do” (e.g., enroll in credit monitoring, watch for phishing) could be one short bullet block for affected individuals.

---

## Sample rewrite

*Below is a condensed, template-style version for the same type of incident (breach disclosure). Use it as a structure; replace placeholders with your own facts and legal review.*

---

**Sample rewrite**

**HEADLINE:** [Company] Announces Data Security Incident; Law Enforcement Involved

**[Date]** — [Company] announced today that it identified unauthorized access to certain personal information. [One sentence: what systems/data and approximate scope.]

[Company] [remediated the issue / fixed the vulnerability] and is working with federal law enforcement. [If applicable: individual(s) responsible have been arrested or identified.]

**What happened:** [One to two sentences: type of access, time frame, how discovered.]

**What was affected:** Approximately [X] individuals. Information involved includes [list]. The following were *not* compromised: [list].

**What we are doing:** We have [containment steps]. We are notifying affected individuals and [offering credit monitoring / identity protection / other]. We will continue to investigate and update [website/dedicated page] as we learn more.

**What you can do:** [Bullet: enroll in offered monitoring, watch for phishing, contact X for questions.]

**For more information:** [URL]. We apologize for the concern this may cause and are committed to [remediation / strengthening security].

---

*This sample rewrite is for structure and training only. Do not use for an actual disclosure without legal and leadership review.*
