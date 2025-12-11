# 🏥 AutoCode Clinic – Multi-Agent Debugger & Repair Studio

A Kaggle Agents Intensive – Capstone Project.

## 📌 Overview

AutoCode Clinic is a multi-agent system designed to automate debugging, error detection, and code repair using orchestrated intelligent agents. It was built as part of the Agents Intensive Capstone Project on Kaggle, where the goal is to leverage agentic AI and multi-agent orchestration to solve real-world tasks.

The system automatically:

1. Analyzes buggy code
2. Runs tests in an isolated sandbox
3. Generates model-driven patches
4. Applies patches and re-validates
5. Improves the program iteratively

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

## System Architecture
```
+-------------------+
|   Orchestrator    |
|  (control center) |
+---------+---------+
          |
          v
+-----------------------+
| StaticAnalysisAgent   |
| - AST scan            |
| - Syntax issues       |
| - Unsafe patterns     |
+----------+------------+
           |
           v
+-----------------------+
| ValidationAgent       |
| - Sandbox execution   |
| - Runs tests          |
| - Captures errors     |
+----------+------------+
           |
   Tests pass? ──────────────── YES → FIXED
           |
           NO
           v
+-----------------------------+
| PatchGenerationAgent        |
| - Reads validation output   |
| - Uses model to generate    |
|   file-replacement patches  |
+----------+------------------+
           |
           v
     (Apply patch)
           |
           └──────────────► Loop back to Orchestrator

```

## Agent Responsibilities
```
+---------------------------+
|     StaticAnalysisAgent   |
+---------------------------+
| • Performs AST parsing    |
| • Detects syntax errors   |
| • Flags unsafe patterns   |
+-------------+-------------+
              |
              v
+---------------------------+
|     ValidationAgent       |
+---------------------------+
| • Runs tests in sandbox   |
| • Captures stdout/stderr  |
| • Determines pass/fail    |
+-------------+-------------+
              |
              v
+---------------------------+
|   PatchGenerationAgent    |
+---------------------------+
| • Reads validation logs   |
| • Uses model wrapper      |
| • Generates JSON patches  |
+-------------+-------------+
              |
              v
+---------------------------+
|     OrchestratorAgent     |
+---------------------------+
| • Controls whole workflow |
| • Applies patches         |
| • Manages iterations      |
+---------------------------+

```

## Multi-Agent Debugging Workflow
```
 +----------------------+
 |   Start Debugging    |
 +----------+-----------+
            |
            v
 +---------------------------+
 | StaticAnalysisAgent       |
 | • Scan code               |
 | • Detect structural issues|
 +------------+--------------+
              |
              v
 +---------------------------+
 | ValidationAgent           |
 | • Execute tests           |
 | • Capture errors          |
 +------------+--------------+
              |
          Tests pass? 
          |        |
          v        v
         YES      NO
          |        |
          v        |
        FIXED      |
                   v
      +---------------------------+
      | PatchGenerationAgent      |
      | • Model-based patching    |
      | • Produces JSON patch     |
      +------------+--------------+
                  |
                  v
      +---------------------------+
      | Apply Patch to Code       |
      +------------+--------------+
                  |
                  v
      +---------------------------+
      | Orchestrator (Loop Back)  |
      +------------+--------------+
                  |
                  v
     (Continue until fixed or max_iters)
```

## Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/vraj826/AutoCode-Clinic.git
cd AutoCode-Clinic
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

## Running the Demo (examples/demo_script.py)
```
python examples/demo_script.py
```
This demonstrates:

1. static analysis
2. failing validation
3. patch generation
4. re-validation
5. successful fix

## Running the Main CLI Runner (src/main.py)
```
python src/main.py --code examples/buggy.py --tests examples/test_buggy.py
```

## Using the Notebooks

Open them with Jupyter:
```
jupyter notebook
```
Then run:

**exploration.ipynb** → Architecture understanding

**demo_run.ipynb** → End-to-end demo

## Running Unit Tests

From the root folder:
```
pytest -q
```
Runs:
1. Agent tests
2. Workflow tests

## Dataset & Artifacts Output

The orchestrator automatically saves:

fixed programs

session logs

patch proposals

summary files

When run in batch mode (Kaggle environment).


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
