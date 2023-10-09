# Copenhagen-Canteen-Collection

A small program that organizes most of the university canteen menu information for the use of university students

## TODO

- [ ] Scrape the menu information from KU canteens
  - [x] KU Frederiksberg Campus
  - [x] KU Nørre Campus
  - [x] KU Søndre Campus
  - [x] KU Geocenter - City
  - [x] KU Gamle - Taastrup
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
- [ ] Add machine translation into some part of the program to translate Danish into English
  - [ ] Maybe add a feature that allows users to choose the language they want to see
  - [ ] Maybe add Chinese Support

## Build on your own

Requirements:

- Python3 with `scrapy` installed

To run this project, simply run

```bash
python crawler/run_spiders.py
```

in root directory. The output will be stored in `data` directory.
