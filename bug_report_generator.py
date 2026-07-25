import ollama
import os
import glob

# ---- STEP 1: Rule-based severity signal (fast, deterministic, no AI needed) ----
HIGH_SEVERITY_KEYWORDS = ["booking", "payment", "cancel_booking", "confirm_booking", "registration"]
MEDIUM_SEVERITY_KEYWORDS = ["filter", "search", "sort", "browsing", "category", "display", "ui", "style"]

def rule_based_severity_hint(test_name, error_message):
    text = (test_name + " " + error_message).lower()
    if any(word in text for word in HIGH_SEVERITY_KEYWORDS):
        return "likely High — involves a core transactional flow"
    if any(word in text for word in MEDIUM_SEVERITY_KEYWORDS):
        return "likely Medium — involves a secondary/UI feature"
    return "uncertain — let the model decide based on context"


# ---- STEP 2: Duplicate check (skip re-generating a report that already exists) ----
def find_existing_similar_report(test_name):
    safe_name = test_name.replace(" ", "_").replace("/", "_").replace("[", "").replace("]", "")
    key_terms = [w for w in safe_name.lower().split("_") if len(w) > 3]

    if not os.path.exists("bug-reports"):
        return None

    for filepath in glob.glob("bug-reports/*.md"):
        filename = os.path.basename(filepath).lower()
        matches = sum(1 for term in key_terms if term in filename)
        if matches >= 2:  # at least 2 meaningful words overlap -> likely the same bug
            return filepath
    return None


# ---- STEP 3: Draft the report, informed by steps 1 and 2 ----
def generate_bug_report(test_name, error_message):
    print(f"\n[Agent] Analyzing failure: {test_name}")

    existing = find_existing_similar_report(test_name)
    if existing:
        print(f"[Agent] Skipping — a similar report already exists: {existing}")
        return

    severity_hint = rule_based_severity_hint(test_name, error_message)
    print(f"[Agent] Rule-based severity signal: {severity_hint}")

    prompt = f"""You are helping a QA engineer draft a bug report from a
failed automated test. Write it in this exact format:

## Bug Report: [short title]
**Severity:** [High/Medium/Low, your best guess]
**Steps to reproduce:** [inferred from the test name and error]
**Expected result:** [what the test expected]
**Actual result:** [what the error says actually happened]

A rule-based check on this failure suggests: {severity_hint}
Use that as a starting signal, but override it if the error message clearly
suggests otherwise. This is a DRAFT for a human to review — do not claim
certainty you don't have.

Test name: {test_name}
Error message: {error_message}"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[{"role": "user", "content": prompt}]
    )

    report_text = response["message"]["content"]

    os.makedirs("bug-reports", exist_ok=True)
    safe_name = test_name.replace(" ", "_").replace("/", "_")
    filename = f"bug-reports/{safe_name}.md"

    with open(filename, "w") as f:
        f.write(report_text)
        f.write(f"\n\n---\n*Rule-based severity signal: {severity_hint}*")
        f.write("\n*DRAFT — pending human review*\n")

    print(f"[Agent] Draft bug report saved: {filename}")