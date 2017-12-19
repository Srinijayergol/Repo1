import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def wordDefinition(word):
   word = word.lower()
   if word in data:
       return data[word]
   elif len(get_close_matches(word, data.keys())) > 0:
       result =  input("Did you mean %s instead? Enter Y for yes and N for no: " %get_close_matches(word, data.keys())[0])
       if result == 'Y':
           return(data[get_close_matches(word, data.keys())[0]])
       elif result == 'N':
           return "The word doesn't exist, please double check!!"
       else:
           return "No other input string accepted, enter either Y for yes or N for no."
   else:
       return "The word doesn't exist, please double check!!"

word = input("Enter the word: ")
output = wordDefinition(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
