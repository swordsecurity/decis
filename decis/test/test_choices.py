#!/usr/bin/python
import sys
from os.path import dirname,abspath
sys.path.append(dirname(dirname(abspath(__file__))))

import decis 

from unittest import TestCase
from unittest import main

class test_choices(TestCase):

    maxDiff = None

    # 1. load choices
    def test_load_choices(self):
        choices_folder = abspath(dirname(__file__)) + "/assets/choices1/choices"
        result = decis.load_choices(choices_folder)
        expected = {"dog": choices_folder + "/dog.md","cat": choices_folder + "/cat.md"}
        self.assertEquals(expected,result)

    # 2. parse anwsers for a choice (choice: title, answers)
    # answer=requirement, answer, satisfaction, description
    def test_parse_answers(self):
        answers_path = abspath(dirname(__file__)) + "/assets/choices1/choices/cat.md"
        result = decis.load_answers(answers_path)
        expected = {}
        expected["Food"] = {"short":"Cheap","score":80,"long":"According to [Walmart][1] it's 14.72 for 35 cans of food."}
        expected["Kids"] = {"short":"Good with kids","score":70,"long":"According to [Pethelpful][2] cats often like kids."}
        expected["Clean"] = {"short":"Clean themselves","score":90,"long":"According to [Pethelpful][2]."}
        self.assertEquals(expected,result)

    # 3. load requirements
    def test_load_requirements(self):
        requirements_path = abspath(dirname(__file__)) + "/assets/choices1/requirements.txt"
        result = decis.load_requirements(requirements_path)
        expected = [("Food",35),("Kids",40),("Clean",25)]
        self.assertEquals(expected,result)

    # 4. calculate outcomes
    def test_calc_outcome(self):
        requirements_path = abspath(dirname(__file__)) + "/assets/choices1/requirements.txt"
        choice_path = abspath(dirname(__file__)) + "/assets/choices1/choices/cat.md"
        requirements = decis.load_requirements(requirements_path)
        result = decis.calc_outcome(requirements,choice_path)
        # formula: calc for each requirement satisfaction * importance, then take average of alld
        # 35 * 80 = 2800
        # 40 * 70 = 2800
        # 25 * 90 = 2250
        # ========+
        #           7850
        # divide by 100
        # = 90,25% match
        expected = 78.50 
        self.assertEquals(expected,result)
    
    # 5. transform data to form
        

if __name__ == '__main__':
    main()

