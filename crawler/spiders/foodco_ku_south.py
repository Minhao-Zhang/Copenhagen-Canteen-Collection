import codecs
import json
import sys
import scrapy

DATA_PATH = "data/KU_"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKDAYS_DANISH = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]


class KUSouthCampusCanteen(scrapy.Spider):
    name = "foodco-ku-south-spider"
    start_urls = [
        "https://www.foodandco.dk/besog-os-her/restauranter/ku/sondre-campus"]
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

        # there are 6 blocks consisting of 4 canteens and a social dining
        # we ignore the student meal as it does not have a menu in Folkekokken
        # and the social dining as it does not count as a canteen
        breakpoints = ["(Jur kantinen - KUA3)", "Der tages forbehold for ændringer!",
                       "(Hum kantinen, KUA 1)", "Der tages forbehold for ændringer",
                       "Hot dish", "med forbehold for ændringer", "TEO"]
        canteen_indexes = [result.index(bp) for bp in breakpoints]
        canteen_indexes.append(len(result) - 1)
        canteen_indexes[3] = canteen_indexes[3] - 1

        jur_result = result[canteen_indexes[0]:canteen_indexes[1]]
        hum_result = result[canteen_indexes[2]:canteen_indexes[3]]
        fol_result = result[canteen_indexes[4]:canteen_indexes[5]]
        teo_result = result[canteen_indexes[6]:canteen_indexes[7]]

        # one of the weekday format in fol_result is wrong, we fix it
        onsdag_index = fol_result.index("onsdag")
        print(onsdag_index)
        if (onsdag_index != -1):
            fol_result[onsdag_index] = "Onsdag"

        # write to a file in UTF-8
        with codecs.open(DATA_PATH + "JUR_KANTIEN.txt", "w", "utf-8") as f:
            for line in jur_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "HUM_KANTIEN.txt", "w", "utf-8") as f:
            for line in hum_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "FOLKEKOKKEN.txt", "w", "utf-8") as f:
            for line in fol_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "TEO.txt", "w", "utf-8") as f:
            for line in teo_result:
                f.write(line + "\n")

        # we now know the result of are the same and are in the format of
        # CANTEEN_NAME
        # WEEK_NUMBER
        # Mandag
        # SOME_LINES
        # ...
        # so we parse them into json file by each day
        def split_and_store(result: list[str]) -> str:
            indexes = [result.index(day) for day in WEEKDAYS_DANISH]
            result_dict = {}
            for i in range(len(indexes) - 1):
                day = WEEKDAYS[i]
                result_dict[day] = "\n".join(
                    result[indexes[i] + 1: indexes[i + 1]])
            result_dict[WEEKDAYS[-1]] = "\n".join(result[indexes[-1] + 1:])
            result_json = json.dumps(result_dict, ensure_ascii=False)

            return result_json

        jur_json = split_and_store(jur_result)
        hum_json = split_and_store(hum_result)
        fol_json = split_and_store(fol_result)
        ted_json = split_and_store(teo_result)

        # store the json file
        with codecs.open(DATA_PATH + "JUR_KANTIEN.json", "w", "utf-8") as f:
            f.write(jur_json)
        with codecs.open(DATA_PATH + "HUM_KANTIEN.json", "w", "utf-8") as f:
            f.write(hum_json)
        with codecs.open(DATA_PATH + "FOLKEKOKKEN.json", "w", "utf-8") as f:
            f.write(fol_json)
        with codecs.open(DATA_PATH + "TEO.json", "w", "utf-8") as f:
            f.write(ted_json)
