from Queries.queries_Plan_Brasil import query_Brasil
from Locators.locators_Plan_Brasil import Locators_Plan_Brasil

class TestCases_Plan_Brasil():

    def __init__(self):
        self.str_Country = Locators_Plan_Brasil.str_Country
        self.int_Code_Country = Locators_Plan_Brasil.int_Code_Country
        self.int_Code_Sub_Country = Locators_Plan_Brasil.int_Code_Sub_Country
        self.str_Date = Locators_Plan_Brasil.str_Date
        self.dict_Tables = Locators_Plan_Brasil.dict_Tables

    def validate_Plan_Brasil(self):
        
        i = 1

        for table, values in self.dict_Tables.items():
            
            print(i)
            query_Brasil(table, values[0], values[1], values[2], values[3])
