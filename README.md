# gearBot
bdo gear database.


## Requirements

> pip install -r requirements.txt

> python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]


## Database Schema

> CREATE TABLE gear (userId int,name varchar(255),link varchar(255),ap int,dp int,id varchar(255))ENGINE=InnoDB DEFAULT CHARSET=utf8;