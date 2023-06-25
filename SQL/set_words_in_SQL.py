#  INSERT INTO words.select_words(choice1,choice2,choice3, additional_choice) VALUES('be','was', 'been','were');
from funcy import chunks
a = []
new_str = ''
i=0
with open('regular_verbs.txt','r+') as f:
    for word in f:
        for i in word:
            # print(i, end= '')
            if i == '\t' or i == '\n':
                a.append(new_str)
                new_str=''
                continue
            new_str = new_str+i
print(a)
result = list(chunks(5, a))
print(result)
for i in range(len(result)):
    print("('",result[i][0],"','",result[i][1],"','",result[i][3],"','",result[i][4],"'),")

