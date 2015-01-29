

def main():
  import requests
  seriesID='LAUCN040010000000005'
  p=requests.get('http://api.bls.gov/publicAPI/v2/timeseries/data/' + seriesID)
  series = p.json()['Results']['series'][0]['data']


  with open('../fixtures/exampleData.json', 'w') as writefile:
      for item in series:
          writefile.write(str(item) +'\n')  
    
    
if __name__ == "__main__":
  main()