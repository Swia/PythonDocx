from docx import Document
import os
import re
#document = open('book1.docx')
document = Document('227.docx')
i = 1
k = i
x = 0
j = ''
result4 = '' 
for p in document.paragraphs:
   i = 1 + i
   #if '7/' in p.text:
   #   result3 = re.split(r'7/', p.text)
   #   print (result3[1])
   if ', заводск' in p.text:
      result4 = re.findall(r'\s\d+\w+', p.text)
      x = len(result4)
      print (result4)
      print (x)

 
   if '7. Установленная причина дефекта' in p.text:
      k = i
      print (p.text)
   if i == k+1:
      for x in range(len(result4)):
         result=re.search(result4[x],p.text)
         print(result[0])

"""if re.search(r'№ \d\d\w\d\d\d', p.text):
         print ('yes')
         #print (re.search(r'№ \w\w\w\w\w\w', p.text))
         #print (re.search(r'\d\d\w\d\d\d', p.text).group(0))
         result = re.split(r'–',p.text)
         result2 = result
         #print (result) 
         #print (result2)
         result3 = re.findall(r'\d\d\w\d\d\d',result2)
         print (result3)
      else:
         print ('no')
"""
           
           
        
        
