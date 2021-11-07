sentence = input("Wpisz ciąg znaków: ")

def dec_to_bin(number):        
    bin_number = ""         
    while number > 0:
        remainder = number % 2
        number = number // 2  
        bin_number = str(remainder) + bin_number
    
    return bin_number

    
def bin_to_dec(str_bin):
    str_bin = list(str_bin)
    exponent = 0
    dec_number = 0
    for i in range(len(str_bin) - 1, -1, -1):
        bit = str_bin[i]
        bit_power = 2 ** exponent
        if bit == "1":
            dec_number = dec_number + bit_power
        exponent = exponent + 1
        
    return dec_number


def hex_to_bin(str_hex):
    hexalph = "0123456789ABCDEF"
    bin_all = ""
    for hexnum in list(str_hex):
    
        if hexnum not in hexalph:
            return print("Niewłaściwy zapis szesnastkowy.")
            
        hex_index = hexalph.find(hexnum)
        bin_part = dec_to_bin(hex_index)
        while len(bin_part) < 4:
            bin_part = "0" + bin_part
        bin_all = bin_all + " " + bin_part

    print(bin_all)
    
    
def hex_to_dec(str_hex):
    hexalph = "0123456789ABCDEF"
    
    dec_number = 0
    exponent = len(str_hex) - 1
    for hexnum in str_hex:
        if hexnum not in hexalph:
            return print("Niewłaściwy zapis szesnastkowy.")
            
        hex_index = hexalph.find(hexnum)
        dec_number = dec_number + hex_index * 16 ** exponent
        exponent = exponent - 1

    print(dec_number)
           

def find_ascii_number(sentence):
    ASCII = ["NUL", "SOH", "STX", "ETX", "EOT", "ENQ", "ACK", "BEL", "BS", "TAB", "LF", "VT", "FF", "CR", "SO", "SI", "DLE", "DC1", "DC2",
            "DC3", "DC4", "NAK", "SYN", "ETB", "CAN", "EM", "SUB", "ESC", "FS", "GS", "RS", "US", " ", "!", '"', "#", "$", "%", "&",
            "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", 
            "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
            "Y", "Z", "[", "^", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", 
            "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "DEL"]
    
    indexes = []       
    for letter in sentence:
        index = ASCII.index(letter)
        indexes.append(index)
 
    return indexes
    
    
def ascii_to_bin(list_of_numbers):
    
    binaries = ""
    for number in list_of_numbers:
        binary = dec_to_bin(number)
        difference = 8 - len(binary)
        if difference != 0:
            binary = difference * "0" + binary
            binaries = binaries + binary
  
    return binaries
    
    
def base_encoding(binaries):
    BASE64 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
             "X","Y","Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
             "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
            
    ascii_bytes = len(binaries)
    base_bytes = int(ascii_bytes / 8)
    base_rest = int(base_bytes % 3)
    
    start = 0
    end = 0
    basechain = ""
    last_complete_chunk = int((base_bytes - base_rest) / 3)
    for i in range(0, last_complete_chunk):
        if end == 0:
            end = end + 24
            start = 0
        else:
            start = end
            end = start + 24
            
        base_all = binaries[start:end]
        base_first = base_all[0:6]
        base_second = base_all[6:12]
        base_third = base_all[12:18]
        base_fourth = base_all[18:24]
        
        base_signs = [base_first, base_second, base_third, base_fourth]
        
        for sign in base_signs:
            bits_value = bin_to_dec(sign)
            base_value = BASE64[bits_value]
            basechain = basechain + base_value
            
    if base_rest != 0:
        start = end
        end = len(binaries)
        base_all = binaries[start:end]
        
        if base_rest == 1:
            base_first = base_all[0:6]
            last_signs = base_all[6:8] + "0000"
            base_signs = [base_first, last_signs]
            
            for sign in base_signs:
                bits_value = bin_to_dec(sign)
                base_value = BASE64[bits_value]
                basechain = basechain + base_value
            
            basechain = basechain + "=="
            
        else:
            base_first = base_all[0:6]
            base_second = base_all[6:12]
            last_signs = base_all[12:16] + "00"
            base_signs = [base_first, base_second, last_signs]
            
            for sign in base_signs:
                bits_value = bin_to_dec(sign)
                base_value = BASE64[bits_value]
                basechain = basechain + base_value
                
            basechain = basechain + "="
            
    return print(basechain)
                
                
indexes = find_ascii_number(sentence)
binaries = ascii_to_bin(indexes)
base_encoding(binaries)
    
        
            
        




        
        
        
