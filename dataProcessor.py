import json

def read_json_file(file_path):

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

def avgAgeCountry(data, transform_func=None):
    if not data:
        return None

    age_sum = {}
    age_count = {}
    
    for person in data:
        country = person.get("country")
        age = person.get("age")
        
        if country is None or age is None:
            continue
        
        if transform_func:
            age = transform_func(age)
        
        if country not in age_sum:
            age_sum[country] = 0
            age_count[country] = 0
        
        age_sum[country] += age
        age_count[country] += 1

    avg_age = {}
    for country, total_age in age_sum.items():
        avg_age[country] = total_age / age_count[country]

    return avg_age