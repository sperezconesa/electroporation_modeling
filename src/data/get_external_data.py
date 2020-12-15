from fetch_data import gsheet_to_csv
from fetch_data import gsheet_to_csv,gsheet_to_csv_url
external_data_dir = './data/external/'
for i in ['APM1', 'APM2', 'APM3', 'APM4', 'BPM1', 'BPM2', 'BPM3', 'BPM4']:
    gsheet_to_csv_url('https://docs.google.com/spreadsheets/d/1zBEQ2AH5vEv1mTwgjwWeu0TDon-cZyZODDN_BCjWpCk/edit#gid=0', f'{i}', external_data_dir+f'{i}.csv')
