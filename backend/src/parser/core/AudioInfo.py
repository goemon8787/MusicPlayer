class AudioInfo:
    def __init__(self, title, path, album=None, artist=None):
        self.title = title
        self.album = album
        self.artist = artist
        self.path = path

    def __repr__(self) -> str:
        mem = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(mem)})"

    def __str__(self) -> str:
        return f"Title: {self.title}, Path: {self.path}, Album: {self.album}, Artist: {self.artist}"

    def get_insert_query(self, table_name):
        column_names = ["path", "title"]
        valuelist = ["'" + self.path + "'", "'" + self.title + "'"]
        if self.album is not None:
            column_names.append("album")
            valuelist.append("'" + self.album + "'")
        if self.artist is not None:
            column_names.append("artist")
            valuelist.append("'" + self.artist + "'")
        columns = ", ".join(column_names)
        values = ", ".join(valuelist)

        return f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    
    def get_select_query(self, table_name):
        path = "'"+self.path+"'"
        title = "'"+self.title+"'"
        return f"SELECT * FROM {table_name} WHERE path = {path} AND title = {title}"
