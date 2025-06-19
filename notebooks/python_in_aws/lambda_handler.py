import json

def calculate_economic_loss(stage, population):
    """Calculate economic loss per day for a given stage and population."""
    rate_per_person_per_stage = 50  # R50 per person per stage
    return stage * rate_per_person_per_stage * population


def process_city_data(city_data):
    """
    Processes a list of city dictionaries.
    Example input:
    [
        {"name": "Cape Town", "stage": 2, "population": 500000},
        {"name": "Joburg", "stage": 3, "population": 800000}
    ]
    """
    processed_results = []

    for city in city_data:
        name = city.get("name")
        stage = city.get("stage", 0)
        population = city.get("population", 0)

        loss = calculate_economic_loss(stage, population)

        processed_results.append({
            "name": name,
            "stage": stage,
            "population": population,
            "estimated_loss": loss
        })

    return processed_results


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    Expects an `event` with `cities` key containing a list of city records.
    """
    try:
        cities = event.get("cities", [])
        result = process_city_data(cities)

        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "message": "Processed successfully"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }


# // To test locally

# # test_lambda.py
# import lambda_function

# test_event = {
#     "cities": [
#         {"name": "Cape Town", "stage": 2, "population": 433688},
#         {"name": "Joburg", "stage": 3, "population": 957441}
#     ]
# }

# response = lambda_function.lambda_handler(test_event, None)
# print(response)
