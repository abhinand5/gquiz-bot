# Import required utilities from Selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_answer_key(driver, filled_form):
    """Function to automatically open the web browser to read and store the question-answer pairs in memory

    Args:
        driver (selenium.webdriver.Chrome): Your Google Chrome Web Driver
        filled_form (str): URL of the form to read the answers from 

    Returns:
        list: List of the questions found
        dict: Answer-Key extracted from the provided form
    """

    driver.get(filled_form)

    try:
        score = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "freebirdFormviewerViewHeaderGradeFraction"))
        )

        score_obtained, total_score = map(int, score.text.split('/'))

        if score_obtained / total_score < 0.8:
            resp = input(f"LOW SCORE - ({score.text}) | ARE YOU SURE? (y/n) : ") 
            if resp == 'n':
                driver.quit()
        
        questions_container = driver.find_elements_by_class_name("freebirdFormviewerViewNumberedItemContainer")

        question_list = []
        answers_list = []

        for question in questions_container:
            q = question.find_element_by_class_name("freebirdFormviewerViewItemsItemItemTitle")
            # print(q.text)
            question_list.append(q.text)

            is_correct = question.find_element_by_class_name("freebirdFormviewerViewItemsItemCorrectnessIcon").get_attribute("aria-label")
            # print(correctness)

            if is_correct == 'Correct':
                answer = question.find_elements_by_class_name("isChecked")[0].text.strip()
            else:
                answer = question.find_elements_by_class_name("isChecked")[2].text.strip()

            answers_list.append(answer)

        answer_key = dict(zip(question_list, answers_list))

        return question_list, answer_key

    except Exception as e:
        print(f"CAUGHT ERROR - {e}")
        driver.quit() 

        return None, None


def fill_answers(driver, form, *args, **kwargs):
    """Function to open the browser and automatically fill the form with extracted answers

    Args:
        driver (selenium.webdriver.Chrome): Your Google Chrome web driver
        form (str): URL of the form to be filled with extracted answers

    Raises:
        Exception: Errors will be logged on the console
    """

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(form)

    question_list, answer_key = args

    try:
        question_container = driver.find_elements_by_class_name("freebirdFormviewerViewNumberedItemContainer")

        for question in question_container:
            q = question.find_element_by_class_name("freebirdFormviewerComponentsQuestionBaseTitle").text
            
            if q not in question_list:
                raise Exception("Question not found in answer key")

            answer = answer_key[q]

            answer_button = question.find_elements_by_class_name("docssharedWizToggleLabeledLabelText")
         
            for a in answer_button:
                if a.text.strip() == answer:
                    a.click()

    except Exception as e:
        print(f"CAUGHT ERROR - {e}")
        driver.quit() 