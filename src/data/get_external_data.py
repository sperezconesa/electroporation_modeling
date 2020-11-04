from fetch_data import gsheet_to_csv
from fetch_data import gsheet_to_csv,gsheet_to_csv_url
external_data_dir = './data/external/'
for i in ['por1', 'por2', 'por3', 'por4', 'non1', 'non2', 'non3', 'non4']:
    gsheet_to_csv_url('https://docs.google.com/spreadsheets/d/1zBEQ2AH5vEv1mTwgjwWeu0TDon-cZyZODDN_BCjWpCk/edit#gid=0', f'{i}', external_data_dir+f'{i}.csv')
