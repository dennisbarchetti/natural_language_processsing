import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
#nltk.download('punkt')
#nltk.download("stopwords")
from nltk.corpus import stopwords

# Press Maiusc+F10 to execute

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    example_string = """
    ... Muad'Dib learned rapidly because his first training was in how to learn.
    ... And the first lesson of all was the basic trust that he could learn.
    ... It's shocking to find how many people do not believe they can learn,
    ... and how many more believe learning to be difficult."""
    sent_tokenize(example_string) #split up example_string into sentences
    word_tokenize(example_string)

    """
    Filtering Stop Words:
    
    Stop words are words that you want to ignore, so you filter them out of your text when you’re processing it. 
    Very common words like 'in', 'is', and 'an' are often used as stop words since they don’t add a lot of meaning to a 
    text in and of themselves.
    
    """
    worf_quote = "Sir, I protest. I am not a merry man!"
    words_in_quote = word_tokenize(worf_quote)
    print("words_in_quote: ",words_in_quote)
    stop_words = set(stopwords.words("english"))
    print("stop_words: ",stop_words)
    filtered_list = []
    for word in words_in_quote:
        if word.casefold() not in stop_words:
            filtered_list.append(word)

    """
    Alternatively, you could use a list comprehension to make a list of all the words in your text that aren’t stop words:
    
    filtered_list = [word
    for word in words_in_quote if word.casefold() not in stop_words]
    
    """
    print("filtered_list: ",filtered_list)
    prova git



