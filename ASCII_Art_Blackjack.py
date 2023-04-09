# ASCII ART 1: Function with for loop to print each line/index of the list

def blackjack_ascii():
    """An ascii art function that uses a for loop to print each line of the ascii art"""
    ascii = [       
    "       Camille's Blackjack Game (Cams-Plan @GitHub)",
    ".------.            _     _            _    _            _",
    "|A_  _ |.          | |   | |          | |  (_)          | |",
    "|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __",
    "| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /",
    "|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <",
    "`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ " ,
    "      |  \/ K|                            _/ |",
    "      `------'                           |__/ "
    ]
    for line in ascii:
        print(line)

# ASCII ART 2: Triple Quotes/Docstring

blackjack_ascii = """
       Camille's Blackjack Game (Cams-Plan @GitHub)
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |
      `------'                           |__/ 
"""
