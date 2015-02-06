import requests


class dice_request():
    def __init__(self):
        self.api_base='http://service.dice.com/api/rest/jobsearch/v1/simple.json?' 
        
    def get(self,input_str):
        p=requests.get(self.api_base + input_str)
        self.response=p.json()
        
        

    
    def write(self,fileName):
      with open(fileName, 'w') as writefile:
          writefile.write(str(self.response) )  
    

def main():
  params='state=md'
  
  api=dice_request()
  api.get(params)
  api.write('../fixtures/diceExampleData.json')
  



    
if __name__ == "__main__":
  main()