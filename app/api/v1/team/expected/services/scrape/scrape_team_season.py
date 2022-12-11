import logging

from bs4 import BeautifulSoup

from app.api.v1.team.expected.models.opponent_total import OpponentTotal
from app.api.v1.team.expected.models.team_advanced import TeamAdvanced
from app.api.v1.team.expected.models.team_season import TeamSeason
from app.api.v1.team.expected.models.team_total import TeamTotal
from app.utils.scrape.content import fetch_html_content, create_soup_instance

logger = logging.getLogger(__name__)


def scrape_team_season_data(season_year: int) -> list[TeamSeason]:
    url = f'https://www.basketball-reference.com/leagues/NBA_{season_year}.html'
    html_content = fetch_html_content(url)
    soup_instance = create_soup_instance(html_content)

    team_advanced_stats = _extract_team_advanced_stats(soup_instance)
    team_totals = _extract_team_totals(soup_instance)
    opponent_totals = _extract_opponent_totals(soup_instance)

    result = [
        TeamSeason(
            team_name=team_name,
            team_advanced=team_advanced,
            team_total=team_totals[team_name],
            opponent_total=opponent_totals[team_name]
        ) for team_name, team_advanced in team_advanced_stats.items()
    ]

    return result


def _extract_team_advanced_stats(soup_instance: BeautifulSoup) -> dict[str, TeamAdvanced]:
    advanced_stats_soup = soup_instance.find(name='table', attrs={'id': 'advanced-team'})

    result = {}
    for row in advanced_stats_soup.find_all('tr')[2:-1]:
        try:
            team_name = row.find('td', {'data-stat': 'team'}).text
            team_wins = row.find('td', {'data-stat': 'wins'}).text
            team_losses = row.find('td', {'data-stat': 'losses'}).text

            result[team_name] = TeamAdvanced(wins=int(team_wins), losses=int(team_losses))
        except AttributeError:
            pass

    return result


def _extract_team_totals(soup_instance: BeautifulSoup) -> dict[str, TeamTotal]:
    team_totals_soup = soup_instance.find(name='table', attrs={'id': 'totals-team'})

    result = {}
    for row in team_totals_soup.find_all('tr')[1:-1]:
        try:
            team_name = row.find('td', {'data-stat': 'team'}).text
            pts_scored = row.find('td', {'data-stat': 'pts'}).text

            result[team_name] = TeamTotal(pts_scored=int(pts_scored))
        except AttributeError:
            pass

    return result


def _extract_opponent_totals(soup_instance: BeautifulSoup) -> dict[str, OpponentTotal]:
    opponent_totals_soup = soup_instance.find(name='table', attrs={'id': 'totals-opponent'})

    result = {}
    for row in opponent_totals_soup.find_all('tr')[1:-1]:
        try:
            team_name = row.find('td', {'data-stat': 'team'}).text
            pts_allowed = row.find('td', {'data-stat': 'opp_pts'}).text

            result[team_name] = OpponentTotal(pts_allowed=int(pts_allowed))
        except AttributeError:
            pass

    return result
