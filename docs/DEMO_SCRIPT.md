# VANGUARD — Demo Video Script

**Target length:** 3–5 minutes  
**Owners:** Juliana (script + slides) · HELL (Band demo capture) · DEV (pipeline run)

---

## Act 1 — Problem (0:00 – 0:30)

**Visual:** Slide — lawyer drowning in PDFs, clock showing "6 weeks"

**Voiceover:**

> When a law firm audits a new SaaS vendor, lawyers spend 40 to 120 hours reading contracts, checking GDPR, SOC 2, and security clauses — per vendor. For a firm evaluating twenty providers a year, that's months of risk exposure and billable time lost.

**On screen:** Highlight manual checklist, red "HIGH RISK" stamp delayed weeks.

---

## Act 2 — Solution (0:30 – 1:00)

**Visual:** Slide — 8 agent icons in Band Room

**Voiceover:**

> Vanguard replaces that manual panel with eight AI agents in a Band Room: INTAKE ingests documents, LEXIS, SENTINEL, and LEDGER analyze in parallel, ARBITER runs structured debate, TRUTHLOCK kills hallucinations, and FORGE plus HERALD deliver the executive report.

**On screen:** Agent name cards — INTAKE · LEXIS · SENTINEL · LEDGER · ARBITER · TRUTHLOCK · FORGE · HERALD

---

## Act 3 — Live demo (1:00 – 3:30)

### Scene A — Upload (1:00 – 1:30)

**Visual:** Streamlit upload screen  
**Action:** Upload AWS or Google Workspace privacy PDF  
**Voiceover:** "We upload a real vendor privacy policy."

### Scene B — Band Room activity (1:30 – 2:30)

**Visual:** Band Room UI — message thread  
**Action:** Show INTAKE message → LEXIS/SENTINEL/LEDGER findings appear  
**Voiceover:** "INTAKE publishes the document hash. Three agents analyze in parallel inside the Room."

**Highlight:** ARBITER opens debate — @LEXIS @SENTINEL contradiction on data retention vs encryption  
**Voiceover:** "When agents disagree, ARBITER opens a structured debate — not a silent pipeline."

### Scene C — TRUTHLOCK (2:30 – 2:50)

**Visual:** TRUTHLOCK invalidation alert in Room  
**Action:** Show invalidation on injected bad claim (prepared test)  
**Voiceover:** "TRUTHLOCK verifies every claim against the source document. Unverified claims block the final report."

### Scene D — Delivery (2:50 – 3:30)

**Visual:** Telegram notification + Streamlit dashboard + PDF  
**Action:** Show 5-line Telegram summary, semáforo dashboard, PDF cover  
**Voiceover:** "HERALD delivers the Risk Score to Telegram, the dashboard, and a signed executive PDF — with the Band Room URL as audit evidence."

---

## Act 4 — Architecture (3:30 – 4:00)

**Visual:** Slide — 3 phases diagram from `docs/ARCHITECTURE.md`

**Voiceover:**

> Three phases: parallel analysis, deliberation with TRUTHLOCK, remediation and delivery. Band is the collaboration backbone — not a log.

---

## Act 5 — Business (4:00 – 4:30)

**Visual:** Slide — TPRM market, time saved

**Voiceover:**

> TPRM is an eight-billion-dollar market growing seventeen percent annually. Vanguard targets mid-size law firms that need enterprise-grade due diligence without enterprise budgets.

---

## Production checklist

- [ ] Screen recording: Streamlit + Band Room + Telegram (OBS)
- [ ] Voiceover recorded or live narration
- [ ] Background music (optional, low volume)
- [ ] Export 1080p MP4
- [ ] Upload unlisted YouTube + link in Lablab
- [ ] Backup: Loom link if YouTube delayed

---

## Fallback if live demo fails

Use pre-recorded Band Room screenshot sequence + voiceover. Never submit without Band Room visual evidence.
