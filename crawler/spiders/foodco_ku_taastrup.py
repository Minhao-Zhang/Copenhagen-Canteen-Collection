import codecs
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_DANISH = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]


class KUTaastrupCampusCanteen(scrapy.Spider):
    name = "foodco-ku-Taastrup-spider"
    start_urls = [
        "https://www.foodandco.dk/besog-os-her/restauranter/ku/gamle-taastrup"]
    custom_settings = {
        "LOG_LEVEL": "ERROR",
    }

    def parse(self, response):
        content = []
        for canteen in response.css(".ContentBlock"):
            for element in canteen.css("*"):
                element_text = element.css("::text").get()
                if (element_text and element_text.strip() != ""):
                    content.append(element_text.strip())

        # there will be duplicate lines, unknown why, but we remove them
        result = []
        for i in range(len(content)):
            if i == 0 or content[i] != content[i - 1]:
                result.append(content[i])

        # save the result to a file in UTF-8
        with codecs.open(DATA_PATH + "GAMLE_TAASTRUP.txt", "w", "utf-8") as f:
            for line in result:
                f.write(line + "\n")

        # we now know the result are in the format of
        # WEEK_NUMBER
        # Mandag: DANISH_MENU
        # Monday: ENGLISH_MENU
        # ...
        # Forbehold for ændringer
        # we parse them into json file by each day

        taa_dict = {}
        for i in range(5):
            taa_dict[WEEKDAYS[i]] = result[1+i*2][len(
                WEEKDAYS_DANISH[i])+2:] + "\n" + result[2+i*2][len(WEEKDAYS[i])+2:]
        gum_json = json.dumps(taa_dict, ensure_ascii=False)

        # write to a file in UTF-8
        with codecs.open(DATA_PATH + "GAMLE_TAASTRUP.json", "w", "utf-8") as f:
            f.write(gum_json)
