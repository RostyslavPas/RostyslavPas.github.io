from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from common import feedback_api
from project.Feedback.rest_api import fb_api


def test_check_registration_slot():
    driver = webdriver.Chrome()
    try:
        page = "https://e.ticketme.org/members/KC-2024/1007"
        driver.get(page)
        found = False
        while not found:
            time.sleep(30)
            driver.refresh()
            list_items = driver.find_elements(
                By.CSS_SELECTOR, ".tb_features_pricing .table tbody tr "
                                 "td:first-child")
            for item in list_items:
                text = item.text
                print(f"Slot number: {text}")
                if text == "22":
                    print("Slot number 22 is found, call is sending!")
                    questionnaire_body = {
                        "address": "+380632059555",
                        "language": "EN",
                        "source": "manual_invite",
                        "survey": 12001
                    }
                    response = feedback_api.post(
                        f'{fb_api}/api/rest/questionnaire/',
                        json=questionnaire_body)
                    assert response.status_code in feedback_api.ok_status_code
                    questionnaire_entity = response.json()
                    QUESTIONNAIRE_HASH = questionnaire_entity['hash']
                    response = feedback_api.post(
                        f'{fb_api}/api/rest/questionnaire/{QUESTIONNAIRE_HASH}/'
                        f'invite/', json={})
                    assert response.status_code in feedback_api.ok_status_code
                    found = True
                    break
    finally:
        driver.quit()