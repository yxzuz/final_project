# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os, copy

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
    for dictionary in Db.search(table_name).table:
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

    def delete(self, my_dict):
        self.table.delete(my_dict)


    def update(self):
        pass

    def join(self, other_table, common_key):
        joined_table = Table(self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps


    def __str__(self):
        return 'Table: ' + self.table_name + str(self.table)


# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary

# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
