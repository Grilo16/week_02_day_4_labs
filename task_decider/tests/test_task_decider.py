import unittest
from src.task_decider import task_decider
from src.task_class import Task

class testTaskDecider(unittest.TestCase):
    
    def setUp(self):
        self.wash_dishes = Task("Wash Dishes", 50)
        self.cook_dinner = Task("Cook Dinner", 50)
        self.clean_windows = Task("Clean Windows", 50)
        self.do_ironing = Task("Do Ironing", 50)
        self.wash_clothes = Task("Wash Clothes", 50)

    
    # Test "Wash dishes" is preferred over "Cook Dinner"
    def test_wash_dishes_over_cook_dinner(self):
        choice = task_decider(self.wash_dishes, self.cook_dinner)
        self.assertEqual("Wash Dishes", choice.description)

        flipped_choice = task_decider(self.cook_dinner, self.wash_dishes)
        self.assertEqual("Wash Dishes", flipped_choice.description)
        
    # Test "Cook Dinner" is preferred over "Clean Windows"
    def test_cook_dinner_over_clean_windows(self):
        choice = task_decider(self.cook_dinner, self.clean_windows)
        self.assertEqual("Cook Dinner", choice.description)
        
        flipped_choice = task_decider(self.clean_windows, self.cook_dinner)
        self.assertEqual("Cook Dinner", flipped_choice.description)

    # Test "Clean Windows" is preferred over "Wash Dishes"
    def test_clean_windows_over_wash_dishes(self):
        choice = task_decider(self.clean_windows, self.wash_dishes)
        self.assertEqual("Clean Windows", choice.description)
    
        fliped_choice = task_decider(self.wash_dishes, self.clean_windows)
        self.assertEqual("Clean Windows", fliped_choice.description)
    
    # Test "Wash Dishes" is preferred over "Wash Clothes"
    def test_wash_dishes_over_wash_clothes(self):
        choice = task_decider(self.wash_dishes, self.wash_clothes)
        self.assertEqual("Wash Dishes", choice.description)
    
        fliped_choice = task_decider(self.wash_clothes, self.wash_dishes)
        self.assertEqual("Wash Dishes", fliped_choice.description)
    
    # Test "Cook Dinner" is preferred over "Do Ironing"
    def test_cook_dinner_over_do_ironing(self):
        choice = task_decider(self.cook_dinner, self.do_ironing)
        self.assertEqual("Cook Dinner", choice.description)
    
        fliped_choice = task_decider(self.do_ironing, self.cook_dinner)
        self.assertEqual("Cook Dinner", fliped_choice.description)
    
    # Test "Clean Windows" is preferred over "Do Ironing"
    def test_clean_windows_over_do_ironing(self):
        choice = task_decider(self.clean_windows, self.do_ironing)
        self.assertEqual("Clean Windows", choice.description)
    
        fliped_choice = task_decider(self.do_ironing, self.clean_windows)
        self.assertEqual("Clean Windows", fliped_choice.description)
    
    # Test "Do Ironing" is preferred over "Wash Clothes"
    def test_do_ironing_over_wash_clothes(self):
        choice = task_decider(self.do_ironing, self.wash_clothes)
        self.assertEqual("Do Ironing", choice.description)
    
        fliped_choice = task_decider(self.wash_clothes, self.do_ironing)
        self.assertEqual("Do Ironing", fliped_choice.description)
    
    # Test "Do Ironing" is preferred over "Wash Dishes"
    def test_do_ironing_over_wash_dishes(self):
        choice = task_decider(self.do_ironing, self.wash_dishes)
        self.assertEqual("Do Ironing", choice.description)
    
        fliped_choice = task_decider(self.wash_dishes, self.do_ironing)
        self.assertEqual("Do Ironing", fliped_choice.description)
    
    # Test "Wash Clothes" is preferred over "Cook Dinner"
    def test_wash_clothes_over_cook_dinner(self):
        choice = task_decider(self.wash_clothes, self.cook_dinner)
        self.assertEqual("Wash Clothes", choice.description)
    
        fliped_choice = task_decider(self.cook_dinner, self.wash_clothes)
        self.assertEqual("Wash Clothes", fliped_choice.description)
    
    # Test "Wash Clothes" is preferred over "Clean Windows"
    def test_wash_clothes_over_clean_windows(self):
        choice = task_decider(self.wash_clothes, self.clean_windows)
        self.assertEqual("Wash Clothes", choice.description)
    
        fliped_choice = task_decider(self.clean_windows, self.wash_clothes)
        self.assertEqual("Wash Clothes", fliped_choice.description)
    