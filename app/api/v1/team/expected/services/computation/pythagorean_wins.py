from app.api.v1.team.expected.models.pythagorean_wins import PythagoreanWins


def compute_pythagorean_wins(pythagorean_exponent: float,
                             team_wins: int,
                             team_losses: int,
                             pts_scored: int,
                             pts_allowed: int) -> PythagoreanWins:
    """Compute Pythagorean wins data & calculations"""

    win_rate = _calculate_win_rate(pythagorean_exponent, pts_scored, pts_allowed)
    win_percentage = round((win_rate * 100), 2)

    games_played = team_wins + team_losses
    expected_wins = _calculate_expected_wins(win_rate, games_played)
    expected_record = f'{expected_wins}-{games_played-expected_wins}'

    win_diff = expected_wins - team_wins
    win_diff_formatted = f'+{win_diff}' if win_diff > 0 else str(win_diff)

    result = PythagoreanWins(
        expected_record=expected_record,
        win_rate=win_rate,
        win_percentage=win_percentage,
        win_diff=win_diff,
        win_diff_formatted=win_diff_formatted)

    return result


def _calculate_win_rate(pythagorean_exponent: float, pts_scored: int, pts_allowed: int) -> float:
    """Calculate Pythagorean win rate"""

    pts_scored_var = pts_scored ** pythagorean_exponent
    pts_allowed_var = pts_allowed ** pythagorean_exponent
    result = pts_scored_var / (pts_scored_var + pts_allowed_var)

    return result


def _calculate_expected_wins(win_rate: float, num_games: int) -> int:
    """Calculate current expected wins"""

    expected_wins = win_rate * float(num_games)
    result = int(round(expected_wins, 0))

    return result
