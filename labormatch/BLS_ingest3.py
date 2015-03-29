import requests
import json
import numpy as np

def extract_data(r):
    '''
    For a collection of series, collapse all months values into a yearly average.
    Return a dict of each seriesID and the corresponding ave value.
    '''
    
    res = dict()
    all_series = r['Results']['series']
    for s in all_series:
        months = s['data']
        val = np.mean([float(m['value']) for m in months])
        res[s['seriesID']]=val
    return res



def series_id_lookup(s,state_table,industry_table):
    '''
    Need to go from series ID to State Name and Industry Name
    '''
    series_template = "SMU" + "19" + "00000" + "43000000" + "01"
    
    state_code = s[3:5]
    industry_code = s[10:12]
    
    return (state_table[str(state_code)],industry_table[str(industry_code)]   )

def main():
        
    # create lookup tables for state names and industry names    
    s = '''
    01	Alabama 
    02	Alaska	
    04	Arizona	
    05	Arkansas	
    06	California	
    08	Colorado	
    09	Connecticut	
    10	Delaware	
    11	District of Columbia	
    12	Florida	
    13	Georgia	
    15	Hawaii	
    16	Idaho	
    17	Illinois	
    18	Indiana	
    19	Iowa	
    20	Kansas	
    21	Kentucky	
    22	Louisiana	
    23	Maine	
    24	Maryland	
    25	Massachusetts	
    26	Michigan	
    27	Minnesota	
    28	Mississippi	
    29	Missouri	
    30	Montana	
    31	Nebraska	
    32	Nevada	
    33	New Hampshire	
    34	New Jersey	
    35	New Mexico	
    36	New York	
    37	North Carolina	
    38	North Dakota	
    39	Ohio	
    40	Oklahoma	
    41	Oregon	
    42	Pennsylvania	
    44	Rhode Island	
    45	South Carolina	
    46	South Dakota	
    47	Tennessee	
    48	Texas	
    49	Utah	
    50	Vermont	
    51	Virginia	
    53	Washington	
    54	West Virginia	
    55	Wisconsin	
    56	Wyoming	
    72	Puerto Rico	
    78	Virgin Islands	 '''
    pairs = [ row.split('\t') for row in s.split("\n")[1:]]
    state_id_table = dict()
    for r in pairs:
        state_id_table[r[0][-2:]] = r[1]
        
    industries = '''
    00	Total Nonfarm	
    05	Total Private	
    06	Goods Producing	
    07	Service-Providing	
    08	Private Service Providing	
    10	Mining and Logging	
    15	Mining, Logging, and Construction	
    20	Construction	
    30	Manufacturing	
    31	Durable Goods	
    32	Non-Durable Goods	
    40	Trade, Transportation, and Utilities	
    41	Wholesale Trade	
    42	Retail Trade	
    43	Transportation and Utilities	
    50	Information	
    55	Financial Activities	
    60	Professional and Business Services	
    65	Education and Health Services	
    70	Leisure and Hospitality	
    80	Other Services	
    90	Government	
    '''
    ind_pairs = [ row.split('\t') for row in industries.split("\n")][1:-1]
    ind_pairs
    industry_id_table = dict()
    for r in ind_pairs:
        industry_id_table[r[0][-2:]] = r[1]
        
     
    
    # now construct list of series for http request   
    
    
    industries_of_interest = [ "30", "20", "43", "42", "65", "90", "50", "55", "70", "10" ]
    series_list = []
    for industry in industries_of_interest:
        series_list.append( "SMU%s00000%s00000001" % ("19",industry) )
    

    
    headers={'Content-type': 'application/json'}
    data = json.dumps({
                        "seriesid": series_list,
                         "startyear": "2014",
                      "endyear": "2014",
                    "registrationKey":"52fef8e6fb614d32a24aa5ca9538e69a"
                      })
   
    # fetch request and decode json
    result=requests.post('http://api.bls.gov/publicAPI/v2/timeseries/data/', data = data, headers = headers).text
    result_j=json.loads(result)
    
    # for each series, extract year-long average value
    IDs_and_vals = extract_data(result_j)
        
    # decode state and industry numeric codes
    result = []
    for s_id in IDs_and_vals.keys():
        (a,b) =  series_id_lookup(s_id,state_id_table,industry_id_table)
        result.append((a,b,IDs_and_vals[s_id]))
        
    # write results in json triples of {StateName,IndustryName, Values}    
    with open('../fixtures/stateIndustryData.json','w') as writefile:
        arr=[]
        for (a,b,c) in result:
            out = dict()
            d = result[0]
            out["StateName"] = a
            out["IndustryName"] = b
            out["Value"] = c
            arr.append(json.dumps(out))
        writefile.write(json.dumps(arr))
        
    
    
if __name__ == "__main__":
    main()      