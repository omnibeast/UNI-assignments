"""
Programer: Saurav Pokharel
Date: 10/08/2024
Description: Translates English word to Pirate. 
"""


english_pirate_dict = {"hello":"ahoy", "to":"ta", "was":"be", "cheat":"hornswaggle", "cheating":"hornswaggle'n",
"toilet":"head", "hi":"yo-ho-ho", "man":"matey","pardon":"avast", "excuse":"arrrgh", "yes":"aye", "my":"me", 
"friend":"matey", "sir":"matey", "miss":"comely wench", "stranger":"scurvy dog", "officer":"foul blaggart", 
"where":"whar", "is":"be", "for":"fer", "are":"be", "am":"be", "the":"th", "going":"goin", "you":"ye", 
"your":"yer", "tell":"be tellin", "know":"be knowin", "far":"many leagues", "old":"barnacle-covered", 
"attractive":"comely", "happy":"grog-filled", "quickly":"smartly", "nearby":"broadside", "restroom":"head", 
"restaurant":"galley", "hotel":"fleabag inn", "bar":"Skull & Scuppers", "mall":"market", "bank":"buried treasure", 
"die":"visit Davey Jones Locker", "died":"visited Davey Jones Locker", "kill":"keel-haul", "killed":"keel-hauled", 
"sleep":"take a caulk", "stupid":"addled", "after":"aft", "stop":"belay", "nonsense":"bilge", "ocean":"briny deep", 
"go":"get ye", "song":"shanty", "money":"doubloons", "drunk":"three sheets to the wind", "food":"grub", "nose":"prow", 
"leave":"weigh anchor", "cheat":"hornswaggle", "forward":"fore", "child":"sprog", "children":"sprogs", "sailor":"swab", 
"lean":"careen", "find":"come across", "mother":"dear ol mum, bless her black soul", 
"mom":"dear ol mum, bless her black soul", "drink":"barrel o rum", "of":"o", "there":"thar", "my":"me", "mine":"me", 
"gun":"cannon", "monkey":"tailed imp", "expert":"old smartly", "flag":"Jolly Roger", "dad":"capn", "teacher":"wise sage", 
"phone":"cursed device", "computer":"magic box", "speak":"parley", "person":"landlubber", "people":"landlubbers", 
"sir":"matey", "hotel":"fleabag", "student":"swabbie", "boy":"matey", "professor":"foul blaggart", "restaurant":"galley", 
"students":"swabbies", "bathroom":"head"}

#header
print("""
______ _           _         _____                   _       _             
| ___ (_)         | |       |_   _|                 | |     | |            
| |_/ /_ _ __ __ _| |_ ___    | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
|  __/| | '__/ _` | __/ _ \   | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
| |   | | | | (_| | ||  __/   | | | | (_| | | | \__ \ | (_| | || (_) | |   
\_|   |_|_|  \__,_|\__\___|   \_/_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   
                                                                           
                                                                           
""")

#translateWord: translates a single word from english to pirate
def translateWord(word):
    word = word.lower()
    if word in english_pirate_dict:
        return english_pirate_dict[word]
    else:
        return word
    


#transalteSentence: take a english sentence and translate to pirate.
def transalteSentence(sentence):
    pirateSentence = ""
    words = sentence.split()
    for i in words:
        i = translateWord(i)
        pirateSentence += i + ""

    return pirateSentence[0].upper() + pirateSentence[1: ]

sentence = ""
while sentence.lower() != "q" and sentence.lower() != "quit":
    sentence = input("Enter your words, or (Q)uit: ")
    print(transalteSentence(sentence))