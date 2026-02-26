# Mock version of nba_api.stats.static for offline testing


def get_teams():
    """Return a sample list of 10 NBA teams (mock data)."""

    teams = [
        {
            "id": 1610612737,
            "full_name": "Atlanta Hawks",
            "abbreviation": "ATL",
            "nickname": "Hawks",
            "city": "Atlanta",
            "state": "Georgia",
            "year_founded": 1949,
        },
        {
            "id": 1610612738,
            "full_name": "Boston Celtics",
            "abbreviation": "BOS",
            "nickname": "Celtics",
            "city": "Boston",
            "state": "Massachusetts",
            "year_founded": 1946,
        },
        {
            "id": 1610612747,
            "full_name": "Los Angeles Lakers",
            "abbreviation": "LAL",
            "nickname": "Lakers",
            "city": "Los Angeles",
            "state": "California",
            "year_founded": 1947,
        },
        {
            "id": 1610612744,
            "full_name": "Golden State Warriors",
            "abbreviation": "GSW",
            "nickname": "Warriors",
            "city": "San Francisco",
            "state": "California",
            "year_founded": 1946,
        },
        {
            "id": 1610612752,
            "full_name": "New York Knicks",
            "abbreviation": "NYK",
            "nickname": "Knicks",
            "city": "New York",
            "state": "New York",
            "year_founded": 1946,
        },
        {
            "id": 1610612748,
            "full_name": "Miami Heat",
            "abbreviation": "MIA",
            "nickname": "Heat",
            "city": "Miami",
            "state": "Florida",
            "year_founded": 1988,
        },
        {
            "id": 1610612740,
            "full_name": "New Orleans Pelicans",
            "abbreviation": "NOP",
            "nickname": "Pelicans",
            "city": "New Orleans",
            "state": "Louisiana",
            "year_founded": 2002,
        },
        {
            "id": 1610612755,
            "full_name": "Philadelphia 76ers",
            "abbreviation": "PHI",
            "nickname": "76ers",
            "city": "Philadelphia",
            "state": "Pennsylvania",
            "year_founded": 1949,
        },
        {
            "id": 1610612761,
            "full_name": "Toronto Raptors",
            "abbreviation": "TOR",
            "nickname": "Raptors",
            "city": "Toronto",
            "state": "Ontario",
            "year_founded": 1995,
        },
        {
            "id": 1610612764,
            "full_name": "Washington Wizards",
            "abbreviation": "WAS",
            "nickname": "Wizards",
            "city": "Washington",
            "state": "District of Columbia",
            "year_founded": 1961,
        },
    ]

    return teams
