<p>
<a href="https://github.com/n0tj/gearBot/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/w/n0tj/gearBot.svg" /></a>

<img src= https://img.shields.io/github/last-commit/n0tj/gearBot.svg />
</p>

# gearBot
bdo gear database, super simple just recently finished coverting the main into cogs which helps for readability.


## Setup
### First Step
> pip install -r requirements.txt

### Second Step
> python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]


> python3 -m pip install -U git+"https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]"

### Third Step
> export PYTHONPATH="/PATH/TO/gearBot/cogs/modules"

Set the python path, I have to figure a different way of doing this, but until then.



## Database Schema
> CREATE TABLE gear (userId int,name varchar(255),link varchar(255),ap int,dp int,id varchar(255))ENGINE=InnoDB DEFAULT CHARSET=utf8;


## Contact me
If you have any questions you can contact me via discord; n0tj#6859 

