import pytest
from agents.static_analysis_agent import StaticAnalysisAgent
from agents.validation_agent import ValidationAgent
from agents.patch_generation_agent import PatchGenerationAgent
from agents.orchestrator import OrchestratorAgent


def test_static_analysis_agent():
    agent = StaticAnalysisAgent("StaticTest")
    code_files = {"file.py": "def add(a,b): return a+b"}
    result = agent.analyze(code_files)

    assert isinstance(result, dict)
    assert "file.py" in result
    assert isinstance(result["file.py"], list)


def test_validation_agent_pass():
    agent = ValidationAgent("ValidatorTest")
    code_files = {"solution.py": "def add(a,b): return a+b"}
    tests = """
import solution
def test_add():
    assert solution.add(2,3) == 5
"""
    ok, output = agent.validate(code_files, tests)

    assert ok is True
    assert isinstance(output, str)


def test_validation_agent_fail():
    agent = ValidationAgent("ValidatorTest")
    code_files = {"solution.py": "def add(a,b): return a-b"}
    tests = """
import solution
def test_add():
    assert solution.add(2,3) == 5
"""
    ok, output = agent.validate(code_files, tests)

    assert ok is False
    assert isinstance(output, str)


def test_patch_generation_agent():
    agent = PatchGenerationAgent("PatchTest")
    code_files = {"solution.py": "def add(a,b): return a-b"}
    static_analysis = {}
    test_output = "AssertionError"

    patch = agent.propose_patch(code_files, test_output, static_analysis)

    assert isinstance(patch, dict)
    assert "patch_type" in patch
    assert "patch" in patch
    assert "explanation" in patch
