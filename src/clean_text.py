from string import punctuation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS

def remove_punctuation(text):
    return ''.join([ch for ch in text if ch not in punctuation])    #remove punctuations using punctuation list

def remove_stopwords(text):
    text = text.lower()                                             #lower case all text
    text = text.replace('\n', ' ')                                  #replace new line with a space ' '
    word_lst = text.split()                                         #split words into list
    word_lst = [word for word in word_lst if word not in stopwords] #remove stopwords using stopwords list
    text = ' '.join([word for word in word_lst if word != ''])      #join back the list to one text
    return text

if __name__ == '__main__':
    str = "about me:  i would love to think that i was some some kind of intellectual: either the dumbest smart guy, or the smartest dumb guy. can't say i can tell the difference. i love to talk about ideas and concepts. i forge odd metaphors instead of reciting cliches. like the simularities between a friend of mine's house and an underwater salt mine. my favorite word is salt by the way (weird choice i know). to me most things in life are better as metaphors. i seek to make myself a little better everyday, in some productively lazy way. got tired of tying my shoes. considered hiring a five year old, but would probably have to tie both of our shoes... decided to only wear leather shoes dress shoes.  about you:  you love to have really serious, really deep conversations about really silly stuff. you have to be willing to snap me out of a light hearted rant with a kiss. you don't have to be funny, but you have to be able to make me laugh. you should be able to bend spoons with your mind, and telepathically make me smile while i am still at work. you should love life, and be cool with just letting the wind blow. extra points for reading all this and guessing my favorite video game (no hints given yet). and lastly you have a good attention span."
    # print(str)
    print(remove_stopwords(str))