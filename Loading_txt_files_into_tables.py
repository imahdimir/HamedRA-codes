"""

  """

from pathlib import Path
from pathlib import PurePath

import pandas as pd


ana_brevetto_tables = {
        'aik'                : 1 ,
        'app_to_punr_ep'     : 2 ,
        'app_to_punr_us'     : 3 ,
        'applications'       : 4 ,
        'applications_ep'    : 5 ,
        'applnid_codfirm'    : 6 ,
        'cpc'                : 7 ,
        'dcst'               : 8 ,
        'equivalents'        : 9 ,
        'ipcclass'           : 10 ,
        'ipcmain'            : 11 ,
        'ipcnacev2'          : 12 ,
        'nplcitations'       : 13 ,
        'nplcitcat'          : 14 ,
        'nplpubl'            : 15 ,
        'patanag'            : 16 ,
        'patanag2'           : 17 ,
        'patcitations'       : 18 ,
        'patcitations_ep'    : 19 ,
        'patcitcat'          : 20 ,
        'patcitorigin'       : 21 ,
        'patlegal'           : 22 ,
        'patpubhis'          : 23 ,
        'priorities'         : 24 ,
        'prty'               : 25 ,
        'titles'             : 26 ,
        'usapplications'     : 27 ,
        'usappln_id_codfirm' : 28 ,
        'uscpc'              : 29 ,
        'usdcst'             : 30 ,
        'usipcclass'         : 31 ,
        'usipcmain'          : 32 ,
        'usipcnacev2'        : 33 ,
        'usnplcitations'     : 34 ,
        'usnplcitcat'        : 35 ,
        'usnplpubl'          : 36 ,
        'uspatanag'          : 37 ,
        'uspatanag2'         : 38 ,
        'uspatcitations'     : 39 ,
        'uspatcitcat'        : 40 ,
        'uspatcitorigin'     : 41 ,
        'uspatlegal'         : 42 ,
        'uspatpubhis'        : 43 ,
        'uspriorities'       : 44 ,
        'usprty'             : 45 ,
        'ustitles'           : 46 ,
        }

companies_tables = {

        }

def main() :
    pass

    ##
    writeFile = open('/Users/mahdimir/Downloads/user_sql.txt' , 'w')
    writeFile.write('use ana_brevetto;\n')

    dirp = Path('/Users/mahdimir/Downloads/icrios/')
    tables_in_path = list(dirp.glob('*.txt'))

    for tblfp in tables_in_path :

        if tblfp.stem in ana_brevetto_tables.keys() :

            line_txt = 'load data local infile ' + '"' + str(tblfp) + '" '
            line_txt += 'into table ' + tblfp.stem + ';\n'

            writeFile.write(line_txt)

    writeFile.close()

    ##
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/ana_brevetto_all_tables.xlsx'
    df = pd.read_excel(fp)

    ##
    dirp = Path('/Users/mahdimir/Downloads/icrios/')
    tables_in_path = list(dirp.glob('*.txt'))
    tables_stems = [x.stem for x in tables_in_path]

    ##
    df.columns
    df = df[df['Tables_in_ana_brevetto'].isin(tables_stems)]
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/ana_brevetto_tables_we_have.xlsx'
    df.to_excel(fp , index = False)

    ##
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/companies_all_tables.xlsx'
    df = pd.read_excel(fp)

    ##
    df.columns
    df = df[df['Tables_in_companies'].isin(tables_stems)]
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/companies_tables_we_have.xlsx'
    df.to_excel(fp , index = False)

    ##
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/inventors_tables.xlsx'
    df = pd.read_excel(fp)

    ##
    df.columns

    ##
    df = df[df['Tables_in_inventors'].isin(tables_stems)]
    fp = '/Users/mahdimir/Downloads/icrios/tables in each sub db/inventors_tables_we_have.xlsx'
    df.to_excel(fp , index = False)

##
if __name__ == "__main__" :
    main()
    print(f'{PurePath(__file__).name} Done.')
