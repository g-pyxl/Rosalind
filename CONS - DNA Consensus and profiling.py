#DNA Consensus and profiling

#f = open('input.txt', 'r')
#g = open('output.txt', 'w')
# Modified to run from manual string input over string import from file.

stringlist = [
    'ATCCAGCT',
    'GGGCAACT',
    'ATGGATCT',
    'AAGCAACC',
    'TTGGAACT',
    'ATGCCATT',
    'ATGGCACT',
    '',
    '',
    ''
    ]
con = []
def trackall(st):

    A = []
    C = []
    G = []
    T = []
    counter = 0
    stringcount = 1
    
    while counter < len(st[0]):
        
        #initial string check - fills list array
        
        for i in st[counter]:
            if i == 'A':
                A.insert(counter, 1) 
                C.insert(counter, 0) 
                G.insert(counter, 0) 
                T.insert(counter, 0)
                counter += 1
            elif i == 'C':
                A.insert(counter, 0) 
                C.insert(counter, 1) 
                G.insert(counter, 0) 
                T.insert(counter, 0)
                counter += 1
            elif i == 'G':
                A.insert(counter, 0) 
                C.insert(counter, 0) 
                G.insert(counter, 1) 
                T.insert(counter, 0)
                counter += 1
            elif i == 'T':
                A.insert(counter, 0) 
                C.insert(counter, 0) 
                G.insert(counter, 0) 
                T.insert(counter, 1)
                counter += 1
                
                
    while stringcount < len(st):

        # Begin filling in the matrix data
        
        newcount = 0
        for x in st[stringcount]:
            
            if x == 'A':
                A[newcount] = A[newcount] + 1 
                counter += 1
                newcount += 1
            elif x == 'C':
                C[newcount] = C[newcount] + 1 
                counter += 1
                newcount += 1
            elif x == 'G':
                G[newcount] = G[newcount] + 1 
                counter += 1
                newcount += 1
            elif x == 'T':
                T[newcount] = T[newcount] + 1 
                counter += 1
                newcount += 1
    
        stringcount += 1
            
        
    #print ('A: ', A)
    alist = ' '.join([str(elem) for elem in A]) 
    print('A:', alist)
    clist = ' '.join([str(elem) for elem in C]) 
    print('C:', clist) 
    glist = ' '.join([str(elem) for elem in G]) 
    print('G:', glist) 
    tlist = ' '.join([str(elem) for elem in T]) 
    print('T:', tlist) 
    
    #Select highest figure from each column
    ccount = 0
    while ccount < len(st[0]):      

        if (A[ccount] >= C[ccount]) and (A[ccount] >= G[ccount]) and (A[ccount] >= T[ccount]):
            con.append('A')
            ccount += 1
            
        elif (C[ccount] >= A[ccount]) and (C[ccount] >= G[ccount]) and (C[ccount] >= T[ccount]):
            con.append('C')
            ccount += 1
            
        elif (G[ccount] >= A[ccount]) and (G[ccount] >= C[ccount]) and (G[ccount] >= T[ccount]):
            con.append('G')
            ccount += 1
            
        elif (T[ccount] >= A[ccount]) and (T[ccount] >= G[ccount]) and (T[ccount] >= C[ccount]):
            con.append('T')
            ccount += 1
    
    conlist = ''.join([str(elem) for elem in con]) 
    return conlist
    
print (trackall(stringlist))
