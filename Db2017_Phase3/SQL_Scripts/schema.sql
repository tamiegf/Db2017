-- This file contains the definitions of the tables used in the application.
-- In pgadmin3 inside 'disaster_app_db' select the sql button, copy this schema and click on the run button.

-- JAVIER
-- User_Address table
create table user_address(uaid serial primary key, uacity varchar(20), uaregion varchar(20), uazipcode varchar(5), gpslat float, gpslong float);

--Users table
create table users(uid serial primary key, uaid integer references user_address(uaid), uType varchar(10), ufirstname varchar(20), ulastname varchar(20));

-- TAMARA
-- Request table
create table request(reqid serial primary key, reqdate date, uid integer references users(uid));

-- Request_Details table
create table request_details(rdid serial primary key, rdqty integer, need_date date, delivery_date date, status varchar(10), reqid integer references request(reqid));

-- Resources table
create table resources(rid serial primary key, rname varchar(20), rqty integer, rprice float, uid integer references users(uid), rdid integer references request_details(rdid));

-- Category table
create table resource_category(cid serial primary key, cname varchar(20),cdescription varchar(40), rid integer references resources(rid));

-- JAVIER
--Resource_Location table
create table resource_location(rlid serial primary key, rcity varchar(20), rregion varchar(20), rid integer references resources(rid));

--Purchase table
create table purchase(pid serial primary key, pdate date, pqty integer, rdid integer references request_details(rdid), ptype varchar(10));


--JESIELY
--Credit Card table
create table creditcard(ccid serial primary key, uid integer references users(uid), ccNumber varchar(19), cvv smallint, ccExpirationDate date, sale boolean);

--Discount table
create table discount(did serial primary key, dPercent float(2), stackable boolean, rid integer references Resources(rid));

--Sales table
create table sales(sid serial primary key, pid integer references Purchase(pid));

--Does table, tiene isCustomer
create table does(ccid integer references creditcard(ccid), pid integer references Purchase(pid),isCustomer boolean, primary key(ccid,pid));


--NEW
create table user_login(lid serial primary key, user_name varchar(20), user_password varchar(20), uid integer references users(uid));
