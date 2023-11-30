# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

class ReadCsv:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.my_csv_data = []
    def read(self):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        with open(os.path.join(__location__, self.csv_file)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.my_csv_data.append(dict(r))
        return self.my_csv_data
def WriteCsv(file_name, Db,table_name,head):
    myFile = open(file_name, 'w', newline='')
    writer = csv.writer(myFile)
    writer.writerow(head)
    for dictionary in Db.search(table_name):
        writer.writerow(dictionary.values())
    myFile.close()

# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []  # tables will be added here

    def insert(self,table):
        """insert table to DB"""
        self.database.append(table)

    def search(self,table_name):
        for x in self.database:
            if x.table_name == table_name:
                return x
        return None  # table was not found in DB

    def __repr__(self):
        s = ''
        for table in self.database:
            s += str(table)
        print()
        return s



# add in code for a Table class
class Table:
    def __init__(self, table_name, table=[]):
        self.table_name = table_name
        self.table = table

    def insert(self, my_dict):
        self.table.append(my_dict)
        # add dict to list


    # def filter(self, condition=''):
    #     my_filtered = []
    #     for x in self.table:
    #         for keys in x.keys():
    #             if keys == ['last']:
    #                 my_filtered.append(keys)
    #     return my_filtered
    def __str__(self):
        return 'Table: ' + self.table_name + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
