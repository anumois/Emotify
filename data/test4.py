import codecs
with codecs.open("anger_result.txt", encoding='utf-8') as f:
    data = [line.split('\t') for line in f.read().splitlines()]

from konlpy.tag import Twitter
twitter = Twitter()
    
frequency = {}

for line in data:
    text = line[0]
    words = twitter.nouns(text)
    for word in words:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

import operator
sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse = True)

anger_frequency = open("anger_frequency.txt", 'w', -1, "utf-8")

for t in sorted_freq:
    anger_frequency.write(t[0] + '\t' + str(t[1]) + '\n')
    
anger_frequency.close()

len(frequency)