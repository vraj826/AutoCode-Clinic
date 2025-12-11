from .base import BaseAgent
from src.utils.sandbox import run_python_tests

class ValidationAgent(BaseAgent):
    def validate(self, code_files, tests):
        self.log("Running validation tests in sandbox")
        return run_python_tests(code_files, tests)
