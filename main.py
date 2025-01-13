character_counts = {}

def count_chars(word):
    # print(f"Processing word '{word}'...")
    for char in word.lower():
        if char.isalpha():
            if not char in character_counts:
                character_counts[char] = 1
            else:
                character_counts[char] += 1
    # print(f"  {character_counts}")
    return

def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count_chars(word)
        count +=1
        # if count > 10:
        #    break
    return count

def sort_value(char_count):
    return char_count["count"]

def print_report(filename, word_count):
    char_counts = []
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")

    # convert character dictionary into list of dictionaries for sorting
    for char, count in character_counts.items():
        char_counts.append({"char": char, "count": count})
    
    # sort list of dictionaries by descending count
    char_counts.sort(reverse = True, key = sort_value)
    
    # print list of character counts
    for char_count in char_counts:
        print(f"The '{char_count['char']}' character was found {char_count['count']} times")
    print("--- End report ---")
    return

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print_report(f.name, word_count)
        #print(f"Character Counts: {character_counts}")
    return

main()