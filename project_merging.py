import os
import shutil
print(os.getcwd())
source = 'D:\\quero'
os.chdir(source)


from docx import Document
def filemerge_creater(name,path):  
    '''
    it merges all the files which we switch in different folder
    '''          
    try:
        
        os.chdir('D:\workbook')
        print(os.getcwd())
        with open(f'{name}.txt','w+') as f:
            os.chdir(path)
            for i in os.listdir(path):
                print(i)
                docy =Document(str(i))
                f.write(f'\t\t{i} \n')
                for para in docy.paragraphs:
                    f.write(para.text)
                    f.write('\n')   
                f.write('\n\n\n')
    except Exception as e:
        print(e)
'''
for i in os.listdir():
    print(i)
lo= []
l = []
co= []
c = []
q = []
for i in os.listdir():
    for j in range(len(os.listdir())):
        if i == f'Assignment_{j}.docx':
            lo.append(i)
            os.rename(i,f'Basic_Assignment_{j}.docx')
        if i == f'Basic_Assignment_{j}.docx':
            l.append(i)        
        else:
            pass


path1 = 'D:\\Basic assignment'
try:
    os.mkdir(path1)
except:
    print('already exists')
for n in l:
    try:
        shutil.move(source+f'\{n}', path1+f'\{n}') 
    except Exception as e:
        print(e)


for i in os.listdir():
    for j in range(len(os.listdir())):
        if i == f'Assignment_{j} (2).docx':
            co.append(i)    
            os.rename(i,f'Advance_Assignment_{j}_{j}.docx')
        #now after changing 
        if i == f'Advance_Assignment_{j}_{j}.docx':
            c.append(i)   
        else:
            pass
path2 = 'D:\\Advance_Assignment'
try:
    os.mkdir(path2)
except:
    print('directory already made')
for n in c:
    try:
        shutil.move(source+f'\{n}',path2+f'\{n}')
    except:
        print('we already move it')


for i in os.listdir():
    for j in range(len(os.listdir())+1):
        if i == f'Programming_Assingment{j}.docx':
            q.append(i)
        else:
            pass
print(q)



import os
os.chdir('D:\\Basic Assignment')
file_name = os.listdir()[1].split('_')[0]
file_name2 = os.listdir()[1].split('_')[1]
name = f'{file_name}_{file_name2}'
print(name)






'''
#coton = [i for i in os.listdir()]
#print(coton)
def file_creation(list,custom):
    file_name = list[0].split('_')[0]
    file_name1 = list[0].split('_')[1]
    print(list[1])
    print(file_name)
    name = f'{file_name}_{file_name1}'
    path1 = f'D:\{name}_{file_name1} Yours_creation'
    source = 'D:\\quero'
    try:
        os.mkdir(path1)
    except:
        pass
    for n in list:
        try:
            shutil.move(source+f'\{n}', path1+f'\{n}') 
        except Exception as e:
            print(e)
    filemerge_creater(custom,path1)



def candy():
    l = []
    lo = []
    for i in os.listdir():
        for j in range(len(os.listdir())):
            if i == f'Assignment_{j}.docx':
                l.append(i)
                print(l)
            else:
                pass
            
    try:
        for k in l:
            print(k)
            os.rename(k,f'Basic_Assignment_{j}.docx')
            for i in os.listdir():
                for j in range(len(os.listdir())):
                    if i == f'Basic_Assignment_{j}.docx':
                        lo.append(i)
                        print(lo)
                    else:
                        pass    
    except:
        pass    
    file_creation(lo,'jadub')

def choco():
    c =[]
    co = []
    for i in os.listdir():
        for j in range(len(os.listdir())):
            if i == f'Assignment_{j} (2).docx':
                c.append(i)  
            else:
                pass
    try:
        for k in c:     
            os.rename(k,f'Advance_Assignment_{j}_{j}.docx')
            for i in os.listdir():
                for j in range(len(os.listdir())):
                    if i == f'Advance_Assignment_{j}_{j}.docx':
                        co.append(i)
                    else:
                        pass
    except:
        pass
    file_creation(co,'jaduA')

def micho():
    m =[]
    mo = []
    for i in os.listdir():
        for j in range(len(os.listdir())):
            if i == f'Programming_Assignment_{j}.docx':
                m.append(i)  
            else:
                pass
    try:
        for k in m:     
            os.rename(k,f'programing_Assignment_{j}_3.docx')
            for i in os.listdir():
                for j in range(len(os.listdir())):
                    if i == f'programing_Assignment_{j}_3.docx':
                        mo.append(i)
                    else:
                        pass 
    except:
        pass
    file_creation(mo,'jaduP')


if __name__ == '__main__':
    try:
        candy()
    except Exception as e:
        print(e)     
    try:
        choco()
    except Exception as e:
        print(e)
    try:
        micho()
    except Exception as e:
        print(e)        