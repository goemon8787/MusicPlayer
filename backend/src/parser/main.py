from pathlib import Path

import mutagen
from core.AudioInfo import AudioInfo


def isAudio(file):
    # 楽曲ファイル判定にしたい
    return file.is_file()


if __name__ == "__main__":
    root_path = Path("/data")

    filelist = list(root_path.glob("**/*"))
    filelist = [
        file for file in filelist if isAudio(file) and mutagen.File(file) is not None
    ]

    for file in filelist:
        m = mutagen.File(file)
        if isinstance(m, mutagen.aiff.AIFF):
            title = m["TIT2"]
            album = m["TALB"]
            artist = m["TPE1"]
            path = file
            audioInfo = AudioInfo(title=title, album=album, artist=artist, path=file)

        if isinstance(m, mutagen.flac.FLAC):
            title = m["title"][0]
            album = m["album"][0]
            artist = m["artist"][0]
            path = file

        info = AudioInfo(title=title, album=album, artist=artist, path=file)
        print(repr(info))
