

from collections import Counter
import matplotlib.pyplot as plt
from itertools import count
file= open("1342-0.txt","r", encoding='utf-8')
read = file.read()
words= read.split()
w = [len(word) for line in read for word in line.rstrip().split(" ")]
sentence= read.split('.')
average_sentence = sum(len(x.split()) for x in sentence) / len(sentence)
average_word= float(sum(w))/float(len(words))
list_words= list(words)
counting= Counter(list_words)
def longest_words(list, numbers):
    counter = count()
    return sorted(list, key = lambda w : (len(w), next(counter)), reverse = True)[:numbers]
print("Number of the words is",len(words))
print("Number of Characters is", len(read))
print("The average word length is", average_word)
print("The average sentence length is",average_sentence)
print("Ten longest words:",longest_words(list_words, 10))
print("Counting the words: \n\n")
#print(counting)
from wordcloud import WordCloud
wordcloud = WordCloud(colormap='prism',
background_color='white')
frequencies= counting.most_common(200)
wordcloud = wordcloud.fit_words(dict(frequencies))
wordcloud = wordcloud.to_file('PrideAndPrejudice.png')
plt.imshow(wordcloud)


