from tracker import create_record
from datetime import datetime
import json
records = [
    create_record("Delhi", "Amazing culture", "05-06-2022"),
    create_record("Goa", "Beautiful beaches", "12-12-2023"),
    create_record("Kochi", "Peaceful place", "20-01-2024")
]
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")
json_data = json.dumps(records, indent=4)
print("JSON Data:")
print(json_data)
parsed_data = json.loads(json_data)
print("\nParsed Records:")
for rec in parsed_data:
    print(f"City: {rec['city']}, Date: {rec['date']}, Comment: {rec['comment']}")
