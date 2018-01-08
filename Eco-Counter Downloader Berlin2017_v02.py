import json
import urllib2
from datetime import date, timedelta, datetime
from time import strftime

#define output path
metriclog = open(ENTER PATH, 'w')

#define time interval
startYear = "20160420"
endYear= "20160420"

#Installations
JANN_Alex={'installation':"Jannowitzbr¸cke", 'direction':"Alexanderplatz", 'link':"38395", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101024661"}
JANN_Mori={'installation':"Jannowitzbr¸cke", 'direction':"Moritzplatz", 'link':"38394", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102024661"}

OBER_Frie={'installation':"Oberbaumbr¸cke", 'direction':"Friedrichshain", 'link':"68446", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032212"}
OBER_Kreu={'installation':"Oberbaumbr¸cke", 'direction':"Kreuzberg", 'link':"68408", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032212"}

ALBE_Sued={'installation':"Alberichstraﬂe", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101033037"}
ALBE_Nord={'installation':"Alberichstraﬂe", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102033037"}

FRAN_Lich={'installation':"FrankfurterAllee", 'direction':"Lichtenberg", 'link':"57506", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032154"}
FRAN_Alex={'installation':"FrankfurterAllee", 'direction':"Alexanderplatz", 'link':"128843", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032154"}

PAUL_West={'installation':"PaulundPaulaUferweg", 'direction':"Westen", 'link':"97516", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101033035"}
PAUL_Oste={'installation':"PaulundPaulaUferweg", 'direction':"Osten", 'link':"97515", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102033035"}

BERL_Nord={'installation':"BerlinerStraﬂe", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032155"}
BERL_Sued={'installation':"BerlinerStraﬂe", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032155"}

MAYB_Oste={'installation':"Maybachufer", 'direction':"Osten", 'link':"43253", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032236"}
MAYB_West={'installation':"Maybachufer", 'direction':"Westen", 'link':"43252", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032236"}

YORC_Kreu={'installation':"Yorckstraﬂe", 'direction':"Kreuzberg", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101033038"}
YORC_Scho={'installation':"Yorckstraﬂe", 'direction':"Schoeneberg", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102033038"}

MONU_Oste={'installation':"Monumentenstraﬂe", 'direction':"Osten", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032165"}
MONU_West={'installation':"Monumentenstraﬂe", 'direction':"Westen", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032165"}

PRIN_Nord={'installation':"Prinzregentenstraﬂe", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101033039"}
PRIN_Sued={'installation':"Prinzregentenstraﬂe", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102033039"}

BREI_Oste={'installation':"Breitenbachplatz", 'direction':"Osten", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032163"}
BREI_West={'installation':"Breitenbachplatz", 'direction':"Westen", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032163"}

MARI_Nord={'installation':"MariendorferDamm", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032166"}
MARI_Sued={'installation':"MariendorferDamm", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032166"}

KLOS_Nord={'installation':"Klosterstraﬂe", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032161"}
KLOS_Sued={'installation':"Klosterstraﬂe", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032161"}

MARK_Sued={'installation':"Markstraﬂe", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032169"}
MARK_Nord={'installation':"Markstraﬂe", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032169"}

SCHW_Nord={'installation':"SchwedterSteg", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032159"}
SCHW_Sued={'installation':"SchwedterSteg", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032159"}

INVA_Oste={'installation':"Invalidenstraﬂe", 'direction':"Osten", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032152"}
INVA_West={'installation':"Invalidenstraﬂe", 'direction':"Westen", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032152"}

KAIS_Sued={'installation':"Kaisersteg", 'direction':"Sueden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/101032237"}
KAIS_Nord={'installation':"Kaisersteg", 'direction':"Norden", 'link':"", 'url':"http://www.eco-public.com/api/cw6Xk4jW4X4R/data/periode/102032237"}


metriclog.write("location,volume,hour,date"  + "\n")
for i in [ 
JANN_Alex,
JANN_Mori,

OBER_Frie,
OBER_Kreu,

ALBE_Sued,
ALBE_Nord,

FRAN_Lich,
FRAN_Alex,

PAUL_West,
PAUL_Oste,

BERL_Nord,
BERL_Sued,

MAYB_Oste,
MAYB_West,

YORC_Kreu,
YORC_Scho,

MONU_Oste,
MONU_West,

PRIN_Nord,
PRIN_Sued,

BREI_Oste,
BREI_West,

MARI_Nord,
MARI_Sued,

KLOS_Nord,
KLOS_Sued,

MARK_Sued,
MARK_Nord,

SCHW_Nord,
SCHW_Sued,

INVA_Oste,
INVA_West,

KAIS_Sued,
KAIS_Nord,]:

    # Specify time interval of results
    # step=2 counts per 15minutes
    # step=3 counts per hour
    # step=4 counts per day   
    url=i['url'] + "?begin=" + startYear + "&end=" + endYear + "&step=3"

    print 'Loading ' + i['installation'] + ' ' + i['direction'] + '...'
    
    
    # counts
    response = urllib2.urlopen(url)
    json_data = response.read()
    datapoints = json.loads(json_data)
    for datapoint in datapoints:
        if datapoint['comptage'] is None:
            continue
        metric_string = i['installation'] + '_' + i['direction']  + ', ' + str(datapoint['comptage']) + ', ' +   str(datetime.fromtimestamp(int(datapoint['timestamp']/1000)).strftime('%H')) +', ' +   str(datetime.fromtimestamp(int(datapoint['timestamp']/1000)).strftime('%d.%m.%Y'))
        metriclog.write(metric_string + "\n")
        
#OUTPUT FORMAT:
#location,volume,hour,date
#Jannowitzbr¸cke_Alexanderplatz, 52, 00, 14.06.2016


metriclog.close()
print 'Done.'