import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# ===== CONFIG =====

INPUT_FILE = "input.csv"
OUTPUT_FILE = "output_links.csv"

# ===== LOAD INPUT =====
df = pd.read_csv(INPUT_FILE)
results = []
for url in df["url"]:

    try:
        print(f"Scraping: {url}")     

        response = requests.get(url, timeout=10)
        response.raise_for_status()      

        soup = BeautifulSoup(response.text, "html.parser")       

        # Ambil semua tag <a>
        links = soup.find_all("a")
      
        for link in links:
            href = link.get("href")
            anchor_text = link.get_text(strip=True)           

            if href:
                # Convert relative URL jadi absolute
                full_url = urljoin(url, href)               
                results.append({
                    "source_page": url,
                    "link_url": full_url,
                    "anchor_text": anchor_text
                })
                
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# ===== SAVE OUTPUT =====
output_df = pd.DataFrame(results)
output_df.to_csv(OUTPUT_FILE, index=False)
print("Done. Results saved to", OUT
