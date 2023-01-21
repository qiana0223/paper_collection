import pandas as pd


def  get_data_from_excel(excel_path:str,tags:list,usecolumns:str):
    df_paper_data = pd.read_excel(excel_path, sheet_name=0, index_col=None, na_values=['NA'],
                                  usecols=usecolumns)

    # remove rows that donot have values for column year
    df_paper_data = df_paper_data[df_paper_data['year'].notna()]

    # sort the rows based on year and paper
    df_paper_data = df_paper_data.sort_values(["year", "paper"], ascending=(False, True))

    # get the rows that have tags specified
    def have_tags(data: str):
        if isinstance(data, float):
            print(data)
            return False
        if len(data) > 0:
            for tag in tags:
                if tag in data:
                    return True
        return False

    df_paper_data['tags'] = df_paper_data['type'].map(lambda x: have_tags(x))
    df_paper_data['year']=df_paper_data['year'].map(lambda x:int(x))

    df_paper_data_tags = df_paper_data[df_paper_data['tags']]
    return df_paper_data_tags