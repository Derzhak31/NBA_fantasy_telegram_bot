import requests, json
from datetime import datetime
from create_bot import headers




def match():
    day = datetime.now().strftime('%Y-%b-%d')
    url = f'https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/{day}'
    response = requests.get(url, headers=headers).text
    data = json.loads(response)
    match_res = ''
    for item in data:
        away = item['AwayTeam']
        home = item['HomeTeam']
        away_total = item['AwayTeamScore']
        home_total = item['HomeTeamScore']
        match_res = match_res + f'{away} {away_total} : {home_total} {home}\n'
    match_res = match_res.replace('None : None', 'матч не начался')
    return match_res

def standings():
    url = 'https://api.sportsdata.io/v3/nba/scores/json/Standings/2023'
    response = requests.get(url, headers=headers).text
    data = json.loads(response)
    table_conf, table_conf_e, table_conf_w, table_div, table_div_a, table_div_c, table_div_s, table_div_n, table_div_p, table_div_sw = ('',)*10
    for item in sorted(data, key=lambda x: x['ConferenceRank']):
        rank_conf = item['ConferenceRank']
        rank_div = item['DivisionRank']
        team = item['Key']
        w = item['Wins']
        l = item['Losses']
        per = item['Percentage']
        series = item['StreakDescription']
        conf = item['Conference']
        div = item['Division']
        # Конференции
        if conf == 'Eastern':
            table_conf_e = table_conf_e + f'{rank_conf} {team} {series} {per} ({w}-{l})\n'
        else:
            table_conf_w = table_conf_w + f'{rank_conf} {team} {series} {per} ({w}-{l})\n'
        # Дивизионы
        if div == 'Atlantic':
            table_div_a = table_div_a + f'{rank_div} {team} {series} {per} ({w}-{l})\n'
        elif div == 'Central':
            table_div_c = table_div_c + f'{rank_div} {team} {series} {per} ({w}-{l})\n'
        elif div == 'Southeast':
            table_div_s = table_div_s + f'{rank_div} {team} {series} {per} ({w}-{l})\n'
        elif div == 'Northwest':
            table_div_n = table_div_n + f'{rank_div} {team} {series} {per} ({w}-{l})\n'
        elif div == 'Pacific':
            table_div_p = table_div_p + f'{rank_div} {team} {series} {per} ({w}-{l})\n'
        else:
            table_div_sw = table_div_sw + f'{rank_conf} {team} {series} {per} ({w}-{l})\n'
    table_conf = f'Eastern\n{table_conf_e}Western\n{table_conf_w}'
    table_div = f'Atlantic\n{table_div_a}Central\n{table_div_c}Southeast\n{table_div_s}Northwest\n{table_div_n}Pacific\n{table_div_p}Southwest\n{table_div_sw}'
    return f'{table_conf}\n{table_div}'


