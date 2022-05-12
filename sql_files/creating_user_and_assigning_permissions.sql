create user 'hms_user'@'localhost' identified by '1234';
grant all privileges on *.* to 'hms_user'@'localhost';
create database if not exists hms;
show databases;
