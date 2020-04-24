from docx import Document
import os
import re
#document = open('book1.docx')
document = Document('226.docx')
i = 1
k = i
for p in document.paragraphs:
   i = 1 + i
   if '7. Установленная причина дефекта' in p.text:
      print (i)
      k = i
   if i == k+1:
      print (p.text)
      if re.search(r'\d\d\w\d\d\d', p.text):
         print ('yes')
         #print (re.search(r'№ \w\w\w\w\w\w', p.text))
         print (re.search(r'\d\d\w\d\d\d', p.text).group(0))
         result = re.split(r'–',p.text)
         print (result[0])
      else:
         print ('no')

           
           
        
        
