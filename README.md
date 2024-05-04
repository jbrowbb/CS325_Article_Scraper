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
- Installing pandas package 2.1.4 with numpy 1.26.3
- Install beautifulsoup4 
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

-Args:
    -article_files: Path to the file containing URLs

-Returns:
    -A list of URLs to be scraped

## module_2.py
- Uses the requests library

```
    def scrape_articles(urls)
```

- Downloads articles, extracts content, and saves to Data/processed folder

-Args:
    urls: A list of URLs to scrape