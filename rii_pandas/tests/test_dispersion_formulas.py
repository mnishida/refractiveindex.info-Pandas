#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from math import nan
import numpy as np
import pandas as pd
from rii_pandas import DispersionFormula


class KnownValues(unittest.TestCase):
    known_values = [
        (1, [0.0 for _ in range(17)], 1.0, 1.0),
        (1, [1.0 if _ < 3 else 0 for _ in range(17)], 0.5, np.sqrt(5 / 3)),
        (1, [0.5 if _ < 3 else 0 for _ in range(17)], 1.0, np.sqrt(6.5 / 3)),
        (2, [0.0 for _ in range(17)], 1.0, 1.0),
        (2, [1.0 if _ < 3 else 0 for _ in range(17)], 0.5, np.sqrt(5 / 3)),
        (2, [0.5 if _ < 3 else 0 for _ in range(17)], 1.0, np.sqrt(2.5)),
        (3, [0.0 for _ in range(17)], 1.0, 0.0),
        (3, [1.0 if _ < 3 else 0 for _ in range(17)], 0.5, np.sqrt(1.5)),
        (3, [0.5 if _ < 3 else 0 for _ in range(17)], 2.0,
         np.sqrt((1 + np.sqrt(2)) / 2)),
        (4, [0.0 for _ in range(17)], 0.5, 0.0),
        (4, [1.0, 1.0, 2.0, 3.0, 2.0] + [0 for _ in range(5, 17)], 2.0,
         np.sqrt(1 / 5)),
        (4, [0.0 for _ in range(9)] + [0.5 for _ in range(9, 17)], 2.0,
         np.sqrt(2 * np.sqrt(2))),
        (5, [0.0 for _ in range(11)], 1.0, 0.0),
        (5, [2.0 for _ in range(11)], 0.5, 4.5),
        (5, [0.5 for _ in range(11)], 2.0, 0.5 + 2.5 * np.sqrt(2)),
        (6, [0.0 for _ in range(11)], 1.0, 1.0),
        (6, [0.5 for _ in range(11)], 2.0, 11.5),
        (6, [0.2 for _ in range(11)], 0.25, 1.2 - 1 / 15.8),
        (7, [0.0 for _ in range(6)], 0.5, 0.0),
        (7, [1.0 for _ in range(6)], np.sqrt(1.028),
         3 + 1.028 + 1.028 ** 2 + 1.028 ** 3),
        (7, [1.0, 0, 0, 0.5, 0.5, 0.5], 0.5, 1 + 21 / 2 ** 7),
        (8, [0.0 for _ in range(4)], 0.5, 1.0),
        (8, [0.1 for _ in range(4)], np.sqrt(0.2), np.sqrt(1.64 / 0.68)),
        (8, [0.2, 0, 0, 0.2], 0.5, np.sqrt(1.5 / 0.75)),
        (9, [0.0 for _ in range(6)], 0.5, 0.0),
        (9, [1.0 for _ in range(6)], np.sqrt(2),
         np.sqrt(2 + (np.sqrt(2) - 1) / (4 - 2 * np.sqrt(2)))),
        (9, [1.0 for _ in range(6)], 2.0, np.sqrt(11 / 6))
    ]

    known_values_for_tabulated = [
        (nan, [[0.01 * i, 0.0, 0.0] for i in range(100)], 0.5, (0.0, 0.0)),
        (nan, [[0.01 * i, 0.02 * i, 0.0] for i in range(100)], 0.5, (1.0, 0.0)),
        (nan, [[0.01 * i, 1.3, 0.01 * i] for i in range(100)], 0.5, (1.3, 0.5))
    ]

    def test_dispersion_formula_known_values(self):
        """dispersion_formula should return function."""
        for i, (formula, cs, wl, result) in enumerate(self.known_values):
            catalog = pd.DataFrame({'formula': [formula], 'tabulated': [''],
                                    'wl_min': [0.25], 'wl_max': [2.0]}).loc[0]
            data = pd.DataFrame({'cs': cs})
            func = DispersionFormula(catalog, data)
            n, k = func(wl)
            self.assertAlmostEqual(n, result)

    def test_dispersion_formula_for_tabulated(self):
        """dispersion_formula should return function."""
        for i, (formula, wlnk, wl, result) in enumerate(
                self.known_values_for_tabulated):
            wlnk = np.array(wlnk)
            wls = wlnk[:, 0]
            ns = wlnk[:, 1]
            ks = wlnk[:, 2]
            catalog = pd.DataFrame({'formula': [formula], 'tabulated': ['nk'],
                                    'wl_min': [0.25], 'wl_max': [2.0]}).loc[0]
            data = pd.DataFrame({'wls_n': wls, 'ns': ns,'wls_k': wls, 'ks': ks})
            func = DispersionFormula(catalog, data)
            self.assertAlmostEqual(func(wl), result)

    def test_dispersion_formula_exception(self):
        catalog = pd.DataFrame({'formula': [1], 'tabulated': [''],
                                'wl_min': [0.25], 'wl_max': [2.0]}).loc[0]
        data = pd.DataFrame({'cs': list(range(17))})
        func = DispersionFormula(catalog, data)
        with self.assertRaises(ValueError):
            func(0.1)
        with self.assertRaises(ValueError):
            func(2.1)
        with self.assertRaises(ValueError):
            func(np.array([0.1 * i for i in range(21)]))


if __name__ == '__main__':
    unittest.main()
