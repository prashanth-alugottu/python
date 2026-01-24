import re
from collections import Counter

def analyze_text(text)-> dict:
    words = re.findall(r"[a-zA-Z]+",text.lower())
    # print(words)
    counts = Counter(words)
    # print(counts)
    top = counts.most_common(3)
    print(top)
    print(dict(top))
    # sum1 = 0
    # for w in words:
    #     print(len(w))
    #     sum1 = sum1 + len(w)
    # rr = sum1/len(words)
    # print(rr)
    
    print(sum(len(w) for w in words)/len(words))
    
text = "Hello world!How@are you doing today? today today today"
analyze_text(text)