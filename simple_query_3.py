from common import *

def total_earning_ondate(id, selected_date):
    print("""The following query will find the rows matching the desired driver_id and date
    and sum up all the fees earned on that date to calculate the total earning.
    """)
    query = '''
        SELECT sum(fee)
          FROM Trips
         WHERE driver_id = %s and date = %s
    '''
    cmd = cur.mogrify(query, [id, selected_date])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Result Table: ", rows)
    print("""Result: The total earning for the driver with id %s on date %s is: """ % (id, selected_date), rows[0][0])

print('''
User-Story-3:
   As a:  driver,
 I want:  to see my total earnings on a certain date,
So that:  I can keep track of my finances.

Simple User Story
''')
total_earning_ondate(8, "2019-11-17")
