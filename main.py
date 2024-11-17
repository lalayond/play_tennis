def run(points: str) -> str:
    POINTS_TO_WIN_GAME = 4
    GAMES_TO_WIN_SET = 6
    POINTS_TO_WIN_TIEBREAK = 7

    games_player_a = 0
    games_player_b = 0
    sets_player_a = 0
    sets_player_b = 0
    points_player_a = 0
    points_player_b = 0
    result = ''
    is_tiebreak = False

    for point in points:
        if point == 'A':
            points_player_a += 1
        else:
            points_player_b += 1
       
        if is_tiebreak:
            if points_player_a >= POINTS_TO_WIN_TIEBREAK and points_player_a - points_player_b >= 2:
                games_player_a += 1
                sets_player_a += 1
                result += f"{games_player_a}-{games_player_b} "
                points_player_a = points_player_b = 0
                is_tiebreak = False
                games_player_a = games_player_b = 0
            elif points_player_b >= POINTS_TO_WIN_TIEBREAK and points_player_b - points_player_a >= 2:
                games_player_b += 1
                sets_player_b += 1
                result += f"{games_player_a}-{games_player_b} "
                points_player_a = points_player_b = 0
                is_tiebreak = False
                games_player_a = games_player_b = 0
            continue

        if points_player_a >= POINTS_TO_WIN_GAME and points_player_a - points_player_b >= 2:
            games_player_a += 1
            points_player_a = points_player_b = 0
        elif points_player_b >= POINTS_TO_WIN_GAME and points_player_b - points_player_a >= 2:
            games_player_b += 1
            points_player_a = points_player_b = 0

        if games_player_a == GAMES_TO_WIN_SET and games_player_b == GAMES_TO_WIN_SET:
            is_tiebreak = True
            points_player_a = points_player_b = 0
        elif games_player_a >= GAMES_TO_WIN_SET and games_player_a - games_player_b >= 2:
            sets_player_a += 1
            result += f"{games_player_a}-{games_player_b} "
            games_player_a = games_player_b = 0
        elif games_player_b >= GAMES_TO_WIN_SET and games_player_b - games_player_a >= 2:
            sets_player_b += 1
            result += f"{games_player_a}-{games_player_b} "
            games_player_a = games_player_b = 0

    if games_player_a > 0 or games_player_b > 0:
        result += f"{games_player_a}-{games_player_b} "

    return result

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
