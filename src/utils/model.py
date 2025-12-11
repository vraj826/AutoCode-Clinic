import json
import os

MODEL_BACKEND = os.environ.get("MODEL_BACKEND", "mock")
MODEL_ACCESS_TOKEN = os.environ.get("MODEL_ACCESS_TOKEN", "")
GENERIC_MODEL_NAME = os.environ.get("GENERIC_MODEL_NAME", "tier3-transformer-large")

def mock_model(prompt: str, max_tokens: int = 512) -> str:
    pl = prompt.lower()
    if "diagnose root cause" in pl or "diagnos" in pl:
        return json.dumps({
            "root_causes": ["incorrect operator", "variable naming issue"],
            "confidence": 0.75,
            "suggested_tests": ["add edge-case tests for negative inputs"]
        })

    if "generate patch" in pl or "patch" in pl:
        return json.dumps({
            "patch_type": "file_replacement",
            "patch": {
                "solution.py": "def add(a, b):\n    return a + b\n"
            },
            "explanation": "Fixed arithmetic operator from - to + in add function."
        })

    return "MOCK_RESPONSE: " + prompt[:200]


def call_model(prompt: str, max_tokens: int = 512, temperature: float = 0.0) -> str:
    if MODEL_BACKEND == "mock":
        return mock_model(prompt, max_tokens=max_tokens)
    else:
        raise RuntimeError("Remote model backend selected but no remote client implemented in this demo.")
