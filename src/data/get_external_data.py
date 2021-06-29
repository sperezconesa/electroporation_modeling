from fetch_data import gsheet_to_csv, gsheet_to_csv_url

external_data_dir = "./data/external/"
for i in [
    "APM","APM-hyp","BPM","BPM-hyp"
]:
    gsheet_to_csv_url(
        "https://docs.google.com/spreadsheets/d/1NuCvZ9va10beMuAz-WwBUTq40x80DMJD3uito4NiDRQ/edit#gid=0",
        f"{i}",
        external_data_dir + f"{i}.csv",
    )
