# gearBot
bdo gear database, super simple just recently finished coverting the main into cogs which helps for readability.

## Requirements

> pip install -r requirements.txt

> python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]

or if you're using zsh

> python3 -m pip install -U git+"https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]"

Then set up your python path

> export PYTHONPATH="/PATH/TO/gearBot/cogs/modules"

## Database Schema

```CREATE TABLE gear (userId int,name varchar(255),link varchar(255),ap int,dp int,id varchar(255))ENGINE=InnoDB DEFAULT CHARSET=utf8;```

## Contact me
If you have any questions you can contact me via discord; n0tj#6859 