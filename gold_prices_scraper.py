import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
time.sleep(2) 

# Base URL for historical gold prices
base_url = "https://www.bullion-rates.com/gold/INR/{}-{}-history.htm"

# Store data
gold_prices = {}

# Loop through years and months
for year in range(2007, 2026):
    for month in range(1, 13):
        if year == 2025 and month > 3:
            break
        
        url = base_url.format(year, month)
        driver.get(url)
        # time.sleep()
        
        try:
            # Find the table containing gold price data
            rows = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//table[@id='dtDGrid']/tbody/tr[@class='DataRow']"))
            )
            # print("in loop")
            for row in rows:
                cols = row.find_elements(By.CLASS_NAME, "rate")
                if len(cols) >= 3:
                    date_str = cols[0].text.strip()
                    # print(date_str)
                    price_per_gram = cols[2].text.strip().replace(",", "")
                    
                    # date to ISO format
                    month, day, year_short = date_str.split("/")
                    full_year = "20" + year_short
                    formatted_date = f"{full_year}-{month}-{day}"
                    
                    gold_prices[formatted_date] = {"price": float(price_per_gram)}

            print(f"Data received for {year}-{month} ({len(rows)} records)")

        except Exception as e:
            print(f"Failed to extract data for {year}-{month}: {e}")
        
        # print("end loop")
driver.quit()


import json
# gold_prices_json = json.dumps(gold_prices, indent=4)
# print(gold_prices_json)

# json save
with open("gold_prices.json", "r+") as file:
    json.dump(gold_prices, file, indent=4)

print("Data saved to gold_prices.json")