# 🚜 Namma Yantra - Playwright Automation Framework (Python)

## 📌 Project Overview
This project automates the testing of the **Namma Yantra** web prototype using
**Python**, **Playwright**, and **Pytest**. The framework follows the **Page
Object Model (POM)** design pattern to keep test scripts clean, reusable, and
maintainable.

Alongside automation, a structured **manual exploratory testing session** was
performed to identify real functional issues in the application — several of
which are still open, and documented below with full reproduction steps. This
project also includes an **AI-assisted bug reporting** feature: on any
automated test failure, a locally-run AI model automatically drafts a
structured bug report, which is then reviewed by hand before being finalized.

---

## 🛠 Tech Stack
- Python 3.14
- Playwright
- Pytest
- Pytest-Playwright
- Pytest-HTML (for report generation)
- Page Object Model (POM)
- Ollama (local LLM, `llama3.2:1b`) — used for AI-assisted bug report drafting
- Git & GitHub

---

## 📂 Project Structure
```
namma-yantra-playwright/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── machine_page.py
│   └── booking_page.py
│
├── tests/
│   ├── conftest.py              # pytest hook — triggers AI bug reports on failure
│   ├── test_registration.py
│   ├── test_machine_browsing.py
│   ├── test_booking.py
│   └── test_my_bookings.py
│
├── bug_report_generator.py      # Ollama-based AI bug report generator
│
├── bug-reports/                 # AI-drafted bug reports (example outputs included)
│
├── manual-testing/
│   ├── charter.md                # Exploratory testing charter
│   ├── session-notes.md          # Raw notes from the testing session
│   └── bug-log.md                # Full write-ups of bugs found manually
│
├── screenshots/
│   └── test-run-4-passed.png
│
├── reports/
│   └── report.html              # Generated HTML test report
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## ✅ Automated Test Scenarios

### 1. Farmer Registration
- Launch application
- Enter user details
- Log in as Farmer
- Verify machine listing page loads

### 2. Machine Browsing
- Verify search box is present
- Verify machine cards render
- Verify machine categories are present
- Verify Book Now buttons are present

### 3. Machine Booking
- Select first available machine
- Open booking page
- Confirm booking
- Verify booking status shows Pending

### 4. My Bookings
- Complete booking flow
- Open My Bookings
- Verify Pending booking appears
- Verify Cancel button visibility

---

## 🐞 Manual Testing — Bugs Identified

A time-boxed exploratory testing session was run against the registration,
browsing, and booking flow, using a written test charter. Full details —
charter, session notes, and complete bug write-ups with reproduction steps —
are in `/manual-testing`.

| Bug ID | Description | Severity |
|--------|--------------|----------|
| BUG-01 | Booking succeeds with invalid registration credentials (invalid phone number not validated) | High |
| BUG-02 | Invalid registration input accepted more broadly | Medium |
| BUG-03 | Machine category filter buttons (Tractor, Harvester, etc.) do not respond to clicks | High |
| BUG-04 | Search does not filter or return results | High |
| BUG-05 | Cancel Booking button does not respond to clicks | High |
| BUG-06 | Booking flow accepts invalid input without validation | Medium |
| BUG-08 | Accepted / Declined tabs do not switch the displayed view | High |
| BUG-10 | Rental duration (+/-) controls not working | Medium |

**Note:** two originally logged items — page refresh logging the user out, and
bookings not persisting after re-login — were reclassified as expected
behavior rather than bugs, since this app runs entirely in-memory with no
backend by design (see the main app's README for details), so no data
persistence across reloads is expected.

These bugs are intentionally left unfixed in the app, since the bug log itself
— written with proper severity classification and full reproduction steps —
is the artifact this section of the project is demonstrating.

---

## 🤖 AI-Assisted Bug Reporting

On any automated test failure, a `pytest` hook (`tests/conftest.py`)
automatically calls a locally-run AI model (Ollama, `llama3.2:1b`) to draft a
structured bug report — severity, steps to reproduce, and expected vs. actual
result — based on the failing test's name and error message. Every draft is
explicitly marked `DRAFT — pending human review` and is reviewed by hand
before being treated as final; nothing here is auto-filed or trusted blindly.

This runs entirely offline on the local machine — no external API calls, no
cost, and no data leaves the machine.

Example reports generated against real bugs found during manual testing:
- `bug-reports/cancel_booking_button_not_functional.md`
- `bug-reports/category_filter_buttons_unresponsive.md`
- `bug-reports/search_does_not_filter_results.md`

---

## ▶️ How to Run

### Clone Repository
```bash
git clone https://github.com/wv511-create/namma-yantra-qa.git
cd namma-yantra-qa
```

### Create and Activate Virtual Environment
```bash
python -m venv venv
```
Windows:
```bash
venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
playwright install
```

### Start the Application
In a separate terminal, start the web prototype (from the app's own repo):
```bash
cd path\to\namma-yantra-share-main\web-prototype
python -m http.server 3000
```
Leave this running — the test suite expects the app at `http://127.0.0.1:3000`.

### Run the Tests
```bash
python -m pytest -v
```

### Generate the HTML Report
```bash
python -m pytest --html=reports/report.html --self-contained-html
```

---

## 📊 Test Execution Result

![Test run — 4 passed](screenshots/test-run-4-passed.png)

```
=====================
4 PASSED
0 FAILED
=====================
```

## 📸 HTML Report

A full interactive HTML report is generated at `reports/report.html`. GitHub
doesn't render HTML files inline, so clone this repo and open the file
directly in a browser to view it, or regenerate it with the command above.

---

## 🎯 Learning Outcomes
- UI automation using Playwright (Python, sync API)
- Python test automation framework development with Pytest
- Page Object Model (POM) design
- Structured manual/exploratory testing with a written charter
- Bug identification, severity classification, and reproducible reporting
- Building a local, offline AI-assisted tool integrated into a test pipeline
- HTML test reporting
- Git & GitHub project management

---

## 👨‍💻 Author
Wani