from app.api.v1.team.expected.models.team_expected import TeamExpected
from app.api.v1.team.expected.models.team_season import TeamSeason
from app.api.v1.team.expected.services.computation.pythagorean_wins import compute_pythagorean_wins
from app.api.v1.team.expected.services.scrape.scrape_team_season import scrape_team_season_data


def orchestrate_team_expected(season_year: int) -> dict[str, TeamExpected]:
    team_season_data = scrape_team_season_data(season_year)
    result = _compute_team_expected_data(team_season_data)

    return result


def _compute_team_expected_data(team_season_data: list[TeamSeason]) -> dict[str, TeamExpected]:
    # Define pythagorean exponent variables
    morey_exponent = 13.91
    hollinger_exponent = 15

    teams = {}
    for team_season in team_season_data:
        team_name = team_season.team_name
        team_wins = team_season.team_advanced.wins
        team_losses = team_season.team_advanced.losses
        pts_scored = team_season.team_total.pts_scored
        pts_allowed = team_season.opponent_total.pts_allowed

        morey_pythagorean = compute_pythagorean_wins(
            morey_exponent, team_wins, team_losses, pts_scored, pts_allowed)
        hollinger_pythagorean = compute_pythagorean_wins(
            hollinger_exponent, team_wins, team_losses, pts_scored, pts_allowed)

        teams[team_name.lower()] = TeamExpected(
            name=team_name,
            wins=team_wins,
            losses=team_losses,
            record=f'{team_wins}-{team_losses}',
            morey_pythagorean=morey_pythagorean,
            hollinger_pythagorean=hollinger_pythagorean)

    result = dict(sorted(teams.items()))

    return result


if __name__ == '__main__':
    result = orchestrate_team_expected(season_year=2023)
    print('debug')
