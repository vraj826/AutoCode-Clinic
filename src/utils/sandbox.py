import tempfile
import shutil
import subprocess
import os

SANDBOX_ROOT = "/tmp/autocode_sandbox"
os.makedirs(SANDBOX_ROOT, exist_ok=True)

def run_python_tests(code_files, test_code, timeout_sec=10):
    tmp = tempfile.mkdtemp(dir=SANDBOX_ROOT)
    try:
        for fname, content in code_files.items():
            with open(os.path.join(tmp, fname), "w") as f:
                f.write(content)

        test_path = os.path.join(tmp, "test_runner.py")
        with open(test_path, "w") as f:
            f.write(test_code)

        proc = subprocess.run(
            ["python", test_path],
            cwd=tmp,
            capture_output=True,
            text=True,
            timeout=timeout_sec
        )

        ok = proc.returncode == 0
        out = proc.stdout + "\n" + proc.stderr
        return ok, out

    finally:
        shutil.rmtree(tmp)
