# Text to Morse Code Converter

## Introduction
The "Text to Morse Code Converter" is a Python script that takes in a 
string of text as a command line argument and outputs the corresponding 
Morse code representation. In building this script, I aimed to consolidate 
and apply the knowledge I gained from completing courses such as CS50 and 
100 Days of Code.

## Usage
To use the script, simply navigate to the directory where the script is 
located and run the following command:


`python morse_code.py '<your_text_to_convert>'`


Replace `<your_text_to_convert>` with the text you want to convert to 
Morse code. The script will output the Morse code representation of the 
input text.

## Approach
I used a variety of techniques and Python feature to build the script.
These include:

- Command line arguments: The script takes in a string of text as a command line argument.
- List comprehension: I utilized list comprehension to create a list 
containing Morse code characters from a `MORSE_CODE` dictionary that maps each alphanumeric character 
to its corresponding Morse code representation.
- Built-in string methods: I used built-in string methods like `upper()` and `strip()` to manipulate 
the input text.
- Regular expressions: To indicate to the user which characters were converted to 
Morse code, I utilized regular expressions to extract only alphanumeric characters and whitespace characters from 
the input text, while omitting any other symbols.
- Unit tests: I wrote unit tests to ensure that the script works as intended.

## Conclusion
Overall, the "Text to Morse Code Converter" is a simple but effective Python script 
that was intended to demonstrate my knowledge of a variety of Python techniques and features. 
While the project could have been done more simply, I wanted to challenge myself and use my knowledge as much as 
possible.