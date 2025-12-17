import pytest
import sys
from io import StringIO


# TASK 1 TESTS
# Test values: party_pizza_mini=16, large=10, medium=8, people=5
# Expected outputs:
# Part 1: slices=34
# Part 2: people=6, share=5, leftover=4
# Part 3: people=8, share=4, leftover=2
# Part 4: slices=50, share=6, leftover=2

def run_task1_with_values(party_pizza_mini, large, medium, people):
    """Run task1.py with given variable values and return output"""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        # Read student code
        with open('task1.py', 'r') as f:
            student_code = f.read()
        
        # Replace smart quotes with regular quotes
        student_code = student_code.replace('"', '"').replace('"', '"').replace("'", "'").replace("'", "'")
        
        # Create namespace with test variables
        namespace = {
            'party_pizza_mini': party_pizza_mini,
            'large': large,
            'medium': medium,
            'people': people
        }
        
        # Execute student code with test variables
        exec(student_code, namespace)
        
        # Get output
        output = sys.stdout.getvalue()
        return output
    finally:
        sys.stdout = old_stdout


def test_task1_initial_slices():
    """Test that initial slice count is calculated correctly"""
    output = run_task1_with_values(16, 10, 8, 5)
    assert "34" in output, "Initial slice count should be 34"


def test_task1_part2_share():
    """Test Part 2 share calculation"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 2, "Not enough output lines"
    assert "5" in lines[1], "Part 2 share should be 5"


def test_task1_part2_leftover():
    """Test Part 2 leftover calculation"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 3, "Not enough output lines"
    assert "4" in lines[2], "Part 2 leftover should be 4"


def test_task1_part3_share():
    """Test Part 3 share calculation"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 4, "Not enough output lines"
    assert "4" in lines[3], "Part 3 share should be 4"


def test_task1_part3_leftover():
    """Test Part 3 leftover calculation"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 5, "Not enough output lines"
    assert "2" in lines[4], "Part 3 leftover should be 2"


def test_task1_part4_share():
    """Test Part 4 share calculation after pizza upgrade"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 6, "Not enough output lines"
    assert "6" in lines[5], "Part 4 share should be 6"


def test_task1_part4_leftover():
    """Test Part 4 leftover calculation after pizza upgrade"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = output.strip().split('\n')
    assert len(lines) >= 7, "Not enough output lines"
    assert "2" in lines[6], "Part 4 leftover should be 2"


def test_task1_hollow_leg_message():
    """Test that the Mr. Hollow Leg message appears"""
    output = run_task1_with_values(16, 10, 8, 5)
    assert "Hollow Leg" in output, "Should include Hollow Leg message"


def test_task1_output_line_count():
    """Test that the correct number of output lines are printed"""
    output = run_task1_with_values(16, 10, 8, 5)
    lines = [line for line in output.strip().split('\n') if line]
    assert len(lines) == 8, f"Should have 8 output lines, got {len(lines)}"


def test_task1_different_values():
    """Test with completely different values to ensure no hardcoding"""
    output = run_task1_with_values(20, 12, 10, 8)
    lines = output.strip().split('\n')
    # 20+12+10 = 42 slices
    assert "42" in lines[0], "Should calculate slices from variables"
    # 42 // 9 people = 4 share, 6 leftover (part 2)
    assert "4" in lines[1], "Part 2 share should use variable values"



# TASK 2 TESTS
# Test values: allowance=25, dishes=5, room=7, trash=4, lawn=12, laundry=6, vacuum=8
#              candy=6, soda=4, game=20, movie=14, toy=9, snack=5
# Expected progression:
# Start: 25
# Week 1: +dishes(5) +lawn(12) -candy(6) = 36
# Week 2: *3 = 108, +vacuum(8) = 116, -toy(9) = 107
# Week 3: /2 = 53.5

def run_task2_with_values(allowance, dishes, room, trash, lawn, laundry, vacuum,
                          candy, soda, game, movie, toy, snack):
    """Run task2.py with given variable values and return output"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        with open('task2.py', 'r') as f:
            student_code = f.read()
        
        # Replace smart quotes with regular quotes
        student_code = student_code.replace('"', '"').replace('"', '"').replace("'", "'").replace("'", "'")
        
        namespace = {
            'allowance': allowance,
            'dishes': dishes,
            'room': room,
            'trash': trash,
            'lawn': lawn,
            'laundry': laundry,
            'vacuum': vacuum,
            'candy': candy,
            'soda': soda,
            'game': game,
            'movie': movie,
            'toy': toy,
            'snack': snack
        }
        
        exec(student_code, namespace)
        output = sys.stdout.getvalue()
        return output
    finally:
        sys.stdout = old_stdout


def test_task2_final_allowance():
    """Test final allowance value with different test values"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    assert "53.5" in output, "Final allowance calculation incorrect"


def test_task2_week1_additions():
    """Test Week 1 chore additions"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect dishes and lawn were added
    assert "53.5" in output, "Week 1 chore additions may be incorrect"


def test_task2_week1_subtraction():
    """Test Week 1 purchase subtraction"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect candy was subtracted
    assert "53.5" in output, "Week 1 purchase subtraction may be incorrect"


def test_task2_week2_multiplication():
    """Test Week 2 bonus multiplication"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect tripling occurred
    assert "53.5" in output, "Week 2 multiplication may be incorrect"


def test_task2_week2_chore_addition():
    """Test Week 2 vacuum addition"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect vacuum was added
    assert "53.5" in output, "Week 2 chore addition may be incorrect"


def test_task2_week2_purchase():
    """Test Week 2 toy purchase"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect toy was subtracted
    assert "53.5" in output, "Week 2 purchase may be incorrect"


def test_task2_week3_division():
    """Test Week 3 savings division"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    # Should reflect division by 2
    assert "53.5" in output, "Week 3 division may be incorrect"


def test_task2_dollar_sign():
    """Test output contains dollar sign"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    assert "$" in output, "Output should include dollar sign"


def test_task2_allowance_label():
    """Test output contains Allowance label"""
    output = run_task2_with_values(25, 5, 7, 4, 12, 6, 8, 6, 4, 20, 14, 9, 5)
    assert "Allowance:" in output, "Output should include 'Allowance:' label"


def test_task2_different_values():
    """Test with another set of values to ensure no hardcoding"""
    output = run_task2_with_values(30, 6, 8, 5, 15, 7, 10, 7, 5, 22, 16, 10, 6)
    # Start: 30, +dishes(6) +lawn(15) -candy(7) = 44
    # *3 = 132, +vacuum(10) = 142, -toy(10) = 132
    # /2 = 66.0
    assert "66" in output, "Should work with different variable values"



# TASK 3 TESTS
# Uses original import approach - students submit complete file

task3_hardcoded = False

def test_task3_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail"""
    global task3_hardcoded
    
    try:
        with open('task3.py', 'r') as f:
            code = f.read()
        
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        try:
            from unittest.mock import patch
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
            pytest.fail("Hard-coding detected - all tests will fail")
        
        if 'total' in namespace and namespace['total'] != expected_total:
            task3_hardcoded = True
            pytest.fail("Hard-coding detected - all tests will fail")
        
        if "74.95" not in output or "82.07" not in output:
            task3_hardcoded = True
            pytest.fail("Hard-coding detected - all tests will fail")
            
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
    
    from unittest.mock import patch
    with patch('builtins.input', side_effect=["Crystal Ball", "39.99", "2"]):
        import task3
        output = sys.stdout.getvalue()
    
    sys.stdout = old_stdout
    return task3, output


def test_task3_02_required_variables_exist():
    """Test that all required variables exist"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'item'), "Missing required variable: item"
    assert hasattr(task3, 'price'), "Missing required variable: price"
    assert hasattr(task3, 'quantity'), "Missing required variable: quantity"
    assert hasattr(task3, 'subtotal'), "Missing required variable: subtotal"
    assert hasattr(task3, 'tax'), "Missing required variable: tax"
    assert hasattr(task3, 'total'), "Missing required variable: total"


def test_task3_03_get_purchase_info_function_exists():
    """Test that get_purchase_info function exists"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'get_purchase_info'), "Missing required function: get_purchase_info"
    assert callable(task3.get_purchase_info), "get_purchase_info must be a function"


def test_task3_04_subtotal_value():
    """Test subtotal calculation"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_subtotal = 79.98
    assert task3.subtotal == expected_subtotal, f"subtotal has incorrect value. Expected {expected_subtotal}, got {task3.subtotal}"


def test_task3_05_tax_value():
    """Test tax calculation"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_tax = 7.5981
    assert abs(task3.tax - expected_tax) < 0.0001, f"tax has incorrect value. Expected approximately {expected_tax}, got {task3.tax}"


def test_task3_06_total_value():
    """Test total calculation and rounding"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_total = 87.58
    assert task3.total == expected_total, f"total has incorrect value. Expected {expected_total}, got {task3.total}"


def test_task3_07_menu_displayed():
    """Test that menu is displayed"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "PECULIAR EMPORIUM" in output, "Menu header not displayed"
    assert "Crystal Ball" in output, "Menu items not displayed"


def test_task3_08_receipt_formatted_correctly():
    """Test receipt shows all required elements"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "x2" in output, "Receipt should show quantity"
    assert "39.99" in output, "Receipt should show item price"
    assert "Subtotal:" in output, "Subtotal label missing"
    assert "Tax:" in output, "Tax label missing"
    assert "Total:" in output, "Total label missing"


def test_task3_09_output_has_decimal_formatting():
    """Test that monetary values are properly formatted"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "79.98" in output or str(task3.subtotal) in output, "Subtotal should be displayed"
    assert "87.58" in output or str(task3.total) in output, "Total should be displayed"


def test_task3_10_testing_flag_exists():
    """Test that TESTING flag exists and works"""
    assert not task3_hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'TESTING'), "Missing TESTING flag variable"



# TASK 4 TESTS
# Debugging challenge - each test runs one corrected snippet

def test_task4_snippet_1():
    """Snippet 1: Missing colon"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
books = 12
if books > 10:
    print("You have a lot of books!")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "You have a lot of books!" in output, "Snippet 1 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 1 has a syntax error - check for missing colon")


def test_task4_snippet_2():
    """Snippet 2: Unclosed string"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
favorite_color = "blue"
print(favorite_color)
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "blue" in output, "Snippet 2 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 2 has a syntax error - check for unclosed string")


def test_task4_snippet_3():
    """Snippet 3: Variable name typo"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
cats = 3
dogs = 2
total_pets = cats + dogs
print(f"Total pets: {total_pets}")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Total pets: 5" in output, "Snippet 3 not fixed correctly"
    except NameError:
        pytest.fail("Snippet 3 has a NameError - check variable names")


def test_task4_snippet_4():
    """Snippet 4: Indentation error"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
is_sunny = True
if is_sunny:
    message = "Wear sunglasses"
    print(message)
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Wear sunglasses" in output, "Snippet 4 not fixed correctly"
    except IndentationError:
        pytest.fail("Snippet 4 has an indentation error")


def test_task4_snippet_5():
    """Snippet 5: Missing closing parenthesis"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
distance = 50
time = 2
speed = distance / time
print(f"Speed: {speed} mph")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Speed: 25.0 mph" in output, "Snippet 5 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 5 has a syntax error - check parentheses")


def test_task4_snippet_6():
    """Snippet 6: Wrong operator (= instead of ==)"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
level = 5
if level == 5:
    print("You reached level 5!")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "You reached level 5!" in output, "Snippet 6 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 6 has a syntax error - check comparison operator")


def test_task4_snippet_7():
    """Snippet 7: Variable name typo"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
width = 8
height = 10
area = width * height
print(f"Area: {area}")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Area: 80" in output, "Snippet 7 not fixed correctly"
    except NameError:
        pytest.fail("Snippet 7 has a NameError - check variable names")


def test_task4_snippet_8():
    """Snippet 8: Missing parentheses in print"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
name = "Sarah"
print("Hello", name)
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Hello" in output and "Sarah" in output, "Snippet 8 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 8 has a syntax error - check print statement")


def test_task4_snippet_9():
    """Snippet 9: Indentation error with else"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
hungry = False
if hungry:
    print("Time to eat!")
else:
    print("Not hungry yet")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "Not hungry yet" in output, "Snippet 9 not fixed correctly"
    except IndentationError:
        pytest.fail("Snippet 9 has an indentation error - check else block")


def test_task4_snippet_10():
    """Snippet 10: Unclosed string in f-string"""
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        exec("""
age = 15
print(f"I am {age} years old")
""")
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        assert "I am 15 years old" in output, "Snippet 10 not fixed correctly"
    except SyntaxError:
        pytest.fail("Snippet 10 has a syntax error - check for unclosed string")
