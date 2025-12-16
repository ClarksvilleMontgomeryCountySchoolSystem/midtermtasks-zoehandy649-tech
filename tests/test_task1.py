import sys
import os
from io import StringIO


def test_00_file_exists():
    """Test that task1.py exists - 1 point"""
    assert os.path.exists('task1.py'), "task1.py not found - have you committed it to GitHub?"


def check_hardcoding_task1():
    """Check for hard-coding - must pass before other tests run"""
    with open('task1.py', 'r') as f:
        code = f.read()
    
    modified_code = code.replace('people = 4', 'people = 5')
    modified_code = modified_code.replace('bg1 = 37', 'bg1 = 40')
    modified_code = modified_code.replace('bg2 = 22', 'bg2 = 30')
    modified_code = modified_code.replace('bg3 = 8', 'bg3 = 15')
    modified_code = modified_code.replace('bg4 = 30', 'bg4 = 25')
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        namespace = {}
        exec(modified_code, namespace)
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    expected_total = 110
    expected_first_share = 18
    expected_second_share = 13
    
    if 'candy_total' in namespace:
        assert namespace['candy_total'] == expected_total, "Hard-coding detected - no points awarded"
    
    assert str(expected_total) in output, "Hard-coding detected - no points awarded"
    assert str(expected_first_share) in output, "Hard-coding detected - no points awarded"
    assert str(expected_second_share) in output, "Hard-coding detected - no points awarded"


def import_and_run_task1():
    """Helper function to import task1 and capture output"""
    check_hardcoding_task1()
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return task1, output


def test_01_required_variables_exist():
    """Test that all required variables exist - 1 point"""
    task1, output = import_and_run_task1()
    assert hasattr(task1, 'candy_total'), "Missing required variable: candy_total"
    assert hasattr(task1, 'share'), "Missing required variable: share"
    assert hasattr(task1, 'leftover'), "Missing required variable: leftover"


def test_02_candy_total():
    """Test total candy calculation - 1 point"""
    task1, output = import_and_run_task1()
    expected_total = 97
    assert str(expected_total) in output, "candy_total miscalculated or not printed"
    assert task1.candy_total == expected_total, "candy_total miscalculated"


def test_03_first_each_share():
    """Test first division - share with 5 people - 1 point"""
    task1, output = import_and_run_task1()
    expected_share = 19
    assert str(expected_share) in output, "share miscalculated in scenario 1"


def test_04_first_leftover():
    """Test first division - leftover with 5 people - 1 point"""
    task1, output = import_and_run_task1()
    expected_leftover = 2
    assert str(expected_leftover) in output, "leftover miscalculated in scenario 1"


def test_05_second_each_share():
    """Test second division - share with 7 people - 1 point"""
    task1, output = import_and_run_task1()
    expected_share = 13
    lines = output.split('\n')
    assert str(expected_share) in '\n'.join(lines[-3:]), "share miscalculated in scenario 2"
    assert task1.share == expected_share, "share miscalculated in scenario 2"


def test_06_second_leftover():
    """Test second division - leftover with 7 people - 1 point"""
    task1, output = import_and_run_task1()
    expected_leftover = 6
    lines = output.split('\n')
    assert str(expected_leftover) in '\n'.join(lines[-2:]), "leftover miscalculated in scenario 2"
    assert task1.leftover == expected_leftover, "leftover miscalculated in scenario 2"


def test_07_output_not_empty():
    """Test that program produces output - 1 point"""
    task1, output = import_and_run_task1()
    assert len(output.strip()) > 0, "Program produces no output"


def test_08_output_has_multiple_lines():
    """Test that output has at least 5 lines - 1 point"""
    task1, output = import_and_run_task1()
    lines = [line for line in output.strip().split('\n') if line.strip()]
    assert len(lines) >= 5, f"Expected at least 5 lines of output, got {len(lines)}"


def test_09_uses_arithmetic_operators():
    """Test that code uses addition and division operators - 1 point"""
    with open('task1.py', 'r') as f:
        code = f.read()
    assert '+' in code, "Should use addition operator"
    assert '//' in code or '/' in code, "Should use division operator"
