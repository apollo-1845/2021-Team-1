from unittest import TestCase

import numpy as np
from PIL import Image

from image_data import sum_of_pixel_brightnesses


class Test(TestCase):
    def test_sum_of_pixel_brightnesses_white(self):
        self.assertEqual(2048 ** 2 * 255 * 3, sum_of_pixel_brightnesses(self.__load_image("resources/white_2048.png")))

    def test_sum_of_pixel_brightnesses_black(self):
        self.assertEqual(0, sum_of_pixel_brightnesses(self.__load_image("resources/black_2048.png")))

    def test_sum_of_pixel_brightnesses_noise(self):
        self.assertEqual(1580563488, sum_of_pixel_brightnesses(self.__load_image("resources/perlin_noise_2048.png")))

    @staticmethod
    def __load_image(path):
        return np.asarray(Image.open(path))
