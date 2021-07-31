from discord.ext import commands
import discord
from main import *
import mariadb
from time import time
import asyncio
import aiohttp


class CocDB:

    def __init__(self):
        self.COCDB = 'testdb123'
        self.API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg2YmRjYjMxLWRkYTQtNDRjZi1hNDM4LTc2ZjVjZDhlNjA0OCIsImlhdCI6MTYyNzY4OTU2OCwic3ViIjoiZGV2ZWxvcGVyLzgwNDFiZTZhLWJiMDktMzkyYS03ZmYyLTVlZGIwMDU0Njg4YiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjUuODMuMTkxLjEwMSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.oUm4Y4sHamlcAkOHu9-TMxOY0yGQMkSwgYv_v-vEREfOevrKJP7KsOBCN2Od7E4RNC9S93SdyQcjEdE-7YHzTw'
        self.FETCHPLAYER_API_URL = f'https://api.clashofclans.com/v1/players/'
        self.db = mariadb.connect(
            user='root', host='localhost', password=None, port=3306)
        self.c = self.db.cursor(buffered=True)
        self.c.execute(f'CREATE DATABASE IF NOT EXISTS `{self.COCDB}`')
        self.db.database = self.COCDB
        self.c.execute('SET AUTOCOMMIT=1')
        self.c.execute(
            'ALTER DATABASE {} CHARACTER SET utf8 COLLATE utf8_unicode_ci;'.format(self.COCDB))
        self.c.execute('''CREATE TABLE IF NOT EXISTS test(
            teststr TEXT,
            testint TEXT)''')


cocdb = CocDB().c
rawcocdb = CocDB()


class CoC(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.LEGEND_SEASONS = [
            '2015-07', '2015-08', '2015-09', '2015-10', '2015-11', '2015-12',
            '2016-01', '2016-02', '2016-03', '2016-04', '2016-05', '2016-06', '2016-07', '2016-08', '2016-09', '2016-10', '2016-11', '2016-12',
            '2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06', '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12',
            '2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07', '2018-08', '2018-09', '2018-10', '2018-11', '2018-12',
            '2019-01', '2019-02', '2019-03', '2019-04', '2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11', '2019-12',
            '2020-01', '2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08', '2020-09', '2020-10', '2020-11', '2020-12',
            '2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07']  # ,'2021-08','2021-09','2021-10','2021-11','2021-12']

    @commands.command()
    @commands.cooldown(2, 15, commands.BucketType.guild)
    @commands.guild_only()
    async def tag(self, ctx, tag):
        ...
        
    @commands.command()
    async def testcall(self, ctx, a,b):
        cocdb.execute('INSERT INTO test (teststr,testint) VALUES (?,?)',(a,b))
        cocdb.execute('SELECT * FROM test')
        result = cocdb.fetchall()
        await ctx.send(result)


def setup(bot):
    bot.add_cog(CoC(bot))