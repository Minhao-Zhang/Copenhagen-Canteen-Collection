import codecs
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_SHORT = ["Mo", "Tu", "We", "Th", "Fr"]
WEEKDAYS_DANISH = ["MANDAG", "TIRSDAG", "ONSDAG", "TORSDAG", "FREDAG"]
WEEKDAYS_DANISH_LOW = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]
WEEKDAYS_DANISH_SHORT = ["Man", "Tir", "Ons", "Tor", "Fre"]


class KUNorthCampusCanteen(scrapy.Spider):
    name = "foodco-ku-north-spider"
    start_urls = [
        "https://www.foodandco.dk/besog-os-her/restauranter/ku/norre-campus"]
    custom_settings = {
        "LOG_LEVEL": "ERROR",
    }

    def parse(self, response):
        content = []
        for canteen in response.css(".ContentBlock"):
            for element in canteen.css("*"):
                element_text = "".join(element.css("::text").getall())
                # element_text = element.css("::text").get()
                if (element_text and element_text.strip() != ""):
                    content.append(element_text.strip())

        # there will be duplicate lines, unknown why, but we remove them
        result = []
        for i in range(len(content)):
            if i == 0 or content[i] != content[i - 1]:
                result.append(content[i])

        # there should be two canteens in north campus that associated with food&co
        # we split the result into two parts
        hco_index = result.index("HCØ KANTINEN")
        bio_index = result.index("BIO CENTERET")
        nbi_index = result.index("NBI KANTINEN")

        hco_result = result[hco_index:bio_index - 1]
        bio_result = result[bio_index:nbi_index - 1]
        nbi_result = result[nbi_index:]

        # write to a file in UTF-8
        with codecs.open(DATA_PATH + "HCØ_KANTINEN.txt", "w", "utf-8") as f:
            for line in hco_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "BIO_CENTERET.txt", "w", "utf-8") as f:
            for line in bio_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "NBI_KANTINEN.txt", "w", "utf-8") as f:
            for line in nbi_result:
                f.write(line + "\n")

        hco_result_json = self.parse_hco_1(hco_result)
        bio_result_json = self.parse_bio(bio_result)
        nbi_result_json = self.parse_nbi_1(nbi_result)

        # store the json file
        with codecs.open(DATA_PATH + "HCØ_KANTINEN.json", "w", "utf-8") as f:
            f.write(hco_result_json)
        with codecs.open(DATA_PATH + "BIO_CENTERET.json", "w", "utf-8") as f:
            f.write(bio_result_json)
        with codecs.open(DATA_PATH + "NBI_KANTINEN.json", "w", "utf-8") as f:
            f.write(nbi_result_json)

    def parse_hco_1(self, result: list[str]) -> str:
        print("PARSING HCO RESULT 1")
        # HCØ KANTINEN
        # WEEK_NUMBER
        # Mandag
        # DANISH_MENU
        # ...
        # Monday
        # ENGLISH_MENU
        # ...
        try:
            # since the format is not consistent, we need to find the indexes
            eng_indexes = []
            dan_indexes = []
            for i in range(5):
                for j in range(len(result)):
                    if result[j].startswith(WEEKDAYS_SHORT[i]):
                        eng_indexes.append(j)
                        break
            eng_indexes.append(len(result) - 1)
            for i in range(5):
                for j in range(len(result)):
                    if result[j].startswith(WEEKDAYS_DANISH_SHORT[i]):
                        dan_indexes.append(j)
                        break
            dan_indexes.append(len(result) - 1)

            result_dict = {}
            result_dict["Name"] = "HCØ_KANTINEN"
            result_dict["WeekNumber"] = result[1].split()[-1]

            for i in range(5):
                day = WEEKDAYS[i]
                result_dict[day] = "\n".join(
                    result[eng_indexes[i] + 1: dan_indexes[i + 1]])
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json
        except:
            return self.parse_hco_2(result)

    def parse_hco_2(self, result: list[str]) -> str:
        print("PARSING HCO RESULT 2")
        # HCØ KANTINEN
        # WEEK_NUMBER
        # Mandag/monday
        # SOME_TEXT
        # ...
        # Tirsdag/Tuesday
        # ...
        try:
            result_dict = {}
            result_dict["Name"] = "HCØ_KANTINEN"
            result_dict["WeekNumber"] = result[1].split(" ")[-1]
            start_index = []
            for i in range(5):
                # find the line number if they start with a weekday
                for j in range(len(result)):
                    if result[j].startswith(WEEKDAYS_DANISH_SHORT[i]):
                        start_index.append(j)
                        break
            start_index.append(len(result) - 1)
            for i in range(5):
                temp = ""
                for j in range(start_index[i] + 1, start_index[i+1]):
                    if result[j].startswith(WEEKDAYS_SHORT[i]):
                        temp += result[j][len(WEEKDAYS[i])+2:] + "\n"
                    else:
                        temp += result[j] + "\n"
                temp = temp[:len(temp)-1]
                result_dict[WEEKDAYS[i]] = temp
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json
        except:
            raise Exception("HCO KANTINEN FORMAT IS NOT CORRECT")

    def parse_bio(self, result: list[str]) -> str:
        print("PARSING BIO RESULT")
        # BIO CENTERET
        # WEEK_NUMBER
        # MONDAY
        # SOME LINE OF TEXT
        # ...
        try:
            indexes = [result.index(day) for day in WEEKDAYS_DANISH]
            result_dict = {}
            result_dict["Name"] = "BIO_CENTERET"
            result_dict["WeekNumber"] = result[1].split()[-1]

            for i in range(len(indexes) - 1):
                day = WEEKDAYS[i]
                result_dict[day] = "\n".join(
                    result[indexes[i] + 1: indexes[i + 1]])
            result_dict[WEEKDAYS[-1]] = "\n".join(result[indexes[-1] + 1:])
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json
        except:
            raise Exception("Cannot parse BIO CENTERET")

    def parse_nbi_1(self, result: list[str]) -> str:
        print("PARSING NBI RESULT 1")
        # NBI KANTINEN
        # WEEK_NUMBER
        # Mandag
        # SOME_TEXT
        # ...
        # Med forbehold for ændringer
        try:
            indexes = []
            for i in range(5):
                for j in range(len(result)):
                    if result[j].startswith(WEEKDAYS_DANISH_SHORT[i]):
                        indexes.append(j)
                        break
            indexes.append(len(result) - 1)

            result_dict = {}
            result_dict["Name"] = "NBI_KANTINEN"
            result_dict["WeekNumber"] = result[1].split()[-1]

            for i in range(len(indexes) - 1):
                day = WEEKDAYS[i]
                result_dict[day] = "\n".join(
                    result[indexes[i] + 1: indexes[i + 1]])
            result_json = json.dumps(result_dict, ensure_ascii=False)

            result_json = json.dumps(result_dict, ensure_ascii=False)
            return result_json
        except:
            return self.parse_nbi_2(result)

    def parse_nbi_2(self, result: list[str]) -> str:
        print("PARSING NBI RESULT 2")
        # NBI KANTINEN
        # WEEK_NUMBER
        # Mandag: SOME_TEXT
        # Mandag:
        # possibly multiple lines
        # ...
        # Med forbehold for ændringer
        try:
            no_colon_result = [
                line for line in result if not line.endswith(":")]

            indexes = []
            for i in range(5):
                for j in range(len(no_colon_result)):
                    if no_colon_result[j].startswith(WEEKDAYS_DANISH_SHORT[i]):
                        indexes.append(j)
                        break

            indexes.append(len(no_colon_result) - 1)
            no_colon_result_dict = {}
            no_colon_result_dict["Name"] = "NBI_KANTINEN"
            no_colon_result_dict["WeekNumber"] = no_colon_result[1].split()[-1]

            for i in range(len(indexes) - 1):
                day = WEEKDAYS[i]
                temp = "\n".join(
                    no_colon_result[indexes[i]: indexes[i + 1]])
                # there is a WEEKDAY_DANISH: in the beginning, we remove it
                colon_index = temp.index(":")
                temp = temp[colon_index + 2:]
                no_colon_result_dict[day] = temp

            no_colon_result_json = json.dumps(
                no_colon_result_dict, ensure_ascii=False)
            return no_colon_result_json
        except:
            raise Exception("Cannot parse NBI KANTINEN")
