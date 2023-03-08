import sys
import re

MORSE_CODE = {
    "A": "•—", "B": "—•••", "C": "—•—•", "D": "—••", "E": "•", "F": "••—•", "G": "——•", "H": "••••", "I": "••",
    "J": "•———", "K": "—•—", "L": "•—••", "M": "——", "N": "—•", "O": "———", "P": "•——•", "Q": "——•—", "R": "•—•",
    "S": "•••", "T": "—", "U": "••—", "V": "•••—", "W": "•——", "X": "—••—", "Y": '—•——', "Z": '——••',
    "1": "•————", "2": "••———", "3": "•••——", "4": "••••—", "5": "•••••", "6": "—••••", "7": "——•••", "8": "———••",
    "9": "————•", "0": "—————", " ": "/"
}


def text_to_morse(text: str, sep: str = " ") -> str:
    """
    Converts the input text to Morse code.
    Args:
        text (str): The text to convert to Morse code.
        sep (str, optional): The symbol used to separate Morse code symbols. Default is a space.
    Returns:
        str: The Morse code representation of the input text, where each Morse symbol is separated by
        the specified separator symbol and words are separated by '/' symbol.
    """
    text = text.strip().upper()
    coded_message = [MORSE_CODE[character] for character in text if character.isalnum() or character.isspace()]
    return sep.join(coded_message)


def main():
    # Check if user provided two required command-line arguments
    if len(sys.argv) == 2:
        plain_text = "".join(re.split(r"[^a-zA-Z0-9\s]*", sys.argv[1]))
        print(f"Plain text: {plain_text}\nMorse code: {text_to_morse(sys.argv[1])}")
    else:
        print("Error: Invalid usage.")
        print("Please provide the required arguments in the correct format when running the script.")
        print("Usage: python morse_code.py '<your_text_to_convert>'")
        sys.exit(1)


if __name__ == "__main__":
    main()
