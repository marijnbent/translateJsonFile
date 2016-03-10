import json
from textblob import TextBlob

#Set your language as toLanguage. Language codes: https://cloud.google.com/translate/v2/using_rest#language-params
toLanguage = "nl"
#Optional, use a different file
file_name = "language.json"
#And thats all! Run the code and enjoy. Be sure the check the translated file, Google Translate is not perfect.

translatedDict = {}
translatedString = ""

with open(file_name) as data_file:
    data = json.load(data_file)

for key,value in data.items():
    print ("en:" + key)
    b = TextBlob(key)

    try:
        b = b.translate(to=toLanguage)
        translatedString = str(b)
    except:
        translatedString = key
        pass

    print (toLanguage + ":" + translatedString)
    translatedDict[key] = translatedString

translatedDict['LANG_NAME'] = toLanguage

print("Translating succeeded. Be sure to check the '" + toLanguage + ".json' and  improve the translation.")

with open(toLanguage + '.json', 'w') as result:
    json.dump(translatedDict, result)

