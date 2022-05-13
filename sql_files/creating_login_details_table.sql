create table if not exists login_details(
user_role  varchar(45) not null,
user_name varchar(45) not null,
password varchar(45) not null,
unique(user_name)
)