from googletrans import Translator
import sys

def translate_text(text, dest_lang='en'):
    """
    Translate text to the specified language.
    
    Args:
        text (str): Text to translate
        dest_lang (str): Destination language code (e.g., 'en' for English, 'es' for Spanish)
    
    Returns:
        str: Translated text
    """
    try:
        translator = Translator()
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error occurred: {str(e)}"

def main():
    print("Language Translator")
    print("------------------")
    
    while True:
        print("\nOptions:")
        print("1. Translate text")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            text = input("\nEnter text to translate: ")
            print("\nCommon language codes:")
            print("en - English")
            print("es - Spanish")
            print("fr - French")
            print("de - German")
            print("it - Italian")
            print("pt - Portuguese")
            print("ru - Russian")
            print("ja - Japanese")
            print("ko - Korean")
            print("zh-cn - Chinese (Simplified)")
            
            dest_lang = input("\nEnter destination language code: ")
            translated_text = translate_text(text, dest_lang)
            print(f"\nTranslated text: {translated_text}")
        
        elif choice == '2':
            print("\nGoodbye!")
            sys.exit(0)
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 