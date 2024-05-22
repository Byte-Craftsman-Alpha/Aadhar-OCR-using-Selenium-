# Image to Text Extraction and JSON Conversion using Selenium and AI Assistant
This Python script uses Selenium WebDriver to extract text from an image and convert it into a JSON format using an AI assistant. The script is divided into several blocks, each with a specific function.

# Required Modules
The following modules are required to run this script:

`selenium`: Web browser automation
You can install the required modules using pip:
```bash
pip install selenium
```

# Block 1: Import Required Libraries
The first block imports the required libraries and sets the path to the image file.

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

image_file_path = r'<path of your file>'
driver = webdriver.Chrome()
```
# Block 2: Text Extractor Class
The text_extractor class is used to extract text from an image using the Image to Text website. The class takes the image file path, Selenium WebDriver, and timeout as input.

```python
class text_extractor:
    def __init__(self, image_file, driver, timeout=10):
        # Initialize variables
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
```
# Block 3: You Chat Class
The you_chat class is used to interact with the You.com AI assistant. The class takes the Selenium WebDriver, prompt, and timeout as input.

```python
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
```
#Block 4: Extract Text and Convert to JSON
The following block uses the text_extractor and you_chat classes to extract text from an image and convert it into a JSON format.

```python
aadhar = text_extractor(image_file_path, driver)
aadhar_text = aadhar.extract()

prompt = you_chat(driver, f"I want you to convert this raw text into a JSON format containing details such as Name_in_Hindi, Name_in_English, DOB, Gender_in_Hindi, Gender_in_english, Aadhar_No, ```{aadhar_text}```")
b = prompt.json
print(b)
```
#Block 5: Quit WebDriver
The final block quits the Selenium WebDriver.

```python
driver.quit()
```
# Modifying the Script
You can modify the script to extract different types of information from the image or use a different AI assistant. To do this, you need to modify the prompt passed to the you_chat class.

For example, if you want to extract the name and address from the image, you can modify the prompt as follows:

```python
prompt = you_chat(driver, f"I want you to extract the name and address from this raw text: `{aadhar_text}`")
```
You can also use a different AI assistant by modifying the URL and CSS selectors used in the you_chat class. For example, if you want to use Google Assistant instead of You.com, you can modify the code as follows:

```python
class you_chat:
    def __init__(self, driver, prompt, timeout=10):
        self.you_chat = driver
        self.prompt = prompt
        self.max_max_timeout = timeout*3
        self.max_timeout = timeout
        self.you_chat.get("https://assistant.google.com/")
        self.prompt_input = WebDriverWait(self.you_chat, self.max_timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="userInput"]'))
        )
        self.prompt_input.send_keys(prompt)
        self.send_button = WebDriverWait(self.you_chat, self.max_max_timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="input_submit"]'))
        )
        self.response_container = WebDriverWait(self.you_chat, self.max_max_timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="userOutput"]'))
        )

        self.response = self.you_chat.execute_script("return(document.querySelector(`[data-testid='userOutput']`).parentNode.innerText)")
        self.json = "{"+self.response.split('{')[1].split('}')[0]+"}"
```
- Make sure to install the necessary Selenium package (pip install selenium) and the Chrome WebDriver (available here) before running the script.
