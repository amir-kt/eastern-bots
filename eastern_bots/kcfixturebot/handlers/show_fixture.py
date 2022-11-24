from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .utils import messages, state_manager
from .utils.scraper import scrape_game_time

from ..bot import dp


@dp.message(Command(commands=["next"]))
async def fixture(message: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        if data is None or "team_name" not in data:
            await message.reply("You need to set a team first")
            return

        game_time = await scrape_game_time(data["team_name"])
        if game_time is not None:
            await state_manager.set_game_time(game_time, state)

        await message.reply(
            messages.next_message(
                await state_manager.get_team_name(state), 
                await state_manager.get_game_date(state), 
                await state_manager.get_game_time(state)
            )
        )

    except:
        await message.reply("Something went wrong!")
