sample_tuple = [('O', 'M', 'I'), ('For', 'Technical', 'Support', 'To', 'Extend', 'Warranty', 'for', 'Complaints', 'and', 'Compliments')]


def join(sample_tuple) -> str:
    return ' '.join(sample_tuple)


result = map(join, sample_tuple)
print(list(result))


# Printing tuple multiple times
sample_tuple = ('O', 'N', 'K', 'A', 'R')
print(sample_tuple * 6)