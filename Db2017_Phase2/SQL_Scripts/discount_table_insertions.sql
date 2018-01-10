-- This file contains several queries to populate the 'discount' table
-- In pgadmin3 inside 'disaster_app_db' select the sql button, copy this schema and click on the run button.

insert into Discount(dPercent,stackable) values (.10, TRUE);

insert into Discount(dPercent,stackable) values (.50, TRUE);

insert into Discount(dPercent,stackable) values (.05, TRUE);

insert into Discount(dPercent,stackable) values (.35, TRUE);

insert into Discount(dPercent,stackable) values (.15, TRUE);
