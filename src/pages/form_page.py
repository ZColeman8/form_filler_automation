from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import JavascriptException
from src.utils.logger import logger
import os
import time

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.phone_input = (By.ID, "userNumber")
        self.birthdate_input = (By.ID, "dateOfBirthInput")
        self.subject_input = (By.ID, "subjectsInput")
        self.picture_upload_input = (By.ID, "uploadPicture")
        self.address_input = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "react-select-3-input")
        self.city_dropdown = (By.ID, "react-select-4-input")
        self.submit_button = (By.ID, "submit")
        self.modal_title = (By.ID, "example-modal-sizes-title-lg")

    def dismiss_ads(self):
        try:
            self.driver.execute_script("""
                const adSelectors = ['iframe', '.adsbygoogle', '.fixedban', '[id^="google_ads_iframe"]'];
                adSelectors.forEach(sel => {
                    document.querySelectorAll(sel).forEach(el => el.remove());
                });
            """)
            logger.debug("Ads dismissed via JavaScript.")
        except JavascriptException as e:
            logger.warning(f"Ad dismissal script failed: {e}")

    def fill_first_name(self, first_name):
        logger.debug(f"Entering first name: {first_name}")
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)

    def fill_last_name(self, last_name):
        logger.debug(f"Entering last name: {last_name}")
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)

    def fill_email(self, email):
        logger.debug(f"Entering email: {email}")
        self.wait.until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def select_gender(self, gender):
        logger.debug(f"Selecting gender: {gender}")
        gender_element = self.driver.find_element(By.XPATH, f"//label[text()='{gender}']")
        self.driver.execute_script("arguments[0].click();", gender_element)

    def fill_phone(self, phone):
        logger.debug(f"Entering phone number: {phone}")
        self.wait.until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone)

    def fill_birthdate(self, birthdate):
        self.dismiss_ads()
        logger.debug(f"Entering birthdate: {birthdate}")
        birth_field = self.wait.until(EC.element_to_be_clickable(self.birthdate_input))
        birth_field.click()
        self.driver.execute_script("arguments[0].value = '';", birth_field)
        birth_field.send_keys(birthdate)
        birth_field.send_keys(Keys.RETURN)

    def fill_subject(self, subject):
        logger.debug(f"Entering subject: {subject}")
        subject_input = self.wait.until(EC.visibility_of_element_located(self.subject_input))
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.RETURN)

    def select_hobby(self, hobby):
        logger.debug(f"Selecting hobby: {hobby}")
        hobby_element = self.driver.find_element(By.XPATH, f"//label[text()='{hobby}']")
        self.driver.execute_script("arguments[0].click();", hobby_element)

    def upload_picture(self, file_path):
        picture_input = self.driver.find_element(*self.picture_upload_input)
        abs_path = os.path.abspath(file_path)
        logger.debug(f"Uploading picture from: {abs_path}")
        picture_input.send_keys(abs_path)

    def fill_address(self, address):
        logger.debug(f"Entering address: {address}")
        self.driver.find_element(*self.address_input).send_keys(address)

    def select_state_and_city(self, state, city):
        logger.debug(f"Selecting state: {state} and city: {city}")
        self.driver.find_element(*self.state_dropdown).send_keys(state)
        self.driver.find_element(*self.state_dropdown).send_keys(Keys.RETURN)
        self.driver.find_element(*self.city_dropdown).send_keys(city)
        self.driver.find_element(*self.city_dropdown).send_keys(Keys.RETURN)

    def submit(self, first_name, last_name):
        self.dismiss_ads()
        logger.debug("Clicking the submit button.")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.driver.find_element(*self.submit_button))
        self.driver.find_element(*self.submit_button).click()

        self.wait.until(EC.visibility_of_element_located(self.modal_title))

        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"confirmation_{first_name}_{last_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)

        logger.debug(f"Saving confirmation screenshot as: {filename}")

        self.driver.save_screenshot(filepath)
        logger.info(f"\n✅ Confirmation screenshot saved to: {filepath}")

    def get_confirmation_text(self):
        logger.debug("Fetching confirmation modal text.")
        modal = self.wait.until(EC.visibility_of_element_located(self.modal_title))
        return modal.text
