"""NBA player-name exception mappings from raw names to clean names.

Use PLAYER_EXCEPTIONS_NBA.get(raw_name, raw_name) to retrieve a clean name
while preserving names that do not have an explicit mapping.
"""

PLAYER_EXCEPTIONS_NBA = {
    "Alexandre Sarr": "Alex Sarr",
    "Ronald Holland": "Ron Holland",
    "Cui Yongxi": "Yongxi Cui",
    "Jakob Poltl": "Jakob Poeltl",
    "Kristaps Porzi??is": "Kristaps Porzingis",
    "Cam Johnson": "Cameron Johnson",
    "Nicolas Claxton": "Nic Claxton",
    "Bub Carrington": "Carlton Carrington",
    "Cam Payne": "Cameron Payne",
    "EJ Harkless": "Elijah Harkless",
}
