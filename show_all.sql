\echo Users table: all users of the uber app (including drivers, passengers, and business reps)
SELECT * FROM Users;

\echo Drivers table: all users that are drivers
SELECT * FROM Drivers;

\echo Passengers table: all users that are passengers (individual users that request rides)
SELECT * FROM Passengers;

\echo Business_Reps table: all users that are business representatives
SELECT * FROM Business_Reps;

\echo Work_with: Relationship between business reps and passengers: the business representatives in this table can give rides to their designated passengers
SELECT * FROM Work_with;

\echo Ride_Types table: all the different types of rides available
SELECT * FROM Ride_Types;

\echo Trips table: all of the completed trips so far
SELECT * FROM Trips;

\echo Casual_Trips table: trips that involve just passengers (i.e. trips not requested by businesses for passengers)
SELECT * FROM Casual_Trips;

\echo Business_Trips table: trips given by business reps to passengers
SELECT * FROM Business_Trips;
