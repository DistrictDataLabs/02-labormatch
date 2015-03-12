import requests
import json
import csv



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
    
    

def main():
        
    prefix = 'SM'
    seasonal = 'U'
    area='00000'
    industry = '60540000'
    datatype = '01'

    #f_area = 'bd.state.txt'
    #area_codes = getcode(f_area)
    f_state = 'sm.state.txt'
    states = getcode(f_state)

    fout = open('sm_series_list.txt', 'w')
    fno = open('sm_series_list_noresutls.txt','w')
    
    series_list = []
    for state in states:
        seriesid = prefix + seasonal + state + area + industry + datatype
        series_list.append(seriesid)
        fout.write(seriesid)
        fout.write('\n')
        series_groups = [series_list[x:x+50] for x in xrange(0, len(series_list), 50)] #only take 50 per multi-series request
        headers = {'Content-type': 'application/json'}
        for group in series_groups:
            data = json.dumps({
                    "seriesid": [seriesid],
                    "startyear": "2011",
                    "endyear": "2014"
                    })
            key='8c3ab1a673a340d39b89f1823419ee79'
            p = requests.post('http://api.bls.gov/publicAPI/v2/timeseries/data/', data = data, headers = headers, auth=(key,''))
            json_data = json.loads(p.text)
            if json_data['status'].find('REQUEST_NOT_PROCESSED')<0:
                for series in json_data['Results']['series']:
                    for item in series['data']:
                        
                        row = {
                            "series_id": series["seriesID"],
                            "year": item['year'],
                            "period": item['period'],
                            "value": item['value'],
                            "has_footnotes": False
                            }
                        
                        if len(item["footnotes"]) > 2:
                            row["has_footnotes"] = True
                            
                        with open('output/sm_data.csv', 'a') as outfile:
                            writer = csv.DictWriter(outfile, ["series_id", "year", "period", "value", "has_footnotes"])
                            writer.writerow(row)
                        outfile.close()
                            
 
            else:
                print seriesid
                fno.write(seriesid)
                fno.write('\n')
                print json_data['status']
                print json_data['message']
                
    
if __name__ == "__main__":
  main()
