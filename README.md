# Threads Scraper

Python tool for searching Threads posts by keyword, then saving the results to `JSON`, `CSV`, or `Excel`.

This project uses requests to an internal Threads endpoint, so scraping requires the `sessionid` cookie from a logged-in account.

## Features

- Search Threads posts by keyword
- Set your own target number of posts
- Avoid duplicate posts based on ID
- Save results as `JSON`, `CSV`, `XLSX`, or all formats at once
- Search multiple keywords in one session
- Includes setup and start scripts for Windows and Linux/macOS

## Project Structure

```text
scrape-threads/
|-- threads_scraper.py
|-- requirements.txt
|-- setup.bat
|-- setup.sh
|-- start.bat
|-- start.sh
`-- results/
```

## Requirements

- Python 3.9+
- `pip`
- Internet connection
- `sessionid` cookie from a logged-in Threads account

## Installation

### Option 1: install directly with pip

```bash
pip install -r requirements.txt
```

### Option 2: use the included script

Windows:

```bat
setup.bat
```

Linux/macOS:

```bash
chmod +x setup.sh start.sh
./setup.sh
```

## How to Run

Windows:

```bat
start.bat
```

Linux/macOS:

```bash
./start.sh
```

Or run it directly with Python:

```bash
python threads_scraper.py
```

## How to Get `sessionid`

1. Log in to `https://www.threads.com`
2. Open your browser's Developer Tools (`F12`)
3. Go to the `Application` or `Storage` tab
4. Open the `Cookies` section
5. Select the `https://www.threads.com` domain
6. Find the cookie named `sessionid`
7. Copy its value and paste it into the program when prompted

## Usage Flow

When the program starts, you will be asked to:

1. Enter `sessionid`
2. Enter a search keyword
3. Set how many posts to collect
4. Choose the output format

Example:

```text
Enter session ID: <your_sessionid>
Search keyword: stocks
Number of posts to collect: 50
Save option: 4
```

## Output

Output files are saved in the `results/` folder using this naming pattern:

```text
threads_<keyword>_<jumlah>posts.json
threads_<keyword>_<jumlah>posts.csv
threads_<keyword>_<jumlah>posts.xlsx
```

Example:

```text
results/threads_saham_50posts.json
results/threads_saham_50posts.csv
results/threads_saham_50posts.xlsx
```

## Saved Data

Each post usually contains these fields:

- `id`
- `code`
- `timestamp`
- `date`
- `user.username`
- `user.full_name`
- `user.is_verified`
- `user.profile_pic_url`
- `caption`
- `like_count`
- `reply_count`
- `repost_count`
- `quote_count`
- `url`
- `hashtags`
- `mentions`
- `tag`

## JSON Example

```json
{
  "id": "3874761242607351150",
  "code": "DXF6tIfD_Vu",
  "date": "2026-04-14 07:45:56",
  "caption": "Example post content",
  "like_count": 271,
  "reply_count": 332,
  "repost_count": 20,
  "quote_count": 0,
  "url": "https://threads.net/@username/post/DXF6tIfD_Vu"
}
```

## Dependencies

Contents of `requirements.txt`:

- `requests`
- `pandas`
- `openpyxl`

## Important Notes

- This scraper depends on internal Threads endpoints that may change at any time.
- If `sessionid` is invalid or expired, requests may fail or return empty results.
- Not every keyword will always return as many posts as the target requests.
- The program will stop early if it cannot find new posts across several consecutive pages.
- Use this tool responsibly and in accordance with the platform's terms.

## Troubleshooting

### `Python not found`

Make sure Python is installed and available from the terminal:

```bash
python --version
```

### Failed to install dependencies

Try upgrading `pip`, then install again:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### No search results

Check the following:

- `sessionid` is still valid
- the keyword actually has results on Threads
- your internet connection is stable
- Threads has not changed the endpoint or response format
