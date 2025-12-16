import sys
from io import StringIO


def check_hardcoding_task2():
    """Check for hard-coding - must pass before other tests run"""
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
    
    if 'allowance' in namespace:
        assert namespace['allowance'] == expected_final, "Hard-coding detected - no points awarded"
    
    assert "10.5" in output or "10.50" in output, "Hard-coding detected - no points awarded"


def import_and_run_task2():
    """Helper function to import task2 and capture output"""
    check_hardcoding_task2()
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return task2, output


def test_01_allowance_variable_exists():
    """Test that allowance variable exists - 1 point"""
    task2, output = import_and_run_task2()
    assert hasattr(task2, 'allowance'), "Missing required variable: allowance"


def test_02_allowance_final_value():
    """Test final allowance value - 1 point"""
    task2, output = import_and_run_task2()
    expected_final = 8.5
    assert task2.allowance == expected_final, f"allowance has incorrect final value. Expected {expected_final}, got {task2.allowance}"


def test_03_output_contains_final_value():
    """Test output contains final allowance - 1 point"""
    task2, output = import_and_run_task2()
    assert "8.5" in output or "8.50" in output, "Output doesn't contain final allowance value"


def test_04_output_has_dollar_sign():
    """Test output contains dollar sign - 1 point"""
    task2, output = import_and_run_task2()
    assert "$" in output, "Output should contain dollar sign ($)"


def test_05_output_label_correct():
    """Test output contains 'Allowance:' label - 1 point"""
    task2, output = import_and_run_task2()
    assert "Allowance:" in output, "Output should contain 'Allowance:' label"


def test_06_output_not_empty():
    """Test that program produces output - 1 point"""
    task2, output = import_and_run_task2()
    assert len(output.strip()) > 0, "Program produces no output"


def test_07_uses_operation_assignment():
    """Test that code uses operation assignment operators - 1 point"""
    with open('task2.py', 'r') as f:
        code = f.read()
    # Check for += or -= or *= or /=
    assert ('+=' in code or '-=' in code or '*=' in code or '/=' in code), \
        "Should use operation assignment operators (+=, -=, *=, /=)"


def test_08_allowance_updated_multiple_times():
    """Test that allowance variable is updated throughout - 1 point"""
    with open('task2.py', 'r') as f:
        code = f.read()
    assert code.count('allowance') >= 8, "Should use allowance variable multiple times"


def test_09_uses_multiple_operation_types():
    """Test that code uses different types of operations - 1 point"""
    with open('task2.py', 'r') as f:
        code = f.read()
    operation_count = sum([
        '+=' in code,
        '-=' in code,
        '*=' in code or '*' in code,
        '/=' in code or '/' in code
    ])
    assert operation_count >= 3, "Should use at least 3 different types of operations"


def test_10_final_value_is_float():
    """Test that final allowance is a float (from division) - 1 point"""
    task2, output = import_and_run_task2()
    assert isinstance(task2.allowance, float), "Final allowance should be a float value"
