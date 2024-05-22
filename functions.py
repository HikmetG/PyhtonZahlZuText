def onesDigit(number: str,lengthOfNumber: int):
    """Finds the number in the ones digit of the given input.

    Args:
        number (str): Number to find the ones digit
        lengthOfNumber (int): Length of the number

    Returns:
        str: Number one to nine in text form
    """
    onesDigitOfNumber = number[lengthOfNumber - 1]
    if(lengthOfNumber == 2 and onesDigitOfNumber == "0"):
        return ""
    elif(onesDigitOfNumber == "1"):
        if(lengthOfNumber == 2):
            return "ein"
        return "eins"
    elif(onesDigitOfNumber == "2"):
        return "zwei"
    elif(onesDigitOfNumber == "3"):
        return "drei"
    elif(onesDigitOfNumber == "4"):
        return "vier"
    elif(onesDigitOfNumber == "5"):
        return "fünf"
    elif(onesDigitOfNumber == "6"):
        return "sechs"
    elif(onesDigitOfNumber == "7"):
        return "sieben"
    elif(onesDigitOfNumber == "8"):
        return "acht"
    elif(onesDigitOfNumber == "9"):
        return  "neun"
   
    
    return "null"

def tensDigit(number: str,lengthOfNumber: int):
    """Finds the number in the tens digit of the given input.

    Args:
        number (str): Number to find the tens digit
        lengthOfNumber (int): Length of the number

    Raises:
        ValueError: If the tens digit of the number is 0. e.g. "00 , 02 , 06"

    Returns:
        str: Number ten to ninety in text form
    """
    
    tensDigitOfNumber = number[lengthOfNumber - 2]

    if(tensDigitOfNumber == "0"):
        raise ValueError('Ungültige Eingabe: Bitte ohne führenden Null')
    elif(tensDigitOfNumber == "1"):
        return "zehn"
    elif(tensDigitOfNumber == "2"):
        return "zwanzig"
    elif(tensDigitOfNumber == "3"):
        return "dreissig"
    elif(tensDigitOfNumber == "6"):
        return "sechzig"
    elif(tensDigitOfNumber == "7"):
        return "siebzig"
    else:
        return onesDigit(tensDigitOfNumber, len(str(tensDigitOfNumber))) + "zig"

    
def turnNumberToText(number:str):
    """Function to convert the number

    Args:
        number (str): Number to be converted into written form

    Returns:
        str: Converted text
    """

    lengthOfNumber = len(str(number))

    if(lengthOfNumber == 1):
        return onesDigit(number, lengthOfNumber)
    elif(lengthOfNumber == 2):
        TensDigit = tensDigit(number,lengthOfNumber) 
        if(TensDigit == "zehn"):
            if(number == "11"):
                return "elf"
            elif(number == "12"):
                return "zwölf"
            elif(number == "16"):
                return "sechzehn"
            elif(number == "17"):  
                return "siebzehn"
            else:
                return onesDigit(number, lengthOfNumber) + tensDigit(number,lengthOfNumber)
        else:
            return onesDigit(number, lengthOfNumber) + ("und" if onesDigit(number, lengthOfNumber) != "" else "") + tensDigit(number,lengthOfNumber)