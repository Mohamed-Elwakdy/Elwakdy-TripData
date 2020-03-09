import matplotlib.pyplot as plt
import csv
import time
import datetime

tokens= []

fn = 'C:/Users/elwakdmf/Desktop/trip_data_1.csv'

f = open(fn,"r")
reader = csv.reader(f)

n = 0
t=0
m=0
l=0
c=0
f=0
j=0
i=0
#Q=0

doc = 0
puc = 0

d ={}
mhist12 = {}
chist = {}

d1 ={}
mhist13 = {}
chist1 = {}

d2 ={}
mhist14 = {}
chist2 = {}

d3 ={}
mhist15 = {}
chist3 = {}

mhist  = {}
mhist1 = {}
mhist2 = {}
mhist3 = {}
mhist4 = {}
mhist5 = {}
mhist6 = {}
mhist7 = {}
mhist8 = {}
mhist9 = {}
mhist10 = {}
mhist11 = {}


f2 = open('strip_data_78.csv','w')
f2.write("")
f2.close()

f2 = open('strip_data_78.csv','a')
writer = csv.writer(f2, delimiter=',',lineterminator='\n')

f3 = open('strip_data_79.csv','w')
f3.write("")
f3.close()

f3 = open('strip_data_79.csv','a')
writer1 = csv.writer(f3, delimiter=',',lineterminator='\n')


f4 = open('strip_data_80.csv','w')
f4.write("")
f4.close()

f4 = open('strip_data_80.csv','a')
writer2 = csv.writer(f4, delimiter=',',lineterminator='\n')


f5 = open('strip_data_81.csv','w')
f5.write("")
f5.close()

f5 = open('strip_data_81.csv','a')
writer3 = csv.writer(f5, delimiter=',',lineterminator='\n')

next(reader)

'''
Smallest_date_pickup_datetime = 0
Largest_date_pickup_datetime =  0
          
Smallest_date_dropoff_datetime = 0
Largest_date_dropoff_datetime = 0
        
Smallest_date_pickup_datetime = 0
Largest_date_pickup_datetime = 0


Smallest_date_dropoff_datetime = 0
Largest_date_dropoff_datetime = 0
'''


min_passenger_count = 0
max_passenger_count = 0

min_pickup_longitude = 0
max_pickup_longitude = 0

min_pickup_latitude = 0
max_pickup_latitude = 0

min_dropoff_longitude = 0
max_dropoff_longitude = 0

min_dropoff_latitude = 0
max_dropoff_latitude = 0

min_rate_code  = 0
max_rate_code  = 0

min_trip_time_in_secs  = 0
max_trip_time_in_secs  = 0

min_trip_distance  = 0
max_trip_distance  = 0




line = ['n','Hour','Avg_Passengers']
writer.writerow(line)
writer1.writerow(line)
writer2.writerow(line)
writer3.writerow(line)


start = time.time()

for line in reader:

        #print (line)

        n+=1        

        ######

        # The name of fields:
        # ------------------

        #['medallion', 'hack_license', 'vendor_id', 'rate_code', 'store_and_fwd_flag', 'pickup_datetime', 'dropoff_datetime',
        # 'passenger_count', 'trip_time_in_secs', 'trip_distance', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
        # 'dropoff_latitude']
            
        ######

        pickup_datetime=line[5]

        ######
        
        fdt = None
        try:

            fdt = datetime.datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
            puc += 1

        except ValueError as e:
            
            print('could not convert'+ str(e))

        #print (dts2)
            
        #######

        dropoff_datetime =line[6]

        #######
        
        fdt1 = None
        try:

            fdt1 = datetime.datetime.strptime(dropoff_datetime, "%Y-%m-%d %H:%M:%S")
            doc+=1

        except ValueError as e:
            
            print('could not convert'+ str(e))

        #print (dts3)

        ########

        # The smallest and lasrgest date of pickup_datetime
        # Compare all dates with the first date in the list "01/01/13  03:11:48"

        if puc == 1:
            Smallest_date_pickup_datetime = fdt
            Largest_date_pickup_datetime = fdt
            
        if doc == 1:
            Smallest_date_dropoff_datetime = fdt1
            Largest_date_dropoff_datetime = fdt1
        
        if fdt is not None: 
            if Smallest_date_pickup_datetime > fdt:
                Smallest_date_pickup_datetime = fdt

            if Largest_date_pickup_datetime < fdt:
                Largest_date_pickup_datetime = fdt

        if fdt1 is not None:  
            if Smallest_date_dropoff_datetime > fdt1:
                Smallest_date_dropoff_datetime = fdt1
                
            if Largest_date_dropoff_datetime < fdt1:
                Largest_date_dropoff_datetime = fdt1

        # The distinct values for each field (if possible)
        # ------------------------------------------------
        
        
        pickup_datetime = line[5].replace('-',':')
        pickup_datetime = pickup_datetime.replace(' ',':')

        pickup_datetime = pickup_datetime[0:4] + ':' + pickup_datetime[5:7] + ':' + pickup_datetime[8:10] + pickup_datetime[10:13]+ pickup_datetime[13:16]
        
        if pickup_datetime in mhist.keys():
            
            mhist[pickup_datetime] += 1  
             
        else:
            
            mhist[pickup_datetime] = 1

        if 'pick:p_:atetime' in mhist:

            del mhist['pick:p_:atetime']

        ###   

        dropoff_datetime = line[6].replace('-',':')
        dropoff_datetime = dropoff_datetime.replace(' ',':')

        dropoff_datetime = dropoff_datetime[0:4] + ':' + dropoff_datetime[5:7] + ':' + dropoff_datetime[8:10] + dropoff_datetime[10:13]+ dropoff_datetime[13:16]
        
        if dropoff_datetime in mhist1.keys():
            mhist1[dropoff_datetime] += 1

        else:
            mhist1[dropoff_datetime] = 1
            
        if 'drop:ff:datetime' in mhist1:

            del mhist1['drop:ff:datetime']

        ###
            
        medallion= line [0]    

        if medallion in mhist2.keys():
            mhist2[medallion] += 1
        else:
            mhist2[medallion] = 1

        if 'medallion' in mhist2:

            del mhist2['medallion']

        ###

        hack_license= line [1]    

        if hack_license in mhist3.keys():
            mhist3[hack_license] += 1
        else:
            mhist3[hack_license] = 1

        if 'hack_license' in mhist3:
            del mhist3['hack_license']

        ###

        rate_code = line [3]    

        if rate_code in mhist4.keys():
             mhist4[rate_code] += 1
        else:
             mhist4[rate_code] = 1

        if 'rate_code' in mhist4:
             del mhist4['rate_code']

        ###

        passenger_count = line [7]    

        if passenger_count in mhist5.keys():
             mhist5[passenger_count] += 1
        else:
             mhist5[passenger_count] = 1

        if 'passenger_count' in mhist5:
             del mhist5['passenger_count']

        ###

        trip_time_in_secs = line [8]    

        if trip_time_in_secs in mhist6.keys():
             mhist6[trip_time_in_secs] += 1
        else:
             mhist6[trip_time_in_secs] = 1

        if 'trip_time_in_secs' in mhist6:
             del mhist6['trip_time_in_secs']

        ###

        trip_distance = line [9]
        #trip_distance = trip_distance[0:4]

        if trip_distance in mhist7.keys():
             mhist7[trip_distance] += 1
        else:
             mhist7[trip_distance] = 1

        if 'trip_distance' in mhist7:
             del mhist7['trip_distance']

        ###print (d)#hour count

        pickup_longitude = line [10]
        pickup_longitude = pickup_longitude [0:6]

        if pickup_longitude in mhist8.keys():
             mhist8[pickup_longitude] += 1
        else:
             mhist8[pickup_longitude] = 1

        if 'pickup' in mhist8:
             del mhist8['pickup']

        ###

        pickup_latitude = line [11]
        pickup_latitude = pickup_latitude [0:6]

        if pickup_longitude in mhist9.keys():
             mhist9[pickup_longitude] += 1
        else:
             mhist9[pickup_longitude] = 1

        if 'pickup' in mhist9:
             del mhist9['pickup']

        ###

        dropoff_longitude = line [12]
        dropoff_longitude = dropoff_longitude [0:6]

        if dropoff_longitude in mhist10.keys():
             mhist10[dropoff_longitude] += 1
        else:
             mhist10[dropoff_longitude] = 1

        if 'dropof' in mhist10:
             del mhist10['dropof']

        ###

        dropoff_latitude = line [13]
        dropoff_latitude = dropoff_latitude [0:6]

        if dropoff_latitude in mhist11.keys():
             mhist11[dropoff_latitude] += 1
        else:
             mhist11[dropoff_latitude] = 1

        if 'dropof' in mhist11:
             del mhist11['dropof']

        # Some sample data for each field in the dataset
        # ----------------------------------------------

       # if n % 5 ==0:
          #      print (line)
                #print ("Hello")

        # The min and max values
        # ----------------------
     
        if t>0:
            
            if t == 1:
                min_passenger_count = line[7]
                max_passenger_count = line[7]

                min_pickup_longitude = line[10]
                min_pickup_longitude = min_pickup_longitude                                                                                                                                   
                max_pickup_longitude = line[10]
                max_pickup_longitude = max_pickup_longitude 

                min_pickup_latitude = line[11]
                min_pickup_latitude = min_pickup_latitude 
                max_pickup_latitude = line[11]
                max_pickup_latitude =max_pickup_latitude 

                min_dropoff_longitude = line[12]
                min_dropoff_longitude = min_dropoff_longitude 
                max_dropoff_longitude = line[12]
                max_dropoff_longitude = max_dropoff_longitude 

                min_dropoff_latitude = line[13]
                min_dropoff_latitude = min_dropoff_latitude
                max_dropoff_latitude = line[13]
                max_dropoff_latitude = max_dropoff_latitude 

                
                min_rate_code = line[3]
                max_rate_code = line[3]

                min_rate_code = line[8]
                max_rate_code = line[8]

                min_trip_distance   = line[9]
                max_trip_distance   = line[9]
                
            else:
                if line[7] > max_passenger_count:
                    max_passenger_count = line[7]
                if line[7] < min_passenger_count:
                    min_passenger_count = line[7]

                if line[10] != "" and float(line[10]) < 100 and float(line[10])>-99:

                        if float(line[10]) < float(max_pickup_longitude):
                            max_pickup_longitude = line[10]
                        if float(line[10]) > float(min_pickup_longitude):
                            min_pickup_longitude = line[10]

                if line[11] != "" and float(line[11]) < 100 and float(line[11])>-99:

                        if float(line[11]) > float(max_pickup_latitude):
                            max_pickup_latitude = line[11]
                        if float(line[11]) < float(min_pickup_latitude):
                            min_pickup_latitude = line[11]

                if line[12] != "" and float(line[12]) < 100 and float(line[12])>-99:

                        if float(line[12]) < float(max_dropoff_longitude):
                            max_dropoff_longitude = line[12]
                        if float(line[12]) > float(min_dropoff_longitude):
                            min_dropoff_longitude = line[12]

                if line[13] != "" and float(line[13]) < 100 and float(line[13])>-99:

                        if float(line[13]) > float(max_dropoff_latitude):
                            max_dropoff_latitude = line[13]
                        if float(line[13]) < float(min_dropoff_latitude):
                            min_dropoff_latitude = line[13]

                if line[3] > max_rate_code:
                        max_rate_code = line[3]
                if line[3] < min_rate_code:
                        min_rate_code = line[3]

                if int(line[8]) > int(max_trip_time_in_secs):
                        max_trip_time_in_secs  = line[8]
                if int(line[8]) < int(min_trip_time_in_secs):
                        min_trip_time_in_secs  = line[8]

                if line[9] > max_trip_distance :
                        max_trip_distance = line[9]
                if line[9] < min_trip_distance :
                        min_trip_distance = line[9]                

        t+=1


        # The average number of passengers each hour of the day (pickup_datetime) 

        Hour_datetime = pickup_datetime[11:13]
        Hour_datetime1 = dropoff_datetime[11:13]

      
        if Hour_datetime in d.keys():
                d[Hour_datetime] += 1
        else:
                d[Hour_datetime] = 1

        if Hour_datetime in mhist12.keys():

                mhist12[Hour_datetime] += int(line[7])
        else:
                mhist12[Hour_datetime] = int(line[7])


        # Get one out of every thousand rows (pickup_datetime)

        if n % 1000 == 0:

                if Hour_datetime in d1.keys():
                        d1[Hour_datetime] += 1
                else:
                        d1[Hour_datetime] = 1

                if Hour_datetime in mhist13.keys():

                        mhist13[Hour_datetime] += int(line[7])
                else:
                        mhist13[Hour_datetime] = int(line[7])
                        
        # The average number of passengers each hour of the day (dropoff_datetime) 

        if Hour_datetime1 in d2.keys():
                d2[Hour_datetime1] += 1
        else:
                d2[Hour_datetime1] = 1


        if Hour_datetime1 in mhist14.keys():
                mhist14[Hour_datetime1] += int(line[7])

        else:
                mhist14[Hour_datetime1] = int(line[7])

        # Get one out of every thousand rows (dropoff_datetime)
        
        if n % 1000 == 0:
                if Hour_datetime1 in d3.keys():
                        d3[Hour_datetime1] += 1
                else:
                        d3[Hour_datetime1] = 1

                if Hour_datetime1 in mhist15.keys():
                        mhist15[Hour_datetime1] += int(line[7])
                else:
                        mhist15[Hour_datetime1] = int(line[7])

                
        #if n > 20:        
         #   break

for k in mhist12.keys():
        chist[k] = int(mhist12.get(k)) / d[k]
                #print (int(mhist.get(k)))
for k in mhist13.keys():
        chist1[k] = int(mhist13.get(k)) / d1[k]

for k in mhist14.keys():
        chist2[k] = int(mhist14.get(k)) / d2[k]
                #print (int(mhist.get(k)))

for k in mhist15.keys():
        chist3[k] = int(mhist15.get(k)) / d3[k]
                        #print (int(mhist.get(k))


for key, val in chist.items():
    line = [str(t),key, str(val)]
    t +=1
    writer.writerow(line)

for key, val in chist1.items():
    line = [str(m),key, str(val)]
    m +=1
    writer1.writerow(line)

for key, val in chist2.items():
    line = [str(l),key, str(val)]
    l +=1
    writer2.writerow(line)

for key, val in chist3.items():
    line = [str(c),key, str(val)]
    c +=1
    writer3.writerow(line)

f2.close()
f3.close()
f4.close()
f5.close()

# Plotting Minimum latitude against Maximum Longitude & maximum Latitude against Minimum Longitude   
'''
# line 1 points 
max_pickup_longitude_latitude = [float(max_pickup_longitude),float(max_pickup_latitude)] 
min_pickup_latitude_longitude = [float(min_pickup_latitude),float(min_pickup_longitude)]

# line 2 points 
max_dropoff_longitude_latitude = [float(max_dropoff_longitude),float(max_dropoff_latitude)] 
min_dropoff_latitude_longitude = [float(min_dropoff_latitude),float(min_dropoff_longitude)]

plt.plot(max_pickup_longitude_latitude, min_pickup_latitude_longitude,'ro', label = "max_min_pickup_longitude_latitude")
plt.plot(max_dropoff_longitude_latitude, min_dropoff_latitude_longitude,'ro', label = "max_min_dropoff_longitude_latitude")

# naming the x axis 
plt.xlabel('max_pickup_dropoff_longitude_latitude') 
# naming the y axis 
plt.ylabel('min_pickup_dropoff_latitude_longitude ') 

# giving a title to my graph 
plt.title('max_min_pickup_dropoff_longitude_latitude') 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show()

'''

print ('Time in seconds =' + str ((time.time()-start)))




print ("Smallest_date_pickup_datetime = ", Smallest_date_pickup_datetime)
print ("Largest_date_pickup_datetime = ", Largest_date_pickup_datetime)

print ("Smallest_date_dropoff_datetime = ", Smallest_date_dropoff_datetime)
print ("Largest_date_dropoff_datetime = ", Largest_date_dropoff_datetime)


print ("Hi")
print ("Hi")
print ("Hi")

        
print (d)#hour count
print (mhist12)#sum of passengers in each hour
print (chist)#passengers per hour (average)

print ("dmhist12")
print ("dmhist12")
print ("dmhist12")
print ("dmhist12")

print (d1)
print (mhist13)
print (chist1)

print ("dmhist13")
print ("dmhist13")
print ("dmhist13")
print ("dmhist13")


print (d2)
print (mhist14)
print (chist2)

print ("dmhist14")
print ("dmhist14")
print ("dmhist14")
print ("dmhist14")


print (d3)
print (mhist15)
print (chist3)

print ("dmhist15")
print ("dmhist15")
print ("dmhist15")
print ("dmhist15")


print ("Hi")
print ("Hi")
print ("Hi")
print ("Hi")
print ("Hi")
print ("Hi")


print (mhist)
print ("mhist")
print ("mhist")
print ("mhist")
print ("mhist")


print (mhist1)
print ("mhist1")
print ("mhist1")
print ("mhist1")
print ("mhist1")
print ("mhist1")


print (mhist2)
print ("mhist2")
print ("mhist2")
print ("mhist2")
print ("mhist2")
print ("mhist2")
print ("mhist2")


print (mhist3)
print ("mhist3")
print ("mhist3")
print ("mhist3")
print ("mhist3")
print ("mhist3")



print (mhist4)
print ("mhist4")
print ("mhist4")
print ("mhist4")
print ("mhist4")
print ("mhist4")
print ("mhist4")


print (mhist5)
print ("mhist5")
print ("mhist5")
print ("mhist5")
print ("mhist5")
print ("mhist5")


print (mhist6)
print ("mhist6")
print ("mhist6")
print ("mhist6")
print ("mhist6")
print ("mhist6")
print ("mhist6")



print (mhist7)
print ("mhist7")
print ("mhist7")
print ("mhist7")
print ("mhist7")
print ("mhist7")


print (mhist8)
print ("mhist8")
print ("mhist8")
print ("mhist8")
print ("mhist8")
print ("mhist8")


print (mhist9)
print ("mhist9")
print ("mhist9")
print ("mhist9")
print ("mhist9")
print ("mhist9")


print (mhist10)
print ("mhist10")
print ("mhist10")
print ("mhist10")
print ("mhist10")

print (mhist11)
print ("mhist11")
print ("mhist11")
print ("mhist11")
print ("mhist11")
print ("mhist11")

print (max_passenger_count)
print (min_passenger_count)
print ("M and N passenger")
print ("M and N passenger")
print ("M and N passenger")
print ("M and N passenger")

print (max_pickup_longitude)
print (min_pickup_longitude)
print ("M and N pickup-Longitude")
print ("M and N pickup-Longitude")
print ("M and N pickup-Longitude")
print ("M and N pickup-Longitude")

print (max_pickup_latitude)
print (min_pickup_latitude)
print ("M and N pickup-Latitude")
print ("M and N pickup-Latitude")
print ("M and N pickup-Latitude")
print ("M and N pickup-Latitude")

print (max_dropoff_longitude)
print (min_dropoff_longitude)
print ("M and N droff-longitude")
print ("M and N droff-longitude")
print ("M and N droff-longitude")
print ("M and N droff-longitude")


print (max_dropoff_latitude)
print (min_dropoff_latitude)
print ("M and N droff-latitude")
print ("M and N droff-latitude")
print ("M and N droff-latitude")
print ("M and N droff-latitude")


print (max_rate_code )
print (min_rate_code)
print ("max_min_rate_code")
print ("max_min_rate_code")
print ("max_min_rate_code")
print ("max_min_rate_code")

print (max_trip_time_in_secs)
print (min_trip_time_in_secs)
print ("max_min_trip_time_in_secs")
print ("max_min_trip_time_in_secs")
print ("max_min_trip_time_in_secs")
print ("max_min_trip_time_in_secs")


print (max_trip_distance)
print (min_trip_distance)
print ("max_min_trip_distance")
print ("max_min_trip_distance")
print ("max_min_trip_distance")
print ("max_min_trip_distance")



'''
with open('C:/Users/elwakdmf/Desktop/trip_data_1.csv', 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    headers = d_reader.fieldnames

print (headers)
print ("headers")
print ("headers")
print ("headers")
print ("headers")


#print(row_count)

for line in reader:
        
        i+=1

print ('Number of rows= ' + str(i))
print ('Number of rowss')
print ('Number of rowss')
print ('Number of rowss')
print ('Number of rowss')

'''
