from tripdata import get_trip
from datetime import datetime
import json
trip = []
trip.append(get_trip("UK", "22|12|2024", "Beautiful City"))
trip.append(get_trip("Canada", "10|1|2025", "Beautiful City"))
trip.append(get_trip("America", "18|11|2025", "Beautiful City"))
for trips in trip:
    date_obj = datetime.strptime(trips["date"],"%d-%m-%y")
    trips["date"] = date_obj.strftime("%B %d %y")
json_data = json.dumps(trips,indent=4)
print(json_data)