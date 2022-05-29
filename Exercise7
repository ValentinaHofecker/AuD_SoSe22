import nltk
from nltk.corpus import wordnet
from nltk.corpus import names
import random
 
#nltk.download()
#nltk.download('wordnet')
#nltk.download('names')
 
def generate_names(char, num): 
    
    # get names starting with given char parameter
    female_names = list(filter(lambda name: name.startswith(char), names.words('female.txt')))
    male_names = list(filter(lambda name: name.startswith(char), names.words('male.txt')))
    
    # shuffle the order of names
    random.shuffle(female_names)
    random.shuffle(male_names)
 
    # slice length of names to be equal to given num parameter
    sliced_female_names = female_names[0:num]
    sliced_male_names = male_names[0:num]
    
    # write names to seperate files (exercise 2)
    with open('female_names.txt', 'w') as writer:
        for line in sliced_female_names:
            writer.write(line + '\n')
    with open('male_names.txt', 'w') as writer:
        for line in sliced_male_names:
            writer.write(line + '\n')
 
    # print male and female names with amount equal to 
    print([(name, 'female') for name in sliced_female_names])
    print([(name, 'male') for name in sliced_male_names])
 
generate_names('A', 3)
 
 
class SynAnt:
    
    def __init__(self, words):
        # data structure in form of list of dictionaries, to store synonyms/antonyms for every word
        self.word_dicts = []
        
        # initialize synonyms and antonyms for every word, using synsets (nltk)
        for word in words:
            synonyms = []
            antonyms = []
            syns = wordnet.synsets(word)
            for syn in syns:
                for l in syn.lemmas():
                    synonyms.append(l.name())
                    if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
            
            # set default output if no synonyms/antonyms found, to avoid reading empty lists
            if len(synonyms) == 0:
                synonyms.append("No synonyms found")
            if len(antonyms) == 0:
                antonyms.append("No antonyms found")
            
            # create a dictionary entry with the synonyms/antonyms found for every word
            self.word_dicts.append({ 'word' : word, 'synonyms' : set(synonyms), 'antonyms' : set(antonyms) })
        
 
    def find_synonyms(self):
        print('Getting Synonyms...')
        for word_dict in self.word_dicts:
            print("Word: {} | Synonyms: {}".format(word_dict['word'], word_dict['synonyms']))
            
    def find_antonyms(self):
        print('Getting Antonyms...')
        for word_dict in self.word_dicts:
            print("Word: {} | Antonyms: {}".format(word_dict['word'], word_dict['antonyms']))
 
 
words_list = [ 'love', 'dark', 'fun' , 'free' ]
syns_and_ants = SynAnt(words_list)
syns_and_ants.find_synonyms()
syns_and_ants.find_antonyms()
