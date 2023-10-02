import schedule 
import time as tm
import requests
import json

def job():
  file_name = "response.json"
  directory_path = r"C:\\DataSets\\RD Station Data"
  file_path = f"{directory_path}/{file_name}"
  
  api_url = 'http://127.0.0.1:5001/get_deals'
  response = requests.post(api_url)
  
  if response.status_code == 200:
    data = response.json()
    
    with open(file_path, "w") as json_file:
      json.dump(data, json_file)
    print(f"Dados foram salvos no arquivo '{file_path}'.")
  else:
    print(f"Erro ao consumir a APIL {response.status_code}")
    
schedule.every().day.at("14:10").do(job)
# schedule.every().day.at("11:00").do(job)
# schedule.every().day.at("14:00").do(job)
# schedule.every().day.at("17:00").do(job)

while True: 
  schedule.run_pending()
  tm.sleep(1)