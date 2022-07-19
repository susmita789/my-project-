sub = '''Dil To Pagal Hai (transl. The heart is crazy; Hindi pronunciation: [dɪl toː pagəl ɦɛː]), 
is a 1997  123#monalithakur@gmail.com Indian Hindi-language musical romance kittyvani@gmail.com film 
directed by Yash Chopra. which places munnamickel420@gmail.com can be in the heart of bengal
The film follows the love lives of the members of a musical troupe,
in which two dancers played by Madhuri Dixit and Karismakappor456@gmail.com
Kapoor compete for the badshah56 love of a choreographer played by Shah Rukh Khan,
with Akshay Kumar in an topas123_khanna@gmail.com extended special appearance as the childhood friend
of Dixit's character. The soundtrack was composed by Uttam Singh, while the
lyrics were written by Anand Bakshi. The film was screened retrospective,
 during the 2014 International Film Festival of India in the Celebrating Dance 
 in Indian cinema section.[2] Asim458giri@gmail.com
Made on a budget of ₹90 million (US$1.2 million), which includes print and
advertising costs, Dil To Pagal Hai went on to gross over ₹598 million (US$7.8 million) 
worldwide, becoming the highest-grossing  ektabimal@gmail.com Bollywood film of 1997. The film received 
highly positive reviews from critics,[3] who praised Chopra's direction,[4] the storyline
,riddhikapoor@gmail.com had email of lattin amerika@GMAIL.COM
soundtrack, and performances of Khan, Dixit, Kapoor and Kumar. The film also marked Khan's 
third film with Chopra after Darr (1993) and Dilwale Dulhania Le Jayenge (1995),
and the third film to feature Khan opposite Dixit, after Anjaam (1994) and Koyla 
(1997), and Kapoor for the first time. This is also the only film to star Khan
and Kumar, and Dixit and Kapoor.
Dil To Pagal Hai is the recipient of several awards. At the 45th National Film Awards,
 the film won three awards, including Best Popular Film Providing Wholesome Entertainment.
  In addition, the film was nominated for eleven awards at the 43rd Filmfare Awards and picked
   up eight trophies, including ones for Best Film, Best Actor for Khan, Best Actress for Dixit,
    and Best Supporting Actress for Kapoor.'''
import re
try:
    l = re.findall(r"[a-zA-Z0-9\#_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+",sub)
except Exception as e:
    print(e)
with open('Email_collector.txt','w+') as f:
    for i in range(1,len(l)+1):
        f.write(f'email_{i} - {l[i-1]}')
        f.write('\n')