import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/title/"

    def open_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(3)

    def apply_filters_and_search(self):
        # 1. Release Date
        release = self.driver.find_element(By.XPATH, "//label[@data-testid='accordion-item-releaseDateAccordion']")
        self.driver.execute_script("arguments[0].click();", release)
        time.sleep(2) 

        From_Date = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='releaseYearMonth-start']")
        From_Date.send_keys("2000")
        time.sleep(1)

        To_Date = self.driver.find_element(By.XPATH, "//input[@data-testid='releaseYearMonth-end']")
        To_Date.send_keys("2026")
        time.sleep(1) 

        # 2. Drama Genre
        drama = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="test-chip-id-Drama"]')
        self.driver.execute_script("arguments[0].click();", drama)
        time.sleep(1)

        # 3. IMDb Ratings
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2) 

        imdb_ratings = self.driver.find_element(By.XPATH, "//label[contains(@data-testid, 'Accordion') and contains(., 'rating')]")
        self.driver.execute_script("arguments[0].click();", imdb_ratings)
        time.sleep(2) 

        From_Rating = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='imdbratings-start']")
        From_Rating.send_keys("7.0")
        time.sleep(1)

        To_Rating = self.driver.find_element(By.XPATH, "//input[@data-testid='imdbratings-end']")
        To_Rating.send_keys("10.0")
        time.sleep(2) 

        # 4. Search Button
        self.driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@data-testid, 'adv-search-get-results')]"))
        )
        self.driver.execute_script("arguments[0].click();", search_button)
        
        # URL change hone ka wait kar rahe hain
        WebDriverWait(self.driver, 15).until(EC.url_contains("search/title/?"))
        time.sleep(5) # Page par result aane ke liye 5 sec ka sukoon bhara wait

    # NAYA FUNCTION: Jo sirf text check karega
    def is_movie_displayed(self, movie_title):
        try:
            # Hum explicitly us word ko pure screen par dhoondh rahe hain
            xpath = f"//*[contains(text(), '{movie_title}')]"
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Agar mil gaya toh uski taraf scroll karke True return kar do
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return True
        except:
            # Agar 10 second mein wo naam screen par nahi dikha, toh False return karo
            return False