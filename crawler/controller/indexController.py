from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
from webdriver_manager.chrome import ChromeDriverManager  
import time

class IndexController:  
    def __init__(self):  
        self.name = "run"  
  
    def run(self):  
        options = Options()  
        options.add_argument('--headless')  
        options.add_argument('--disable-gpu') 
        options.add_argument('--disable-dev-shm-usage') 
  
        driver = None  
        try:  
            driver = webdriver.Chrome(options=options)  
            driver.get("https://twitter.com")  
            time.sleep(5)  
            print("已打开 Twitter")  
        except Exception as e:  
            print(f"发生错误: {e}")  
        finally:  
            if driver is not None: 
                driver.quit()  