import argparse
from pathlib import Path

import mutagen
import MySQLdb
from core.AudioInfo import AudioInfo


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=str, default="/data")
    parser.add_argument("--host", type=str, default="music")
    parser.add_argument("--user",  type=str, default="root")
    parser.add_argument("--passwd", type=str, default="root")
    parser.add_argument("--db", type=str, default="music_player")
    parser.add_argument("--table", type=str, default="info")
    return parser.parse_args()

def isaudio(file):
    # 楽曲ファイル判定にしたい
    return file.is_file()

def get_info(file):
    m = mutagen.File(file)
    if isinstance(m, mutagen.aiff.AIFF):
        title = str(m["TIT2"])
        album = str(m["TALB"])
        artist = str(m["TPE1"])

    if isinstance(m, mutagen.flac.FLAC):
        title = m["title"][0]
        album = m["album"][0]
        artist = m["artist"][0]

    return AudioInfo(title=title, album=album, artist=artist, path=str(file))

def insert_info(info):
    cursor.execute(info.get_insert_query(args.table))

def isin_db(info):
    cursor.execute(info.get_select_query(args.table))
    row = cursor.fetchone()
    return row is not None

args = parse_args()

conn = MySQLdb.connect(
    host=args.host,
    user=args.user,
    passwd=args.passwd,
    db=args.db,
    charset='utf8'    
)
cursor = conn.cursor()


if __name__ == "__main__":
    root_path = Path("/data")

    filelist = list(root_path.glob("**/*"))

    querylist = []
    for file in filelist:
        if not isaudio(file):
            continue
        if mutagen.File(file) is None:
            continue
        
        info = get_info(file)
        
        if not isin_db(info):
            insert_info(info)

    conn.commit()
    conn.close()
