"""Utilities for standardizing player names."""

import math
import re


# Keep this mapping in the same order as the original Excel LAMBDA.
_REPLACEMENTS = {
    ",": "",
    ".": "",
    "-": " ",
    "'": "",
    "’": "",
    "\u0081": "",
    "Á": "A",
    "Ã­": "i",
    "Ã¡": "a",
    "Ã±": "n",
    "Ã©": "e",
    "Ã¶": "o",
    "Ã‰": "e",
    "Ã³": "o",
    "Ãº": "u",
    "é": "e",
    "í": "i",
    "ñ": "n",
    "ó": "o",
    "ö": "o",
    "Ş": "S",
    "ú": "u",
    "ü": "u",
    "Ć": "C",
    "Č": "C",
    "Ô": "O",
    "Ç": "C",
    "È": "E",
    "Š": "S",
    "Ž": "Z",
    "ć": "c",
    "ç": "c",
    "è": "e",
    "ô": "o",
    "š": "s",
    "ž": "z",
    "č": "c",
    "ū": "u",
    "Ä": "A",
    "Å": "A",
    "Œ": "OE",
    "œ": "OE",
    "Đ": "D",
    "á": "a",
    "Ó": "O",
    "A\u008d": "O",
    "Ã": "A",
    "Ã¤": "a",
}

_SUFFIX_PATTERN = re.compile(r"\s+(JR|SR|III|II|IV|V)$", re.IGNORECASE)


def clean_player_name(name):
    """Clean a player name using the rules from the Excel LAMBDA.

    Missing values (None, NaN, and pandas.NA) are returned unchanged.
    Non-missing values must be strings.
    """
    if name is None or type(name).__name__ == "NAType":
        return name

    if isinstance(name, float) and math.isnan(name):
        return name

    if not isinstance(name, str):
        raise TypeError("Player name must be a string or a missing value")

    cleaned = name
    for find_text, replace_text in _REPLACEMENTS.items():
        cleaned = cleaned.replace(find_text, replace_text)

    cleaned = re.sub(r" +", " ", cleaned).strip()
    cleaned = _SUFFIX_PATTERN.sub("", cleaned)
    return cleaned.strip()
