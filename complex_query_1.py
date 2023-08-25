from common import *

def busRep_requests_for_employees(b_id, p_id):
    print('Get a driver and then insert into Trips')
    query = '''
        INSERT INTO Trips(date, start_time, end_time, pickup_location,
                            destination, distance, duration, fee, driver_id)
            VALUES('2018-05-23', '10:45:00', '11:00:00', '123 Baker St.',
                    '124 Porter St.', 3.0, 15, 9.45,
                    (SELECT d.user_id
                        FROM Drivers as d
                        LIMIT 1));

        SELECT * FROM Trips;
        '''
    cmd = cur.mogrify(query, [b_id, p_id])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    table = PrettyTable(['trip_id', 'date', 'start_time', 'end_time',\
    'pickup_location', 'destination', 'distance', 'duration', 'fee', \
    'driver_id'])
    for row in rows:
        table.add_row(row)
    print(table)
    print()
    print('Now, insert latest trip into Business_Trips')
    tmpl = '''
        INSERT INTO Business_Trips
            VALUES((SELECT max(trip_id)
                      FROM Trips), %s, %s);

        SELECT * FROM Business_Trips;'''

    cmd = cur.mogrify(tmpl, [b_id, p_id])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    table = PrettyTable(['trip_id', 'business_rep_id', 'passenger_id'])
    for row in rows:
        table.add_row(row)
    print(table)
    print()
    print("Business Representative-"+str(b_id)+" requested ride for Passenger-" + str(p_id))

print('''user-story-5:
   As a:  Business Representative
 I want:  To request rides for my employees and/or clients
So that:  they can get to their destination without using their own money

Complex
''')

busRep_requests_for_employees(2, 1)
