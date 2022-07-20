def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.speak(str)

import time
from datetime import date 
import requests   

if __name__ =='__main__':
    #speak('Sushmita whats about your health right now, give me a quick update   According that i plan your diet') 
    # 
    #
    
    try:

        headers = {'Authorization' : '51da8cc77f304eb2be9c1e7c984acdb2'} 
        params ={'q' :'tata',# it play major role
                'from' :f'{date.today()}',
                 
                 'catagory':'business',#catagory is bullshit
                 'language': 'en',
                 'country' : 'in'}       
        response = requests.get('https://newsapi.org/v2/top-headlines' ,params = params,headers=headers)
        yours = response.json()
        #camly = json.loads(yours)
        #article = yours[2]
        get_art =  yours['articles']
        #print(get_art)
        sol = len(get_art)
        for i in range(sol):
            get_element = get_art[i]
            stro = get_element['title']
            print(stro)
            speak(stro)
            print('\n')
            time.sleep(3) 
    except Exception as e:
        print(e)
