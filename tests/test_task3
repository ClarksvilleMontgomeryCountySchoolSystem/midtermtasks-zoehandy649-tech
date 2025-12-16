import sys
from io import StringIO
from unittest.mock import patch


def check_hardcoding_task3():
    """Check for hard-coding - must pass before other tests run"""
    with open('task3.py', 'r') as f:
        code = f.read()
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        # Mock different input values
        with patch('builtins.input', side_effect=["Phoenix Feather", "14.99", "5"]):
            namespace = {}
            exec(code, namespace)
            output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Expected: 14.99 * 5 = 74.95, tax = 74.95 * 0.095 = 7.12025, total = 82.07
    expected_subtotal = 74.95
    expected_total = 82.07
    
    if 'subtotal' in namespace:
        assert namespace['subtotal'] == expected_subtotal, "Hard-coding detected - no points awarded"
    
    if 'total' in namespace:
        assert namespace['total'] == expected_total, "Hard-coding detected - no points awarded"
    
    assert "74.95" in output, "Hard-coding detected - no points awarded"
    assert "82.07" in output, "Hard-coding detected - no points awarded"


def import_and_run_task3():
    """Helper function to import task3 and capture output"""
    check_hardcoding_task3()
    
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    if 'task3' in sys.modules:
        del sys.modules['task3']
    
    # Mock input to provide test values
    with patch('builtins.input', side_effect=["Crystal Ball", "39.99", "2"]):
        import task3
        output = sys.stdout.getvalue()
    
    sys.stdout = old_stdout
    return task3, output


def test_01_required_variables_exist():
    """Test that all required variables exist - 1 point"""
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'item'), "Missing required variable: item"
    assert hasattr(task3, 'price'), "Missing required variable: price"
    assert hasattr(task3, 'quantity'), "Missing required variable: quantity"
    assert hasattr(task3, 'subtotal'), "Missing required variable: subtotal"
    assert hasattr(task3, 'tax'), "Missing required variable: tax"
    assert hasattr(task3, 'total'), "Missing required variable: total"


def test_02_get_purchase_info_function_exists():
    """Test that get_purchase_info function exists - 1 point"""
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'get_purchase_info'), "Missing required function: get_purchase_info"
    assert callable(task3.get_purchase_info), "get_purchase_info must be a function"


def test_03_subtotal_value():
    """Test subtotal calculation - 1 point"""
    task3, output = import_and_run_task3()
    expected_subtotal = 79.98
    assert task3.subtotal == expected_subtotal, f"subtotal has incorrect value. Expected {expected_subtotal}, got {task3.subtotal}"


def test_04_tax_value():
    """Test tax calculation - 1 point"""
    task3, output = import_and_run_task3()
    expected_tax = 7.5981
    assert abs(task3.tax - expected_tax) < 0.0001, f"tax has incorrect value. Expected approximately {expected_tax}, got {task3.tax}"


def test_05_total_value():
    """Test total calculation and rounding - 1 point"""
    task3, output = import_and_run_task3()
    expected_total = 87.58
    assert task3.total == expected_total, f"total has incorrect value. Expected {expected_total}, got {task3.total}"


def test_06_menu_displayed():
    """Test that menu is displayed - 1 point"""
    task3, output = import_and_run_task3()
    assert "PECULIAR EMPORIUM" in output, "Menu header not displayed"
    assert "Crystal Ball" in output, "Menu items not displayed"


def test_07_receipt_formatted_correctly():
    """Test receipt shows all required elements - 1 point"""
    task3, output = import_and_run_task3()
    assert "x2" in output, "Receipt should show quantity"
    assert "39.99" in output, "Receipt should show item price"
    assert "Subtotal:" in output, "Subtotal label missing"
    assert "Tax:" in output, "Tax label missing"
    assert "Total:" in output, "Total label missing"


def test_08_output_has_decimal_formatting():
    """Test that monetary values are properly formatted - 1 point"""
    task3, output = import_and_run_task3()
    assert "79.98" in output, "Subtotal should be displayed"
    assert "87.58" in output, "Total should be displayed"


def test_09_uses_round_function():
    """Test that code uses round() function - 1 point"""
    with open('task3.py', 'r') as f:
        code = f.read()
    assert 'round(' in code, "Should use round() function for total"


def test_10_uses_type_conversion():
    """Test that code uses float() and int() conversion - 1 point"""
    with open('task3.py', 'r') as f:
        code = f.read()
    assert 'float(' in code, "Should use float() to convert price input"
    assert 'int(' in code, "Should use int() to convert quantity input"
