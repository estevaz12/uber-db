from common import *

def avg_earning_by_daynight(id):
    print("""The following query will find the rows matching the desired driver_id
    and carry out 2 steps:
    (1) calculate average day earning by (total earning at day)/(number of dates driven at day)
    (2) calculate average night earning by (total earning at night)/(number of dates driven at night)
    """)
    query = '''
        SELECT sum(fee), count(trip_id), sum(fee) / count(trip_id)
          FROM Trips
         WHERE driver_id = %s and start_time > '06:00:00' and start_time < '19:00:00'
    '''
    cmd = cur.mogrify(query, [id])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Result Table: ", rows)
    print("""(1) The Total earning of driver %s by day is: """ % id, rows[0][2])
    print("calculated by: total earning at day / total trips at day, or %s / %s" % (rows[0][0], rows[0][1]))

    query2 = '''
        SELECT sum(fee), count(trip_id), sum(fee) / count(trip_id)
          FROM Trips
         WHERE driver_id = %s and start_time < '06:00:00' or start_time > '19:00:00'
    '''
    cmd = cur.mogrify(query2, [id])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print("Result Table: ", rows)
    print("""(1) The average earning of driver %s by night is: """ % id, rows[0][2])
    print("calculated by: total earning at night / total trips at night, or %s / %s" % (rows[0][0], rows[0][1]))

print('''
User-Story-1:
   As a:  driver,
 I want:  to know my average earnings by day and by night
So that:  I can plan what time of the day I want to work to maximize my earnings.

Simple - Analytical User Story

Definition of Day: from 06:00:00 to 19:00:00, adjusted to the local time of the trip
Definition of Night: from 19:00:00 to 06:00:00, adjusted to the local time of the trip
''')
avg_earning_by_daynight(8)
