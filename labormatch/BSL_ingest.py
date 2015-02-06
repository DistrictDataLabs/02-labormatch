import requests


class BLSrequest():
    def __init__(self):
        self.api_base='http://api.bls.gov/publicAPI/v2/timeseries/data/' 
        
    def get(self,input_str):
        p=requests.get(self.api_base + input_str)
        self.response=p.json()['Results']['series'][0]['data']
        
        
    def post(self, input_str):    
        p=requests.post(self.api_base + input_str)
        return p # TO DO
    
    def write(self,fileName):
      with open(fileName, 'w') as writefile:
        for item in self.response:
          writefile.write(str(item) +'\n')  
    

def main():

  exampleSeries='LAUCN040010000000005' #'OEUM530000154100000000004'
  api=BLSrequest()
  api.get(exampleSeries)
  api.write('../fixtures/exampleData.json')
  



    
if __name__ == "__main__":
  main()
