import pytest
import sys
import importlib.util


def load_task_module(task_name, variables):
    """
    Load a task module with modified variables for testing.
    
    Args:
        task_name: Name of the task file (e.g., 'task1')
        variables: Dict of variable names and values to inject
    
    Returns:
        The loaded module
    """
    spec = importlib.util.spec_from_file_location(task_name, f"{task_name}.py")
    module = importlib.util.module_from_spec(spec)
    
    # Inject test variables into module namespace
    for var_name, var_value in variables.items():
        setattr(module, var_name, var_value)
    
    # Execute the module
    spec.loader.exec_module(module)
    
    return module


# TASK 1 TESTS
# Test values: party_pizza_mini=16, large=10, medium=8, people=5
# Expected outputs:
# Part 1: slices=34
# Part 2: people=6, share=5, leftover=4
# Part 3: people=8, share=4, leftover=2
# Part 4: slices=50, share=6, leftover=2

def test_task1_initial_slices(capsys):
    """Test that initial slice count is calculated correctly"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    assert "34" in captured.out


def test_task1_part2_share(capsys):
    """Test Part 2 share calculation"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 2 share should be in line index 1
    assert "5" in lines[1]


def test_task1_part2_leftover(capsys):
    """Test Part 2 leftover calculation"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 2 leftover should be in line index 2
    assert "4" in lines[2]


def test_task1_part3_share(capsys):
    """Test Part 3 share calculation"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 3 share should be in line index 3
    assert "4" in lines[3]


def test_task1_part3_leftover(capsys):
    """Test Part 3 leftover calculation"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 3 leftover should be in line index 4
    assert "2" in lines[4]


def test_task1_part4_share(capsys):
    """Test Part 4 share calculation after pizza upgrade"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 4 share should be in line index 5
    assert "6" in lines[5]


def test_task1_part4_leftover(capsys):
    """Test Part 4 leftover calculation after pizza upgrade"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = captured.out.strip().split('\n')
    # Part 4 leftover should be in line index 6
    assert "2" in lines[6]


def test_task1_hollow_leg_message(capsys):
    """Test that the Mr. Hollow Leg message appears"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    assert "Mr. Hollow Leg" in captured.out or "Hollow Leg" in captured.out


def test_task1_output_line_count(capsys):
    """Test that the correct number of output lines are printed"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    load_task_module('task1', test_vars)
    
    captured = capsys.readouterr()
    lines = [line for line in captured.out.strip().split('\n') if line]
    assert len(lines) == 8  # 7 calculation outputs + 1 Hollow Leg message


def test_task1_no_errors(capsys):
    """Test that task1 runs without errors"""
    test_vars = {'party_pizza_mini': 16, 'large': 10, 'medium': 8, 'people': 5}
    
    try:
        load_task_module('task1', test_vars)
        captured = capsys.readouterr()
        # If we got here, no exceptions were raised
        assert True
    except Exception as e:
        pytest.fail(f"Task1 raised an exception: {e}")


# Placeholder for TASK 2 TESTS (to be added)
# Placeholder for TASK 3 TESTS (to be added)
# Placeholder for TASK 4 TESTS (to be added)
