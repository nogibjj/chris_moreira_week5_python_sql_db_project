import requests


def extract(
    url="https://raw.githubusercontent.com/nogibjj/chris_moreira_week5_python_sql_db_project/main/data/Spotify_Most_Streamed_Songs.csv",
    file_path="data/Spotify_Most_Streamed_Songs.csv",
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
