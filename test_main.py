"""
Test goes here
"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_create_record():
    """tests create_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create_record",
            "Blinding Lights",  # track_name
            "The Weeknd",  # artist_name
            "1",  # artist_count
            "2019",  # released_year
            "11",  # released_month
            "29",  # released_day
            "500",  # in_spotify_playlists
            "150",  # in_spotify_charts
            "3200000000",  # streams
            "200",  # in_apple_playlists
            "G#",  # key
            "Major",  # mode
            "65",  # danceability_percent
            "75",  # valence_percent
            "85",  # energy_percent
            "5",  # acousticness_percent
            "0",  # instrumentalness_percent
            "10",  # liveness_percent
            "4",  # speechiness_percent
            "https://cover.url",  # cover_url
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_update_record():
    """tests update_record()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update_record",
            "1",  # record_id
            "Good 4 U",  # track_name
            "Olivia Rodrigo",  # artist_name
            "1",  # artist_count
            "2021",  # released_year
            "5",  # released_month
            "14",  # released_day
            "900",  # in_spotify_playlists
            "300",  # in_spotify_charts
            "2000000000",  # streams
            "250",  # in_apple_playlists
            "A",  # key
            "Major",  # mode
            "60",  # danceability_percent
            "50",  # valence_percent
            "70",  # energy_percent
            "20",  # acousticness_percent
            "0",  # instrumentalness_percent
            "15",  # liveness_percent
            "5",  # speechiness_percent
            "https://cover.url",  # cover_url
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete_record():
    """tests delete_record()"""
    result = subprocess.run(
        ["python", "main.py", "delete_record", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_general_query():
    """tests general_query()"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "general_query",
            "SELECT * FROM SpotifyDB WHERE artist_name = 'The Weeknd'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Blinding Lights" in result.stdout


def test_read_data():
    """tests read_data()"""
    result = subprocess.run(
        ["python", "main.py", "read_data"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create_record()
    test_read_data()
    test_update_record()
    test_delete_record()
    test_general_query()
