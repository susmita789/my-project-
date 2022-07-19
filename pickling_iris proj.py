import requests
import pickle
'''
import requests

try:
    url = 'https://httpbin.org/post'
    files = {'file': ('report.csv')}

    payload={}
    files=[
    ('file',('report.csv',open('/report.csv','rb'),'text/csv'))
    ]
    headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 0000000'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
'''
'''
import time
from datetime import date
try:

    headers = {'Authorization' : '51da8cc77f304eb2be9c1e7c984acdb2'} 
    params ={'q':'IPL',
            'from' :f'{date.today()}',
                      
             'category':'sports',
             'language': 'en',
             'country' : 'in'}        
    response = requests.get('https://newsapi.org/v2/top-headlines' ,params = params,headers=headers)
    yours = response.json()
    #camly = json.loads(yours)
    #article = yours[2]
    get_art =  yours['articles']
    #print(get_art)
    #print(len(get_art))
    for i in range(10):
        get_element = get_art[i]
        str = get_element['title']
        print(str)
        print('\n')
        time.sleep(3) 
except Exception as e:
    print(e)
'''
try:
    #internet should be opened during this project
    rep = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    f = open('iris_data.txt','w')
    f.write(rep.text)
    f.close()
    f =open('iris_data.txt')
    l = f.read().split('\n')
    lit =[i.split(',') for i in l]
    #print(lit)
    #pickling
    #with open('iris_pikku.pkl','wb') as poco:
    #    pickle.dump(lit,poco)
    #unpickleing
    with open('iris_pikku.pkl','rb') as doco:
        reedy = pickle.load(doco)
        print(reedy)

except Exception as e:
    print(e)

