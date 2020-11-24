import os
import pickle

class File:
    # To check whether the file empty
    def isFileEmpty(self, argv):
        return os.stat(argv).st_size == 0

    # To check whether the file exist
    def isFileExist(self, argv):
        return os.path.exists(argv)

    # To read a byte file
    def read_file(self, argv):
        objects = []
        if (self.isFileExist(argv)):
            if (not self.isFileEmpty(argv)):
                with (open(argv, "rb")) as openfile:
                    while True:
                        try:
                            objects.append(pickle.load(openfile))
                        except EOFError:
                            break
        return objects

    # To write byte file
    def write_byte_file(self, file_name, app):
        with open(file_name, 'ab') as handle:
            pickle.dump(app, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # To write a file
    def write_file(self, file_name, app):
        with open(file_name, 'a') as the_file:
            the_file.write(app)    
    
    # Load file to objects
    def load_file(self, objects):
        return pickle.loads(objects)

    # dump the objects
    def dump_file(self, objects):
        return pickle.dumps(objects)