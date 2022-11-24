from textwrap import dedent

start_message = dedent(
    """\
    *Use me to get the game time of your next basketball game at Casey stadium.

    /team - to select the name of your team
    /next - to get your next game's fixture
"""
)

set_team_message = dedent(
    """\
    What is your team name?
"""
)


def team_selected(team_name):
    return dedent(
        f"""\
        \"{team_name}\" has been selected as your team
    """
    )


def next_message(team_name, game_day, game_time):
    return dedent(
        f"""\
        The next game for {team_name} is on {game_day} at {game_time}
    """
    )
