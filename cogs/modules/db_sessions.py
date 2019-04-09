import discord
from discord.ext.commands import Bot
import asyncio
import keys
import aiomysql


loop = asyncio.get_event_loop()


@asyncio.coroutine
def sql_user_mention(name):
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('select id from gear where name=%s;', name)
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        return(r)
        yield from cur.close()
        conn.close()


@asyncio.coroutine
def sql_name(name):
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop , charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('select name from gear where name=%s;', name)
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        sanitize_user_id_v1 = str(r)
        sanitize_user_id_v2 = sanitize_user_id_v1.replace("(('", "")
        sanitize_user_id_v3 = sanitize_user_id_v2.replace("',),)", "")
        return(sanitize_user_id_v3)
        yield from cur.close()
        conn.close()


@asyncio.coroutine
def sql_link(name):
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT link FROM gear WHERE name = %s;', name)
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        sanitize_user_id_v1 = str(r)
        sanitize_user_id_v2 = sanitize_user_id_v1.replace("(('", "")
        sanitize_user_id_v3 = sanitize_user_id_v2.replace("',),)", "")
        return(sanitize_user_id_v3)
        yield from cur.close()
        conn.close()


@asyncio.coroutine
def sql_id(user_id):
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT name from gear WHERE id = %s', user_id)
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        sanitize_user_id_v1 = str(r)
        sanitize_user_id_v2 = sanitize_user_id_v1.replace("(('", "")
        sanitize_user_id_v3 = sanitize_user_id_v2.replace("',),)", "")
        return(sanitize_user_id_v3)
    yield from cur.close()
    conn.close()


@asyncio.coroutine
def sql_count():
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT COUNT(*) from gear')
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        #print("SLOWER {}".format(r))
            sanitize_user_id_v1 = str(r)
            sanitize_user_id_v2 = sanitize_user_id_v1.replace("((", "")
            sanitize_user_id_v3 = sanitize_user_id_v2.replace(",),)", "")
            return(sanitize_user_id_v3)

    yield from cur.close()
    conn.close()


@asyncio.coroutine
async def sql_check_name(name):
    conn = await aiomysql.connect(host=keys.host, port=3306,
                                  user=keys.user, password=keys.password,
                                  db=keys.db, loop=loop, charset='utf8mb4')
    async with conn.cursor() as cur:
        await cur.execute('SELECT name from gear where name = %s', (name))
        r = cur.fetchall()
        # await conn.commit()
        return(r)
        #print("Name: ", r)
        conn.close()


@asyncio.coroutine
def sql_check_name_v2(name):
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT name from gear where name = %s', (name))
    r = yield from cur.fetchone()
    if not r:
        print('List is empty bruv.')
    else:
        #print("FASTER {}".format(r))
        sanitize_user_id_v1 = str(r)
        sanitize_user_id_v2 = sanitize_user_id_v1.replace("('", "")
        sanitize_user_id_v3 = sanitize_user_id_v2.replace("',)", "")
        return(sanitize_user_id_v3)

    yield from cur.close()
    conn.close()



@asyncio.coroutine
async def sql_counter():
    conn = await aiomysql.connect(host=keys.host, port=3306,
                                  user=keys.user, password=keys.password,
                                  db=keys.db, loop=loop, charset='utf8mb4')
    async with conn.cursor() as cur:
        await cur.execute('UPDATE gearData set queries = queries + 1;')
        await conn.commit()
        print("+1 Query")
        conn.close()

@asyncio.coroutine
def sql_get_counter():
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT queries from gearData;')
    r = yield from cur.fetchone()
    if not r:
        print('List is empty bruv.')
    else:
        #print("FASTER {}".format(r))
            sanitize_user_id_v1 = str(r)
            sanitize_user_id_v2 = sanitize_user_id_v1.replace("(", "")
            sanitize_user_id_v3 = sanitize_user_id_v2.replace(",)", "")
            return(sanitize_user_id_v3)

    yield from cur.close()
    conn.close()



@asyncio.coroutine
def sql_lol():
    conn = yield from aiomysql.connect(host=keys.host, port=3306,
                                       user=keys.user, password=keys.password,
                                       db=keys.db, loop=loop, charset='utf8mb4')
    cur = yield from conn.cursor()
    yield from cur.execute('SELECT COUNT(*) from gear')
    r = yield from cur.fetchall()
    if not r:
        print('List is empty bruv.')
    else:
        return(r)

    yield from cur.close()
    conn.close()


@asyncio.coroutine
async def sql_new_user(name, link, user_id):
    conn = await aiomysql.connect(host=keys.host, port=3306,
                                  user=keys.user, password=keys.password,
                                  db=keys.db, loop=loop, charset='utf8mb4')
    async with conn.cursor() as cur:
        await cur.execute('INSERT into gear (name,link) values (%s,%s)', (name, link))
        await cur.execute('UPDATE gear set id = %s where name =%s', (user_id, name))
        await conn.commit()
        print("New User!")
        conn.close()

@asyncio.coroutine
async def sql_update_link(name, link):
    conn = await aiomysql.connect(host=keys.host, port=3306,
                                  user=keys.user, password=keys.password,
                                  db=keys.db, loop=loop, charset='utf8mb4')
    async with conn.cursor() as cur:
        await cur.execute('UPDATE gear set link= %s where name= %s;', (link, name))
        await cur.execute('commit;')
        await conn.commit()
        conn.close()
