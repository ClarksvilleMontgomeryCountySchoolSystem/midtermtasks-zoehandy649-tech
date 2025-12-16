import sys
import os
from io import StringIO

# Global flag for hard-coding detection
hardcoded = False


def test_00_file_exists():
    """Test that task2.py exists - 1 point"""
    assert os.path.exists('task2.py'), "task2.py not found - have you committed it to GitHub?"


def test_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail - 1 point"""
    global hardcoded
    
    try:
        with open('task2.py', 'r') as f:
            code = f.read()
        
        modified_code = code.replace('allowance = 15', 'allowance = 20')
        modified_code = modified_code.replace('room = 5', 'room = 6')
        modified_code = modified_code.replace('soda = 2', 'soda = 3')
        modified_code = modified_code.replace('movie = 10', 'movie = 12')
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            namespace = {}
            exec(modified_code, namespace)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        # Expected: 20 + 2 + 6 - 3 = 25, * 2 = 50, + 4 = 54, - 12 = 42, / 4 = 10.5
        expected_final = 10.5
        
        # Check if hard-coded
        if 'allowance' in namespace and namespace['allowance'] != expected_final:
            hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if "10.5" not in output and "10.50" not in output:
            hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
            
    except AssertionError:
        raise
    except Exception:
        # If we can't run the hard-coding check due to syntax errors, let other tests run
        pass


def import_and_run_task2():
    """Helper function to import task2 and capture output"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return task2, output


def test_02_allowance_variable_exists():
    """Test that allowance variable exists - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert hasattr(task2, 'allowance'), "Missing required variable: allowance"


def test_03_allowance_final_value():
    """Test final allowance value - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    expected_final = 8.5
    assert task2.allowance == expected_final, f"allowance has incorrect final value. Expected {expected_final}, got {task2.allowance}"


def test_04_output_contains_final_value():
    """Test output contains final allowance - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "8.5" in output or "8.50" in output, "Output doesn't contain final allowance value"


def test_05_output_has_dollar_sign():
    """Test output contains dollar sign - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "$" in output, "Output should contain dollar sign ($)"


def test_06_output_label_correct():
    """Test output contains 'Allowance:' label - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "Allowance:" in output, "Output should contain 'Allowance:' label"


def test_07_output_not_empty():
    """Test that program produces output - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert len(output.strip()) > 0, "Program produces no output"


def test_08_uses_operation_assignment():
    """Test that code uses operation assignment operators - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    with open('task2.py', 'r') as f:
        code = f.read()
    # Check for += or -= or *= or /=
    assert ('+=' in code or '-=' in code or '*=' in code or '/=' in code), \
        "Should use operation assignment operators (+=, -=, *=, /=)"


def test_09_allowance_updated_multiple_times():
    """Test that allowance variable is updated throughout - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    with open('task2.py', 'r') as f:
        code = f.read()
    assert code.count('allowance') >= 8, "Should use allowance variable multiple times"
