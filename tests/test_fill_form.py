from src.pages.form_page import FormPage
from src.utils.test_data import form_test_data
from src.utils.logger import logger
import pytest

@pytest.mark.parametrize(
        "first_name, last_name, email, gender, phone, birthdate, subject, hobby, picture, address, state, city", form_test_data)

def test_fill_form(driver, first_name, last_name, email, gender, phone, birthdate, subject, hobby, picture, address, state, city):
    logger.info(f"Starting test for: {first_name} {last_name}")
    driver.get("https://demoqa.com/automation-practice-form")
    driver.refresh()

    form_page = FormPage(driver)
    form_page.dismiss_ads()

    logger.debug("Filling form fields...")
    form_page.fill_first_name(first_name)
    form_page.fill_last_name(last_name)
    form_page.fill_email(email)
    form_page.select_gender(gender)
    form_page.fill_phone(phone)
    form_page.fill_birthdate(birthdate)
    form_page.fill_subject(subject)
    form_page.select_hobby(hobby)
    form_page.upload_picture(picture)
    form_page.fill_address(address)
    form_page.select_state_and_city(state, city)

    logger.debug("Submitting the form...")
    form_page.submit(first_name, last_name)

    confirmation_text = form_page.get_confirmation_text()
    logger.debug(f"Confirmation text: {confirmation_text}")
    assert "Thanks for submitting the form" in confirmation_text
    logger.info(f"Test passed for: {first_name} {last_name}")