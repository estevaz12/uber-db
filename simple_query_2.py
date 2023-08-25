from common import *

def assign_allowance_and_maxRides(b_id, p_id, allowance, maxRides):
    print('Business Representative-%s gives Passenger-%s $%s amount of money for %s rides' %(b_id, p_id,allowance, maxRides))
    query = '''
        INSERT INTO Work_with(business_rep_id, passenger_id, allowance_amount, max_num_rides)
             VALUES (%s,%s,%s,%s);

        SELECT * FROM Work_with;
    '''
    cmd = cur.mogrify(query, (b_id, p_id, allowance, maxRides))
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print()
    table = PrettyTable(['b_id', 'p_id', 'allowance', 'maxRides'])
    for row in rows:
        table.add_row(row)
    print(table)
    print('Business Representative-%s has given Passenger-%s $%s for %s' %(b_id, p_id,allowance, maxRides))

print('''user-story-2:
   As a:  Business Representative
 I want:  To assign an allowance and max number of rides to employees or clients
So that:  Different employees can request rides

Simple''')

assign_allowance_and_maxRides(2,5,75,4)
