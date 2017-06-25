import csv

class CSVread:
    def __init__(self, file):
        self.file = file

    def get_file(self):
        try:
            with open(self.file, "r") as f:
                self.reader = [row for row in csv.reader(f, delimiter = ",")]
                return self.reader
        except IOError as err:
            print("I/O error({0}): {1}".format(errno, strerror))
        return

     
