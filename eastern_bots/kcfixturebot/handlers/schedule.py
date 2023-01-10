from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from ..bot import dp
from ..models import Schedule
from .utils import state_manager, strings


@dp.message(Command(commands=["reminder"]))
async def schedule_reminder(message: types.Message, state: FSMContext):
    team_name = await state_manager.get_team_name()
    if not team_name:
        await message.answer(strings.set_team_message)
        return

    schedule = Schedule(user_id=message.chat.id, fixture_schedule=message.text)
    schedule.save()

    await message.answer(f"schedule created for {message.text}")
