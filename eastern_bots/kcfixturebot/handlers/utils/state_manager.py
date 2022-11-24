async def set_game_time(game_time, state):
    if game_time is not None and state is not None:
        data = await state.get_data()
        time, day, date = game_time
        
        data["game_date"] = date
        data["game_time"] = time
        data["game_day"] = day

        await state.set_data(data)


async def get_team_name(state):
    data = await state.get_data()
    if data is not None and "team_name" in data:
        return data["team_name"]


async def get_game_date(state):
    data = await state.get_data()
    if data is not None and "game_date" in data:
        return data["game_date"]


async def get_game_time(state):
    data = await state.get_data()
    if data is not None and "game_time" in data:
        return data["game_time"]

