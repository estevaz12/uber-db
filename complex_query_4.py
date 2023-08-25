from common import *

def request_multiple_rides(pass_id, n):
    print('Insert request-by-request because trip_id\'s and driver must be different')
    for i in range(n):
        print('Get a driver and then insert into Trips')
        query = '''
            INSERT INTO Trips(date, start_time, end_time, pickup_location,
                              destination, distance, duration, fee, driver_id)
                VALUES('2019-11-28', '07:00:00', '07:30:00', '123 Blue St.',
                       '124 Red St.', 5.0, 30, 7.65,
                       (SELECT d.user_id
                          FROM Drivers as d
                         ORDER BY d.user_id ASC -- need it for OFFSET
                        OFFSET %s
                         LIMIT 1));

            SELECT * FROM Trips;
            '''
        cmd = cur.mogrify(query, [i])
        print_cmd(cmd)
        cur.execute(cmd)
        rows = cur.fetchall()
        print()
        table = PrettyTable(['trip_id', 'date', 'start_time', 'end_time',\
        'pickup_location', 'destination', 'distance', 'duration', 'fee', \
        'driver_id'])
        for row in rows:
            table.add_row(row)
        print(table)
        print()
        print('Now, insert latest trip into Casual_Trips')
        tmpl = '''
            INSERT INTO Casual_Trips
                VALUES((SELECT max(trip_id)
                          FROM Trips), %s);

            SELECT * FROM Casual_Trips;'''

        cmd = cur.mogrify(tmpl, [pass_id])
        print_cmd(cmd)
        cur.execute(cmd)
        rows = cur.fetchall()
        print()
        table = PrettyTable(['trip_id', 'passenger_id'])
        for row in rows:
            table.add_row(row)
        print(table)
    print()
    print("Passenger-"+str(pass_id)+" requested "+str(n)+" rides")

print('''user-story-8:
   As a:  Passenger
 I want:  To request multiple rides to the same location
So that:  I can transport a large group of people

Complex
''')
request_multiple_rides(1, 2)
