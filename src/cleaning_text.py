from string import punctuation
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords = ENGLISH_STOP_WORDS

# def lowercase_text(text):
#     return text.lower() # lower case all text

# def remove_punctuation(text):
#     return ''.join([ch for ch in text if ch not in punctuation]) 

# def remove_newline(text):
#     new_line = text.replace('\n', ' ') 
#     return new_line

# def text_to_words_lst(text):
#     return text.split(' ') # as function name refers to

# def words_lst_to_text(words_lst):
#     return ' '.join([word for word in words_lst if word != '']) # 

# def remove_stopwords(text):
#     word_lst = text_to_words_lst(text) #call above function to do the works
#     word_lst_no_sw = [word for word in word_lst if word not in stopwords] # take a words list and remove stopwords
#     text = words_lst_to_text(word_lst_no_sw) #call above function to do the works
#     return text
# def replace_names(word_lst, name_set, replacement_val):
#     return word_lst

def remove_punctuation(text):
    return ''.join([ch for ch in text if ch not in punctuation])    #remove punctuations using punctuation list

def remove_stopwords(text):
    text = text.lower()                                             #lower case all text
    text = remove_punctuation(text)
    text = text.replace('\n', ' ')                                  #replace new line with a space ' '
    word_lst = text.split()                                         #split words into list
    word_lst = [word for word in word_lst if word not in stopwords] #remove stopwords using stopwords list
    text = ' '.join([word for word in word_lst if word != ''])      #join back the list to one text
    return text

if __name__ == '__main__':
    str = 'i GO tO the movie\nand I love it'
    print(str)
    print(remove_stopwords(str))

