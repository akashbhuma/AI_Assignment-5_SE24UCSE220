class TravelPlanner:
    def __init__(self):
        self.destinations = {
            "Hyderabad": {
                "interest": ["Culture", "Food"],
                "food": ["Hyderabadi Biryani", "Haleem"],
                "activities": ["Charminar Visit", "Golconda Fort", "Ramoji Film City"],
                "hotel": 2800,
                "travel": 4000
            },
            "Chennai": {
                "interest": ["Beach", "Culture"],
                "food": ["Dosa", "Chettinad Chicken"],
                "activities": ["Marina Beach", "Kapaleeshwarar Temple", "Shopping"],
                "hotel": 2500,
                "travel": 4500
            },
            "Varanasi": {
                "interest": ["Spiritual", "Culture"],
                "food": ["Kachori Sabzi", "Malaiyo"],
                "activities": ["Ganga Aarti", "Kashi Vishwanath Temple", "Boat Ride"],
                "hotel": 2000,
                "travel": 5000
            },
            "Shimla": {
                "interest": ["Mountain", "Nature"],
                "food": ["Siddu", "Madra"],
                "activities": ["Mall Road", "Jakhoo Temple", "Trekking"],
                "hotel": 3500,
                "travel": 7000
            },
            "Munnar": {
                "interest": ["Nature", "Adventure"],
                "food": ["Appam", "Kerala Curry"],
                "activities": ["Tea Gardens", "Eravikulam National Park", "Boating"],
                "hotel": 3200,
                "travel": 6500
            },
            "Kochi": {
                "interest": ["Food", "Culture"],
                "food": ["Kerala Sadya", "Fish Curry"],
                "activities": ["Fort Kochi", "Chinese Fishing Nets", "Backwater Cruise"],
                "hotel": 3000,
                "travel": 5500
            }
        }
        

    def generate_plan(self, name, budget, interest):
        matches = []

        for place, info in self.destinations.items():
            if interest in info["interest"]:
                hotel_cost = info["hotel"] * 3
                travel_cost = info["travel"]
                activity_cost = 2000

                total_cost = hotel_cost + travel_cost + activity_cost

                if total_cost <= budget:
                    matches.append((place, info, total_cost))

        if not matches:
            return None

        matches.sort(key=lambda x: x[2])

        place, info, total_cost = matches[0]

        remaining = budget - total_cost

        return {
            "Name": name,
            "Destination": place,
            "Interest": interest,
            "Budget": budget,
            "Hotel Cost (3 Nights)": info["hotel"] * 3,
            "Travel Cost": info["travel"],
            "Activities Cost": 2000,
            "Total Estimated Cost": total_cost,
            "Remaining Budget": remaining,
            "Food Recommendations": info["food"],
            "Activities": info["activities"],
            "Tour Plan": [
                "Day 1 - Arrival and Local Sightseeing",
                "Day 2 - Major Attractions and Activities",
                "Day 3 - Food Exploration and Shopping",
                "Day 4 - Return Journey"
            ]
        }


planner = TravelPlanner()

name = input("Enter Your Name: ")
budget = int(input("Enter Your Budget (₹): "))
interest = input(
    "Enter Your Interest (Beach, Adventure, History, Culture, Mountain, Nature, Food): "
)

plan = planner.generate_plan(name, budget, interest)

if plan:
    print("\n========== PERSONALIZED TRAVEL PLAN ==========\n")

    for key, value in plan.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print("  -", item)
        else:
            print(f"{key}: {value}")
else:
    print("\nNo destination matches your budget and interests.")
