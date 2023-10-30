import codecs
import datetime
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_DANISH = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]


class KUGeoCenterCampusCityCanteen(scrapy.Spider):
    name = "foodco-ku-geocenter-spider"
    start_urls = [
        "https://www.foodandco.dk/besog-os-her/restauranter/ku/geocenter-city"]
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

        # save to a file in UTF-8
        with codecs.open(DATA_PATH + "GEOCENTER_CITY.txt", "w", "utf-8") as f:
            for line in result:
                f.write(line + "\n")

        # we now know the result of are the same and are in the format of
        # Monday
        # SOME_LINES
        # ...
        # so we parse them into json file by each day
        def split_and_store(result: list[str]) -> str:
            indexes = [result.index(day) for day in WEEKDAYS]
            result_dict = {}
            result_dict["Name"] = "GEOCENTER_CITY"
            # result_dict["WeekNumber"] = result[0].split(" ")[-1]
            # this canteen does not provide week number
            # we default this to the current week

            week_number = datetime.datetime.today().isocalendar()[1]
            result_dict["WeekNumber"] = week_number

            for i in range(len(indexes) - 1):
                day = WEEKDAYS[i]
                result_dict[day] = "\n".join(
                    result[indexes[i] + 1: indexes[i + 1]])
            result_dict[WEEKDAYS[-1]] = "\n".join(result[indexes[-1] + 1:])
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json

        geo_result = split_and_store(result)

        with codecs.open(DATA_PATH + "GEOCENTER_CITY.json", "w", "utf-8") as f:
            f.write(geo_result)
