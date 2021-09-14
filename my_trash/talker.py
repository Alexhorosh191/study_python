import pandas as pd
good = pd.read_csv('good.tsv', sep='\t')
good.sample(3)
rep = good[good.context_0 == 'как дела?'].reply
if rep.shape[0] > 0:
    print(rep.sample(1).iloc[0])