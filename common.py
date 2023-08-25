import psycopg2 as pg2
from prettytable import PrettyTable

con = pg2.connect(database='project', user='isdb')
con.autocommit = True
cur = con.cursor()

SHOW_CMD = True
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))
