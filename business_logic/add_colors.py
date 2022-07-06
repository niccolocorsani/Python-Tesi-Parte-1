import os
import pandas as pd

from termcolor import colored

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_from_file_and_place_in_list(path):
    lines = []
    with open(path) as f:
        for line in f.readlines():
            if line != '\n':
                lines.append(line)

    return lines


def generate_sparql_lines(lines):
    colors = []
    i = 0


    for element in lines:
        try:
            if type(element[0]) is float:
                 element[0] = str(element[0]).replace('.0', '')
            if 'blu' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#0004ff')
            if 'gial' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#0004ff')
            if 'aran' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#ff8000')
            if 'bian' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#A0A0A0')
            if 'viol' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#7700ff')
            if 'verd' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#1eff00')
            if 'azzur' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#00ffff')
            if 'ner' in element[1].lower():
                colors.append('Flusso_' + element[0] + ';DataProperty;color;#000000')


        except Exception as ex:
            print(ex)

            continue

    return colors


if __name__ == '__main__':

    xl = pd.ExcelFile(ROOT_DIR + '/colori_flussi.xlsx')

    sheets = xl.sheet_names

    path_name_original_images = os.listdir(ROOT_DIR + '/colori/')

    for sheet in sheets:
        df = pd.read_excel(ROOT_DIR + '/colori_flussi.xlsx', sheet)
        list_of_flow = df.values.tolist()
        colors = generate_sparql_lines(list_of_flow)
        for color in colors:
            f = open(ROOT_DIR + '/all_csv/' + sheet, 'a')
            f.write('\n')
            f.write(color)
            f.close()
