from aiogram import Bot
from asgiref.sync import async_to_sync


@async_to_sync
async def send_fixtures(bot: Bot):
    return await bot.send_message(chat_id="-825805806", text="Hey")
