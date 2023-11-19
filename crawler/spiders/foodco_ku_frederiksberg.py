import codecs
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_SHORT = ["Mon", "Tue", "Wed", "Thu", "Fri"]
WEEKDAYS_DANISH = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
WEEKDAYS_DANISH_SHORT = ["Man", "Tir", "Ons", "Tor", "Fre"]


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

        gum_json = self.parse_gum(gum_result)
        gim_json = self.parse_gim(gim_result)

        # store the json file
        with codecs.open(DATA_PATH + "GUMLE_KANTINE.json", "w", "utf-8") as f:
            f.write(gum_json)
        with codecs.open(DATA_PATH + "GIMLE_KANTINE.json", "w", "utf-8") as f:
            f.write(gim_json)

    def parse_gum(self, result: list[str]) -> str:
        print("PARSING GUMLE KANTINE")
        # GUMLE KANTINE
        # WEEK_NUMBER
        # Mandag: DANISH_MENU
        # Monday: ENGLISH_MENU
        # ...
        try:
            result_dict = {}
            result_dict["Name"] = "GUMLE_KANTINE"
            result_dict["WeekNumber"] = result[1].split(" ")[-1]
            for i in range(5):
                result_dict[WEEKDAYS[i]] = result[2+i*2][len(
                    WEEKDAYS_DANISH[i])+2:] + "\n" + result[3+i*2][len(WEEKDAYS[i])+2:]
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json
        except:
            raise Exception("Cannot parse GUMLE KANTINE")

    def parse_gim(self, result: list[str]) -> str:
        print("PARSING GIMLE KANTINE")
        # GIMLE KANTINE
        # WEEK_NUMBER
        # Monday: ENGLISH_MENU
        # MAYBE_MULTIPLE_LINE
        # ...
        # Forbehold for ændringer (subject to change at the end)
        try:
            result_dict = {}
            result_dict["Name"] = "GIMLE_KANTINE"
            result_dict["WeekNumber"] = result[1].split(" ")[-1]
            start_index = []

            # bug on week 47, Tuesday is spelled as tuesday
            # replace all tuesday with Tuesday
            for l in range(len(result)):
                if "tuesday" in result[l]:
                    result[l] = result[l].replace("tuesday", "Tuesday")

            for i in range(5):
                # find the line number if they start with a weekday
                for j in range(len(result)):
                    if result[j].startswith(WEEKDAYS_SHORT[i]):
                        start_index.append(j)
                        break
            start_index.append(len(result) - 1)
            for i in range(5):
                temp = ""
                for j in range(start_index[i], start_index[i+1]):
                    if result[j].startswith(WEEKDAYS_SHORT[i]):
                        temp += result[j][len(WEEKDAYS[i])+2:] + "\n"
                    else:
                        temp += result[j] + "\n"
                temp = temp[:len(temp)-1]
                result_dict[WEEKDAYS[i]] = temp
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json
        except:
            raise Exception("Cannot parse GIMLE KANTINE")
