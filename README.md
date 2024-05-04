## article.txt
- filled with five urls from Variety that are articles over YouTube:
    - MatPat leaving YouTube
    - Free streaming of Escape the Night by Joey Graceffa
    - 2018 YouTube Rewind being cringey
    - Ned Fulmer getting removed from The Try Guys channel
    - Grand Theft Auto 6 is the most viewed YouTube trailer

## requirements.yml
- Created a base in conda called article_reader with python version 3.10.11
- Activated the environment

###
- Exporting article_reader environment as requirements.yml
- Moved into Project-1 folder
- Deactivated environment

## powershell
To get to part 2 use
```
    git checkout part_2
```

```
    cd CS325_p2
```

## run.py
- Uses get_urls from module_1 to grab the articles from the text file and separates the links from each other
- Uses scrape_articles from module_2 to scrape the urls for the text data and writes them into separate articles

## module_1.py
- Reads URLs from a test file

- Args:
    - article_files: Path to the file containing URLs

- Returns:
    - A list of URLs to be scraped

## module_2.py
- Uses the requests library

```
    def scrape_articles(urls)
```

- Downloads articles, extracts content, and saves to Data/processed folder

- Args:
    urls: A list of URLs to scrape

## llmapi.py
- Uses Gemini AI system with an API key to summarize the extracted text from the article scraper

To get an API key to run with program:
    1. In the searchbar type 
    ``` Google API key ```

    2. Click on first link, then "Get an API key"
        (This will open up a new window for Google AI Studio)

    3. Click the button that says "Create API key"
        a. create a name for the project the API key will be used on
        b. click "Create API key in existing project"
    
    4. Open a plain text editor like Notepad.
        a. Define a variable named API_KEY, and assign your API key to it
        ``` API_KEY = your_api_key.```
        b. Save this file with the extension .env inside the main folder.
        c. Once completed, your API key will be safely stored in an .env file.