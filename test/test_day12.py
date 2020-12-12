# MIT License
#
# Copyright (c) 2020 Andrew Krepps
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import unittest

from advent2020.day12 import get_part1_answer
from advent2020.day12 import get_part2_answer
from advent2020.day12 import parse_commands


ship_data = """
F10
N3
F7
R90
F11
"""


class Day12Test(unittest.TestCase):
    def test_day12(self):
        lines = [line.strip() for line in ship_data.split("\n") if len(line.strip()) > 0]
        commands = parse_commands(lines)
        self.assertEqual(get_part1_answer(commands), 25)
        self.assertEqual(get_part2_answer(commands), 286)
