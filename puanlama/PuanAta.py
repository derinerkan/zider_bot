import tsv
import re

reader = tsv.TsvReader(open('karint_corpus.tsv', encoding='utf-8'))

for i in reader:
    # print(' '.join(i))
    msg = list(i)[1]
    if re.search(r'.sozluk.', msg) is not None:
        print(msg)
