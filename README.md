# Copenhagen-Canteen-Collection

A small program that organizes most of the university canteen menu information for the use of university students

## Collaboration

I am actively looking for collaborations. If you want to join this project, please contact me at [my email](mailto:z.minhao.01+coding@gmail.com) or create a pull request!

## TODO

- [ ] Build a website that displays the menu information
  - [ ] A map where users can see the location of the canteens
    - [ ] Add a date to the top of the page
    - [x] Add a banner to the to of the page on weekends saying that the canteen is closed
  - [x] A page where users can see the general information and menu information of a specific canteen
  - [x] A text page where users can see all the menu for a specific day
- [ ] Automate the process of scraping and updating the website
  - [x] Fix bugs that comes from ill-formatted website
  - [ ] The format of the website is not consistent with lots of typos. Thus, it is harder for me to scrape the information and I need to constantly add possible scrapers
- [x] Scrape the menu information from KU canteens
  - [x] KU Frederiksberg Campus
  - [x] KU Nørre Campus
  - [x] KU Søndre Campus
  - [x] KU Geocenter - City
  - [x] KU Gamle - Taastrup
  - [x] KU Skovskolen (IGNORED AS NO INFO)
- [ ] Scrape the menu information from CBS canteens
  - [ ] CBS Solbjerg Plads
  - [ ] CBS Dalgas Have
  - [ ] CBS Porcelænshaven
  - [ ] CBS Kilen
  - [ ] CBS Flintholm
  - [ ] CBS Graduate House
- [ ] Add machine translation into some part of the program to translate Danish into English
  - [ ] Add a note saying that which are the machine translation which are real text
  - [ ] Maybe add a feature that allows users to choose the language they want to see
  - [ ] Maybe add Chinese Support

## Build on your own

Requirements:

- Python3 with `scrapy` installed
- node v18.18.0+
- npm 9.8.1+

To run this project, simply run

```bash
npm install
python crawler/run_spiders.py
npm run dev
```

in root directory. The output will be stored in `data` directory and the website will be hosted on the displayed URL in terminal.
