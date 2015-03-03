import requests
import json
import prettytable



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
    
    series_groups = [series_list[x:x+50] for x in xrange(0, len(series_list), 50)] #only take 50 per multi-series request
    headers = {'Content-type': 'application/json'}
    for group in series_groups:
        
        data = json.dumps({
                "seriesid": group,
                "startyear": "2011",
                "endyear": "2014"
                })
        key='8c3ab1a673a340d39b89f1823419ee79' ###############update with your own api key##############
        p = requests.post('http://api.bls.gov/publicAPI/v1/timeseries/data/', data = data, headers = headers, auth=(key,''))
        json_data = json.loads(p.text)
        if json_data['status'].find('REQUEST_NOT_PROCESSED')<0:
            for series in json_data['Results']['series']:
                x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
                seriesId = series['seriesID']
                for item in series['data']:
                    year = item['year']
                    period = item['period']
                    value = item['value']
                    footnotes=""
                    for footnote in item['footnotes']:
                        if footnote:
                            footnotes = footnotes + footnote['text'] + ','
                output = open('output/BLS_'+ seriesId + '.txt','w')
                output.write (x.get_string())
                output.close()

        else:
            print json_data['message']
                   

    

       
    
if __name__ == "__main__":
  main()
