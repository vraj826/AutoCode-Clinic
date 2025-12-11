import uuid
import argparse
import json
from agents.orchestrator import OrchestratorAgent


def load_file(path: str) -> str:
    """Utility: load text file."""
    with open(path, "r") as f:
        return f.read()


def run_single_job(code_path: str, test_path: str):
    code_content = load_file(code_path)
    test_content = load_file(test_path)

    filename = code_path.split("/")[-1]
    code_files = {filename: code_content}

    session_id = "session-" + str(uuid.uuid4())
    orchestrator = OrchestratorAgent()

    result = orchestrator.handle_job(session_id, code_files.copy(), test_content)

    print("\n===============================")
    print(" AUTO CODE CLINIC RESULT")
    print("===============================")
    print(json.dumps(result, indent=2))


def main():
    parser = argparse.ArgumentParser(description="AutoCode Clinic – CLI Runner")
    parser.add_argument("--code", required=True, help="Path to Python file with buggy code")
    parser.add_argument("--tests", required=True, help="Path to the test file")
    args = parser.parse_args()

    run_single_job(args.code, args.tests)


if __name__ == "__main__":
    main()
