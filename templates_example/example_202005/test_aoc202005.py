import pathlib
import pytest
import aoc202005 as aoc #change aoc_template to name of file
'''
a file used to test aoc solutions
'''

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example_input.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example_input_2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [357, 567, 119, 820]

def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 820


def test_part2():
    """Test part 2 on example input"""
    data = [3, 9, 4, 8, 5, 10, 7, 11]
    assert aoc.part2(data) == 6
