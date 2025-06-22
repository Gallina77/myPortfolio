class MorseCodeTranslator:
    def __init__(self):
        # Dictionary representing the morse code chart with the most common characters
        self.morse_code_dict = {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----.", "0": "-----", " ": "/",
            ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
            ":": "---..."
        }

    def encrypt(self, text):
        """Convert text to morse code"""
        upper_case_text = text.upper()
        try:
            #separates letters with spaces
            result = " ".join([self.morse_code_dict[letter] for letter in upper_case_text])
            return result
        #If Letter is not found in Morse Code Dictionary
        except KeyError as e:
            print(f"This letter is not found in the morse dictionary {str(e)}")


    #Reverse function to decode morse code back to text
    def decrypt(self, text):
        encrypted_text = []
        for word in text.split():
            matches = [k for k, v in self.morse_code_dict.items() if v == word]
            if matches:
                encrypted_text.extend(matches)
            else:
                print(f"Unknown morse code pattern: {word}")
        return "".join(encrypted_text)






