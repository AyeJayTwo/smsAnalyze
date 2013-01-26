"""Created this quickly to convert a json file generously provided on StackOverflow
   and turn it into a dictionary which is quickly searchable. Made it a pickle because
   pickles are delicious."""
import json
import pickle

data = json.load(open('area_codes.json'))

area_codes = {}

for x in data['area_codes']:
    area_codes[x['area_code']] = (x['city'],x['lat'],x['lng'])

pickle.dump(area_codes,open('area_codes.pkl','wb'))