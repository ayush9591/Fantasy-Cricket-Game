import sqlite3

#connecting to cricket_db.db
db = sqlite3.connect("cricket_db.db")
cur = db.cursor()
cur.execute("select * from match;")
p_info = cur.fetchall()

def calculate_points(p_info):
    points = 0.0
    score = p_info[1]
    fours=float(p_info[3])
    sixes=float(p_info[4])
    twos = int((score - 4 * fours - 6 * sixes) / 2)
    wickets = float(p_info[8])
    # Strike rate = runs/balls faced
    try:
        strike_rate = float(p_info[1]) / float(p_info[2])
    except:
        strike_rate = 0
    # Economy rate = given runs/over(bowled in over)
    try:
        economy = float(p_info[7]) / (float(p_info[5]) / 6)
    except:
        economy = 0
    Fielding = float(p_info[9]) + float(p_info[10]) + float(p_info[11])

    # 1 point for hitting a boundary and 2 runs ,2 points for over boundary,10 points each for catch and wicket
    points += (twos + fours + 2 * sixes + 10 * Fielding + 10*wickets)

    if score >= 50:
        points += 5  # 5 points for century
        if score >= 100:
            points += 10  # 10 points for half century

    if strike_rate > 1:  # for strike rate>100
        points += 4
    elif strike_rate >= 0.8:
        points += 2  # 2 points for strike rate >= 80

    if wickets >= 3:
        points += 5  # Additional 5 points for 3 wickets
        if wickets > 5:
            points += 10  # Additional 5 points for 3 wickets

    if economy >= 3.5 and economy <= 4.5:
        points += 4  # 4 points for eco rate between 3.5 and 4.5
    elif economy >= 2 and economy < 3.5:
        points += 7  # 7 points for economy rate between 2 and 3.5
    elif economy < 2:
        points += 10  # 10 points for economy rate less than 2
    return points

player_points = {}
for i in p_info:
    player_points[i[0]] = calculate_points(i)

print(player_points)

