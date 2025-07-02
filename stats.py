def get_num_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    # Only keep alphabetic characters (including special letters if needed)
    filtered_counts = {k: v for k, v in char_counts.items() if k.isalpha()}
    sorted_counts = sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts
