from common import *

def request_driver_and_type(pass_id, d_rating, r_type):
    print('Find a driver with a rating >= '+str(d_rating)+' and a(n) '+r_type+ \
          ' vehicle and insert into Trips')
    query = '''
        INSERT INTO Trips(date, start_time, end_time, pickup_location,
                          destination, distance, duration, fee, driver_id)
            VALUES('2019-11-28', '07:00:00', '07:30:00', '123 Blue St.',
                   '124 Red St.', 5.0, 30, 7.65,
                   (SELECT d.user_id
                      FROM Drivers as d
                           JOIN Ride_Types as r
                             ON d.vehicle_type = r.ride_type_id
                     WHERE (d.driver_rating >= %s) AND (r.name = %s)
                     LIMIT 1)
        );

        SELECT * FROM Trips;
    '''
    cmd = cur.mogrify(query, (d_rating, r_type))
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
    print("Passenger-"+str(pass_id)+" got a ride from a "+str(d_rating)+ \
          " driver in a(n) "+r_type+" vehicle")

print('''user-story-6:
   As a:  Passenger
 I want:  To be able to be picked up only by drivers above a certain
          rating with a certain type of car
So that:  I can enjoy from the best-quality driving and car experience

Complex
''')
request_driver_and_type(3, 4.2, 'XL')
