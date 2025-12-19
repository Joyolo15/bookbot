def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    text = text.lower() 
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def sort_char_counts(char_counts):
    # Convert {"a": 10, "b": 5} → [{"char": "a", "num": 10}, {"char": "b", "num": 5}]
    items = [{"char": c, "num": n} for c, n in char_counts.items()]

    # Helper used by .sort()
    def by_num(item):
        return item["num"]

    # Sort greatest → least
    items.sort(key=by_num, reverse=True)

    return items


