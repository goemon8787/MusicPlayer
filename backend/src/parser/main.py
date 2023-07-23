import argparse
from pathlib import Path
import os

import mutagen
import MySQLdb
from core.AudioInfo import AudioInfo


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, default="/data")
    parser.add_argument("--host", type=str, default="music")
    parser.add_argument("--user", type=str, default="root")
    parser.add_argument("--passwd", type=str, default=os.environ["MYSQL_ROOT_PASSWORD"])
    parser.add_argument("--db", type=str, default="music_player")
    parser.add_argument("--table", type=str, default="info")
    return parser.parse_args()


def isaudio(file):
    # 楽曲ファイル判定にしたい
    return file.is_file()


def get_info(file):
    m = mutagen.File(file)
    if isinstance(m, mutagen.aiff.AIFF):
        title = str(m.get("TIT2"))
        album = str(m.get("TALB"))
        artist = str(m.get("TPE1"))
    elif isinstance(m, mutagen.flac.FLAC):
        title = str(m.get("title", [None])[0])
        album = str(m.get("album", [None])[0])
        artist = str(m.get("artist", [None])[0])
    elif isinstance(m, mutagen.mp3.MP3):
        title = str(m.get("TIT2"))
        album = str(m.get("TALB"))
        artist = str(m.get("TPE1"))
    elif isinstance(m, mutagen.mp4.MP4):
        title = str(m.get('\xa9nam', [None])[0])
        album = str(m.get('\xa9alb', [None])[0])
        artist = str(m.get("\xa9ART", [None])[0])
    else:
        print(type(m))
        ValueError

    return AudioInfo(title=title, album=album, artist=artist, path=str(file))


    return AudioInfo(title=title, album=album, artist=artist, path=str(file))


def insert_info(info):
    cursor.execute(info.get_insert_query(args.table), tuple(info.__dict__.values()))

def isin_db(info):
    cursor.execute(info.get_select_query(args.table), (info.path, info.title))
    row = cursor.fetchone()
    return row is not None


args = parse_args()

conn = MySQLdb.connect(
    host=args.host, user=args.user, passwd=args.passwd, db=args.db, charset="utf8"
)
cursor = conn.cursor()


if __name__ == "__main__":
    root_path = Path("/data")

    filelist = list(root_path.glob("**/*"))

    querylist = []
    for file in filelist:
        if not isaudio(file):
            continue
        try:
            if mutagen.File(file) is None:
                continue
        except mutagen.flac.FLACNoHeaderError:
            print("invalid flac file:",file)
            continue

        info = get_info(file)

        if not isin_db(info):
            insert_info(info)

    conn.commit()
    conn.close()
