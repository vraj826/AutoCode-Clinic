# 🏥 AutoCode Clinic – Multi-Agent Debugger & Repair Studio

A Kaggle Agents Intensive – Capstone Project.

## 📌 Overview

AutoCode Clinic is a multi-agent system designed to automate debugging, error detection, and code repair using orchestrated intelligent agents. It was built as part of the Agents Intensive Capstone Project on Kaggle, where the goal is to leverage agentic AI and multi-agent orchestration to solve real-world tasks.

This project demonstrates:

🧠 Autonomous multi-agent reasoning

🔁 Iterative feedback-driven debugging

🧩 Modular, extendable agent architecture

🛠️ Automated code repair mechanisms

🧪 Safe execution + validation loops

## 🌐 Kaggle Links

### Capstone Writeup:
https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/autocode-clinic-multi-agent-d-rs

### Code Notebook:
https://www.kaggle.com/code/vrajkumarshah/autocode-clinic

## 📁 Project Structure
```
AutoCode-Clinic/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── notebooks/
│   ├── exploration.ipynb
│   └── demo_run.ipynb
├── src/
│   ├── agents/
│   │   ├── base.py
│   │   ├── orchestrator.py
│   │   ├── patch_generation_agent.py
│   │   ├── static_analysis_agent.py
│   │   ├── validation_agent.py
│   ├── utils.py
│   │   ├── analyzer.py
│   │   ├── model.py
│   │   ├── sandbox.py
│   │   ├── session_state.py
├── tests/
│   ├── test_agents.py
│   └── test_workflow.py
└── examples/
    └── demo_script.py
```

## ⚙️ Features
### 🤖 Multi-Agent Workflow

AutoCode Clinic uses four functional components:
```
| Component        | Description                                             |
|------------------|---------------------------------------------------------|
| Analyzer Agent   | Reads and evaluates input code, flags potential issues  |
| Debugger Agent   | Executes code, collects traces, identifies errors       |
| Fixer Agent      | Suggests revised or corrected code sections             |
| Orchestrator     | Manages communication, iterations, and evaluation       |
```

### 🔁 Iterative Repair Loop

The system automatically cycles through:
1. Detect
2. Reproduce
3. Repair
4. Validate
until stability is reached.

### 🧩 Modular & Extensible

Add new agents, tools, linters, test modules, or execution backends with minimal changes.

## 🚀 Getting Started
### 1️⃣ Clone the Repository
```
git clone https://github.com/<your-username>/AutoCode-Clinic.git
cd AutoCode-Clinic
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run a Demo
```
python src/runner.py examples/demo_script.py
```

## 🧪 Running Tests
```
pytest tests/
```
This verifies agent communication, code repair logic, and internal workflow integrity.

## 📘 Notebooks
```
| Notebook            | Purpose                                       |
|---------------------|-----------------------------------------------|
| exploration.ipynb   | Understanding the agent architecture          |
| demo_run.ipynb      | Demonstration of the repair workflow outputs  |
```

## 🔍 How It Works

The process is agent-driven:

1. **Analyzer Agent** reads the provided code.

2. **Debugger Agent** runs the code or tests, capturing stack traces.

3. **Fixer Agent** proposes modifications based on analyzer + debugger input.

4. **Orchestrator** evaluates improvements, re-runs agents, and finalizes output.

This creates a **self-improving debugging loop**, similar to industry-grade AI agent systems.

## 📊 Results Summary 

### Result for Demo Case 1
```
RESULT: {'status': 'fixed', 'iterations': 1, 'output': '\n'}

SESSION HISTORY (truncated):
 {
  "history": [
    {
      "analysis": {
        "solution.py": []
      }
    },
    {
      "validation": {
        "ok": false,
        "output": "\nTraceback (most recent call last):\n  File \"/tmp/autocode_sandbox/tmpy0idf1wc/test_runner.py\", line 8, in <module>\n    test_add()\n  File \"/tmp/autocode_sandbox/tmpy0idf1wc/test_runner.py\", line 5, in test_add\n    assert solution.add(2,3) == 5\n           ^^^^^^^^^^^^^^^^^^^^^^\nAssertionError\n"
      }
    },
    {
      "patch_proposed": {
        "patch_type": "file_replacement",
        "patch": {
          "solution.py": "def add(a, b):\n    return a + b\n"
        },
        "explanation": "Fixed arithmetic operator from - to + in add function."
      }
    },
    {
      "patched_files": [
        "solution.py"
      ]
    },
    {
      "validation": {
        "ok": true,
        "output": "\n"
      }
    }
  ],
  "analysis": [],
  "patches": []
}
```

### Result for Demo Case 2
```

| ID                          | Status | Iterations | Artifact                                                               |
|-----------------------------|--------|------------|------------------------------------------------------------------------|
| add_swapped_args            | fixed  | 0          | /kaggle/working/artifacts/session_sess-ab9e4b7...                      |
| add_with_pass               | fixed  | 0          | /kaggle/working/artifacts/session_sess-05fde62...                      |
| wrong_variable_name         | fixed  | 0          | /kaggle/working/artifacts/session_sess-d5d41e4...                      |
| add_returns_none            | fixed  | 0          | /kaggle/working/artifacts/session_sess-50b5974...                      |
| bug_wrong_logic             | fixed  | 0          | /kaggle/working/artifacts/session_sess-e08d2b0...                      |
| add_constant_error          | fixed  | 0          | /kaggle/working/artifacts/session_sess-0cacf87...                      |
| flip_operands               | fixed  | 0          | /kaggle/working/artifacts/session_sess-f4ec444...                      |
| add_missing_argument        | fixed  | 0          | /kaggle/working/artifacts/session_sess-ba2bf2e...                      |
| add_print_instead_of_return | fixed  | 0          | /kaggle/working/artifacts/session_sess-62fc70d...                      |
| wrong_return                | fixed  | 0          | /kaggle/working/artifacts/session_sess-b4d3ba0...                      |

Fix rate: 1.00
Fixed programs saved to: /kaggle/working/fixed_programs
Session logs saved to: /kaggle/working/artifacts

```

## 🛠️ Tech Stack

Python 3.9+

Multi-Agent Framework

Code Execution Environment

PyTest

Jupyter Notebooks

## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for details.

## 👤 Author

Vrajkumar Shah

Kaggle: https://www.kaggle.com/vrajkumarshah

GitHub: https://github.com/vrajshah826
