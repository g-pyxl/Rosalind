#DNA Motif locator

DNAstring = 'GATATATGCATATACTT'
Motifstring = 'ATAT'

def findall(DNA, motif):
    print (DNA.find(motif) + 1)
    start = DNA.find(motif) + 1
    while start >= 1:
        if DNA.find(motif, start) <= 0:
            print ('No more matches found.')
            return
        else:
            print (DNA.find(motif, start) + 1)
            start = (DNA.find(motif, start) + 1)
    return

findall(DNAstring, Motifstring)
