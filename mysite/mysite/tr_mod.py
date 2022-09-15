from googletrans import Translator

def translate(text="Hello", language='en'):
    trans = Translator()
    # str1=input("Enter a string: ")
    # language=input("Enter the language: ")
    out = trans.translate(text, dest=language)
    return out.text

if __name__ == "__main__":
    print(translate())
