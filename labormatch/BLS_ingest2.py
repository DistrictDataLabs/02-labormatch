import requests
import json
import prettytable
import sys



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
    
    if len(sys.argv)>1:
        key = str(sys.argv[1])
    else:
        key='8c3ab1a673a340d39b89f1823419ee79'
    print key
    
    prefix = 'BD'
    seasonal = 'S'
    unit = '0'
    sizeclass = '01'
    recordtype = 'Q'
    ownership = '5'

    ratelevel = 'L'
    dataelement = '1'
    industry_codes = ['100020', '100030','200080']
    dataclass = '03'

    f_area = 'bd.state.txt'
    area_codes = getcode(f_area)
    
    fout = open('bd_series_list.txt', 'w')
    series_list = []
    for areacode in area_codes:
        for industry in industry_codes:
            seriesid = prefix + seasonal + areacode + industry + unit + dataelement+ sizeclass + dataclass +ratelevel + recordtype + ownership
            series_list.append(seriesid)
            fout.write(seriesid)
            fout.write('\n')
    #series_groups = [series_list[x:x+50] for x in xrange(0, len(series_list), 50)] #only take 50 per multi-series request                                      
            headers = {'Content-type': 'application/json'}
    #for group in series_groups:                                                                                                                                
            data = json.dumps({
                    "seriesid": [seriesid],
                    "startyear": "2011",
                    "endyear": "2014"
                    })
            
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
                            output = open('output/BLS_'+ seriesid + '.txt','w')
                            output.write (row)

            else:
                print json_data['message']
                   

    

       
    
if __name__ == "__main__":
  main()
