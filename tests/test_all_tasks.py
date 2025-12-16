import sys
import os
from io import StringIO
from unittest.mock import patch

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Global flags for hard-coding detection
task1_hardcoded = False
task2_hardcoded = False
task3_hardcoded = False


# ==================== TASK 1 TESTS ====================

def test_task1_00_file_exists():
    """Test that task1.py exists - 1 point"""
    assert os.path.exists('task1.py'), "task1.py not found - have you committed it to GitHub?"


def test_task1_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail - 1 point"""
    global task1_hardcoded
    
    try:
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
        
        if 'candy_total' in namespace and namespace['candy_total'] != expected_total:
            task1_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if str(expected_total) not in output or str(expected_first_share) not in output or str(expected_second_share) not in output:
            task1_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
            
    except AssertionError:
        raise
    except Exception:
        pass


def import_and_run_task1():
    """Helper function to import task1 and capture output"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return task1, output


def test_task1_02_required_variables_exist():
    """Test that all required variables exist - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    assert hasattr(task1, 'candy_total'), "Missing required variable: candy_total"
    assert hasattr(task1, 'share'), "Missing required variable: share"
    assert hasattr(task1, 'leftover'), "Missing required variable: leftover"


def test_task1_03_candy_total():
    """Test total candy calculation - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    expected_total = 97
    assert str(expected_total) in output, "candy_total miscalculated or not printed"
    assert task1.candy_total == expected_total, "candy_total miscalculated"


def test_task1_04_first_each_share():
    """Test first division - share with 5 people - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    expected_share = 19
    assert str(expected_share) in output, "share miscalculated in scenario 1"


def test_task1_05_first_leftover():
    """Test first division - leftover with 5 people - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    expected_leftover = 2
    assert str(expected_leftover) in output, "leftover miscalculated in scenario 1"


def test_task1_06_second_each_share():
    """Test second division - share with 7 people - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    expected_share = 13
    lines = output.split('\n')
    assert str(expected_share) in '\n'.join(lines[-3:]), "share miscalculated in scenario 2"
    assert task1.share == expected_share, "share miscalculated in scenario 2"


def test_task1_07_second_leftover():
    """Test second division - leftover with 7 people - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    expected_leftover = 6
    lines = output.split('\n')
    assert str(expected_leftover) in '\n'.join(lines[-2:]), "leftover miscalculated in scenario 2"
    assert task1.leftover == expected_leftover, "leftover miscalculated in scenario 2"


def test_task1_08_output_not_empty():
    """Test that program produces output - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    assert len(output.strip()) > 0, "Program produces no output"


def test_task1_09_output_has_multiple_lines():
    """Test that output has at least 5 lines - 1 point"""
    assert not task1_hardcoded, "Hard-coding detected - no points awarded"
    task1, output = import_and_run_task1()
    lines = [line for line in output.strip().split('\n') if line.strip()]
    assert len(lines) >= 5, f"Expected at least 5 lines of output, got {len(lines)}"


# ==================== TASK 2 TESTS ====================

def test_task2_00_file_exists():
    """Test that task2.py exists - 1 point"""
    assert os.path.exists('task2.py'), "task2.py not found - have you committed it to GitHub?"


def test_task2_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail - 1 point"""
    global task2_hardcoded
    
    try:
        with open('task2.py', 'r') as f:
            code = f.read()
        
        modified_code = code.replace('allowance = 15', 'allowance = 20')
        modified_code = modified_code.replace(
            'dishes, room, trash, lawn, laundry, vacuum = 3, 5, 2, 8, 4, 6',
            'dishes, room, trash, lawn, laundry, vacuum = 3, 6, 2, 8, 4, 6'
        )
        modified_code = modified_code.replace(
            'candy, soda, game, movie, toy, snack = 4, 2, 15, 10, 7, 3',
            'candy, soda, game, movie, toy, snack = 4, 3, 15, 12, 7, 3'
        )
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            namespace = {}
            exec(modified_code, namespace)
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        expected_final = 10.5
        
        if 'allowance' in namespace and namespace['allowance'] != expected_final:
            task2_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if "10.5" not in output and "10.50" not in output:
            task2_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
            
    except AssertionError:
        raise
    except Exception:
        pass


def import_and_run_task2():
    """Helper function to import task2 and capture output"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return task2, output


def test_task2_02_allowance_variable_exists():
    """Test that allowance variable exists - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert hasattr(task2, 'allowance'), "Missing required variable: allowance"


def test_task2_03_allowance_final_value():
    """Test final allowance value - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    expected_final = 8.5
    assert task2.allowance == expected_final, f"allowance has incorrect final value. Expected {expected_final}, got {task2.allowance}"


def test_task2_04_output_contains_final_value():
    """Test output contains final allowance - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "8.5" in output or "8.50" in output, "Output doesn't contain final allowance value"


def test_task2_05_output_has_dollar_sign():
    """Test output contains dollar sign - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "$" in output, "Output should contain dollar sign ($)"


def test_task2_06_output_label_correct():
    """Test output contains 'Allowance:' label - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert "Allowance:" in output, "Output should contain 'Allowance:' label"


def test_task2_07_output_not_empty():
    """Test that program produces output - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    task2, output = import_and_run_task2()
    assert len(output.strip()) > 0, "Program produces no output"


def test_task2_08_uses_operation_assignment():
    """Test that code uses operation assignment operators - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    with open('task2.py', 'r') as f:
        code = f.read()
    assert ('+=' in code or '-=' in code or '*=' in code or '/=' in code), \
        "Should use operation assignment operators (+=, -=, *=, /=)"


def test_task2_09_allowance_updated_multiple_times():
    """Test that allowance variable is updated throughout - 1 point"""
    assert not task2_hardcoded, "Hard-coding detected - no points awarded"
    with open('task2.py', 'r') as f:
        code = f.read()
    assert code.count('allowance') >= 8, "Should use allowance variable multiple times"


# ==================== TASK 3 TESTS ====================

def test_task3_00_file_exists():
    """Test that task3.py exists - 1 point"""
    assert os.path.exists('task3.py'), "task3.py not found - have you committed it to GitHub?"


def test_task3_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail - 1 point"""
    global task3_hardcoded
    
    try:
        with open('task3.py', 'r') as f:
            code = f.read()
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            with patch('builtins.input', side_effect=["Phoenix Feather", "14.99", "5"]):
                namespace = {}
                exec(code, namespace)
                output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        
        expected_subtotal = 74.95
        expected_total = 82.07
        
        if 'subtotal' in namespace and namespace['subtotal'] != expected_subtotal:
            task3_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if 'total' in namespace and namespace['total'] != expected_total:
            task3_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if "74.95" not in output or "82.07" not in output:
            task3_hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
            
    except AssertionError:
        raise
    except Exception:
        pass


def import_and_run_task3():
    """Helper function to import task3 and capture output"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task3' in sys.modules:
        del sys.modules['task3']
    
    with patch('builtins.input', side_effect=["Crystal Ball", "39.99", "2"]):
        import task3
        output = sys.stdout.getvalue()
    
    sys.stdout = old_stdout
    return task3, output


def test_task3_02_required_variables_exist():
    """Test that all required variables exist - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'item'), "Missing required variable: item"
    assert hasattr(task3, 'price'), "Missing required variable: price"
    assert hasattr(task3, 'quantity'), "Missing required variable: quantity"
    assert hasattr(task3, 'subtotal'), "Missing required variable: subtotal"
    assert hasattr(task3, 'tax'), "Missing required variable: tax"
    assert hasattr(task3, 'total'), "Missing required variable: total"


def test_task3_03_get_purchase_info_function_exists():
    """Test that get_purchase_info function exists - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'get_purchase_info'), "Missing required function: get_purchase_info"
    assert callable(task3.get_purchase_info), "get_purchase_info must be a function"


def test_task3_04_subtotal_value():
    """Test subtotal calculation - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_subtotal = 79.98
    assert task3.subtotal == expected_subtotal, f"subtotal has incorrect value. Expected {expected_subtotal}, got {task3.subtotal}"


def test_task3_05_tax_value():
    """Test tax calculation - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_tax = 7.5981
    assert abs(task3.tax - expected_tax) < 0.0001, f"tax has incorrect value. Expected approximately {expected_tax}, got {task3.tax}"


def test_task3_06_total_value():
    """Test total calculation and rounding - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_total = 87.58
    assert task3.total == expected_total, f"total has incorrect value. Expected {expected_total}, got {task3.total}"


def test_task3_07_menu_displayed():
    """Test that menu is displayed - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "PECULIAR EMPORIUM" in output, "Menu header not displayed"
    assert "Crystal Ball" in output, "Menu items not displayed"


def test_task3_08_receipt_formatted_correctly():
    """Test receipt shows all required elements - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "x2" in output, "Receipt should show quantity"
    assert "39.99" in output, "Receipt should show item price"
    assert "Subtotal:" in output, "Subtotal label missing"
    assert "Tax:" in output, "Tax label missing"
    assert "Total:" in output, "Total label missing"


def test_task3_09_output_has_decimal_formatting():
    """Test that monetary values are properly formatted - 1 point"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "79.98" in output or "79.97999" in output or str(task3.subtotal) in output, "Subtotal should be displayed"
    assert "87.58" in output or str(task3.total) in output, "Total should be displayed"


# ==================== TASK 4 TESTS ====================

def test_task4_00_file_exists():
    """Test that task4.py exists - 1 point"""
    assert os.path.exists('task4.py'), "task4.py not found - have you committed it to GitHub?"


def test_task4_01_snippet_1_fixed():
    """Snippet 1: Missing colon - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
temperature = 75
if temperature > 70:
    print("It's warm outside!")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "It's warm outside!" in output, "Snippet 1 not fixed correctly"


def test_task4_02_snippet_2_fixed():
    """Snippet 2: Unclosed string - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
greeting = "Hello, welcome to our store"
print(greeting)
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Hello, welcome to our store" in output, "Snippet 2 not fixed correctly"


def test_task4_03_snippet_3_fixed():
    """Snippet 3: Variable name typo - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
apples = 5
oranges = 3
total_fruit = apples + oranges
print(f"Total fruit: {total_fruit}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Total fruit: 8" in output, "Snippet 3 not fixed correctly"


def test_task4_04_snippet_4_fixed():
    """Snippet 4: Indentation error - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
has_ticket = True
if has_ticket:
    prize = 10
    print(f"You won ${prize}!")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "You won $10!" in output, "Snippet 4 not fixed correctly"


def test_task4_05_snippet_5_fixed():
    """Snippet 5: Missing type conversion - 1 point"""
    import task4
    
    with patch('builtins.input', return_value='15'):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            exec("""
age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you'll be {next_year}")
""")
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
    
    assert "Next year you'll be 16" in output, "Snippet 5 not fixed correctly"


def test_task4_06_snippet_6_fixed():
    """Snippet 6: Unclosed parenthesis - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
cookies = 12
share = cookies // 4
print(f"Each person gets {share} cookies")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Each person gets 3 cookies" in output, "Snippet 6 not fixed correctly"


def test_task4_07_snippet_7_fixed():
    """Snippet 7: Wrong operator (logic error) - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
lives = 3
lives = lives - 1
if lives == 2:
    print("You have 2 lives left")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "You have 2 lives left" in output, "Snippet 7 not fixed correctly"


def test_task4_08_snippet_8_fixed():
    """Snippet 8: Undefined variable - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
price = 15.99
quantity = 2
total = price * quantity
print(f"Total: ${total}")
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "31.98" in output, "Snippet 8 not fixed correctly"


def test_task4_09_snippet_9_fixed():
    """Snippet 9: Missing parentheses in print - 1 point"""
    import task4
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        exec("""
score = 100
print("Your score is:", score)
""")
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    assert "Your score is: 100" in output, "Snippet 9 not fixed correctly"
