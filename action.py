import json
import sqlite3



#insert_sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date) VALUES (?,?,?,?,?,?) '''


con = sqlite3.connect("techniques.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS techniques (id INT,name TEXT,description TEXT,type TEXT,die_pool INT, dam_die_pool INT)''')
con.commit()
#x=cursor.execute('''SELECT sql FROM sqlite_master WHERE name='techniques'  ''').fetchall()

print(x)

features_dict = {'name':'_empty',
				'desciption':'_empty',
				'type':"_empty",
				'id':None,
				'die_pool':0,
				'damage_die_pool':0}


def create_action_file(fd):
	json_strng = json.dumps(fd)
	with open(f'./{fd["name"]}.json','w+') as j:
		j.write(json_strng)
	j.close()

test_tech_obj = {"name":"test_technique","desciption":"some random shit","type":"lightsaber","id":0,"die_pool":10,"damage_die_pool":11}
create_action_file(test_tech_obj)
