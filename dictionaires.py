import string

def word_frequency(sentence):
    translator = str.maketrans('', '', string.punctuation)
    words = sentence.translate(translator).lower().split()
    frequency = {}
    
    for word in words:
        frequency[word] = frequency.get(word, 0) +1
        
    return frequency 

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence) 
print(result)  