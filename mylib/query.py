"""Query the SpotifyDB database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """Adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """Runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("SpotifyDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    track_name,
    artist_name,
    artist_count,
    released_year,
    released_month,
    released_day,
    in_spotify_playlists,
    in_spotify_charts,
    streams,
    in_apple_playlists,
    key,
    mode,
    danceability_percent,
    valence_percent,
    energy_percent,
    acousticness_percent,
    instrumentalness_percent,
    liveness_percent,
    speechiness_percent,
    cover_url,
):
    """Create example query for SpotifyDB"""
    conn = sqlite3.connect("SpotifyDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO SpotifyDB 
        (track_name, artist_name, artist_count, released_year, released_month, 
        released_day, in_spotify_playlists, in_spotify_charts, streams, 
        in_apple_playlists, key, mode, danceability_percent, valence_percent, 
        energy_percent, acousticness_percent, instrumentalness_percent, liveness_percent, 
        speechiness_percent, cover_url) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            track_name,
            artist_name,
            artist_count,
            released_year,
            released_month,
            released_day,
            in_spotify_playlists,
            in_spotify_charts,
            streams,
            in_apple_playlists,
            key,
            mode,
            danceability_percent,
            valence_percent,
            energy_percent,
            acousticness_percent,
            instrumentalness_percent,
            liveness_percent,
            speechiness_percent,
            cover_url,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO SpotifyDB VALUES (
            {track_name}, {artist_name}, {artist_count}, {released_year}, {released_month}, 
            {released_day}, {in_spotify_playlists}, {in_spotify_charts}, {streams}, 
            {in_apple_playlists}, {key}, {mode}, {danceability_percent}, {valence_percent}, 
            {energy_percent}, {acousticness_percent}, {instrumentalness_percent}, {liveness_percent}, 
            {speechiness_percent}, {cover_url});"""
    )


def update_record(
    record_id,
    track_name,
    artist_name,
    artist_count,
    released_year,
    released_month,
    released_day,
    in_spotify_playlists,
    in_spotify_charts,
    streams,
    in_apple_playlists,
    key,
    mode,
    danceability_percent,
    valence_percent,
    energy_percent,
    acousticness_percent,
    instrumentalness_percent,
    liveness_percent,
    speechiness_percent,
    cover_url,
):
    """Update example query for SpotifyDB"""
    conn = sqlite3.connect("SpotifyDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE SpotifyDB 
        SET track_name=?, artist_name=?, artist_count=?, released_year=?, released_month=?, 
        released_day=?, in_spotify_playlists=?, in_spotify_charts=?, streams=?, 
        in_apple_playlists=?, key=?, mode=?, danceability_percent=?, valence_percent=?, 
        energy_percent=?, acousticness_percent=?, instrumentalness_percent=?, liveness_percent=?, 
        speechiness_percent=?, cover_url=?
        WHERE id=?
        """,
        (
            track_name,
            artist_name,
            artist_count,
            released_year,
            released_month,
            released_day,
            in_spotify_playlists,
            in_spotify_charts,
            streams,
            in_apple_playlists,
            key,
            mode,
            danceability_percent,
            valence_percent,
            energy_percent,
            acousticness_percent,
            instrumentalness_percent,
            liveness_percent,
            speechiness_percent,
            cover_url,
            record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE SpotifyDB SET 
        track_name={track_name}, artist_name={artist_name}, artist_count={artist_count}, 
        released_year={released_year}, released_month={released_month}, released_day={released_day}, 
        in_spotify_playlists={in_spotify_playlists}, in_spotify_charts={in_spotify_charts}, 
        streams={streams}, in_apple_playlists={in_apple_playlists}, key={key}, mode={mode}, 
        danceability_percent={danceability_percent}, valence_percent={valence_percent}, 
        energy_percent={energy_percent}, acousticness_percent={acousticness_percent}, 
        instrumentalness_percent={instrumentalness_percent}, liveness_percent={liveness_percent}, 
        speechiness_percent={speechiness_percent}, cover_url={cover_url} 
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """Delete example query for SpotifyDB"""
    conn = sqlite3.connect("SpotifyDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM SpotifyDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM SpotifyDB WHERE id={record_id};")


def read_data():
    """Read data from SpotifyDB"""
    conn = sqlite3.connect("SpotifyDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM SpotifyDB")
    data = c.fetchall()
    log_query("SELECT * FROM SpotifyDB;")
    return data
