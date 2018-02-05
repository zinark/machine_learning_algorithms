class DataSource(object):

    def __init__(self):
        pass

    @staticmethod
    def sample_decision_data():
        return {
            "Gender": ["Male", "Male", "Female", "Female", "Male", "Male", "Female", "Female", "Male", "Female"],
            "CarOwnership": [0, 1, 1, 0, 1, 0, 1, 1, 2, 2],
            "TravelCost": ["Cheap", "Cheap", "Cheap", "Cheap", "Cheap", "Standard", "Standard", "Expensive",
                           "Expensive", "Expensive"],
            "IncomeLevel": ["Low", "Medium", "Medium", "Low", "Medium", "Medium", "Medium", "High", "Medium", "High"],
            "Transportation": ["Bus", "Bus", "Train", "Bus", "Bus", "Train", "Train", "Car", "Car", "Car"]
        }

    @staticmethod
    def and_table():
        return {
            "O": [1, 1, 1, 0],
            "X": [1, 1, 0, 0],
            "Y": [1, 0, 1, 0],
        }

    @staticmethod
    def fruits():
        return [
            ['Green', 3, 'Apple'],
            ['Yellow', 3, 'Apple'],
            ['Red', 1, 'Grape'],
            ['Red', 1, 'Grape'],
            ['Yellow', 1, 'Lemon']
        ]

    @staticmethod
    def weights_and_heights():
        return {
            "feature_names": ["weight"],
            "target_name": "height",
            "targets": [75, 71, 83, 63, 70],
            "data": [
                [180], [174], [184], [168], [178]
            ]
        }

    @staticmethod
    def plan_matrix():
        return {
            "feature_names": ["task_id", "category", "time_elapsed", "tested", "tested2"],
            "data": [
                ["t01", "backend", 4, 1, 1],
                ["t01", "frontend", 5, 1, 1],
                ["t01", "design", 1, 1, 1],
                ["t01", "analyse", 4, 1, 1],

                ["t02", "backend", 11, 1, -1],
                ["t02", "frontend", 8, 1, -1],
                ["t02", "design", 7, 1, 1],
                ["t02", "analyse", 9, 1, -1],

                ["t03", "backend", 2, -1, 0],
                ["t03", "frontend", 6, -1, 0],
                ["t03", "design", 3, -1, 0],
                ["t03", "analyse", 4, -1, 0]
            ]}
