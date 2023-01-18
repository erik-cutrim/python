import requests  
r = requests.get("http://phd-data-service.aws.guideinvestimentos.com.br/funds/positions?reference_date=2022-10-27")  


print(type(r))