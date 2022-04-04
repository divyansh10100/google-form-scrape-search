import requests
from bs4 import BeautifulSoup

res=requests.get('https://docs.google.com/forms/d/e/1FAIpQLSfpZcHWnlx0EkhsXKh0sPvRH7FF1jly94pC0v24yYrX-fLgIw/formResponse')
soup=BeautifulSoup(res.text,'html.parser')
ques=soup.select('.freebirdFormviewerComponentsQuestionBaseTitle')
def questions(ques):
    qu=[]
    for inx, item in enumerate(ques):
        title=ques[inx].getText()
        qu.append(title)
    for i in qu:
        with open('/home/Hp/VSC/python/scraped.txt', mode='a') as file1:
            file1.write(i+'\n')
    return qu
print(questions(ques))
 