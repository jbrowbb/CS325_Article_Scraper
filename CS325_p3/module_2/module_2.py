from pathlib import Path
from bs4 import BeautifulSoup
import requests

def scrape_articles(urls):
    """ Downloads articles, extracts content, and saves to processed folder

        Args:
        urls: A lsit of URLs to scrape.
    """

    output_dir = Path(__file__).resolve().parent.parent / 'Data'/'processed'

    # Scrape and save data for each URL
    for idx, url in enumerate(urls):
        try:
            # Download webpafe content
            response = requests.get(url)
            response.raise_for_status()     # Exception for non-200 status codes

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract article text
            article_text = soup.get_text(strip=True)        # Gets all text

            # Save data to a text file in the processed directory
            article_file = output_dir / f'article_{idx + 1}.txt'
            with article_file.open('w', encoding='utf-8') as f:
                f.write(article_text)
            print(f"Article {idx +1} scraped and saved")

        except Exception as e:
            print(f"Error scraping article {idx + 1}: {e}")