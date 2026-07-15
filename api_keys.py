

import secrets


API_KEYS = {}



def generate_api_key():

    key = secrets.token_hex(32)

    API_KEYS[key] = "active"

    return key



def validate_api_key(key):

    return (
        key in API_KEYS
        and API_KEYS[key] == "active"
    )
