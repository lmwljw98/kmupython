f = open("Les_Miserables-Victor_Hugo.txt","r")

wordList = f.read().split()

wordCount = {}

for w in wordList:
    
    w = w.upper()
    w = w.replace(".","")
    w = w.replace("?","")
    w = w.replace("\'","")
    w = w.replace("\"","")
    
    if w not in wordCount:
        wordCount[w] = 1

    else:
        wordCount[w] += 1
    
# wordCount[w] = wordCount.get(w,0) + 1

f.close()

for w in sorted(wordCount, key=wordCount.get, reverse=True):
    print(w, wordCount[w])
