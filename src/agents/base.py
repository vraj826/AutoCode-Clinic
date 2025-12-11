import logging

logger = logging.getLogger("autocode_clinic")

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def log(self, msg: str):
        logger.info(f"[{self.name}] {msg}")
