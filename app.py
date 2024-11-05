#spet1  importing speelin corrector

from spellchecker import SpellChecker


#step2  creating an app class

class SpellCheakerApp:
    def __init__(self):
        self.spellcheaker = SpellChecker()
    
    def correct_text(self, text):
        words = text.split()
        corrected_words = []
  #STEP3  checking the spelling of the words      
        for word in words:
            corrected_word = self.spellcheaker.correction(word)
            if corrected_word != word.lower():
                print(f'"{word}" has been corrected to "{corrected_word}"')
                corrected_words.append(corrected_word)
#STEP4  joining the corrected words

        return ' '.join(corrected_words)
#step5 running the app
    def run(self):
        print('Welcome to the Spelling Corrector App!')
        
        while True:
            text = input('Enter text to check spelling (or type "exit" to quit): ')
            
            if text.lower() == 'exit':
                print('cloosing the app goodbye!')
                break
            
            corrected_text = self.correct_text(text)
            print(f'Corrected text: {corrected_text}')
               
#step6 running the main app

if __name__ == '__main__':
    SpellCheakerApp().run()
    