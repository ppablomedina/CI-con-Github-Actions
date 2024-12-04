import os

# Create project structure
project_name = "my_project"
os.makedirs(f"{project_name}/", exist_ok=True)
os.makedirs("tests/", exist_ok=True)

# Create a simple module
with open(f"{project_name}/example.py", "w") as f:
    f.write("""\
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
""")

# Create a test file
with open("tests/test_example.py", "w") as f:
    f.write("""\
import pytest
from my_project.example import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
""")

# Create requirements.txt
with open("requirements.txt", "w") as f:
    f.write("""\
pytest
pytest-cov
""")

# Create pytest configuration file
with open("pytest.ini", "w") as f:
    f.write("""\
[pytest]
addopts = --cov=my_project --cov-report=xml
""")

# Create a README file
with open("README.md", "w") as f:
    f.write(f"# {project_name}\n\nA simple Python project for CI demonstration.")

# Display created files to the user
# import ace_tools as tools; tools.display_files_to_user("/mnt/data")
