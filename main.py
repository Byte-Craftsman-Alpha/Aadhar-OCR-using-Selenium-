import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

image_file_path = r'C:\Users\ANOOP CHAUDHARI\Documents\image.jpg'
driver = webdriver.Chrome()

class text_extractor:
    def __init__(self, image_file, driver, timeout=10):
        self.max_max_timeout = timeout*3
        self.max_timeout = timeout
        self.TextExtractor = driver
        self.TextExtractor.get("https://imagetotext.online/")
        self.file_input = WebDriverWait(self.TextExtractor, self.max_timeout).until(
            EC.presence_of_element_located((By.ID, "photo"))
        )
        self.file_input.send_keys(image_file)
        self.submit_button = WebDriverWait(self.TextExtractor, self.max_timeout).until(
            EC.visibility_of_element_located((By.ID, "submit-btn"))
        )
        self.submit_button.click()
        self.response = WebDriverWait(self.TextExtractor, self.max_max_timeout).until(
            EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, '#mydata0'), 'DOB')
        )
        self.response_text = self.TextExtractor.execute_script("return document.querySelector('#mydata0').value")
        
    def extract(self):
        return(self.response_text)
    
class you_chat:
    def __init__(self, driver, prompt, timeout=10):
        self.you_chat = driver
        self.prompt = prompt
        self.max_max_timeout = timeout*3
        self.max_timeout = timeout
        self.you_chat.get("https://you.com/?chatMode=default")
        self.prompt_input = WebDriverWait(self.you_chat, self.max_timeout).until(
            EC.presence_of_element_located((By.ID, "search-input-textarea"))
        )
        self.prompt_input.send_keys(prompt)
        self.send_button = WebDriverWait(self.you_chat, self.max_max_timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-eventactionname="click_send"]'))
        )
        self.response_container = WebDriverWait(self.you_chat, self.max_max_timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="youchat-suggestions-container"]'))
        )
        
        self.response = self.you_chat.execute_script("return(document.querySelector(`[data-testid='youchat-text']`).parentNode.innerText)")
        self.json = "{"+self.response.split('{')[1].split('}')[0]+"}"

aadhar = text_extractor(image_file_path, driver)
aadhar_text = aadhar.extract()
        
prompt = you_chat(driver, f"I want you to convert this raw text into a JSON format containing details such as Name_in_Hindi, Name_in_English, DOB, Gender_in_Hindi, Gender_in_english, Aadhar_No, ```{aadhar_text}```")
extracted_JSON = prompt.json
print(extracted_JSON)
driver.quit()
