from typing import Any

def get_num_words(content: str) -> int:
    return len(content.split())

def get_num_characters(content: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for c in content.lower():
        if c in counts.keys():
            counts[c] = counts[c] + 1
        else:
            counts[c] = 1
    return counts

def generate_report(counts: dict[str, int]) -> list[dict[str, Any]]:
    characters: list[dict[str, Any]] = []
    for character in counts.keys():
        character_map: dict[str, Any] = {}
        character_map["character"] = character
        character_map["number"] = counts.get(character)
        characters.append(character_map)
    characters.sort(reverse=True, key=sort_on)
    return characters

def sort_on(characters: dict[str, Any]) -> int:
    return characters["number"]
