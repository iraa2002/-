# TODO решите задачу
import json

def task() -> float:
    json_file = "input.json"
    with open(json_file) as f:
        json_data = json.load(f)

    # Сумма произведений score и weight
    total = sum(item["score"] * item["weight"] for item in json_data)

    return round(total, 3)



print(task())
