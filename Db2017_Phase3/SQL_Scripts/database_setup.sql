-- This file contains the initial setup for the DisasterApp Database
-- Run these commands separately on postgresql terminal (Maybe)

-- Create a user named 'disappusr' with password 'icom5016'
CREATE USER disappusr WITH PASSWORD 'icom5016' SUPERUSER CREATEROLE CREATEDB;

-- Create a database named 'disaster_app_db'
CREATE DATABASE disaster_app_db;

-- Grant privileges of created database to created user
GRANT ALL PRIVILEGES ON DATABASE disaster_app_db TO disappusr;