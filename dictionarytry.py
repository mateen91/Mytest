import os

class detailInfo:
    def __init__(self, date , maxtemp, mintemp, maxhumid, minhumid):
        self.date= date
        self.maxTemp= maxtemp
        self.minTemp = mintemp
        self.maxHumid= maxhumid
        self.minHumid= minhumid


filecount=0
my_dict={}
yearlist=[]
path = '/home/mateenahmeed/Downloads/weatherdata'
for filename in os.listdir(path):
    filecount=filecount+1
    print(str(filecount)+'-Filename--> '+ filename)
    tokens = filename.split("_")
    year= tokens[2]
    print year
    list1=[]
    if year in my_dict:
        list1=my_dict[year]
        print("got old one ")
    else:
        my_dict[year]=list1
        yearlist.append(year)
        print("got new one ")

    file=open(path+"/"+filename, 'r')
    firstline = 1
    for line in file:
        details = line.split(",")
        if len(details) > 1:
            date= details[0];
            maxT= details[1]
            if len(maxT) == 1:
                maxT="0"+maxT
            minT= details[3]
            if len(minT) == 1:
                minT="0"+minT
            maxH= details[7]
            if len(maxH) == 1:
                maxH="0"+maxT
            minH= details[9]
            if len(minH) == 1:
                minH="0"+minH

            list1.append( detailInfo(date,maxT,minT,maxH,minH))
            #list1.append( detailInfo(details[0],details[1],details[3],details[7],details[9]))
    file.close()
    my_dict[year]=list1



list_cur= my_dict["2003"]
list_cur.sort( key=lambda x: x.maxTemp, reverse=True)
print list_cur[12].maxHumid
for x in list_cur:
    print (x.date +" == " + x.maxTemp +" == "+x.minTemp  +" == " + x.maxHumid +" == "+x.minHumid )

yearlist.sort()
print("Year     MaxTemp     MinTemp     MaxHumid    Minhumid")
print("-----------------------------------------------------")
for year in yearlist:
    #print ("==> " +year)
    list_cur= my_dict[year]


    list_cur.sort( key=lambda x: x.maxTemp, reverse=True)
    pos=0
    while True:
        if (list_cur[pos].maxTemp == "Max TemperatureC") or (list_cur[pos].maxTemp == ""):
            pos = pos +1
            #print "temp check"
        else:
            maxT= list_cur[pos].maxTemp
            break

    #for x in list_cur:
      # print (x.date +" == " + x.maxTemp +" == "+x.minTemp  +" == " + x.maxHumid +" == "+x.minHumid )


    #newlist = sorted(list1, key=lambda x: x.maxTemp, reverse=True)
    #print ( "Max temperature"+list_cur[12].date +" == " + list_cur[12].maxTemp +" == "+list_cur[12].minTemp )
    #for x in list1:
       # print (x.date +" == " + x.maxTemp +" == "+x.minTemp )
        #print x.maxTemp
       # print(x.maxHumid)
    #break
    list_cur.sort( key=lambda x: x.minTemp, reverse=False)
    #print list_cur[0].minTemp
    pos=0
    while True:
        if (list_cur[pos].minTemp == "Min TemperatureC") or (list_cur[pos].minTemp == ""):
            pos = pos +1
           # print "temp check"
        else:
            minT=  list_cur[pos].minTemp
            break

    #print ("Min temperature"+list_cur[0].date +" == " + list_cur[0].maxTemp +" == "+list_cur[0].minTemp )

    list_cur.sort( key=lambda x: x.minHumid, reverse=False)
    #print list_cur[0].minHumid
    pos=0
    while True:
        if (list_cur[pos].minHumid == " Min Humidity") or (list_cur[pos].minHumid == ""):
            pos = pos +1
            #print "min humid check"
        else:
            minH= list_cur[pos].minHumid
            break
    #print ("Min humidity"+list_cur[0].date +" == " + list_cur[0].maxHumid +" == "+list_cur[0].minHumid )



    list_cur.sort( key=lambda x: x.maxHumid, reverse=True)
    #print list_cur[0].maxHumid
    pos=0
    while True:
        if (list_cur[pos].maxHumid == "Max Humidity") or (list_cur[pos].maxHumid == ""):
            pos = pos +1
            #print "max humid  check"
        else:
            maxH=  list_cur[pos].maxHumid
            break
    #print ("Max humidity"+list_cur[12].date +" == " + list_cur[12].maxHumid +" == "+list_cur[12].minHumid )
    #for x in list1:
        #print (x.date +" == " + x.maxTemp +" == "+x.minTemp )

    print(year +"       "+ maxT +"          "+ minT +"          "+maxH +"           "+minH)


