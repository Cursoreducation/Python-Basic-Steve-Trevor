import contextlib


class DebugConnectionDB:
    def __init__(self, *args):
        self.connection_obj = db.connect(args)

    def __enter__(self):
        return self.connection_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection_obj.comit()
        self.connection_obj.close()
        return False





class Open2:
    def __init__(self, file_name, mode):
        __file = open(file_name, "r")
        self.__temp = __file.read()
        __file.close()
        self.__file_name = file_name

        try:
            self.file_obj = open(file_name, mode)
        except FileNotFoundError:
            self.file_obj = open(file_name, "w")

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type", exc_type)
        self.file_obj.close()
        if exc_type is None:
            return True

        file = open(self.__file_name, "w")
        file.write(self.__temp)
        file.close()

        if exc_type is NameError:
            return False

        return True
