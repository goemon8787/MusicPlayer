class AudioInfo:
    def __init__(self, title, path, album=None, artist=None):
        self.title = title
        self.album = album
        self.artist = artist
        self.path = path.replace("'", "\\'")
        print(self.path)

    def __repr__(self):
        mem = [f"{key}={value!r}" for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(mem)})"

    def __str__(self):
        return (
            f"Title: {self.title}, Path: {self.path}, "
            f"Album: {self.album}, Artist: {self.artist}"
        )

    def get_insert_query(self, table_name):
        column_names = ["path", "title"]
        valuelist = [self.path, self.title]
        if self.album is not None:
            column_names.append("album")
            valuelist.append(self.album)
        if self.artist is not None:
            column_names.append("artist")
            valuelist.append(self.artist)
        columns = ", ".join(column_names)
        values = ", ".join("%s" for _ in valuelist)  # パラメータ化されたクエリのためにプレースホルダを使用

        return f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

    def get_select_query(self, table_name):
        return f"SELECT * FROM {table_name} WHERE path = %s AND title = %s"  # パラメータ化されたクエリのためにプレースホルダを使用
