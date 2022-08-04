import unittest
from src.task_class import Task

class testTaskClass(unittest.TestCase):
    
    def setUp(self):
        self.task1 = Task("Wash Dishes", 50)
        self.task2 = Task("Cook Dinner", 50)
        self.task3 = Task("Clean Windows", 50)

    
    # test class paramters
    def test_class_has_description_and_duration(self):
        self.assertEqual("Wash Dishes", self.task1.description)
        self.assertEqual(50, self.task1.duration)
    
        self.assertEqual("Cook Dinner", self.task2.description)
        self.assertEqual(50, self.task2.duration)
    
        self.assertEqual("Clean Windows", self.task3.description)
        self.assertEqual(50, self.task3.duration)

