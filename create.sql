-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-11-27 19:58:55.207

-- tables
-- Table: Business_Reps
CREATE TABLE Business_Reps (
    user_id serial  NOT NULL,
    business_name text  NOT NULL,
    team_size int  NOT NULL,
    CONSTRAINT Business_Reps_pk PRIMARY KEY (user_id)
);

-- Table: Business_Trips
CREATE TABLE Business_Trips (
    trip_id serial  NOT NULL,
    business_rep_id serial  NOT NULL,
    passenger_id serial  NOT NULL,
    CONSTRAINT Business_Trips_pk PRIMARY KEY (trip_id)
);

-- Table: Casual_Trips
CREATE TABLE Casual_Trips (
    trip_id serial  NOT NULL,
    passenger_id serial  NOT NULL,
    CONSTRAINT Casual_Trips_pk PRIMARY KEY (trip_id)
);

-- Table: Drivers
CREATE TABLE Drivers (
    user_id serial  NOT NULL,
    driver_rating decimal(2,1)  NOT NULL,
    license_num int  NOT NULL,
    vehicle_license_num text  NOT NULL,
    vehicle_type serial  NOT NULL,
    CONSTRAINT Drivers_pk PRIMARY KEY (user_id)
);

-- Table: Passengers
CREATE TABLE Passengers (
    user_id serial  NOT NULL,
    review_score decimal(2,1)  NOT NULL,
    CONSTRAINT Passengers_pk PRIMARY KEY (user_id)
);

-- Table: Ride_Types
CREATE TABLE Ride_Types (
    ride_type_id serial  NOT NULL,
    name text  NOT NULL,
    capacity int  NOT NULL,
    CONSTRAINT Ride_Types_pk PRIMARY KEY (ride_type_id)
);

-- Table: Trips
CREATE TABLE Trips (
    trip_id serial  NOT NULL,
    date date  NOT NULL,
    start_time time  NOT NULL,
    end_time time  NOT NULL,
    pickup_location text  NOT NULL,
    destination text  NOT NULL,
    distance decimal(2,1)  NOT NULL,
    duration int  NOT NULL CHECK (duration = (DATE_PART('hour', end_time - start_time) * 60 + DATE_PART('minute', end_time - start_time))),
    fee money  NOT NULL,
    driver_id serial  NOT NULL,
    CONSTRAINT Trips_pk PRIMARY KEY (trip_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id serial  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    email text  NOT NULL,
    phone char(10)  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- Table: Work_with
CREATE TABLE Work_with (
    business_rep_id serial  NOT NULL,
    passenger_id serial  NOT NULL,
    allowance_amount money  NOT NULL,
    max_num_rides int  NOT NULL,
    CONSTRAINT Work_with_pk PRIMARY KEY (business_rep_id,passenger_id)
);

-- foreign keys
-- Reference: Business_Reps_Users (table: Business_Reps)
ALTER TABLE Business_Reps ADD CONSTRAINT Business_Reps_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Business_Trips_Business_Reps (table: Business_Trips)
ALTER TABLE Business_Trips ADD CONSTRAINT Business_Trips_Business_Reps
    FOREIGN KEY (business_rep_id)
    REFERENCES Business_Reps (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Business_Trips_Passengers (table: Business_Trips)
ALTER TABLE Business_Trips ADD CONSTRAINT Business_Trips_Passengers
    FOREIGN KEY (passenger_id)
    REFERENCES Passengers (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Business_Trips_Trips (table: Business_Trips)
ALTER TABLE Business_Trips ADD CONSTRAINT Business_Trips_Trips
    FOREIGN KEY (trip_id)
    REFERENCES Trips (trip_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Casual_Trips_Passengers (table: Casual_Trips)
ALTER TABLE Casual_Trips ADD CONSTRAINT Casual_Trips_Passengers
    FOREIGN KEY (passenger_id)
    REFERENCES Passengers (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Casual_Trips_Trips (table: Casual_Trips)
ALTER TABLE Casual_Trips ADD CONSTRAINT Casual_Trips_Trips
    FOREIGN KEY (trip_id)
    REFERENCES Trips (trip_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Drivers_Ride_Types (table: Drivers)
ALTER TABLE Drivers ADD CONSTRAINT Drivers_Ride_Types
    FOREIGN KEY (vehicle_type)
    REFERENCES Ride_Types (ride_type_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Drivers_Users (table: Drivers)
ALTER TABLE Drivers ADD CONSTRAINT Drivers_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Passengers_Users (table: Passengers)
ALTER TABLE Passengers ADD CONSTRAINT Passengers_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Trips_Drivers (table: Trips)
ALTER TABLE Trips ADD CONSTRAINT Trips_Drivers
    FOREIGN KEY (driver_id)
    REFERENCES Drivers (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Work_with_Business_Reps (table: Work_with)
ALTER TABLE Work_with ADD CONSTRAINT Work_with_Business_Reps
    FOREIGN KEY (business_rep_id)
    REFERENCES Business_Reps (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- Reference: Work_with_Passengers (table: Work_with)
ALTER TABLE Work_with ADD CONSTRAINT Work_with_Passengers
    FOREIGN KEY (passenger_id)
    REFERENCES Passengers (user_id)
    NOT DEFERRABLE
    INITIALLY IMMEDIATE
;

-- End of file.
