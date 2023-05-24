#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, stringVal):
        if (type(stringVal) == str):
          self._value = stringVal
        else:
          print("The value must be a string.")
    
    def is_sentence(self):
        if self._value.endswith("."):
              return True
        else:
              return False
        
    def is_question(self):
        if self._value.endswith("?"):
            return True
        else:
            return False
    
    def is_exclamation(self):
        if self._value.endswith("!"):
            return True
        else:
            return False
    
    def count_sentences(self):
        no_doubles = self._value.replace("!!", ".")
        no_questions = no_doubles.replace("?", ".")
        all_periods = no_questions.replace("...", ".")
        sentences = all_periods.count(".")
        return sentences

        

      


    
    
    
