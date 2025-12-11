from .base import BaseAgent
from src.utils.analyzer import simple_static_analyzer

class StaticAnalysisAgent(BaseAgent):
    def analyze(self, code_files):
        self.log("Running static analysis")
        return {fname: simple_static_analyzer(content) for fname, content in code_files.items()}
