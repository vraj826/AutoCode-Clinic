import ast

def simple_static_analyzer(code: str):
    issues = []
    try:
        tree = ast.parse(code)
    except Exception as e:
        issues.append(f"SyntaxError: {e}")
        return issues

    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "eval":
            issues.append("Use of eval() detected - risky")

    return issues
