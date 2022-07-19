#                      SEARCH ENGINE                                   @@@@uncomplete

list = ['python is the first language I had studied',
        'my suggestion to learn python everyone as early as possible',
        'python has a huge set of librry and module',
        'python string module',
        'python regex module',
        'develop your website with flask',
        'python set module in python datastructure course',
        'web development with danjo']

def sorting(dom):
    return dom.value()

def my_module(meto,ex):
    l = ex.split()
    dict = {}
    for i in range(len(meto)):
        b = meto[i].strip()
        sum  = 0
        for j in l:
            for k in b:
                if j == k:
                    sum +=1
                else:
                    pass
        dict[meto[i]] = sum
    endor = dict.items()
    main = endor.sort(reverse = True, key = sorting)
    for o in main:
        print(o[0])


extra = input('Enter your query - ')
my_module(list,extra)
