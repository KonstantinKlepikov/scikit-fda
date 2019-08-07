import unittest

import matplotlib.pyplot as plt
import numpy as np
from skfda import FDataGrid
from skfda.exploratory.depth import band_depth, fraiman_muniz_depth
from skfda.exploratory.visualization.boxplot import Boxplot, SurfaceBoxplot


class TestBoxplot(unittest.TestCase):

    def test_fdboxplot_univariate(self):
        data_matrix = [[1, 1, 2, 3, 2.5, 2],
                       [0.5, 0.5, 1, 2, 1.5, 1],
                       [-1, -1, -0.5, 1, 1, 0.5],
                       [-0.5, -0.5, -0.5, -1, -1, -1]]
        sample_points = [0, 2, 4, 6, 8, 10]
        fd = FDataGrid(data_matrix, sample_points)
        fdataBoxplot = Boxplot(fd, method=fraiman_muniz_depth)
        np.testing.assert_array_equal(
            fdataBoxplot.median.ravel(),
            np.array([-1., -1., -0.5, 1., 1., 0.5]))
        np.testing.assert_array_equal(
            fdataBoxplot.central_envelope[0].ravel(),
            np.array([-1., -1., -0.5, -1., -1., -1.]))
        np.testing.assert_array_equal(
            fdataBoxplot.central_envelope[1].ravel(),
            np.array([-0.5, -0.5, -0.5, 1., 1., 0.5]))
        np.testing.assert_array_equal(
            fdataBoxplot.non_outlying_envelope[0].ravel(),
            np.array([-1., -1., -0.5, -1., -1., -1.]))
        np.testing.assert_array_equal(
            fdataBoxplot.non_outlying_envelope[1].ravel(),
            np.array([-0.5, -0.5, -0.5,  1.,  1.,  0.5]))
        self.assertEqual(len(fdataBoxplot.envelopes), 1)
        np.testing.assert_array_equal(
            fdataBoxplot.envelopes[0],
            fdataBoxplot.central_envelope)
        np.testing.assert_array_equal(fdataBoxplot.outliers,
                                      np.array([True, True, False, False]))


if __name__ == '__main__':
    print()
    unittest.main()
