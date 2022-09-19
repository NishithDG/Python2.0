import mysql.connector
import json
import pandas as pd
import  numpy  as np
import re



class DM:
        conn = mysql.connector.connect(host="localhost",
                                       user = "root",
                                       password = "1234",
                                       database = "pyassign",
                                       )
        mycursor = conn.cursor()

        #table creation
        def create_table(self):
            self.conn._execute_query("DROP TABLE IF EXISTS json_to_table;")
            self.mycursor.execute("CREATE TABLE json_to_table (name varchar(100),"
                                  "phone varchar(100),"
                                  "email varchar(200),"
                                  "address varchar(255),"
                                  "region varchar(100),"
                                  "country varchar(100),"
                                  "list integer,postalzip varchar(200),currency varchar(100));")
            self.conn.commit()
            print("Table created succesfully")

            #loading db from json

        def insert_data(self):
            with open(r'sample_data_for_assignment.json', encoding="utf-8") as f:
                data = json.load(f)
                print("Data Loaded")

            for values in data["data"]:
                self.mycursor.execute("INSERT into json_to_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
                self.conn.commit()
            print("Data Added")

        #db_to_df
        def db_to_df(self):
            self.mycursor.execute("select * from json_to_table;")
            rows = self.mycursor.fetchall()

            self.df = pd.DataFrame(rows,columns=["name",
                                         "phone","email","address","region","country","list","postalzip",
                                         "currency"
                                         ])

            print(self.df)

        #format email address
        def format_email(self):
            for i in range(len(self.df)):
                email = self.df.loc[i,'email']
                newEmail = email.split('@')[0] + '@gmail.com'
                self.df.loc[i,'email'] = newEmail

            print(self.df['email'])

        def change_pin_code(self):
            self.df["postalzip"] = self.df["postalzip"].str.replace('[^0-9]', "")
            self.df["postalzip"] = self.df["postalzip"].astype(np.int64)
            print(self.df["postalzip"])

        def convert_ph_no(self, ph_no):
            ph_no = re.sub("[^0-9]", "", ph_no)
            return_string = ''
            for i in range(0, len(ph_no), 2):
                try:
                    temp_no = int(ph_no[i] + ph_no[i + 1])
                except IndexError:
                    return return_string
                if temp_no < 65:
                    return_string += "O"
                else:
                    return_string += chr(temp_no)

            return return_string

        def modify_Dataframe_for_ph_no(self):
            for i in range(len(self.df)):
                self.df.loc[i, "phone"] = self.convert_ph_no(self.df.loc[i, "phone"])
            print(self.df["phone"])

if __name__ == '__main__':
    obj = DM()
    obj.create_table()
    obj.insert_data()
    obj.db_to_df()
    obj.format_email()
    obj.change_pin_code()
    obj.modify_Dataframe_for_ph_no()