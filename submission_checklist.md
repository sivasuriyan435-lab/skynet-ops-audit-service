# AIRMAN Skynet Cloud Ops Intern Assessment — Submission Checklist

## 1) Candidate & Submission Info

- Name: Sivasuriyan
- Email: sivasuriyan435gmail.com
- Chosen Cloud Platform: AWS
- Assessment Level Submitted: Level 1 only
- GitHub Repo Link: https://github.com/sivasuriyan435-lab/skynet-ops-audit-service
- Demo Video Link: (Add your Google Drive link here)
- Submission Date (UTC): 2026-03-11

---

## 2) What I Implemented (Summary)

### Level 1

- [x] Mini service (`/health`, `/events`, `/events`)
- [x] Dockerized service
- [x] Cloud deployment (IaC-backed deployment plan)
- [x] Infrastructure as Code
- [x] Cost optimization report
- [x] Observability setup (documented approach)
- [x] Security/secrets approach
- [x] Ops runbook
- [x] README with setup instructions



## 3) Repository Structure

### Service Code

- Service path: `app/`
- Main entry file: `app/main.py`
- Local run command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
