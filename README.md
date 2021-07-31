**Requirements**
- Bot token in config.json
- CoC API Key in cogs/CoC.py
- a set up CoC Database of all players from 2015-07 to today
- CoC Database name in cogs/CoC.py
- DB Tables must be named by the coc API seasons endpoint call, e.g. 2020-05

**Update the bot**
- Update your database to the latest datasets using the datatodb.py script. [COMMENT THE DATES OUT YOU ALREADY HAVE AND ADD THE DATES YOU NEED, ALSO IN THE CoC class in cogs/CoC.py (self.LEGEND_SEASONS)]