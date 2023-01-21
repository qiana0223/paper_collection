import pandas as pd

from gen_markdown.utils import get_str_length


def write_markdown_0(df_data:pd.DataFrame, output_file_path:str,description:str):
    with open(output_file_path, 'w', encoding='utf8') as f:
        f.write(description + '\n')
        f.write('========\n')

        f.write("| No | Title | Year | Venue  | \n")
        f.write("| ---- | ---- | ----- | ----  | \n")

        i=1
        for index, row in df_data.iterrows():

            # line="|"+str(i)+"|["+str(row[0]) +"]("+str(row[2])+")|"+str(int(row[1]))+"|"+citation+"|\n"
            line ="|"+str(i) +"|[" + get_str_length(str(row[0])) + "](" + str(row[3]) + ")|" + str(row[1])+"|"+ str(row[2])+" | \n"

            f.write(line)
            i+=1
    f.close()


def write_markdown_1(df_data:pd.DataFrame, output_file_path:str,description:str):
    with open(output_file_path, 'w', encoding='utf8') as f:
        f.write(description + '\n')
        f.write('========\n')

        f.write("| Title | Year | Venue | Citation | Abstract | \n")
        f.write("| ---- | ----- | ---- | ----- | ------ | \n")

        for index, row in df_data.iterrows():
            citation = "<details><summary>cite</summary>" + \
                       str(row[4]).replace('\n', '</br>') + "</details>"
            abstract = "<details><summary>abstract</summary>" + \
                       str(row[5]).replace('\n', '</br>') + "</details>"

            # line="|"+str(i)+"|["+str(row[0]) +"]("+str(row[2])+")|"+str(int(row[1]))+"|"+citation+"|\n"
            line = "|[" + get_str_length(str(row[0])) + "](" + str(row[3]) + ")|" + str(row[1]) + "|" + str(
                row[2]) + "|" + citation + "|" + abstract + " | \n"

            f.write(line)
    f.close()