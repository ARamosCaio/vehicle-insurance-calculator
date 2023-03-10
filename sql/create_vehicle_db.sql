create database vehicles;
use vehicles;

create table car_info (
    id int not null auto_increment primary key,
    model varchar(30) not null,
    brand varchar(30) not null,
    year_manufacture varchar(4) not null,
    price decimal(9,2) not null
);

desc car_info
