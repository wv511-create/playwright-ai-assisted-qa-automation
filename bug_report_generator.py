import ollama
import os

def generate_bug_report(test_name, error_message):
    prompt = f"""You are helping a QA engineer draft a bug report from a
failed automated test. Write it in this exact format:

## Bug Report: [short title]
**Severity:** [High/Medium/Low, your best guess]
**Steps to reproduce:** [inferred from the test name and error]
**Expected result:** [what the test expected]
**Actual result:** [what the error says actually happened]

Test name: {test_name}
Error message: {error_message}

Only output the bug report in the format above. This is a DRAFT for a human
to review — do not claim certainty you don't have."""

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
        f.write("\n\n---\n*DRAFT — pending human review*\n")

    print(f"Draft bug report saved: {filename}")