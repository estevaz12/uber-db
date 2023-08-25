from common import *

def total_milage_ondate(id, selected_date):
    print("""The following query will find the rows matching the desired driver_id and date
    and sum up all the miles driven (distance) on that date to calculate the total milage.
    """)
    query = '''
        SELECT sum(distance)
          FROM Trips
         WHERE driver_id = %s and date = %s
    '''
    cmd = cur.mogrify(query, [id, selected_date])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Result Table: ", rows)
    print("""Result: The total milage for the driver with id %s on date %s is: """ % (id, selected_date), rows[0][0])

print('''
User-Story-4:
   As a:  driver,
 I want:  to find  the total number of miles driven on a day
So that:  I can budget my gasoline usage.

Simple User Story
''')
total_milage_ondate(8, "2019-11-17")
