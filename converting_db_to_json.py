import pandas as pd
import json 

# Converting EXCEL file to JSON 
data = pd.read_excel('C:\\Users\\maria\\OneDrive\\Documentos\\Estudos\\API Monster High\\base_mh.xlsx')
df = pd.DataFrame(data)

js_dataframe = df.to_json(orient='records')
print(js_dataframe)

# Saving JSON 
with open('mh_json.json', 'w') as arquivo_mh:
    json.dump(json.loads(js_dataframe), arquivo_mh, indent=4)