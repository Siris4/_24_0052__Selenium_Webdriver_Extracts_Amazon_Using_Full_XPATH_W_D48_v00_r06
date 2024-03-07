
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

url = "https://www.amazon.com.mx/King-6-8Kg-Chocolate-Ronnie-Coleman/dp/B010V80O6U/ref=sr_1_1?__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3HU8WC4XGEE1P&dib=eyJ2IjoiMSJ9.8zJrbK9-7ryYD1sv6SuB-9kebI1sRsdJjXV1x4TjWurcsuheh1yedYrLZ97__19cY0TZVYDAZT4f6CyDRZFnQm6maMvUhjmJgQc-exONqiJoNdo5s-z8eGnG_oW117HfODYQBkkwA6x7XienYSH-VQRoe5eRAjGv1dBo18eOWoZJKVU8a-mf3o3oDWMUfkud6w2Kb11BHRVnVwfBPp7VL_lqMic8wPUNShVbJqOqY1_IMCLxw_vXsjwIwYmr742mKfK4jHzQQ4BhDdEbQ43-viDFcNJUJ3VgjKp7WaFJCs4.6r3RdcQgrL_awo17kcdqz-ZP9eP4W6equPef6J1Dmlo&dib_tag=se&keywords=king+mass&qid=1709600277&sprefix=king+mass+%2Caps%2C131&sr=8-1&ufe=app_do%3Aamzn1.fos.4e545b5e-1d45-498b-8193-a253464ffa47"

# opening Chrome:
options = webdriver.ChromeOptions()

# and keeping Chrome open:
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

# Ways to find the data:

# CLASS_NAME:
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-decimal")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# OR:

# FULL XPATH:
price_dollar = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[4]/div[3]/div[4]/div[14]/div/div/div[3]/div[1]/span[2]/span[2]/span[2]")
price_cents = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[4]/div[3]/div[4]/div[14]/div/div/div[3]/div[1]/span[2]/span[2]/span[3]")

# OR:

# CSS_Selector:
# price_dollar = driver.find_element(By.CSS_SELECTOR, value="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole")
# price_cents = driver.find_element(By.CSS_SELECTOR, value="#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-fraction")




print(f"The price of your product is: ${price_dollar.text}.{price_cents.text}.")








# closes the active and single tab (not all of them, and doesn't necessarily shutdown the Chrome browser):
# driver.close()

# quits the entire web browser INCLUDING all of the tabs that are still OPEN (the moment it loads the webpage):
driver.quit()    # COMMENT THIS OUT TO KEEP IT OPEN!!!!




