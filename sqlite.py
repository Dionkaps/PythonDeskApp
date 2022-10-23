import sqlite3
from unicodedata import name
from AppOpener import run

conn = sqlite3.connect('javatpoint.db')
print("Opened database successfully")

conn.execute('''DROP TABLE UserData''')

conn.execute('''CREATE TABLE IF NOT EXISTS UserData
       (NAME TEXT NOT NULL,
       LINK           TEXT    NOT NULL
         );''')
print("Table created successfully")

conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('GitHub','GitHub Desktop')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Blitz','Blitz')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Notion','Notion 2.0.27')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('League of Legends','League of Legends')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Zoom','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('1','GitHub Desktop')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('2','Blitz')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('3','Notion 2.0.27')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('4','League of Legends')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('5','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('SPECIAL','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('GitHub','Blitz')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Blitz','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Notion','Notion 2.0.27')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('League of Legends','League of Legends')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('Zoom','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('1','GitHub Desktop')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('2','Blitz')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('3','Notion 2.0.27')");  
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('4','League of Legends')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('5','Zoom')"); 
conn.execute("INSERT INTO UserData (NAME,LINK) VALUES ('SPECIAL','Blitz')"); 
conn.commit()  
print("Records inserted successfully")

def select():
   data = conn.execute(" SELECT * FROM UserData");  
   
   for row in data:  
      print("NAME = ", row[0])  
      print("LINK = ", row[1], "\n") 


def find_by_name(name):
   for row in conn.execute("SELECT LINK FROM UserData WHERE NAME=?", (name,)):
      link = row[0]
      run(link)

def table_population(name_list):
   name_list = []
   data = conn.execute("SELECT DISTINCT NAME FROM UserData");  
   for row in data:  
      name_list.append(row[0])
   return  name_list

def add_new_items(name,link):
   cursor = conn.cursor()
   insert_com = "INSERT INTO UserData(NAME,LINK) VALUES(?,?)"
   data = (name,link)
   cursor.execute(insert_com,data)
   cursor.close()
   conn.commit

def delete_items(name):
   cursor = conn.cursor()
   insert_com = """DELETE FROM UserData WHERE NAME =?"""
   data = (name)
   cursor.execute(insert_com,(data,))
   cursor.close()
   conn.commit

def table_population_on_update(name_list, name):
   name_list = [] 

   for row in conn.execute("SELECT DISTINCT LINK FROM UserData WHERE NAME=?", (name,)): 
      name_list.append(row[0])
   return  name_list

def update_delete_items(name,link):
   conn.execute("DELETE FROM UserData WHERE NAME =? AND LINK=?", (name,link))
def sql_update(name,new_name):
   conn.execute("UPDATE UserData SET NAME =? WHERE NAME =?", (new_name,name))