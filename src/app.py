from custom_functions import shared
import numpy
import json


def lambda_handler(event, context):

    arr = numpy.array([1, 2, 3, 4, 5])
    print(arr)
    return {
        "statusCode":
        200,
        "body":
        json.dumps({
            "message": shared.say_hello(),  # invoke layer function
            "python-lib-output": str(arr)
        }),
    }
