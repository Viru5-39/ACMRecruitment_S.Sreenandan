def word_freq_c(txt):
    punc='''\/_()-[]{};:'"<>,./?!@#$%^&*'''
    lower=text.lower()
    no_punc=""
    for char in lower:
        if char not in punc:
            no_punc+=char
 
    words=no_punc.split()
    word_counts={}
    for word in words:
        if word in word_counts:
            word_counts[word]+=1
        else:
            word_counts[word]=1
    def get_count(item):
            return item[1]

    sorted_list=sorted(word_counts.items(),key=get_count,reverse=True)

    print("---WORD COUNTS---")
    for word,count in sorted_list:
        print(f"{word}-->{count}")
text=''' I am Sreenandan.
         I am writing a program on counting number of words in a paragraph.
         I have to display it in descending order.''' 
word_freq_c(text)

