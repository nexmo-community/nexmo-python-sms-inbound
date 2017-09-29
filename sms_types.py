import os
import hug
import nexmo


@hug.type(extend=hug.types.text)
def telephone_number(value):
    """Validates number using Nexmo basic insight API"""

    nexmo_client = nexmo.Client(
        key=os.environ['NEXMO_API_KEY'],
        secret=os.environ['NEXMO_API_SECRET']
    )

    response = nexmo_client.get_basic_number_insight(number=value)

    if response['status'] is not 0:
        raise ValueError('Value is not a valid telephone number.')

    return value
