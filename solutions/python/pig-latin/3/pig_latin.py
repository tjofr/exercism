"""
Module to provide functions of translation to pig latin
Your parents have challenged you and your sibling to a game
of two-on-two basketball. Confident they'll win, they let you score 
the first couple of points, but then start taking over the game. 
Needing a little boost, you start speaking in Pig Latin, which is a 
made-up children's language that's difficult for non-children to 
understand.
This will give you the edge to prevail over your parents!
"""

VOWELS=('a','e','i','o','u')
RULE1_INIT=('xr','yt')
def first_vowel(text):
    """
    :param text: str - word to analyze
    :return: index - first vowel index
    """
    index=0
    while index < len(text) and text[index] not in VOWELS:
        index += 1
    return index

def first_y(text):
    """
    :param text: str - word to analyze
    :return: index - first not beginning y index
    """
    index=1
    while index < len(text) and text[index] != 'y':
        index += 1
    return index
    

def translate_word(word):
    """
    :param word: str - word to translate
    :return: str - translated text
    """
    output=''
    if len(word) == 0 :
        return None

    index_first_vowel=first_vowel(word)
    index_first_y=first_y(word)
    #
    #RULE1
    #If a word begins with a vowel, or starts with "xr" or "yt", 
    #add an "ay" sound to the end of the word.
    #For example:
    #"apple" -> "appleay" (starts with vowel)
    #"xray" -> "xrayay" (starts with "xr")
    #"yttria" -> "yttriaay" (starts with "yt")
    #
    if index_first_vowel == 0 or word[0:2] in RULE1_INIT:
        output = word

    elif index_first_vowel >= 1:
        if word[index_first_vowel-1:index_first_vowel+1] == 'qu':
            #
            # RULE3
            #If a word starts with zero or more consonants followed by "qu", 
            #first move those consonants (if any) and the "qu" part to the end of 
            #the word, and then add an "ay" sound to the end of the word.
            #For example:
            #"quick" -> "ickqu" -> "ickquay" (starts with "qu", no preceding consonants)
            #"square" -> "aresqu" -> "aresquay" (starts with one consonant followed by "qu")
            if len(word) > 2:
                output=word[index_first_vowel+1:] + word[0:index_first_vowel+1]
            else:
                output='qu'
        elif index_first_y < index_first_vowel <= len(word):
            #
            #RULE 4
            #If a word starts with one or more consonants followed by "y", first move the consonants 
            #preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.
            #Some examples:
            #"my" -> "ym" -> "ymay" (starts with single consonant followed by "y")
            #"rhythm" -> "ythmrh" -> "ythmrhay" (starts with multiple consonants followed by "y")

            output=word[index_first_y:] + word[0:index_first_y]
        else:
            #
            #RULE2
            #If a word begins with one or more consonants, first move those consonants to the 
            #end of the word and then add an "ay" sound to the end of the word.
            #For example:
            #"pig" -> "igp" -> "igpay" (starts with single consonant)
            #"chair" -> "airch" -> "airchay" (starts with multiple consonants)
            #"thrush" -> "ushthr" -> "ushthray" (starts with multiple consonants)
            output=word[index_first_vowel:]+word[0:index_first_vowel]
    return output+'ay'

def translate(text):
    """
    :param text: str - text to translate
    :return: str - translated text
    """  

    return   ' '.join(translate_word(word) for word in text.split())