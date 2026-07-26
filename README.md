# Playwright + AI-Assisted QA Automation

A second, independent QA pass on the same app as my
[Selenium + Cucumber project](https://github.com/wv511-create/selenium-cucumber-qa-automation) —
this time using Python, Playwright, and Pytest, with the Page Object Model.

Alongside automation, I ran a structured manual exploratory testing session to
find real functional issues in the app — several are still open and documented
below with full reproduction steps. This project also includes an
AI-assisted bug reporting feature: on any automated test failure, a
locally-run AI model automatically drafts a structured bug report, which I
review by hand before treating it as final.

## Tech stack

- Python 3.14
- Playwright, Pytest, pytest-playwright, pytest-html
- Page Object Model
- Ollama (local LLM, `llama3.2:1b`) for AI-assisted bug report drafting

## Project structure

```
playwright-ai-assisted-qa-automation/
├── pages/                    Page Object Model classes
├── tests/                    Playwright test suite + conftest.py hook
├── bug_report_generator.py   Ollama-based bug report generator
├── bug-reports/               example AI-drafted reports
├── manual-testing/            charter, session notes, full bug log
├── screenshots/                test run evidence
├── reports/                    generated HTML test report
├── requirements.txt
└── pytest.ini
```

## Automated test scenarios

1. **Farmer Registration** — launch app, enter details, log in as Farmer,
   verify machine listing page loads
2. **Machine Browsing** — verify search box, machine cards, categories, and
   Book Now buttons render
3. **Machine Booking** — select a machine, open booking page, confirm booking,
   verify status shows Pending
4. **My Bookings** — complete a booking, open My Bookings, verify it appears
   with Cancel button visible

## Manual testing — bugs identified

A time-boxed exploratory session was run against registration, browsing, and
booking, using a written test charter. Full details are in `/manual-testing`.

| Bug ID | Description | Severity |
|---|---|---|
| BUG-01 | Booking succeeds with invalid registration credentials (phone number not validated) | High |
| BUG-02 | Invalid registration input accepted more broadly | Medium |
| BUG-03 | Machine category filter buttons don't respond to clicks | High |
| BUG-04 | Search does not filter or return results | High |
| BUG-05 | Cancel Booking button does not respond to clicks | High |
| BUG-06 | Booking flow accepts invalid input without validation | Medium |
| BUG-08 | Accepted / Declined tabs don't switch the displayed view | High |
| BUG-10 | Rental duration (+/-) controls not working | Medium |

Two originally logged items — page refresh logging the user out, and bookings
not persisting after re-login — were reclassified as expected behavior rather
than bugs, since the app runs entirely in-memory with no backend by design.

These bugs are intentionally left unfixed, since the bug log itself — with
proper severity classification and full reproduction steps — is the artifact
this part of the project demonstrates.

## Agentic AI-assisted bug reporting

On any test failure, a pytest hook (`tests/conftest.py`) triggers a multi-step
decision pipeline in `bug_report_generator.py` — not a single AI call:

1. **Duplicate check** — scans existing reports in `bug-reports/` and skips
   generating a new one if a similar failure has already been documented.
2. **Rule-based severity signal** — a fast, deterministic check against known
   high/medium-impact keywords (booking, payment, registration vs. filter,
   search, display), computed before any AI call.
3. **LLM-drafted report** — a locally-run AI model (Ollama, `llama3.2:1b`)
   drafts the bug report, informed by the rule-based signal but able to
   override it based on the actual error content.

Every draft is explicitly marked `DRAFT — pending human review`, and every
report is reviewed by hand before being treated as final. The rule-based
signal and the AI's own assessment sometimes disagree — that disagreement is
intentional and useful, since it surfaces genuine ambiguity for the human
reviewer rather than silently picking one.

Runs entirely offline — no external API calls, no cost, no data leaves the
machine.

Example reports:
- `bug-reports/cancel_booking_button_not_functional.md`
- `bug-reports/category_filter_buttons_unresponsive.md`
- `bug-reports/search_does_not_filter_results.md`
`

## Run locally

```bash
git clone https://github.com/wv511-create/playwright-ai-assisted-qa-automation.git
cd playwright-ai-assisted-qa-automation

python -m venv venv
venv\Scripts\activate        # Windows

pip install -r requirements.txt
playwright install
```

In a separate terminal, start the app this suite tests against (from the
[selenium-cucumber-qa-automation](https://github.com/wv511-create/selenium-cucumber-qa-automation)
repo):
```bash
cd web-prototype
python -m http.server 3000
```

Then run the tests:
```bash
python -m pytest -v
```

Generate the HTML report:
```bash
python -m pytest --html=reports/report.html --self-contained-html
```

## Test execution result

![Test run — 4 passed](screenshots/test-run-4-passed.png)

```
4 PASSED, 0 FAILED
```

A full interactive HTML report is generated at `reports/report.html`. GitHub
doesn't render HTML inline, so clone the repo and open it directly in a
browser, or regenerate it with the command above.

## What this project demonstrates

UI automation with Playwright (Python, sync API), test framework design with
Pytest and the Page Object Model, structured manual/exploratory testing with a
written charter, bug identification with severity classification, and
building a local, offline AI-assisted tool integrated directly into a test
pipeline.

## Author

Kittu
