import pytest
from agents.orchestrator import OrchestratorAgent
import uuid


def test_orchestrator_fix_flow():
    orchestrator = OrchestratorAgent()

    code_files = {"solution.py": "def add(a,b): return a-b"}
    tests = """
import solution
def test_add():
    assert solution.add(2, 3) == 5
"""

    session_id = "test-" + str(uuid.uuid4())

    result = orchestrator.handle_job(
        session_id=session_id,
        code_files=code_files.copy(),
        tests=tests,
        max_iters=2
    )

    assert isinstance(result, dict)
    assert "status" in result
    assert result["status"] in ["fixed", "unfixed"]
    assert "iterations" in result


def test_orchestrator_no_crash_on_empty_tests():
    orchestrator = OrchestratorAgent()

    code_files = {"solution.py": "def add(a,b): return a-b"}
    tests = ""  # no tests

    session_id = "test-" + str(uuid.uuid4())
    result = orchestrator.handle_job(
        session_id=session_id,
        code_files=code_files.copy(),
        tests=tests,
        max_iters=2
    )

    assert isinstance(result, dict)
    assert "status" in result
