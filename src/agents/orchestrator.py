import uuid
from .base import BaseAgent
from .static_analysis_agent import StaticAnalysisAgent
from .patch_generation_agent import PatchGenerationAgent
from .validation_agent import ValidationAgent
from src.utils.session_state import state_manager

class OrchestratorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Orchestrator")
        self.analysis_agent = StaticAnalysisAgent("StaticAnalysis")
        self.patch_agent = PatchGenerationAgent("PatchGen")
        self.validator = ValidationAgent("Validator")

    def handle_job(self, session_id, code_files, tests, max_iters=3):
        state_manager.init_session(session_id)

        analysis = self.analysis_agent.analyze(code_files)
        state_manager.append(session_id, "analysis", analysis)

        for i in range(max_iters):
            self.log(f"Loop iteration {i+1}")

            ok, output = self.validator.validate(code_files, tests)
            state_manager.append(session_id, "validation", {"ok": ok, "output": output})

            if ok:
                self.log("Validation passed")
                return {"status": "fixed", "iterations": i, "output": output}

            patch_obj = self.patch_agent.propose_patch(code_files, output, analysis)
            state_manager.append(session_id, "patch_proposed", patch_obj)

            if patch_obj.get("patch_type") == "file_replacement" and isinstance(patch_obj.get("patch"), dict):
                for fname, new_content in patch_obj["patch"].items():
                    code_files[fname] = new_content
                state_manager.append(session_id, "patched_files", list(patch_obj["patch"].keys()))
            else:
                self.log("Unsupported patch type")

        self.log("Exhausted iterations without successful fix")
        return {"status": "unfixed", "iterations": max_iters, "last_output": output}
