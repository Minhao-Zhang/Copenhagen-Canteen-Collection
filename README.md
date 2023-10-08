# Copenhagen-Canteen-Collection

A small program that organizes most of the University canteen menu information for the use of university students

## TODO

- [ ] Scrape the menu information from KU canteens
  - [ ] KU Frederiksberg Campus
  - [ ] KU Nørre Campus
  - [x] KU Søndre Campus
  - [ ] KU Geocenter - City
  - [ ] KU Gamle - Taastrup
  - [x] KU Skovskolen
- [ ] Scrape the menu information from CBS canteens
  - [ ] CBS Solbjerg Plads
  - [ ] CBS Dalgas Have
  - [ ] CBS Porcelænshaven
  - [ ] CBS Kilen
  - [ ] CBS Flintholm
  - [ ] CBS Graduate House
- [ ] Build a website that displays the menu information
- [ ] Automate the process of scraping and updating the website

## Building on your own

Requirements:

- Python3 with `scrapy` installed

To run this project, simply run

```bash
python crawler/run_spiders.py
```

in root directory. The output will be stored in `data` directory.
