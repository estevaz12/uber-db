from common import *

def trip_history(pass_id):
    print('Get all the information by joining Casual_Trips and Trips on a ' + \
          'specific passenger; \n'+ \
          'get the driver information by joining Trips and Drivers; \n' + \
          'order by most recent to least')
    tmpl = '''
        SELECT t.date, t.start_time, t.pickup_location, t.destination,
               t.duration, t.fee, CONCAT(u.first_name, ' ', u.last_name),
               d.driver_rating
          FROM Casual_Trips as c
               JOIN Trips as t
                    ON c.trip_id = t.trip_id
               JOIN Drivers as d
                    ON t.driver_id = d.user_id
               JOIN Users as u
                    ON d.user_id = u.user_id
         WHERE c.passenger_id = %s
         ORDER BY t.date DESC, t.start_time DESC;
    '''
    cmd = cur.mogrify(tmpl, [pass_id])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    table = PrettyTable(['date', 'start_time', 'pickup_location', 'dest',\
    'duration', 'fee', 'driver', 'd_rating'])
    for row in rows:
        table.add_row(row)
    print(table)

print('''user-story-7:
   As a:  Passenger
 I want:  To see a history of my trips along with the driver’s information for
          each trip
So that:  I can review my trip information and my driver’s previous ratings

Complex
''')
trip_history(1)
