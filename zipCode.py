import csv
from pyzipcode import ZipCodeDatabase

def _get_zip_code_instance(zip_code):
    zip_code_database = ZipCodeDatabase()
    return zip_code_database[str(zip_code)]

def get_city_state_by_zip(zip_code):
    """
    Lookup a US zip code for corresponding city and state

    Args:
        zip_code (string / int) : zip code for lookup

    Returns:
        city (string): corresponding city
        state (string): corresponding state
        None: If no match is found
    """

    zip_code_instance = _get_zip_code_instance(zip_code)

    city = zip_code_instance.city
    state = zip_code_instance.state

    if len(str(state)) == 0:
        return None

    return zip_code_instance.city, zip_code_instance.state

def get_lat_long_by_zip(zip_code):
    """
    Lookup a US zip code for corresponding latitude
    and longitude

    Args:
        zip_code (string / int): zip code for lookup

    Returns:
        latitude (string): corresponding latitude
        longitude (string) :corresponding longitude
        None: If no match is found
    """
    
    zip_code_instance = _get_zip_code_instance(zip_code)
    latitude = zip_code_instance.latitude
    longitude = zip_code_instance.longitude

    if len(str(latitude)) == 0:
        return None

    return latitude, longitude
