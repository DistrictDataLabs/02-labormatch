import requests


class BLSrequest():
    def __init__(self):
        self.api_base='http://api.bls.gov/publicAPI/v2/timeseries/data/' 
        
    def get(self,input_str):
        p=requests.get(self.api_base + input_str)
        if p.json()['Results']:
            self.response=p.json()['Results']['series'][0]['data']
        else:
            self.response=p.json()['Results']
        
        
    def post(self, input_str):    
        p=requests.post(self.api_base + input_str)
        return p # TO DO
    
    def write(self,fileName):
      with open(fileName, 'w') as writefile:
        for item in self.response:
          writefile.write(str(item) +'\n')  
    
          
def getcode(fname):
    f_oe = open(fname,'r')
    mylist = []

    for line in f_oe:
        code=line.split('\t')[0]
        if code.isdigit():
            mylist.append(code)

    return mylist
    

def main():
    prefix = 'OE'
    seasonal = 'U'
    areatype = 'N'
    
    f_occupation = 'oe.occupation.txt'
    occupation_codes=getcode(f_occupation)

    f_area = 'oe.area.txt'
    area_codes=getcode(f_area)

    f_industry='oe.industry.txt'
    industry_codes=getcode(f_industry)

    f_datatype='oe.datatype.txt'
    datatype_codes=getcode(f_datatype)
  
    for areacode in area_codes:
        for industry in industry_codes:
            for occupation in occupation_codes:
                for datatype in datatype_codes:
                    myseries = prefix + seasonal + areatype + areacode +industry + occupation + datatype
    
                    output_fname = './fixtures/'+'BLS_'+myseries+'.json'
                    api=BLSrequest()
                    api.get(myseries)
                    api.write(../fixtures/output_fname)
    
  #exampleSeries='LAUCN040010000000005' #'OEUM530000154100000000004'
  #api=BLSrequest()
  #api.get(exampleSeries)
  #api.write('../fixtures/exampleData.json')
  



    
if __name__ == "__main__":
  main()