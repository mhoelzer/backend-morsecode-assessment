#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morse code decoder

When transmitting the Morse code, the international standard specifies that:

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
However, the standard does not specify how long that "time unit" is. 
And in fact different 
operators would transmit at different speed. An amateur person may need a few seconds to 
transmit a single character, a skilled professional can transmit 60 words per minute, 
and robotic transmitters may go way faster.

OK FOR REAL??  60 WPM??
https://morsecode.scphillips.com/translator.html

For this kata we assume the message receiving is performed automatically by the hardware 
that checks the line periodically, and if the line is connected (the key at the remote 
station is down), 1 is recorded, and if the line is not connected (remote key is up), 
0 is recorded. After the message is fully received, it gets to you for decoding as a 
string containing only symbols 0 and 1.

"""
import re

# This dictionary is supplied within the Codewars test suite.
MORSE_CODE = {
    '.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '...---...': 'SOS', '-...': 'B',
    '-..-': 'X', '.-.': 'R', '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
    '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?', '.----': '1', '-.-': 'K',
    '-..': 'D', '-....': '6', '-...-': '=', '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M',
    '-.': 'N', '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
    '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G', '--.-': 'Q',
    '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':', '-.--': 'Y', '-': 'T',
    '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0', '----.': '9', '.-..-.': '"',
    '-.--.': '(', '---..': '8', '...--': '3'
}


def find_mult(bits):
    """Finds least amount of occurrences of 0 or 1"""
    raise NotImplementedError("Please implement this")


def decodeBits(bits):
    """Translate a string of 1's & 0's to dots and dashes"""
    # for the trailing/extra zeros
    bits = bits.strip("0")
    # for no 0s/min() arg of min_zeros is empty
    if "0" not in bits:
        return "."
    # split on 1 and 0 to see te stuff
    ones_bits = bits.split("0")
    zeros_bits = bits.split("1")
    # get len and find min to have that be mlitplier to multiply the 1 and 0 by to get the stuff
    min_ones = min([len(ones) for ones in ones_bits if ones])
    # ^^^ the if is needed b/c "" is also in the ones/zeros_bits
    min_zeros = min([len(zeros) for zeros in zeros_bits if zeros])
    minny = min(min_ones, min_zeros)  # b/c they might be diff mins
    return bits.replace("0000000" * minny, "   ").replace("111" * minny, "-").replace("000" * minny, " ").replace("1" * minny, ".").replace("0" * minny, "")


def decodeMorse(morse_code):
    """Translates a string of dots and dashes to human readable text"""
    unmorsed = ""
    for word in morse_code.split("   "):
        for letter in word.split():
            unmorsed += MORSE_CODE[letter]
        unmorsed += " "
    print(unmorsed.strip())
    return unmorsed.strip()
