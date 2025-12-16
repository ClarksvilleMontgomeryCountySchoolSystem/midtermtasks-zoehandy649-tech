import sys
import os
from io import StringIO
from unittest.mock import patch

# Global flag for hard-coding detection
hardcoded = False


def test_00_file_exists():
    """Test that task3.py exists - 1 point"""
    assert os.path.exists('task3.py'), "task3.py not found - have you committed it to GitHub?"


def test_01_check_hardcoding():
    """Check for hard-coding - if detected, all other tests will fail - 1 point"""
    global hardcoded
    
    try:
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
        
        # Check if hard-coded
        if 'subtotal' in namespace and namespace['subtotal'] != expected_subtotal:
            hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if 'total' in namespace and namespace['total'] != expected_total:
            hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
        
        if "74.95" not in output or "82.07" not in output:
            hardcoded = True
            assert False, "Hard-coding detected - all tests will fail"
            
    except AssertionError:
        raise
    except Exception:
        # If we can't run the hard-coding check due to syntax errors, let other tests run
        pass


def import_and_run_task3():
    """Helper function to import task3 and capture output"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    
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


def test_02_required_variables_exist():
    """Test that all required variables exist - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'item'), "Missing required variable: item"
    assert hasattr(task3, 'price'), "Missing required variable: price"
    assert hasattr(task3, 'quantity'), "Missing required variable: quantity"
    assert hasattr(task3, 'subtotal'), "Missing required variable: subtotal"
    assert hasattr(task3, 'tax'), "Missing required variable: tax"
    assert hasattr(task3, 'total'), "Missing required variable: total"


def test_03_get_purchase_info_function_exists():
    """Test that get_purchase_info function exists - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert hasattr(task3, 'get_purchase_info'), "Missing required function: get_purchase_info"
    assert callable(task3.get_purchase_info), "get_purchase_info must be a function"


def test_04_subtotal_value():
    """Test subtotal calculation - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_subtotal = 79.98
    assert task3.subtotal == expected_subtotal, f"subtotal has incorrect value. Expected {expected_subtotal}, got {task3.subtotal}"


def test_05_tax_value():
    """Test tax calculation - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_tax = 7.5981
    assert abs(task3.tax - expected_tax) < 0.0001, f"tax has incorrect value. Expected approximately {expected_tax}, got {task3.tax}"


def test_06_total_value():
    """Test total calculation and rounding - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    expected_total = 87.58
    assert task3.total == expected_total, f"total has incorrect value. Expected {expected_total}, got {task3.total}"


def test_07_menu_displayed():
    """Test that menu is displayed - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "PECULIAR EMPORIUM" in output, "Menu header not displayed"
    assert "Crystal Ball" in output, "Menu items not displayed"


def test_08_receipt_formatted_correctly():
    """Test receipt shows all required elements - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "x2" in output, "Receipt should show quantity"
    assert "39.99" in output, "Receipt should show item price"
    assert "Subtotal:" in output, "Subtotal label missing"
    assert "Tax:" in output, "Tax label missing"
    assert "Total:" in output, "Total label missing"


def test_09_output_has_decimal_formatting():
    """Test that monetary values are properly formatted - 1 point"""
    assert not hardcoded, "Hard-coding detected - no points awarded"
    task3, output = import_and_run_task3()
    assert "79.98" in output, "Subtotal should be displayed"
    assert "87.58" in output, "Total should be displayed"
