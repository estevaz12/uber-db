from common import *

def spent_this_month(id, month):
    print("""The following query will find the sum of how much money Business Representatitve-%s has spent this month
      by filterinng through the Business_Reps, Business_Trips, and Trips""" %id)
    query = '''
        SELECT sum(t.fee)
          FROM Trips as t
               JOIN Business_Trips as bt
                 ON bt.trip_id = t.trip_id
               JOIN Business_Reps as br
                 ON br.user_id = bt.business_rep_id
         WHERE br.user_id = %s and t.date IN (SELECT date
                                             FROM Trips
                                            WHERE date_part('month', date) = %s);
    '''
    cmd = cur.mogrify(query, [id,month])
    print_cmd(cmd)
    cur.execute(cmd)
    rows = cur.fetchall()
    print(""" The Total Amount Spent this Month so far is: %s """ %rows[0])

print('''
User-Story-10:
   As a:  Business Representative
 I want:  to know how much I have spent on transporting my employees this month
So that:  I can keep track of spending and plan business finances accordingly.

Complex - Analytical User Story
''')
spent_this_month(2,3)
