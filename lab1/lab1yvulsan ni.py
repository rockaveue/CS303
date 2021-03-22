from collections import deque, OrderedDict
from textblob import TextBlob

print("Dulguun B180910062\n")
data = {}
data2 = {}
data3 = {}
day_1 = ['home','school','restaurant','home']
day_2 = ['home','school','restaurant','home']
day_3 = ['school','cafe','hospital','restaurant']
day_4 = ['home', 'school', 'restaurant', 'cafe']
days = day_1 + day_2 + day_3 + day_4
#sentence утгад бүх үгнүүдээ зайгаар тусгаарлан оруулав
sentence = ' '.join(days)
# print(days)
# textblob -ийн ngrams-ийг ашиглан sentence -дэх үгнүүдийг "n=2"-оор 2, 2-оор ngrams утгад авав.
ngram_object = TextBlob(sentence)
ngrams = ngram_object.ngrams(n=2)

# 1 газар хэдэн удаа давтагдахыг олохдоо deque лист ашиглаж days-д байгаа бүх үгээ deq-д хийв
deq = deque()
for asd in days:
    deq.append(asd)

# Дараалалж 2 газар хэдэн удаа орсныг шалгахад зориулж өөр нэг deque лист-нд зайгаар тусгаарлаж 2 үгнүүдийг deq1-т хийв
deq1 = deque()
for we in range(0, len(days)-1):
    deq1.append(days[we]+ ' '+ days[we+1])
# print(deq1)

# Дараалалж 3 газар хэдэн удаа орсныг шалгахад зориулж өөр нэг deque лист-нд зайгаар тусгаарлаж 3 үгнүүдийг deq2-т хийв
deq2 = deque()
for wer in range(0, len(days)-2):
    deq2.append(days[wer] + ' '+  days[wer + 1] + ' ' +days[wer + 2])

# Бүх давтагдаагүй утгыг хадгалан шууд хэвлэв
unique_locations= set (days) # unique locations
print(f'unique locations are {unique_locations}')
print()

# 1 газар хэдэн удаа давтагдахыг олохын тулд data гэсэн dict утгад deq-д хийсэн нийт утгуудаас тоог нь авч тухай бүрт хийх давталт
for location in unique_locations:
    data[location] = deq.count(location)
# үр дүнг ихээс бага руу sort хийн хэвлэв
sorted_data = sorted(data.items(), key=lambda a: a[1], reverse = True)
print('\n1 удаа давтагдсан утгуудын тоо')
print(sorted_data)
print('----------------------------------------------------------')
# Дарааллалсан 2 газар хэдэн удаа давтагдахыг мөн адил аргаар давталт ашиглан тоог data2 dict-д хийн хэвлэв
utga = ''
for i in range(0, len(ngrams)):
    utga = ''
    utga = ngrams[i][0] + ' ' + ngrams[i][1]
    # for j in range(len(ngrams[i])):
    #     utga = utga + ' ' + ngrams[i][j]
    data2[utga] = deq1.count(utga)
print('\nДараалалж 2 удаа давтагдсан утгуудын тоо')
print(data2)

print('----------------------------------------------------------')
# sentence -дэх үгнүүдийг "n=3"-оор 3, 3-аар ngrams утгад авав.
ngram_object = TextBlob(sentence)
ngrams = ngram_object.ngrams(n=3)

# Дарааллалсан 3 газар хэдэн удаа давтагдахыг мөн адил аргаар давталт ашиглан тоог data3 dict-д хийн хэвлэв
for i in range(0, len(ngrams)):
    utga = ''
    utga = ngrams[i][0] + ' ' + ngrams[i][1] + ' ' + ngrams[i][2]
    # for j in range(len(ngrams[i])):
    #     utga = utga + ngrams[i][j]
    data3[utga] = deq2.count(utga)
print('\nДараалалж 3 удаа давтагдсан утгуудын тоо')
print(data3)
print('---------------------------------------------')
# data3 дахь хамгийн их утга
print('\ndata3 дахь хамгийн их утга')
print(f"{max(data3, key=data3.get)} : {max(data3.values())}")

# sorted_data3 = sorted(data3.items(), key=lambda a: a[1], reverse = True)

# print(sorted_data3[0])
    



""" pip install -U textblob
python -m textblob.download_corpora
from textxblob import TextBlob
sentence = ""
ngram_object = TextBlob(sentence)
ngrams = ngram_object.ngrams(n=2)
print(ngrams) """