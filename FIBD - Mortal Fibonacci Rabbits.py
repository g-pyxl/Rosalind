def wabbits(n,m):
    
    #Starting month
    
    immature = 1
    mature = 0
    months = 1
    newbabies = 0
    genbox = [1]
    
    #Begin month 2
    
    while months < n:
        
        months += 1
        mature += immature
        immature = 0
        immature += newbabies
        
        total = mature + immature
        genbox.insert(months, total)
        
        #kill off older generations
        if months > m:
            total -= genbox[months - m - 1]
            
        newbabies = total - immature
        
    #print (genbox)
    return total
    
print (wabbits(6,3))
