\c postgres

DROP DATABASE IF EXISTS project;

CREATE DATABASE project;
\c project
\i create.SQL

-- If you wanna use serial, omit id
\copy Users(first_name,last_name,email,phone) FROM Users.csv csv header
\copy Ride_Types(name,capacity) FROM Ride_Types.csv csv header
\copy Drivers(user_id,driver_rating,license_num,vehicle_license_num,vehicle_type) FROM Drivers.csv csv header
\copy Passengers(user_id,review_score) FROM Passengers.csv csv header
\copy Business_Reps(user_id, business_name, team_size) FROM Business_Representatives.csv csv header
\copy Work_with(business_rep_id, passenger_id, allowance_amount, max_num_rides) FROM Work_with.csv csv header
\copy Trips(date,start_time,end_time,pickup_location,destination,distance, duration,fee,driver_id) FROM Trips.csv csv header
\copy Casual_Trips(trip_id,passenger_id) FROM Casual_Trips.csv csv header
\copy Business_Trips(trip_id, business_rep_id, passenger_id) FROM Business_Trips.csv csv header
