import matplotlib
import matplotlib.pyplot as plt
import os
import pandas as pd
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

plt.gcf().subplots_adjust(bottom=0.4)

if __name__ == '__main__':

    df = pd.read_csv(ROOT_DIR + '/dfshap_Unico.csv')
    list_of_shaps = df.values.tolist()

    variables = 'timestamp,prediction,TemperaturareattoreR4001,TemperaturareattoreR4002,TemperaturareattoreR4003,S4304,caricocloruroferricostandard,S904C,S904B,S904A,caricocloruroferricopotabile,S904E,S904D,QuantitaNaOHperBatchNaClO_2,QuantitaNaOHperBatchNaClO,ConversioneNaOH,ConversioneKOHlinea1,KOHrampa1caricoprodotti,KOHrampa2caricoprodotti,S487,S484,S5104,caricoiposodio,S857,S856,S851,S852,S854,S871,RedoxFeCl3Pot,diff_S4304,diff_S904C,diff_S904B,diff_S904A,diff_S904E,diff_S904D,diff_S487,diff_S484,diff_S5104,diff_S857,diff_S856,diff_S851,diff_S852,diff_S854,diff_S871'

    list_of_variables = variables.split(',')

    dic = {}
    list = []
    i = 0
    ##Inizialization of dic
    for var in list_of_variables:
        dic[list_of_variables[i]] = []
        i = i + 1
    ##Value to dic
    for elements in list_of_shaps:
        i = 0
        for element in elements:
            dic[list_of_variables[i]].append(element)
            i = i + 1

    date = None
    x = []
    for date in dic.get('timestamp'):
        try:
            x.append(datetime.strptime(date, '%Y-%m-%d %H:%M:%S'))
        except:
            x.append(datetime.strptime(date, '%Y-%m-%d'))
            continue

    xs = matplotlib.dates.date2num(x)
    hfmt = matplotlib.dates.DateFormatter('%Y-%m-%d %H:%M:%S')











    legends = []

    d = 0
    #### Plot all in one
    # for element in dic.keys():
    #     if element == 'prediction' or element == 'timestamp': continue
    #     fig = plt.figure()
    #     ax = fig.add_subplot(1, 1, 1)
    #     ax.xaxis.set_major_formatter(hfmt)  # Per metterlo in formato data e ora visto che dovrebbe essere un float
    #     plt.setp(ax.get_xticklabels(), rotation=15)
    #     ax.plot(xs, dic.get(element))
    #     plt.xlabel(element)
    #     plt.tight_layout()
    #

        # legends.append(element)

    ## plt.xticks(x) to plot all x values

    plt.legend(legends)

    plt.show()

    #### Plot separately
    for element in dic.keys():
        if element == 'prediction' or element == 'timestamp': continue

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_major_formatter(hfmt)
        plt.setp(ax.get_xticklabels(), rotation=15)
        ax.plot(xs, dic.get(element))
        plt.xlabel(element)
        plt.tight_layout()
        ## plt.xticks(x) to plot all x values
        plt.show()
        fig.savefig(ROOT_DIR+'/plots/'+element)


    print('fine')

### TODO rifare stesso algoritmo con i float in basso per vedere se fatto giusto l'esercizio
