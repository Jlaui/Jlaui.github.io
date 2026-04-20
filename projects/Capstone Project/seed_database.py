from crud import AnimalShelter
import random

# Initialize the database connection
db = AnimalShelter()

# Clear existing data to prevent duplicates
db.collection.delete_many({})

# Expanded pool of first names
first_names = [
    "Bella", "Max", "Luna", "Charlie", "Rocky", "Milo", "Daisy", "Bailey",
    "Cooper", "Sadie", "Toby", "Lola", "Bear", "Duke", "Zoe", "Harley",
    "Leo", "Ruby", "Oscar", "Rosie", "Maggie", "Sophie", "Jack", "Nala",
    "Buddy", "Chloe", "Bentley", "Coco", "Murphy", "Lilly", "Teddy", "Riley",
    "Ginger", "Lucky", "Gracie", "Simba", "Scout", "Pepper", "Abby", "Shadow",
    "Jake", "Ellie", "Sam", "Luna", "Buster", "Lily", "Oscar", "Mia", "Lucky",
    "Spot", "Ranger", "Poppy", "Parker", "Paprika", "Roger", "Henry", "Blue",
    "Wiley", "Bailey", "Snoopy", "Bebee", "Daisy", "Wyatt", "Georgie", "Baxter",
    "Buster", "Charley", "Cooper", "Buddie", "Teddy", "Rocky", "Foxy", "Apollo",
    "Bandit", "Chester", "Zeus", "Nico", "Draco", "Dobby", "Duke", "Hera",
    "Mars", "Pluto", "Gus", "Gunner", "Gunmetal", "Homer", "Jasper", "Leo",
    "Allen", "Moose", "Murphie", "Ollie", "Ozzy", "Peanut", "Pepper", "Hazel",
    "Smokey", "Sparky", "Turbo", "Tank", "Hank", "Mini", "Mavis", "Tanner",
    "Bettie", "Maggie", "Maggy", "Walker", "Wolf", "Yogi", "Booboo", "Ziggie",
    "Charlie", "Marlo", "Ruby", "Brutus", "Chopper", "Pickles", "Scooby",
    "Scrappy", "Marmaduke", "Sir Waggington", "Chewbarka", "Eddie", "Superdog",
    "Tim Allen", "Bacon", "Cyprus", "Hunter", "Milo", "Norman", "Jack", "Cosmo",
    "Rocket", "Lucy", "Thyme", "Snail", "Georgia", "Bonnie", "Bubbles", "Buggy",
    "Molly", "Angel", "Penny", "Fiona", "Shrek", "Donkey", "Oreo", "Willow", "Bobo",
    "Tinker", "Roxy", "Fuzzy", "Fizzy", "Frank", "Harper", "Alex", "Justin", "Tilly",
    "Nova", "Comet", "Outlook 2016", "Lovegood", "Janus", "Honey", "Tiger", "Winnie",
    "Diva", "Spirit Airlines", "Gigi", "Lola", "Koala", "Sugar", "Period", "Jenny",
    "Bernabette", "Peter", "Perry", "Hercules", "Stu", "Stew", "Sheldon", "Shelly",
    "Rajesh", "Leonard", "Penny", "Harrison", "John", "Wildling", "Willy"
]

breeds = [
    "Labrador Retriever", "German Shepherd", "Golden Retriever",
    "Doberman Pinscher", "Newfoundland", "Alaskan Malamute",
    "Chesapeake Bay Retriever", "Old English Sheepdog",
    "Siberian Husky", "Rottweiler", "Border Collie", "Australian Shepherd"
]

traits_pool = ["calm", "trainable", "energetic", "friendly", "loyal", "alert"]

# Generate 150 animal records
animals = []

for _ in range(150):
    # Random single name
    unique_name = random.choice(first_names)

    # Random traits
    num_traits = random.randint(1, 4)
    traits = random.sample(traits_pool, num_traits)

    # Random location across the U.S.
    location_lat = round(random.uniform(24.396308, 49.384358), 5)
    location_long = round(random.uniform(-125.0, -66.93457), 5)

    animal = {
        "name": unique_name,
        "breed": random.choice(breeds),
        "age_upon_outcome_in_weeks": random.randint(5, 260),
        "traits": traits,
        "location_lat": location_lat,
        "location_long": location_long
    }

    animals.append(animal)

# Insert into MongoDB
db.collection.insert_many(animals)
