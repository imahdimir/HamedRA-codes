"""

    """

import pandas as pd
from pyjarowinkler import distance


efp = '/Users/mahdi/Downloads/Zephyr_Export_7.xlsx'
hanfp = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/HAN-202202/202202_HAN_NAMES.prq'

tnc = 'Target name'
cnc = 'Clean_name'
tcc = 'Target country code'
exhr = 'exact_match_harm'
pcc = 'Person_ctry_code'

##
# fp = '/Users/mahdi/Downloads/202202_HAN_NAMES.txt'
# df3 = pd.read_table(fp , sep = '|')

##
han = pd.read_parquet(hanfp)
df = pd.read_excel(efp , sheet_name = 'Results')

##
tn = df[[tnc , tcc]]

##
tn[exhr] = tn[tnc].isin(han[cnc])

##
tn_1 = tn[tn[exhr]]

##
harm_1 = han[han[cnc].isin(tn_1[tnc])]

##
merg = tn_1.merge(harm_1 , left_on = tnc , right_on = cnc , how = 'outer')

##
merg['same_country'] = merg['Target country code'].eq(merg['Person_ctry_code'])

##
merg['same_country1'] = merg.groupby(tnc)['same_country'].transform('any')

##
tn = tn.merge(merg , how = 'left')

##
tn_2 = tn[tn['same_country1'].ne(True)]
tn_2 = tn_2[[tnc , tcc , exhr]]

##
def find_similar_in_df(targ , df , country = None , tresh = .8) :
    if country is not None :
        df = df[df[pcc].eq(country)]

    df[tnc] = targ
    df['sim'] = df[cnc].apply(
            lambda x : distance.get_jaro_distance(targ , x , winkler = True)
            )
    return df[df['sim'].ge(tresh)]

##
tdf = find_similar_in_df(tn_2.at[0 , tnc] , han , tn_2.at[0 , tcc])

##
simdf = pd.DataFrame()

for ind , ser in tn_2.iterrows() :
    _df = find_similar_in_df(ser[tnc] , han , ser[tcc])
    simdf = pd.concat([simdf , _df])

##
simdf['1-sim'] = 1 - simdf['sim']
simdf = simdf.sort_values([tnc , '1-sim'])

##
simdf.to_excel('similarities.xlsx' , index = False)


##
