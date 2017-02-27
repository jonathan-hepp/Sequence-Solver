#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_sequence_solver
----------------------------------

Tests for `sequence_solver` module.
"""


import sys
import unittest
from sequence_solver import strategies


class TestSequence_solver(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_simple_increment(self):
        solver = strategies.DiffTableStrategy()
        next_item = solver.solve([1, 3, 5])
        self.assertEqual(7, next_item)

    def test_002_negative(self):
        solver = strategies.DiffTableStrategy()
        next_item = solver.solve([0, -5, -10])
        self.assertEqual(-15, next_item)

    def test_003_growing_increment(self):
        solver = strategies.DiffTableStrategy()
        next_item = solver.solve([7, 14, 22, 31, 41])
        self.assertEqual(52, next_item)

    def test_004_alphabet(self):
        solver = strategies.AlphabetSubstitutionStrategy()
        next_item = solver.solve(["a", "c", "e"])
        self.assertEqual("g", next_item)

    def test_005_alphabet_reverse(self):
        solver = strategies.AlphabetSubstitutionStrategy()
        next_item = solver.solve(["x", "u", "q", "l"])
        self.assertEqual("f", next_item)

    def test_006_fibonacci(self):
        solver = strategies.SpecialCasesStrategy()
        next_item = solver.solve([1,1,2,3,5,8,13])
        self.assertEqual(21, next_item)

    def test_007_fibonacci2(self):
        solver = strategies.SpecialCasesStrategy()
        next_item = solver.solve([5,8,13,21,34])
        self.assertEqual(55, next_item)

    def test_008_fibonacci_unordered(self):
        solver = strategies.SpecialCasesStrategy()
        self.assertRaises(Exception, solver.solve, [55,13,8,21,5,34])

    def test_009_non_fibonacci(self):
        solver = strategies.SpecialCasesStrategy()
        self.assertRaises(Exception, solver.solve, [5,8,13,19,34])


