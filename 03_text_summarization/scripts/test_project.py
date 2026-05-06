#!/usr/bin/env python3
"""
Test script for the expanded text summarization project.
Verifies that both notebooks can be executed and produce valid outputs.
"""

import os
import sys
import subprocess
import tempfile

def test_notebook(notebook_path):
    """Test a Jupyter notebook using nbconvert."""
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return False
    
    print(f"✅ Notebook found: {notebook_path}")
    
    # Create a temporary directory for outputs
    with tempfile.TemporaryDirectory() as tmpdir:
        # Use nbconvert to execute the notebook
        cmd = [
            "jupyter", "nbconvert",
            "--execute",
            "--to", "notebook",
            "--output", os.path.join(tmpdir, "executed.ipynb"),
            "--ExecutePreprocessor.timeout", "300",
            notebook_path
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Notebook execution failed: {result.stderr}")
                return False
            else:
                print(f"✅ Notebook executed successfully: {notebook_path}")
                return True
        except Exception as e:
            print(f"❌ Error executing notebook: {e}")
            return False

def main():
    """Main test function."""
    base_dir = "/home/lawrancekoh/projects/data-science/03_text_summarization"
    notebooks = [
        "notebooks/03-2_text_summarization_expanded.ipynb",
        "notebooks/03-1_text_summarization.ipynb"
    ]
    
    print("=" * 60)
    print("Testing Expanded Text Summarization Project")
    print("=" * 60)
    
    all_passed = True
    for notebook in notebooks:
        full_path = os.path.join(base_dir, notebook)
        if not test_notebook(full_path):
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("✅ All tests passed!")
        return 0
    else:
        print("❌ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())