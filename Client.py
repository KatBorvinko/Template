import json
import pickle
import Config

COUNTRIES = Config.countries

for key, value in COUNTRIES.items():
    print(key, value, '\n')

# convert dictionary to JSON
countries_json = json.dumps(COUNTRIES)
print(countries_json)

# convert dictionary to binary
with open('countries.pickle', 'wb') as file:
    pickle.dump(COUNTRIES, file)

# convert to XML file


# serialization/ pickle with class method
def serialise_dictionary(self, serialization):
    if Config.serialization_option == "JSON":
        with open('dico.json', 'w') as f:
            json.dump(self.dictionary, f)
            print('Dictionary serialised. Filename: JSON')
    elif Config.serialization_option == "BINARY":
        with open('dico.bin', 'wb') as f:
            pickle.dump(self.dictionary, file)
            print('Dictionary serialised. Filename: Binary')
