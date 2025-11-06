animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]


def count_animals(txt):

    from collections import Counter

    def backtrack(remaining_chars, animal_idx):

        if animal_idx >= len(animals):
            return 0

        max_count = backtrack(remaining_chars, animal_idx + 1)

        animal = animals[animal_idx]
        animal_chars = Counter(animal)

        times = float('inf')
        for char, count in animal_chars.items():
            if char in remaining_chars:
                times = min(times, remaining_chars[char] // count)
            else:
                times = 0
                break

        for use_times in range(1, times + 1):
            new_remaining = remaining_chars.copy()
            for char, count in animal_chars.items():
                new_remaining[char] -= count * use_times

            count_with_this = use_times + backtrack(new_remaining, animal_idx + 1)
            max_count = max(max_count, count_with_this)

        return max_count

    char_counter = Counter(txt.lower())
    return backtrack(char_counter, 0)

print(count_animals("cockdogwdufrbir"))