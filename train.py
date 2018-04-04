import sqlite3
import pandas as pd


db_file = "C:\\sqlite\db\pythonsqlite.db"

# for db in db_file:
conn = sqlite3.connect(db_file)
c = conn.cursor()
limit = 50
last_unix = 0
cur_length = limit
counter = 0
test_done = False
	
while cur_length == limit:
	
	df = pd.read_sql("SELECT * FROM interviews WHERE role NOT NULL;", conn)
	cur_length = len(df)

	np_df = df.as_matrix()
	# for i in range(cur_length):
	# 	row = np_df[i]
	# 	if row[2] == "A":
	# 		print(row[3])

	if not test_done:
	    with open('test.from','a', encoding='utf8') as f:
	    	for i in range(cur_length):
	    		row = np_df[i]
	    		if row[2] == "Q":
	    			f.write(row[3]+'\n')

	    with open('test.to','a', encoding='utf8') as f:
	        for i in range(cur_length):
	        	row = np_df[i]
	        	if row[2] == "A":
	        		f.write(row[3]+'\n')

	    test_done = True
	    print("true")

	else:
		with open('test.from','a', encoding='utf8') as f:
			for i in range(cur_length):
				row = np_df[i]
				if row[2] == "Q":
					f.write(row[3]+'\n')

		with open('test.to','a', encoding='utf8') as f:
			for i in range(cur_length):
				row = np_df[i]
				if row[2] == "A":
					f.write(row[3]+'\n')

		print("else")


	counter += 1
	if counter % 20 == 0:
		print(counter*limit,'rows completed so far')




