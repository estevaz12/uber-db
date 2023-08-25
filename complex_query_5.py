from common import *

def average_trip_duration(pass_id, pickup_location, destination):
    print('Look up the average duration of trips for a certain passenger'+ \
          ' from a certain pickup_location to a certain destination')
    tmpl = '''
        SELECT c.passenger_id, t.pickup_location, t.destination, avg(t.duration)
          FROM Casual_Trips as c
               JOIN Trips as t
                    ON c.trip_id = t.trip_id
         WHERE (c.passenger_id = %s) AND (t.pickup_location = %s)
               AND (t.destination = %s)
         GROUP BY c.passenger_id, t.pickup_location, t.destination
    '''
    cmd = cur.mogrify(tmpl, (pass_id, pickup_location, destination))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    table = PrettyTable(['pass_id', 'pickup_location', 'dest', \
                         'avg. duration'])
    table.add_row(rows[0])
    print(table)

print('''user-story-9:
   As a:  Passenger
 I want:  To know the average time for certain trips
So that:  I can plan my trips ahead of time without being late

Complex - Analytical
''')
average_trip_duration(1, '123 Elm st.', '124 Elm st.')
