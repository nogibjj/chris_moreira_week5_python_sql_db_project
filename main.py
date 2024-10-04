"""handles cli commands"""

import sys
import argparse
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    update_record,
    delete_record,
    create_record,
    general_query,
    read_data,
)


def handle_arguments(args):
    """add action based on initial calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "extract",
            "transform_load",
            "update_record",
            "delete_record",
            "create_record",
            "general_query",
            "read_data",
        ],
    )

    # Here we change args[:1] to args to parse all arguments properly
    args = parser.parse_args(args)

    if args.action == "update_record":
        parser.add_argument("record_id", type=int)
        parser.add_argument("track_name")
        parser.add_argument("artist_name")
        parser.add_argument("artist_count", type=int)
        parser.add_argument("released_year", type=int)
        parser.add_argument("released_month", type=int)
        parser.add_argument("released_day", type=int)
        parser.add_argument("in_spotify_playlists", type=int)
        parser.add_argument("in_spotify_charts", type=int)
        parser.add_argument("streams", type=int)
        parser.add_argument("in_apple_playlists", type=int)
        parser.add_argument("key")
        parser.add_argument("mode")
        parser.add_argument("danceability_percent", type=int)
        parser.add_argument("valence_percent", type=int)
        parser.add_argument("energy_percent", type=int)
        parser.add_argument("acousticness_percent", type=int)
        parser.add_argument("instrumentalness_percent", type=int)
        parser.add_argument("liveness_percent", type=int)
        parser.add_argument("speechiness_percent", type=int)
        parser.add_argument("cover_url")

    if args.action == "create_record":
        parser.add_argument("track_name")
        parser.add_argument("artist_name")
        parser.add_argument("artist_count", type=int)
        parser.add_argument("released_year", type=int)
        parser.add_argument("released_month", type=int)
        parser.add_argument("released_day", type=int)
        parser.add_argument("in_spotify_playlists", type=int)
        parser.add_argument("in_spotify_charts", type=int)
        parser.add_argument("streams", type=int)
        parser.add_argument("in_apple_playlists", type=int)
        parser.add_argument("key")
        parser.add_argument("mode")
        parser.add_argument("danceability_percent", type=int)
        parser.add_argument("valence_percent", type=int)
        parser.add_argument("energy_percent", type=int)
        parser.add_argument("acousticness_percent", type=int)
        parser.add_argument("instrumentalness_percent", type=int)
        parser.add_argument("liveness_percent", type=int)
        parser.add_argument("speechiness_percent", type=int)
        parser.add_argument("cover_url")

    if args.action == "general_query":
        parser.add_argument("query")

    if args.action == "delete_record":
        parser.add_argument("record_id", type=int)

    # parse the remaining arguments
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = handle_arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract()
    elif args.action == "transform_load":
        print("Transforming data...")
        load()
    elif args.action == "update_record":
        update_record(
            args.record_id,
            args.track_name,
            args.artist_name,
            args.artist_count,
            args.released_year,
            args.released_month,
            args.released_day,
            args.in_spotify_playlists,
            args.in_spotify_charts,
            args.streams,
            args.in_apple_playlists,
            args.key,
            args.mode,
            args.danceability_percent,
            args.valence_percent,
            args.energy_percent,
            args.acousticness_percent,
            args.instrumentalness_percent,
            args.liveness_percent,
            args.speechiness_percent,
            args.cover_url,
        )
    elif args.action == "delete_record":
        delete_record(args.record_id)
    elif args.action == "create_record":
        create_record(
            args.track_name,
            args.artist_name,
            args.artist_count,
            args.released_year,
            args.released_month,
            args.released_day,
            args.in_spotify_playlists,
            args.in_spotify_charts,
            args.streams,
            args.in_apple_playlists,
            args.key,
            args.mode,
            args.danceability_percent,
            args.valence_percent,
            args.energy_percent,
            args.acousticness_percent,
            args.instrumentalness_percent,
            args.liveness_percent,
            args.speechiness_percent,
            args.cover_url,
        )
    elif args.action == "general_query":
        general_query(args.query)
    elif args.action == "read_data":
        data = read_data()
        print(data)
    else:
        print(f"Unknown action: {args.action}")


if __name__ == "__main__":
    main()
