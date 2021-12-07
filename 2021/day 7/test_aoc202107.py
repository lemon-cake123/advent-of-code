import pathlib
import pytest
import aoc202107 as aoc #change aoc_template to name of file
'''
a file used to test aoc solutions
'''

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example_input.txt").read_text().strip()
    return aoc.parse(puzzle_input)



def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [16,1,2,0,4,2,7,1,2,14]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 37


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 168


