def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)




def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return len(dna1) > len(dna2)




def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    num_occurrences = 0
    
    for char in dna:
        if char in nucleotide:
            num_occurrences += 1
    
    return num_occurrences




def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1




def is_valid_sequence(sequence):
    '''(str) -> bool
    
    Return True if and only if the DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G').
    
    >>> is_valid_sequence('CGGCC')
    True
    >>> is_valid_sequence('ATCGGCC')
    True
    >>> is_valid_sequence('ATECGRGCC')
    False
    >>> is_valid_sequence('ATCGRGCC')
    False
    >>> is_valid_sequence('ATCGGCC')
    True
    >>> is_valid_sequence('cggcc')
    False
    >>> is_valid_sequence('atecgrgcc')
    False
    '''
    for ch in sequence:
        if ch not in 'ATCG':
            return False
    
    return True




def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str
    
    Return the dna by Inserting the given dna2 at the given index location of dna1. 
    
    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT',3)
    'CCGATG'
    >>> insert_sequence('CCGG','AT',4)
    'CCGGAT'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    '''
    return dna1[ : index ] + dna2 + dna1[ index : len(dna1) ]

def get_complement(nucleotide):
    '''(str) -> str
    
    Return the nucleotide's complement. A for T and C for G and vice versa
     
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C
    >>> get_complement(get_complement('G'))
    G
    >>> get_complement(get_complement('A'))
    A
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    else:
        return 'C'
    
def get_complementary_sequence(dna):
    '''(str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence
    
    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('TA')
    'TA'
    >>> get_complementary_sequence('ACGTACG')
    'TGCATGC'
    >>> get_complementary_sequence('TGCATGC')
    'ACGTACG'
    >>> get_complementary_sequence(get_complementary_sequence('TA'))
    'TA'
    >>> get_complementary_sequence(get_complementary_sequence('ACGTACG'))
    'ACGTACG'
    '''
    complement_dna = ''
    
    for nucleotide in dna:
        complement_dna += get_complement(nucleotide)
    
    return complement_dna    
    