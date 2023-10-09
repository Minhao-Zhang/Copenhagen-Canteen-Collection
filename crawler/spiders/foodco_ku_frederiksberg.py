import codecs
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_DANISH = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]


class KUFrederiksbergCampusCanteen(scrapy.Spider):
    name = "foodco-ku-frederiksberg-spider"
    start_urls = [
        "https://www.foodandco.dk/besog-os-her/restauranter/ku/frederiksberg-campus"]
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

        # there should be two canteens in Frederiksberg campus that associated with food&co
        # we split the result into two parts
        gim_index = result.index("GIMLE KANTINE")
        if (gim_index == -1):
            sys.exit("Cannot find GIMLE KANTINE")

        gum_result = result[:gim_index]
        gim_result = result[gim_index:]

        # write to a file in UTF-8
        with codecs.open(DATA_PATH + "GUMLE_KANTINE.txt", "w", "utf-8") as f:
            for line in gum_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "GIMLE_KANTINE.txt", "w", "utf-8") as f:
            for line in gim_result:
                f.write(line + "\n")

        # we now know the result are in the format of
        # GUMLE KANTINE
        # WEEK_NUMBER
        # Mandag: DANISH_MENU
        # Monday: ENGLISH_MENU
        # ...
        # we parse them into json file by each day

        gum_dict = {}
        for i in range(5):
            gum_dict[WEEKDAYS[i]] = gum_result[2+i*2][len(
                WEEKDAYS_DANISH[i])+2:] + "\n" + gum_result[3+i*2][len(WEEKDAYS[i])+2:]
        gum_json = json.dumps(gum_dict, ensure_ascii=False)

        # GIMLE KANTINE
        # WEEK_NUMBER
        # Monday: ENGLISH_MENU
        # MAYBE_MULTIPLE_LINE
        # ...
        # Forbehold for ændringer (subject to change at the end)

        # we parse them into json file by each day

        gim_dict = {}
        start_index = []
        for i in range(5):
            # find the line number if they start with a weekday
            for j in range(len(gim_result)):
                if gim_result[j].startswith(WEEKDAYS[i]):
                    start_index.append(j)
                    break
        start_index.append(len(gim_result) - 1)
        for i in range(5):
            temp = ""
            for j in range(start_index[i], start_index[i+1]):
                if gim_result[j].startswith(WEEKDAYS[i]):
                    temp += gim_result[j][len(WEEKDAYS[i])+2:] + "\n"
                else:
                    temp += gim_result[j] + "\n"
            temp = temp[:len(temp)-1]
            gim_dict[WEEKDAYS[i]] = temp
        gim_json = json.dumps(gim_dict, ensure_ascii=False)

        # store the json file
        with codecs.open(DATA_PATH + "GUMLE_KANTINE.json", "w", "utf-8") as f:
            f.write(gum_json)
        with codecs.open(DATA_PATH + "GIMLE_KANTINE.json", "w", "utf-8") as f:
            f.write(gim_json)
