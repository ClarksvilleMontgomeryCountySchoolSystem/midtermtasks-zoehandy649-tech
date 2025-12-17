import pytest
import subprocess
import sys
import re


# TASK 1 TESTS
# Expected outputs with given values (14, 8, 6, 6):
# Part 1: slices=28
# Part 2: people=7, share=4, leftover=0
# Part 3: people=9, share=3, leftover=1
# Part 4: slices=42, share=4, leftover=6

def run_task1():
    """Run task1.py and return output"""
    result = subprocess.run(
        [sys.executable, 'task1.py'],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout

def get_task1_code():
    """Read task1.py code for inspection"""
    with open('task1.py', 'r') as f:
        return f.read()


def test_task1_initial_slices():
    """Test that initial slice count is calculated correctly"""
    output = run_task1()
    assert "28" in output, "Initial slice count should be 28"


def test_task1_no_hardcoded_28():
    """Test that 28 is not hardcoded - must calculate from variables"""
    code = get_task1_code()
    # Remove the given variables section and comments
    code_lines = code.split('\n')
    code_to_check = []
    past_given = False
    for line in code_lines:
        if 'slices = ' in line and '=' in line and '+' in line:
            past_given = True
        if past_given:
            code_to_check.append(line)
    
    code_without_given = '\n'.join(code_to_check)
    assert '28' not in code_without_given, "Do not hardcode 28 - use variables"


def test_task1_part2_share():
    """Test Part 2 share calculation"""
    output = run_task1()
    lines = output.strip().split('\n')
    assert len(lines) >= 2, "Not enough output lines"
    assert "4" in lines[1], "Part 2 share should be 4"


def test_task1_no_hardcoded_share():
    """Test that share values are calculated, not hardcoded"""
    code = get_task1_code()
    # Look for share = followed by just a number (not //)
    assert not re.search(r'share\s*=\s*[0-9]+\s*$', code, re.MULTILINE), "Do not hardcode share values - use // operator"


def test_task1_part2_leftover():
    """Test Part 2 leftover calculation"""
    output = run_task1()
    lines = output.strip().split('\n')
    assert len(lines) >= 3, "Not enough output lines"
    assert "0" in lines[2], "Part 2 leftover should be 0"


def test_task1_no_hardcoded_leftover():
    """Test that leftover values are calculated, not hardcoded"""
    code = get_task1_code()
    # Look for leftover = followed by just a number (not %)
    assert not re.search(r'leftover\s*=\s*[0-9]+\s*$', code, re.MULTILINE), "Do not hardcode leftover values - use % operator"


def test_task1_part3_share():
    """Test Part 3 share calculation"""
    output = run_task1()
    lines = output.strip().split('\n')
    assert len(lines) >= 4, "Not enough output lines"
    assert "3" in lines[3], "Part 3 share should be 3"


def test_task1_part4_share():
    """Test Part 4 share calculation after pizza upgrade"""
    output = run_task1()
    lines = output.strip().split('\n')
    assert len(lines) >= 6, "Not enough output lines"
    assert "4" in lines[5], "Part 4 share should be 4"


def test_task1_part4_leftover():
    """Test Part 4 leftover calculation after pizza upgrade"""
    output = run_task1()
    lines = output.strip().split('\n')
    assert len(lines) >= 7, "Not enough output lines"
    assert "6" in lines[6], "Part 4 leftover should be 6"


def test_task1_hollow_leg_message():
    """Test that the Mr. Hollow Leg message appears"""
    output = run_task1()
    assert "Hollow Leg" in output, "Should include Hollow Leg message"


# Placeholder for TASK 2 TESTS (to be added)
# Placeholder for TASK 3 TESTS (to be added)
# Placeholder for TASK 4 TESTS (to be added)
