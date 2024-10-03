import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/chris_moreira_week5_python_sql_db_project/main/Spotify%20Most%20Streamed%20Songs.csv",
    file_path="Spotify%20Most%20Streamed%20Songs.csv",
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
