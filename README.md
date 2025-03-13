# Wikipedia Largest Companies Scraper

This Python script scrapes data from Wikipedia's "List of largest companies by revenue" page and saves it as a CSV file.

## Features
- Extracts company ranking, name, revenue, industry, and headquarters.
- Cleans and structures the data into a Pandas DataFrame.
- Handles industry classification dynamically.
- Saves the final dataset as `data.csv`.

## Requirements
Ensure you have Python installed and install the necessary dependencies:

- requests~=2.32.3
- pandas~=2.2.3
- beautifulsoup4~=4.13.3


## Usage
Run the script using:
```sh
python script.py
```
This will generate a `data.csv` file with the extracted data.

## Notes
- Ensure you have an active internet connection while running the script.
- The Wikipedia table structure may change over time, requiring minor updates to the parsing logic.

## License
This project is open-source and available under the MIT License.
