import sqlite3
import sys

if len(sys.argv) == 2:
  path = sys.argv[1]
else:
  path = ':memory:'

con = sqlite3.connect(path)
con.isolation_level = None
cur = con.cursor()

while True:
  sql = input('>>').strip()
  if sql == '':
    break
  if sqlite3.complete_statement(sql):
    try:
      cur.execute(sql)
      if sql.upper().startswith('SELECT'):
        print(cur.fetchall())
    except sqlite3.Error as e:
      print('Error : ', e.args[0])
    else:
      print('Success')
  else:
    print('Invalid sql statemet')
con.close()
print('quit')
