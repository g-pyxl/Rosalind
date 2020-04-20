def DNAtoRNA(rawDNA):
    start = 0
    end = 3
    protein = ''
    while start < len(rawDNA):
        RF = rawDNA[start:end]
        start += 3
        end += 3

        #begin converting to protein - incomplete! Add remaining genetic code.

        if RF == 'UUU':
            protein += 'F'
        if RF == 'UUC':
            protein += 'F'
        if RF == 'UUA':
            protein += 'L'
        if RF == 'UUG':
            protein += 'L'
            
        if RF == 'CUU':
            protein += 'L'
        if RF == 'CUC':
            protein += 'L'
        if RF == 'CUA':
            protein += 'L'
        if RF == 'CUG':
            protein += 'L'

        if RF == 'AUU':
            protein += 'I'
        if RF == 'AUC':
            protein += 'I'
        if RF == 'AUA':
            protein += 'I'
        if RF == 'AUG':
            protein += 'M'

        if RF == 'GUU':
            protein += 'V'
        if RF == 'GUC':
            protein += 'V'
        if RF == 'GUA':
            protein += 'V'
        if RF == 'GUG':
            protein += 'V'

        if RF == 'UCU':
            protein += 'S'
        if RF == 'UCC':
            protein += 'S'
        if RF == 'UCA':
            protein += 'S'
        if RF == 'UCG':
            protein += 'S'

        if RF == 'CCU':
            protein += 'P'
        if RF == 'CCC':
            protein += 'P'
        if RF == 'CCA':
            protein += 'P'
        if RF == 'CCG':
            protein += 'P'

        if RF == 'ACU':
            protein += 'T'
        if RF == 'ACC':
            protein += 'T'
        if RF == 'ACA':
            protein += 'T'
        if RF == 'ACG':
            protein += 'T'

        if RF == 'GCU':
            protein += 'A'
        if RF == 'GCC':
            protein += 'A'
        if RF == 'GCA':
            protein += 'A'
        if RF == 'GCG':
            protein += 'A'
            
    return protein

print (DNAtoRNA('AUGGCGTCGCGUUGUGCTCTGUUGUGUCGCUGCG'))
