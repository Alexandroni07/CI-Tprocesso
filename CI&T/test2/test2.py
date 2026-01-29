def seven_segmentify(time_: str) -> str:
  
    numbers = {
        '0': (" _ ", "| |","|_|"),
        '1': ("   ", "  |","  |"),
        '2': (" _ ", " _|","|_ "),
        '3': (" _ ", " _|"," _|"),
        '4': ("   ", "|_|", "  |"),
        '5': (" _ ", "|_ ", " _|"),
        '6': (" _ ", "|_ ", "|_|"),
        '7': (" _ ", "  |", "  |"),
        '8': (" _ ", "|_|", "|_|"),
        '9': (" _ ", "|_|", " _|"),
        ':': ("   ", " . ", " . "),
        ' ': ("   ", "   ", "   ")
      }
    
    # zero logic at the beginning
    display_chars = list(time_)
    if display_chars[0] == '0':
        display_chars[0] = ' '
    
    output_lines = ["","",""]
    
    # construction of the hour
    for char in display_chars: 
      cr = numbers[char]
      for i in range(3):
        output_lines[i] += cr[i]
    
    return "\n".join(output_lines)