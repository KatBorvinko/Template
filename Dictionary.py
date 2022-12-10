# Creating a dictionary of 20 countries
import json
import pickle

countries = dict({'1': 'Argentina',
                  '2': 'Australia',
                  '3': 'Brazil',
                  '4': 'Colombia',
                  '5': 'Egypt',
                  '6': 'France',
                  '7': 'Germany',
                  '8': 'Greece',
                  '9': 'Hong Kong',
                  '10': 'Kiribati',
                  '11': 'Lesotho',
                  '12': 'Madagascar',
                  '13': 'Mexico',
                  '14': 'Nepal',
                  '15': 'New Zealand',
                  '16': 'Nigeria',
                  '17': 'Philippines',
                  '18': 'Portugal',
                  '19': 'United Arab Emirates',
                  '20': 'United Kingdom'})
for key, value in countries.items():
    print(key, value, '\n')

# convert dictionary to JSON
countries_json = json.dumps(countries)
print(countries_json)


# convert to binary
with open('countries.pickle', 'wb') as file:
    pickle.dump(countries, file)

# serialization/ pickle with class method
def serialise_dictionary(self, format):
    if format == "JSON":
        with open('dico.json', 'w') as file:
            json.dump(self.dictionary, file)
            print('Dictionary serialised as JSON. Filename: dico.json')
    elif format == "BINARY":
        with open('dico.bin', 'wb') as file:
            pickle.dump(self.dictionary, file)
            print('Dictionary serialised as BINARY. Filename: dico.bin')
