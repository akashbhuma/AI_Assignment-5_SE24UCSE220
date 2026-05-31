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

    def generate_plan(self, name, budget, interest, days):
        matches = []
        for place, info in self.destinations.items():
            if interest in info["interest"]:

                hotel_cost = info["hotel"] * days
                travel_cost = info["travel"]
                activity_cost = days * 500

                total_cost = hotel_cost + travel_cost + activity_cost

                if total_cost <= budget:
                    matches.append((place, info, total_cost))

        if not matches:
            return None

        matches.sort(key=lambda x: x[2])

        place, info, total_cost = matches[0]

        remaining = budget - total_cost

        itinerary = []

        for day in range(1, days + 1):
            if day == 1:
                itinerary.append(f"Day {day} - Arrival and Local Sightseeing")
            elif day == days:
                itinerary.append(f"Day {day} - Shopping and Return Journey")
            else:
                activity = info["activities"][(day - 2) % len(info["activities"])]
                itinerary.append(f"Day {day} - {activity}")

        return {
            "Name": name,
            "Destination": place,
            "Interest": interest,
            "Trip Duration": f"{days} Days",
            "Budget": budget,
            "Hotel Cost": hotel_cost,
            "Travel Cost": travel_cost,
            "Activities Cost": activity_cost,
            "Total Estimated Cost": total_cost,
            "Remaining Budget": remaining,
            "Food Recommendations": info["food"],
            "Activities": info["activities"],
            "Tour Plan": itinerary
        }


planner = TravelPlanner()

name = input("Enter Your Name: ")
budget = int(input("Enter Your Budget (₹): "))
interest = input(
    "Enter Your Interest (Beach, Adventure, Culture, Food, Mountain, Nature, Spiritual): "
)
days = int(input("Enter Number of Days: "))

plan = planner.generate_plan(name, budget, interest, days)

if plan:
    print("\nPERSONALIZED TRAVEL PLAN:\n")

    for key, value in plan.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print("  -", item)
        else:
            print(f"{key}: {value}")

    print("\nAI Suggestions")


    interest_lower = interest.lower()

    if interest_lower == "adventure":
        print("- Carry safety equipment and comfortable trekking shoes")

    if interest_lower == "nature":
        print("- Carry a camera and suitable outdoor clothing")

    if interest_lower == "beach":
        print("- Carry sunscreen, sunglasses and light clothing")

    if interest_lower == "spiritual":
        print("- Visit major temples and attend local cultural events")

    if budget < 15000:
        print("- Consider public transport and budget hotels to reduce expenses")

    if budget > 30000:
        print("- Premium hotels and additional activities can be included")

    if plan["Destination"] == "Hyderabad":
        print("- Try Hyderabadi Biryani and visit Charminar in the evening")

    if plan["Destination"] == "Chennai":
        print("- Best time to visit Marina Beach is early morning")

    if plan["Destination"] == "Varanasi":
        print("- Do not miss the Ganga Aarti at Dashashwamedh Ghat")

    if plan["Destination"] == "Shimla":
        print("- Carry warm clothes, especially during winter")

    if plan["Destination"] == "Munnar":
        print("- Visit tea gardens during daylight hours for the best experience")

    if plan["Destination"] == "Kochi":
        print("- Take a backwater cruise and try local seafood")

    print("\nThank you for using AI Travel Planner!")
else:
    print("\nNo destination matches your budget and interests.")
