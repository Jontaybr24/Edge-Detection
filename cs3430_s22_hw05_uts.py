#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: cs3430_s22_hw05_uts.py
# description: unit tests for CS 3430: S22: Assignment 05
# bugs to vladimir dot kulyukin in canvas.
##############################################################

import unittest
from cs3430_s22_hw05 import depil
from PIL import Image

class cs3430_s22_hw05_uts(unittest.TestCase):

    ### ================ Problem 1: Unit Tests =====================

    def __test_depil(self, inpath, outpath, default_delta=1.0, magn_thresh=20):
        input_image  = Image.open(inpath)
        output_image = depil(input_image, default_delta=default_delta, magn_thresh=magn_thresh)
        output_image.save(outpath)
        del input_image
        del output_image

    def test_hw05_prob01_ut01(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 01 ************')
        self.__test_depil('imgs/img.jpg', 'out_imgs/EdgeImage_01_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 01: pass')

    def test_hw05_prob01_ut02(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 02 ************')
        self.__test_depil('imgs/EdgeImage_02.jpg', 'out_imgs/EdgeImage_02_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 02: pass')
    """
    def test_hw05_prob01_ut03(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 03 ************')
        self.__test_depil('imgs/EdgeImage_03.jpg', 'out_imgs/EdgeImage_03_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 03: pass')

    def test_hw05_prob01_ut04(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 04 ************')
        self.__test_depil('imgs/EdgeImage_04.jpg', 'out_imgs/EdgeImage_04_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 04: pass')

    def test_hw05_prob01_ut05(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 05 ************')
        self.__test_depil('imgs/EdgeImage_05.jpg', 'out_imgs/EdgeImage_05_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 05: pass')

    def test_hw05_prob01_ut06(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 06 ************')
        self.__test_depil('imgs/EdgeImage_06.jpg', 'out_imgs/EdgeImage_06_ed.jpg')        
        print('CS 3430: S22: HW05: Problem 01: Unit Test 06: pass')

    def test_hw05_prob01_ut07(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 07 ************')
        self.__test_depil('imgs/EdgeImage_07.jpg', 'out_imgs/EdgeImage_07_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 07: pass')

    def test_hw05_prob01_ut08(self):
        print('\n***** CS3430: S22: HW05: Problem 01: Unit Test 08 ************')
        self.__test_depil('imgs/road_01.png', 'out_imgs/road_01_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 08: pass')

    def test_hw05_prob01_ut09(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 09 ************')
        self.__test_depil('imgs/road_02.png', 'out_imgs/road_02_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 09: pass')

    def test_hw05_prob01_ut10(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 10 ************')
        self.__test_depil('imgs/BirdOrnament.jpg', 'out_imgs/BirdOrnament_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 10: pass')

    def test_hw05_prob01_ut11(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 11 ************')
        self.__test_depil('imgs/hive01.png', 'out_imgs/hive01_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 11: pass')

    def test_hw05_prob01_ut12(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 12 ************')
        self.__test_depil('imgs/hive02.png', 'out_imgs/hive02_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 12: pass')

    def test_hw05_prob01_ut13(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 13 ************')
        self.__test_depil('imgs/hive03.png', 'out_imgs/hive03_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 13: pass')

    def test_hw05_prob01_ut14(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 14 ************')
        self.__test_depil('imgs/lunch.jpg', 'out_imgs/lunch_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 14: pass')

    def test_hw05_prob01_ut15(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 15 ************')
        self.__test_depil('imgs/june.jpg', 'out_imgs/june_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 15: pass')

    def test_hw05_prob01_ut16(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 16 ************')
        self.__test_depil('imgs/nt_01.jpg', 'out_imgs/nt_01_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 16: pass')

    def test_hw05_prob01_ut17(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 17 ************')
        self.__test_depil('imgs/sudoku.jpg', 'out_imgs/sudoku_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 17: pass')

    def test_hw05_prob01_ut18(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 18 ************')
        self.__test_depil('imgs/elephant.jpg', 'out_imgs/elephant_ed.jpg')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 18: pass')

    def test_hw05_prob01_ut19(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 19 ************')
        self.__test_depil('imgs/road_03.png', 'out_imgs/road_03_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 19: pass')

    def test_hw05_prob01_ut20(self):
        print('\n***** CS3430: S22: HW09: Problem 01: Unit Test 20 ************')
        self.__test_depil('imgs/road_04.png', 'out_imgs/road_04_ed.png')
        print('CS 3430: S22: HW05: Problem 01: Unit Test 20: pass')

    def runTest(self):
        pass
        """

if __name__ == '__main__':
    unittest.main()
