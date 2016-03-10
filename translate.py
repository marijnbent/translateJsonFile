import json
from textblob import TextBlob

with open('language.json') as data_file:
    data = json.load(data_file)

translatedDict = {}
translatedString = ""
toLanguage = "nl"

for key,value in data.items():
    print ("EN:" + key)
    b = TextBlob(key)

    try:
        b = b.translate(to=toLanguage)
        translatedString = str(b)
    except:
        translatedString = key
        pass

    print (toLanguage.capitalize() + ":" + translatedString)
    translatedDict[key] = translatedString

translatedDict['LANG_NAME'] = toLanguage

with open(toLanguage + '.json', 'w') as result:
    json.dump(translatedDict, result)

