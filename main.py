def read_from_file(path: str):
    """Reads a file with the given parameter path and returns the file as a list of strings, split on newline (\n).

    Args:
        path (str): the path of the readable file

    Returns:
        list(str): list of strings
    """
    with open(path, "r" ,encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]  

def count_words(text: list):
    """Counts the total number of words in a list of strings.

    Args:
        text (list): list of strings

    Returns:
        int: total number of words
    """
    word_count = 0
    for line in text:
        words = line.split()  
        word_count += len(words)
    return word_count

def main():
    sentences = read_from_file("en_resa_genom_svenska_skogen.txt")  
    total_words = count_words(sentences)  
    print(f"Antal ord: {total_words}")

if __name__ == "__main__":
    main()
