# Db2017
Data base resources project

# Backened System for Disaster Site Resources Locator
# Phase I- Conceptual Design


This is the phase 1 of a backend application used to manage resources on a Disaster Site using Flask. The data un the application is managed by a relational database system, and exposed to client applications through a REST API. The database engine is relational and our project is implemented in Python. The user will be able to browse categories for resoursece, search for specific items, specify who is supplying items, and who needs the items.
The application manages data from six tables:
1. User- The person who either is the administrator of the database system, a person who needs resources or a person who supplies resources
2. Request- The requests made by a user for one or more resources.
3. Resources- Resources that are being requested and shows the availability of the requested resources
4. Category- Categorizes each resource into a category
5. Request Details- has all the requests made by users with all the details of each request, including date requested, quantity and status.
6. Purchase- shows the purchases made by each user, including purchase date, resources purchased or reserved, quantity and requests.

The application is organized in three broad layers:
1. Main- Main app module takes care to setup the routes for the Rest API and calling the proper handler objects to process the request.
2. Handlers- Handlers takes care of implementing the logic of each REST call. Each handler rely upon the Data Access Objects to extract data from the database, based on the type pf request for a data. They provide the appropiate HTTP response code.
3. DAOs- Data Access Objects (DAOs) take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropiate types. For phase 1, all the DAOs are hardwired.

## Requirements

The following software is required to run this application:
1. Pyscopg2 - library to connect to PostgreSQL form Python
2. Flask - web bases framework to implement the REST API.
3. PostgreSQL - database engine
4. PgAdmin3 - app to manage the databases 
