# Mock database (list of dictionaries)
MOCK_DATABASE = [
    {'id': 3, 'name': 'Charlie'},
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'}
]

def get_sorted_data():
    """
    Sorts the mock database by the 'id' field.
    """
    return sorted(MOCK_DATABASE, key=lambda item: item['id'])