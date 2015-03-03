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
    
    num_line = 0
    for line in f_oe:
        code=line.split('\t')[0]
        if num_line>0:
            mylist.append(code)
        num_line = num_line +1
    return mylist

    return mylist
    

def main():
    prefix = 'BD'#'OE'
    seasonal = 'S'#'U'
    unit = '0'
    sizeclass = '01'
    recordtype = 'Q'
    ownership = '5'

    f_area = 'bd.state.txt'
    area_codes = getcode(f_area)
    

    f_industry = 'bd.industry.txt'
    industry_codes = getcode(f_industry)

    f_dataelement = 'bd.dataelement.txt'
    dataelements = getcode(f_dataelement)

    f_dataclass = 'bd.dataclass.txt'
    dataclasses = getcode(f_dataclass)

    f_ratelevel = 'bd.ratelevel.txt'
    ratelevels = getcode(f_ratelevel)
  
    fout = open('bd_series_list.txt', 'w')

    series_list = []
    print 'hi'
    for areacode in area_codes:
        for industry in industry_codes:
            for de in dataelements:
                for dc in dataclasses:
                    for rl in ratelevels:
                        seriesid = prefix + seasonal + areacode + industry + unit + de + sizeclass + dc +rl + recordtype + ownership
                        fout.write(seriesid)
                        fout.write('\n')
   
 

                        output_fname = 'output/'+'BLS_'+seriesid+'.json'
                        api=BLSrequest()
                        api.get(seriesid)
                        api.write(output_fname)
                        
    fout.close()
    
  #exampleSeries='LAUCN040010000000005' #'OEUM530000154100000000004'
  #api=BLSrequest()
  #api.get(exampleSeries)
  #api.write('../fixtures/exampleData.json')
  



    
if __name__ == "__main__":
  main()
