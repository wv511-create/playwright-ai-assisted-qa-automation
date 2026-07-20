import pytest
from bug_report_generator import generate_bug_report

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        test_name = item.name
        error_message = str(call.excinfo.value) if call.excinfo else "Unknown error"
        generate_bug_report(test_name, error_message)