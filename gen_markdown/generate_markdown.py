import numpy as np

from constants import *
from gen_markdown.excel_read import get_data_from_excel
from gen_markdown.markdown_write import write_markdown_0, write_markdown_1

for data in gen_data:
    # get data from the excel
    df_data = get_data_from_excel(paper_collection_path + input_excel,data['tags'],data['use_columns'])

    # filter out the data not to be presented
    df_results = df_data[data['data_to_be_present']]
    df_results = df_results.replace(np.nan, '&nbsp;')

    # write to a file
    output_file_path=project_dir+data['mk_name']
    if data['write_method']=='write_markdown_0':
        write_markdown_0(df_results,output_file_path,data['description'])
    elif data['write_method']=='write_markdown_1':
        write_markdown_1(df_results, output_file_path, data['description'])
    else:
        pass