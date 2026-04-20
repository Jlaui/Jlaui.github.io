from typing import List, Dict


def rank_animal(animal: Dict, category: str = "") -> int:
    # Computes a weighted score for a single animal based on attributes.

    score = 0  # Initalize score

    # Weighted breed score based on rescue category
    breed_scores = {
        "water": ["Labrador Retriever", "Newfoundland", "Chesapeake Bay Retriever"],
        "mountain": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog"],
        "disaster": ["Doberman Pinscher", "Golden Retriever", "German Shepherd"]
    }

    # Add five points if the animal breed matches the category
    if category in breed_scores and animal.get("breed") in breed_scores[category]:
        score += 5

    # Age scoring (in weeks)
    age = animal.get("age_upon_outcome_in_weeks", 0)
    if 104 <= age <= 156:
        score += 3

    # Traits scoring
    traits = animal.get("traits", [])
    if "calm" in traits:
        score += 2
    if "trainable" in traits:
        score += 2

    return score  # Return total weighted score


def rank_animals(animal_list: List[Dict], category: str = "") -> List[Dict]:

    # Assigns a score to each animal and returns a ranked list.

    for animal in animal_list:
        animal["score"] = rank_animal(animal, category)
    return sorted(animal_list, key=lambda x: x["score"], reverse=True)
