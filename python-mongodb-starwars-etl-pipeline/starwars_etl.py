import requests
from pymongo import MongoClient

# Connect to the local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select the starwars database
db = client["starwars"]

# Access the existing characters collection
characters_collection = db["characters"]

# Send a GET request to the SWAPI starships endpoint
response = requests.get("https://swapi.dev/api/starships/")

# Print the HTTP status code to confirm the API request was successful
# print(f"API response status code: {response.status_code}")

# Convert the JSON response into a Python dictionary
data = response.json()

# Print the full SWAPI response dictionary
# print(data)

# Print the number of starships returned on the first API page
# print(len(data["results"]))

# Get all starships from every SWAPI page
def get_all_starships():
    url = "https://swapi.dev/api/starships/"
    all_starships = []

    while url:
        response = requests.get(url)
        data = response.json()

        # Add the starships from the current page to the list
        all_starships.extend(data["results"])

        # Move to the next page. When there is no next page, this becomes None
        url = data["next"]

    return all_starships

# Call the function and store all starships in a list
starships = get_all_starships()

# Check that all 36 starships were retrieved
# print(f"Total starships retrieved: {len(starships)}")

# Test whether a character can be found in MongoDB using the pilot's SWAPI URL
pilot_url = "https://swapi.dev/api/people/13/"

# Search the characters collection for a matching URL
pilot = characters_collection.find_one({"url": pilot_url})

# Print the result of the lookup
#print(pilot)

# Test that a character can be found in MongoDB by name
pilot = characters_collection.find_one({"name": "Chewbacca"})

# Print the matching character document
# print(pilot)

# Get the MongoDB ObjectId for a pilot using their SWAPI URL
def get_pilot_object_id(pilot_url):
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()

    pilot_name = pilot_data["name"]

    pilot = characters_collection.find_one({"name": pilot_name})

    return pilot["_id"]


# Test that a pilot SWAPI URL returns the matching MongoDB ObjectId
# print(get_pilot_object_id("https://swapi.dev/api/people/13/"))

# Replace every pilot URL with the matching MongoDB ObjectId
def replace_pilot_urls(starships):
    for starship in starships:
        pilot_object_ids = []

        for pilot_url in starship["pilots"]:
            pilot_object_ids.append(get_pilot_object_id(pilot_url))

        starship["pilots"] = pilot_object_ids

    return starships


# Replace pilot URLs in all starship documents
starships = replace_pilot_urls(starships)

# Test that pilot URLs were replaced with MongoDB ObjectIds
#print(starships[4]["pilots"])

# Reference the starships collection
starships_collection = db["starships"]

# Remove any existing starship documents before inserting the new data
starships_collection.delete_many({})

# Insert all transformed starship documents
result = starships_collection.insert_many(starships)

# Confirm how many starships were inserted
print(f"Starships inserted: {len(result.inserted_ids)}")
