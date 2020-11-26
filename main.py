import yaml
from selenium import webdriver 
# Import the functions from ./gquiz_bot.py file
from gquiz_bot import extract_answer_key, fill_answers 

# Read bot configurations
with open("config.yml") as file:
    cfg = yaml.load(file, Loader=yaml.FullLoader)

# Your browser's web driver path
DRIVER_PATH = cfg['driver_path']
# URL of Form to be filled
FORM = cfg['form_url']
# Prefilled form with answers
FILLED_FORM = cfg['filled_form']

# Load Google Chrome User Profile details
user_profile = cfg['user_profile']
USER_DATA_DIR, USER_PROFILE = cfg['user_profile'].rsplit('\\', maxsplit=1) 

if __name__ == "__main__":
    # opens chrome with the profile mentioned
    options = webdriver.chrome.options.Options()
    options.add_argument("start-maximized")
    options.add_argument("--user-data-dir="+USER_DATA_DIR)
    options.add_argument("--profile-directory="+USER_PROFILE)
    
    # create web driver with required config
    driver = webdriver.Chrome(
        executable_path=DRIVER_PATH,
        options=options,
    )

    # Extracts the answers from prefilled form - view ./gquiz_bot.py for code
    question_list, answer_key = extract_answer_key(driver, FILLED_FORM)

    # Opens the browser and fills the form with extracted answers - view ./gquiz_bot.py for code
    fill_answers(driver, FORM, question_list, answer_key)
