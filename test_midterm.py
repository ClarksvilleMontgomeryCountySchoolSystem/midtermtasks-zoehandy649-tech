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


# Placeholder for TASK 2 TESTS (to be added)
# Placeholder for TASK 3 TESTS (to be added)
# Placeholder for TASK 4 TESTS (to be added)
