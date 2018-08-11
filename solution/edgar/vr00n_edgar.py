from bs4 import BeautifulSoup
import requests
import json
table_full=[]
with open('edgar.json', 'a') as fp:
    print >>fp, '['
    for i in xrange(1,11):
        url = 'http://0.0.0.0/companies/?page='+str(i)
        #print url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        tags = soup.findAll("a", {"id":True})
        for j in xrange(0,len(tags)):
            #print tags[i].text.strip()
            url2 = 'http://0.0.0.0/companies/'+str(tags[j].text.strip())
            response2 = requests.get(url2)
            soup2 = BeautifulSoup(response2.content, "html.parser")
            table_data = [[cell.text for cell in row("td")] for row in soup2("tr")]
            table_full.append(json.dump(dict(table_data), fp))            
            if i*j < 90:
                print >>fp, ','
    print >>fp, ']'
