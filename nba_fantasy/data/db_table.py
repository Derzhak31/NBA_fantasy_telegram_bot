from nba_fantasy.create_bot import DB, API


def table_team_update():
    try:
        db = DB()
        data = API('https://api.sportsdata.io/v3/nba/scores/json/Standings/2023').data()
        with db.cur() as cur:
            for item in data:
                team_id = item['TeamID']
                win = item['Wins']
                los = item['Losses']
                per = item['Percentage']
                ser = item['StreakDescription']
                cur.execute(f"""UPDATE team_table SET win = '{win}', los = '{los}', per = '{per}', ser = '{ser}'
                                WHERE team_id = {team_id};""")
        print('[INFO] team_table updated')
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def eastern():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE conf='Eastern' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def western():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE conf='Western' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def atlantic():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Atlantic' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def central():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Central' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def northwest():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Northwest' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def pacific():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Pacific' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def southeast():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Southeast' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')


def southwest():
    try:
        db = DB()
        with db.cur() as cur:
            cur.execute("SELECT team, ser, win, los, per FROM team_table WHERE div='Southwest' ORDER BY per DESC")
            count = 0
            table = ''
            for row in cur.fetchall():
                count += 1
                x = f'{count}) {row[0]} {row[1]} {row[2]}-{row[3]}({row[4]})\n'
                table = table + x
            return table
    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if db:
            db.close()
            print('[INFO] PostgreSQL connection closed')
