def s_char_change(thing) :
    
    thing = thing.upper()
        
    special_char = [".", "?", "!", "-", "/", ",", ":", ";", '"', "(",
                    ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in special_char :
        thing = thing.replace(i, " ")

    return thing

def word_count(w_list) :
    
    for w in w_list:
     
        if w[0] == "'" :
            w = w[1:]

	if w != "" :      
		if w[-1] == "'" :
			w = w[:len(w)-1]

		if w not in word_dic:
			word_dic[w] = 1

		else:
			word_dic[w] += 1
    
def solution() :
    
    ret_list = []
    
    with open('Les_Miserables-Victor_Hugo.txt', 'r') as f :

        context = f.read()
 
        changed_text = s_char_change(context)

        wordList = changed_text.split()

        word_count(wordList)
        
        for word in sorted(sorted(word_dic), key = word_dic.get, reverse=True):
            ret_list.append((word, word_dic[word]))
            
        f.close()
            
    return ret_list

if __name__ == '__main__' :
    word_dic = {}
    solution_list = solution()
    for each in solution_list :
        print(each)
