# create a task decider function here
def task_decider(task_1, task_2):
    task_preferences = {
        "Wash Dishes": ["Cook Dinner", "Wash Clothes"],
        "Cook Dinner": ["Clean Windows", "Do Ironing"],
        "Clean Windows": ["Wash Dishes", "Do Ironing"],
        "Do Ironing": ["Wash Clothes", "Wash Dishes"],
        "Wash Clothes": ["Cook Dinner", "Clean Windows"]
    }

    task_1_name = task_1.description
    task_2_name = task_2.description

    if task_1_name in task_preferences[task_2_name]:
        return task_2
    
    if task_2_name in task_preferences[task_1_name]:
        return task_1


