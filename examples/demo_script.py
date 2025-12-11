"""
AutoCode Clinic - Demo Script
This script runs a simple example showing how the multi-agent debugging system
analyzes, validates, patches, and re-validates buggy code.
"""

from agents.orchestrator import OrchestratorAgent
import uuid


def main():
    # Buggy program to fix
    code_files = {
        "solution.py": """
def add(a, b):
    return a - b   # <-- intentional bug
"""
    }

    # Test that should pass
    tests = """
import solution

def test_add():
    assert solution.add(2, 3) == 5

if __name__ == '__main__':
    test_add()
"""

    session_id = "demo-" + str(uuid.uuid4())
    orchestrator = OrchestratorAgent()

    print("\n=== Running AutoCode Clinic Demo ===\n")
    result = orchestrator.handle_job(
        session_id=session_id,
        code_files=code_files.copy(),
        tests=tests,
        max_iters=3
    )

    print("\n=== FINAL RESULT ===")
    print(result)

    print("\nDemo complete! The agents attempted to fix the buggy add() function.")
    print("You can inspect session state or artifacts for more details.\n")


if __name__ == "__main__":
    main()
