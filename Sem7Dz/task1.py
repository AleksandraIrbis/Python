poem = input("введете рифму через пробел    ")
words = poem.split()
 
 
lst = [sum(x in 'аА' for x in lin)
 for lin in words]
 
if len(set(lst)) == 1 :
    res = "Парам пам-пам"  
else: res = "Пам парам"
 
print(res)