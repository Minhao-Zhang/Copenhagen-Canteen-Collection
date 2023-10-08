import codecs
import json
import sys
import scrapy 

DATA_PATH = "data/"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEDDAYS_DANISH = ["MANDAG", "TIRSDAG", "ONSDAG", "TORSDAG", "FREDAG"]

class KUFrederiksbergCampusCanteen(scrapy.Spider):
    name = "ku-frederiksberg-spider"
    start_urls = ["https://www.foodandco.dk/besog-os-her/restauranter/ku/frederiksberg-campus"]
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
        
        # the NBI KANTINEN does not seems to get update, we ignore that for now
        nbi_index = result.index("NBI KANTINEN")
        if (nbi_index != -1):
            result = result[:nbi_index]
        
        # there should be two canteens in north campus that associated with food&co 
        # we split the result into two parts
        bio_index = result.index("BIO CENTERET")
        if (bio_index == -1):
            sys.exit("Cannot find BIO CENTERET") 
        
        hco_result = result[:bio_index]
        bio_result = result[bio_index:]
        
         # write to a file in UTF-8
        with codecs.open(DATA_PATH + "HCØ_KANTINEN.txt", "w", "utf-8") as f:
            for line in hco_result:
                f.write(line + "\n")
        with codecs.open(DATA_PATH + "BIO_CENTERET.txt", "w", "utf-8") as f:
            for line in bio_result:
                f.write(line + "\n")
        
        
        # we now know the result are in the format of 
        # CANTEEN_NAME
        # WEEK_NUMBER
        # MONDAY
        # SOME LINE OF TEXT
        # ... 
        # we parse them into json file by each day
        
        # looking at the website, HCØ KANTINEN use English weekdays (first-cap) 
        # and BIO CENTERET use Danish weekdays (all-cap)
        
        def split_and_store(result: list[str], weekdays: list[str]) -> dict[str, str]:
            indexes = [result.index(day) for day in weekdays]
            result_dict = {}
            for i in range(len(indexes)):
                day = weekdays[i]
                result_dict[day] = result[indexes[i] + 1: indexes[i + 1]]
            return result_dict
            
            
        hco_result_dict = split_and_store(hco_result, WEEKDAYS)
        bio_result_dict = split_and_store(bio_result, WEEDDAYS_DANISH)
        
        hco_result_json = json.dumps(hco_result_dict, ensure_ascii=False)
        bio_result_json = json.dumps(bio_result_dict, ensure_ascii=False)
        
        # store the json file 
        with codecs.open(DATA_PATH + "HCØ_KANTINEN.json", "w", "utf-8") as f:
            f.write(hco_result_json)
        with codecs.open(DATA_PATH + "BIO_CENTERET.json", "w", "utf-8") as f:
            f.write(bio_result_json)
        
        
       
        