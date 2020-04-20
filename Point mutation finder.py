#Point mutation seeker

DNAstring1 = 'GAGCCTACTAACGGGAT'
DNAstring2 = 'CATCGTAATGACGGCCT'
st1box = ''
st2box = ''

def pointmutation(st1, st2):
    position = 0
    counter = 0
    while position < len(st1):
        st1box = st1[position]
        st2box = st2[position]
        position += 1
        
        if st1box != st2box:
            #print ('Point mutation found!')
            counter += 1
            
    return counter
        
print (pointmutation(DNAstring1, DNAstring2))
