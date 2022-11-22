from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from . import messages

from ..bot import dp

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@dp.message(Command(commands=["next"]))
async def fixture(message: types.Message, state: FSMContext):
    await message.reply("ok")
    return
    data = await state.get_data()
    if data is None or "team_name" not in data:
        await message.reply("You need to set a team first")
        return

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(
        "https://www.playhq.com/basketball-victoria/org/casey-basketball-association/senior-domestic-summer-202223"
        "/thursday-men-b-grade/1035e459/R9")
    sleep(1.5)

    num_teams = len(driver.find_elements(
        By.XPATH,
        '//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div'
    ))
    print(f"num_teams: {num_teams}")

    for i in range(2, num_teams + 1):
        print(f'i: {i}')
        team1_name = driver.find_element(
            By.XPATH,
            f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
            f'1]/div[1]/div/a '
        ).text
        team2_name = driver.find_element(
            By.XPATH,
            f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
            f'1]/div[3]/div/a '
        ).text
        if data["team_name"] in [team1_name, team2_name]:
            datetime = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f'2]/span[1]/div[2]/span '
            ).text
            time, day, date = datetime.split(',')
            data["game_date"] = date
            data["game_time"] = time
            data["game_day"] = day
            await state.set_data(data)
            break

    driver.close()
    await message.reply(messages.next_message(data["team_name"], date, time))
