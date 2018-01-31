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
