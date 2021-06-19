# Lyrics Scrapper

This is a simple project that extracts lyrics from artists using Scrapy.

## Usage

First install the dependencies

```bash
python -m venv .virtualenv
source ./.virtualenv/bin/activate
pip install -r requirements.txt
```

Create an output folder

```bash
mkdir output
```

And now execute the crawler. So far we have one for musica.com

```bash
scrapy crawl musica.com -O output/dy.json -a artist_id=4324
```

For this example we grab the artist id from the platform manually.
