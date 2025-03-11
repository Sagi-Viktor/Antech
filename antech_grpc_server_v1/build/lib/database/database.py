from config import MOCK_DATABASE

def get_device_by_id(device_id):
    """
    Mock function to fetch a device by its ID from the mock database.
    """
    return next((d for d in MOCK_DATABASE["devices"] if d["device_id"] == device_id), None)
