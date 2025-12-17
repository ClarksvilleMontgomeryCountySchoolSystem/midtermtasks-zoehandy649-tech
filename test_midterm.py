import pytest
import subprocess
import sys


# TASK 1 TESTS
# Test values: party_pizza_mini=16, large=10, medium=8, people=5
# Expected outputs:
# Part 1: slices=34
# Part 2: people=6, share=5, leftover=4
# Part 3: people=8, share=4, leftover=2
# Part 4: slices=50, share=6, leftover=2

def run_task1_with_test_values():
    """Run task1.py with modified test values and return output"""
    code = """
party_pizza_mini = 16
large = 10
medium = 8
people = 5

exec(open('task1.py').read())
"""
    result = subprocess.run(
        [sys.executable, '-c', code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout


def test_task1_initial_slices():
    """Test that initial slice count is calculated correctly"""
    output = run_task1_with_test_values()
    assert "34" in output, "Initial slice count should be 34"


def test_task1_part2_share():
    """Test Part 2 share calculation"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 2, "Not enough output lines"
    assert "5" in lines[1], "Part 2 share should be 5"


def test_task1_part2_leftover():
    """Test Part 2 leftover calculation"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 3, "Not enough output lines"
    assert "4" in lines[2], "Part 2 leftover should be 4"


def test_task1_part3_share():
    """Test Part 3 share calculation"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 4, "Not enough output lines"
    assert "4" in lines[3], "Part 3 share should be 4"


def test_task1_part3_leftover():
    """Test Part 3 leftover calculation"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 5, "Not enough output lines"
    assert "2" in lines[4], "Part 3 leftover should be 2"


def test_task1_part4_share():
    """Test Part 4 share calculation after pizza upgrade"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 6, "Not enough output lines"
    assert "6" in lines[5], "Part 4 share should be 6"


def test_task1_part4_leftover():
    """Test Part 4 leftover calculation after pizza upgrade"""
    output = run_task1_with_test_values()
    lines = output.strip().split('\n')
    assert len(lines) >= 7, "Not enough output lines"
    assert "2" in lines[6], "Part 4 leftover should be 2"


def test_task1_hollow_leg_message():
    """Test that the Mr. Hollow Leg message appears"""
    output = run_task1_with_test_values()
    assert "Hollow Leg" in output, "Should include Hollow Leg message"


def test_task1_output_line_count():
    """Test that the correct number of output lines are printed"""
    output = run_task1_with_test_values()
    lines = [line for line in output.strip().split('\n') if line]
    assert len(lines) == 8, f"Should have 8 output lines, got {len(lines)}"


def test_task1_runs_without_error():
    """Test that task1 runs without errors"""
    try:
        output = run_task1_with_test_values()
        assert output, "Task should produce output"
    except subprocess.TimeoutExpired:
        pytest.fail("Task1 timed out")
    except Exception as e:
        pytest.fail(f"Task1 raised an exception: {e}")


# Placeholder for TASK 2 TESTS (to be added)
# Placeholder for TASK 3 TESTS (to be added)
# Placeholder for TASK 4 TESTS (to be added)
