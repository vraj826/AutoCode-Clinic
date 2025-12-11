import json
from .base import BaseAgent
from src.utils.model import call_model

class PatchGenerationAgent(BaseAgent):
    def propose_patch(self, code_files, test_output, static_analysis):
        self.log("Proposing patch (via model wrapper)")

        prompt = (
            "Generate patch for failing code.\n"
            f"Files: {list(code_files.keys())}\n"
            f"StaticAnalysis: {json.dumps(static_analysis)}\n"
            f"TestOutput: {test_output}\n"
            "Return a JSON with keys: patch_type, patch, explanation."
        )

        resp = call_model(prompt)

        try:
            parsed = json.loads(resp)
        except Exception:
            parsed = {
                "patch_type": "file_replacement",
                "patch": {list(code_files.keys())[0]: resp},
                "explanation": "Auto-generated (fallback)"
            }

        return parsed
