#lists

colleges = ['iit','nit','clg of engg']
print(colleges[2])

colleges[2] ="clg"
print(colleges[2])
print(colleges)
print(colleges[1:3])

list2 =['table','chair','fan','clothes','bottle']
#list2.append('microphone')
list2.insert(3,'microphone')
print(list2)
list2.remove('microphone')
print(list2 + ['pillow', 'tibelight','bed'])
print(list2)
print(len(list2))
print(max(list2))
print(min(list2))