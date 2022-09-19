"""Given an input text, Code a program (in python) that displays the number of
repetitions of each word.
Sample text: "Hi how are things? How are you? Are you a developer? I am also a
developer"
Plus: Implement a test to the task performed
(Preferably with UnitTest or Pytest).
"""


def words_counter(text):
    """The Function counts the number of times each word appears in a text.

    Parameters:
            - text: It is a string of characters.
    Returns:
        A dictionary with word:frequency pairs with the words contained in the text and their frequency.
    """
    filter_words = ",;.:/?!-"
    text = text.upper()
    for x in filter_words:
        text = text.replace(x, "")
    text = text.split()

    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


if __name__ == "__main__":
    text_in = (
        "Hi how are things? How are you? Are you a developer? I am also a developer"
    )
    print(f"Cantidad de palabras: {words_counter(text_in)}")
