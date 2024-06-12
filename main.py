import pandas as pd

from create_ics.create_ics import create_ics

df = pd.read_excel('./exam.xls', engine='xlrd')

ics_data = create_ics(df)

ics_file_path = './exam.ics'
with open(ics_file_path, 'w', encoding='utf-8') as file:
    file.write(ics_data)
