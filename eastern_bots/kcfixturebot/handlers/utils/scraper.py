from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


async def scrape_game_info(team_name: str):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
    chrome_options.page_load_strategy = 'normal'

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
        ).text.lower()
        team2_name = driver.find_element(
            By.XPATH,
            f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
            f'1]/div[3]/div/a '
        ).text.lower()
        if team_name.lower() in [team1_name, team2_name]:
            datetime = driver.find_element(
                By.XPATH,
                f'//*[@id="root"]/section/main/div/div/div[1]/section/section/div/div/div/div/ul/li/div[{i}]/div/div['
                f'2]/span[1]/div[2]/span '
            ).text
            driver.close()
            return datetime.split(',')
    driver.close()
