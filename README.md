<p>
<img src= https://img.shields.io/github/last-commit/n0tj/gearBot.svg />
<a href="https://discordbots.org/bot/344643767313235968" >
  <img src="https://discordbots.org/api/widget/servers/344643767313235968.svg" alt="gearBot" />
</a>
<a href="https://discordbots.org/bot/344643767313235968" >
  <img src="https://discordbots.org/api/widget/status/344643767313235968.svg" alt="gearBot" />
</a>
</p>

# gearBot
bdo gear database, super simple just recently finished coverting the main into cogs which helps for readability.


## General Use
>!gear or !gearhelp will give you the help commands.


>!gear <@link> will update you your gear screenshot in the database.
 

>!gear <@user> will query the database for a users gear screenshot and share it to the channel where requested.



## Build
### First Step
> pip install -r requirements.txt

### Second Step
> python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]


> python3 -m pip install -U git+"https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]"

### Third Step
> export PYTHONPATH="/PATH/TO/gearBot/cogs/modules"

Set the python path, I have to figure a different way of doing this, but until then.

### Fourth Step
> mysql

> create databse gearBot

> use gearBot

> CREATE TABLE gear (userId int,name varchar(255),link varchar(255),ap int,dp int,id varchar(255))ENGINE=InnoDB DEFAULT CHARSET=utf8;

> alter database gearBot default collate utf8mb4_bin;

> SHOW VARIABLES LIKE 'collat%'; 



## Contact me
If you have any questions you can contact me via discord; n0tj#6859 

