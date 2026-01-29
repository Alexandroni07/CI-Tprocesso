from typing import List

def possibilities(word: str) -> List[str]:
    # map of morse code 
    cod_morse = {
        ".": "E",    "-": "T",
        "..": "I",   ".-": "A",   "-.": "N",   "--": "M",
        "...": "S",  "..-": "U",  ".-.": "R",  ".--": "W",
        "-..": "D",  "-.-": "K",  "--.": "G",  "---": "O"
    }
    
    # initialize to build combinations 
    pos = [""]
    
    for s in word:
        new_pos = []
        for combination in pos:
            # if the character is a wildcard, branch into both dot and dash possibilities
            if s == "?":
                new_pos.append(combination + ".")
                new_pos.append(combination + "-")
            else:
                new_pos.append(combination + s)
        pos = new_pos
    
    # translate all generated morse sequences into characters and filter
    result = [cod_morse[code] for code in pos if code in cod_morse]
    
    return result