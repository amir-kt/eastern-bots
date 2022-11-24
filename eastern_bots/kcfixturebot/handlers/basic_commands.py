from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from .utils import messages

from ..bot import dp


@dp.message(Command(commands=["start"]))
async def start(message: types.Message, state: FSMContext):
    await state.set_state(State("started"))
    await message.answer(messages.start_message)
