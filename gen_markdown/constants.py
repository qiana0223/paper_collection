"""
https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
generate Readme file for github
"""
paper_collection_path="C:\\Users\\18178\paper_pool\\"
input_excel='paper_pool.xlsx'
project_dir='C:\\Users\\18178\\PycharmProjects\\paper_collection\\'


gen_data=[
    {
         'tags':['ST','st'],
         'use_columns':"A,B,C,D,E",
         'mk_name': 'security_analysis_and_testing.md',
         'data_to_be_present':['paper','year','venue','link'],
         'write_method':'write_markdown_0',
         'description':'A bibliography of papers on security analysis and testing of Ethereum smart contracts or relevant papers.'

     },

    {
        'tags':['ML','ml'],
        'use_columns':"A,B,C,D,E,G,H",
        'mk_name': 'machine_learning_based_papers.md',
        'data_to_be_present':['paper','year','venue','link','bibTex' , 'abstract'],
        'write_method':'write_markdown_1',
        'description':'A bibliography of papers that apply machine learning to analyze Ethereum smart contracts.'
     },

    {
        'tags': ['SE', 'SC'],
        'use_columns': "A,B,C,D,E",
        'mk_name': 'symbolic_execution_related_papers.md',
        'data_to_be_present': ['paper','year','venue','link'],
        'write_method': 'write_markdown_0',
        'description': 'A bibliography of papers related to symbolic execution of Ethereum smart contracts.'
    },

    {
        'tags': ['SV', 'sv'],
        'use_columns': "A,B,C,D,E",
        'mk_name': 'security_vulnerabilities.md',
        'data_to_be_present': ['paper', 'year', 'venue', 'link'],
        'write_method': 'write_markdown_0',
        'description': 'A bibliography of papers on security vulnerabilities in Ethereum smart contracts'
    },

    {
        'tags': ['Survey','survey'],
        'use_columns': "A,B,C,D,E",
        'mk_name': 'survey_literature_review.md',
        'data_to_be_present': ['paper', 'year', 'venue', 'link'],
        'write_method': 'write_markdown_0',
        'description': 'A bibliography of survey papers or literature reviews.'
    },
]



