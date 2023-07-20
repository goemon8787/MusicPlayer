class AudioInfo:
    def __init__(self, title,path,album=None,artist=None):
        self.title = title
        self.album = album
        self.artist = artist
        self.path = path
    
    def __repr__(self) -> str:
        mem = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(mem)})"
    
    