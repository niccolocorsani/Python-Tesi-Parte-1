import os

from from_txt_file_analisys import read_from_file_and_place_in_list, generate_lines

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':

    path_name_original_images = os.listdir(ROOT_DIR + '/images_txt/')
    lines = []

    for path_name in path_name_original_images:

        lines = read_from_file_and_place_in_list(ROOT_DIR + '/images_txt/' + path_name)
        nodes_csv, edges_csv, measures_csv = generate_lines(lines, path_name)

        for edge in edges_csv:
            if 'Class' in edge:
                edges_csv.remove(edge)

        for edge in edges_csv:
            if 'Class' in edge:
                edges_csv.remove(edge)
