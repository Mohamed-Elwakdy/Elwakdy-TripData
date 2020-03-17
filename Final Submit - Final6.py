import csv
import time
import datetime
import math

tokens= []

fn = 'trip_data_1.csv'

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
u=0

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

d4 ={}
mhist16 = {}
chist4 = {}

d5 ={}
mhist17 = {}
chist5 = {}

d6 ={}
mhist18 = {}
chist6 = {}

d7 ={}
mhist19 = {}
chist7 = {}

mhist  = {}
mhist1 = {}
mhist2 = {}
mhist3 = {}
mhist4 = {}
mhist5 = {}
mhist6 = {}
mhist7 = {}

mhist_inside_Boundingbox = {}
mhist_outside_Boundingbox = {}

mhist1_inside_Boundingbox = {}
mhist1_outside_Boundingbox = {}

mhist2_inside_Boundingbox = {}
mhist2_outside_Boundingbox = {}

mhist3_inside_Boundingbox = {}
mhist3_outside_Boundingbox = {}

####

mhist2_inside_small_Boundingbox ={}

f2 = open('strip_data_118.csv','w')
f2.write("")
f2.close()
f2 = open('strip_data_118.csv','a')
writer = csv.writer(f2, delimiter=',',lineterminator='\n')

f3 = open('strip_data_119.csv','w')
f3.write("")
f3.close()
f3 = open('strip_data_119.csv','a')
writer1 = csv.writer(f3, delimiter=',',lineterminator='\n')

f4 = open('strip_data_120.csv','w')
f4.write("")
f4.close()
f4 = open('strip_data_120.csv','a')
writer2 = csv.writer(f4, delimiter=',',lineterminator='\n')

f5 = open('strip_data_121.csv','w')
f5.write("")
f5.close()
f5 = open('strip_data_121.csv','a')
writer3 = csv.writer(f5, delimiter=',',lineterminator='\n')

f6 = open('strip_data_122.csv','w')
f6.write("")
f6.close()
f6 = open('strip_data_122.csv','a')
writer4 = csv.writer(f6, delimiter=',',lineterminator='\n')

f7 = open('strip_data_123.csv','w')
f7.write("")
f7.close()
f7 = open('strip_data_123.csv','a')
writer5 = csv.writer(f7, delimiter=',',lineterminator='\n')

f8 = open('strip_data_124.csv','w')
f8.write("")
f8.close()
f8 = open('strip_data_124.csv','a')
writer6 = csv.writer(f8, delimiter=',',lineterminator='\n')

f9 = open('strip_data_125.csv','w')
f9.write("")
f9.close()
f9 = open('strip_data_125.csv','a')
writer7 = csv.writer(f9, delimiter=',',lineterminator='\n')


next(reader)


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


###

max_passenger_count_bounding = 0
min_passenger_count_bounding = 0

max_pickup_longitude_bounding = 0
min_pickup_longitude_bounding = 0

max_pickup_latitude_bounding = 0
min_pickup_latitude_bounding = 0

max_dropoff_longitude_bounding = 0
min_dropoff_longitude_bounding = 0

max_dropoff_latitude_bounding = 0
min_dropoff_latitude_bounding = 0
                
min_rate_code_bounding = 0
max_rate_code_bounding = 0

min_trip_distance_bounding = 0
max_trip_distance_bounding = 0

min_trip_distance_bounding   = 0
max_trip_distance_bounding   = 0


max_rate_code_insidebox = 0
min_rate_code_insidebox = 0

max_trip_time_in_secs_insidebox = 0
min_trip_time_in_secs_insidebox = 0

max_trip_distance_insidebox = 0
min_trip_distance_insidebox = 0


max_passenger_count_insidebox = 0
min_passenger_count_insidebox = 0

#####

max_pickup_longitude_big_bounday = 0
min_pickup_longitude_big_bounday = 0

max_pickup_latitude_big_bounday = 0
min_pickup_latitude_big_bounday = 0

max_dropoff_longitude_big_bounday = 0
min_dropoff_longitude_big_bounday = 0

max_dropoff_latitude_big_bounday = 0
min_dropoff_latitude_big_bounday = 0

max_pickup_longitude_smallbounding = 0
min_pickup_longitude_smallbounding = 0

max_pickup_latitude_smallbounding = 0
min_pickup_latitude_smallbounding = 0

max_dropoff_small_longitude_bounding = 0
min_dropoff_small_longitude_bounding = 0


max_rate_code_insidebox_Pickuplatitude = 0
 

line = ['n','Hour','Avg_Passengers']

writer.writerow(line)
writer1.writerow(line)
writer2.writerow(line)
writer3.writerow(line)

line1 = ['n','Day','Avg_Passengers']
writer4.writerow(line1)
writer5.writerow(line1)
writer6.writerow(line1)
writer7.writerow(line1)

start = time.time()


for line in reader:
        
        i+=1

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
            
        #######

        dropoff_datetime =line[6]

        #######
        
        fdt1 = None
        try:

            fdt1 = datetime.datetime.strptime(dropoff_datetime, "%Y-%m-%d %H:%M:%S")
            doc+=1

        except ValueError as e:
            
            print('could not convert'+ str(e))

        ########

        # The smallest and lasrgest date of pickup_datetime
        # -------------------------------------------------

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
             

        # Some sample data for each field in the dataset
        # ----------------------------------------------

        if n % 1000000 == 0:
                print (line)
                
        # The min and max values
        # ----------------------
     
        if t>0:
                
            if t == 1:
                min_passenger_count = line[7]
                max_passenger_count = line[7]

                #Longitude is in the range -180 and +180 specifying coordinates west and east of the Prime Meridian, respectively.
                #For reference, the Equator has a latitude of 0°, the North pole has a latitude of 90° north (written 90° N or +90°),
                #and the South pole has a latitude of -90°.

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

                # Longitude and Latitude (inside the bounding box) 

                min_pickup_longitude_bounding = line[10]
                min_pickup_longitude_bounding = min_pickup_longitude_bounding                                                                                                                                   
                max_pickup_longitude_bounding = line[10]
                max_pickup_longitude_bounding = max_pickup_longitude_bounding

                min_pickup_latitude_bounding = line[10]
                min_pickup_latitude_bounding = min_pickup_latitude_bounding                                                                                                                               
                max_pickup_latitude_bounding = line[10]
                min_pickup_latitude_bounding = min_pickup_latitude_bounding
                
            else:

                # Max and Minimum passengers where the maxmum number of passengers in a vichale is 5 and minimum number is
                # 1
                
                if line[7] > max_passenger_count and int (line[7]) < 6 :
                    max_passenger_count = line[7]
                if line[7] < min_passenger_count and int (line [7]) > 0 and int (line [7]) < 6:
                    min_passenger_count = line[7]               


                #########
                
                # Here, I take the logitude and latitude points into consideration into a big boundary box and then calculate the max and min
                # values.

                if line[10] != "" and float(line[10]) <= 180 and float(line[10])>= -180 and line[11] != "" and float(line[11]) <= 90 and float(line[11])>=-90:

                     if float(line[10]) < float(max_pickup_longitude_big_bounday):
                            max_pickup_longitude_big_bounday = line[10]
                     if float(line[10]) > float(min_pickup_longitude_big_bounday):
                            min_pickup_longitude_big_bounday = line[10]
        

                     if float(line[11]) > float(max_pickup_latitude_big_bounday):
                            max_pickup_latitude_big_bounday = line[11]
                     if float(line[11]) < float(min_pickup_latitude_big_bounday):
                            min_pickup_latitude_big_bounday = line[11]


                     if line[12] != "":
                             if float(line[12]) < float(max_dropoff_longitude_big_bounday):
                                     max_dropoff_longitude_big_bounday = line[12]
                             if float(line[12]) > float(min_dropoff_longitude_big_bounday):
                                     min_dropoff_longitude_big_bounday = line[12]

                     if line[13] != "":
                             if float(line[13]) > float(max_dropoff_latitude_big_bounday):
                                     max_dropoff_latitude_big_bounday = line[13]
                             if float(line[13]) < float(min_dropoff_latitude_big_bounday):
                                     min_dropoff_latitude_big_bounday = line[13]
                      # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LONGITUDE 
                #-----------------------------------------------------------------------------------------------------

                # compute the number points of pickup longitude inside the bounding box
                # The number of points inside the bounding box for 50000 pickup longitude is really big number compared to the number of points
                # outside the bounding box:

                # {'-74.00': 5077, '-73.97': 8477, '-73.96': 5123, '-73.99': 8103, '-73.98': 11736, '-74.01': 921, '-73.78': 515,
                #'-73.95': 5087, '-73.86': 368, '-73.94': 1710, '-73.90': 70, '-73.87': 461, '-73.79': 95, '-73.92': 287, '-73.93': 361,
                #'-73.91': 221, '-73.77': 172, '-73.81': 18, '-73.88': 61, '-73.89': 65, '-73.80': 27, '-74.10': 1, '-73.85': 25,
                #'-73.84': 18, '-74.15': 2, '-74.16': 4, '-73.74': 1, '-74': 5, '-73.83': 18, '-73.82': 12, '-74.04': 8, '-74.03': 3,
                #'-74.02': 5, '-73.73': 1, '-74.09': 2, '-74.07': 1, '-74.05': 1, '-74.08': 1, '-74.06': 1, '-73.70': 1, '-73.72': 1,
                #'-74.12': 1, '-74.14': 1, '-74.23': 1, '-73.75': 1, '-73.76': 1}

                # The number of points inside the bounding box for 500000 pickup longitude is really big number compared to the number of
                # points outside the bounding box:

                #{'-74.00': 50131, '-73.97': 90306, '-73.96': 52216, '-73.99': 82372, '-73.98': 117241, '-74.01': 10205, '-73.78': 6956,
                #'-73.95': 44821, '-73.86': 6017, '-73.94': 11850, '-73.90': 483, '-73.87': 6760, '-73.79': 1338, '-73.92': 1721,
                #'-73.93': 2677, '-73.91': 1192, '-73.77': 1906, '-73.81': 112, '-73.88': 860, '-73.89': 416, '-73.80': 246, '-74.10': 8,
                #'-73.85': 145, '-73.84': 183, '-74.15': 13, '-74.16': 54, '-73.74': 5, '-74': 54, '-73.83': 117, '-73.82': 52, '-74.04': 29,
                #'-74.03': 49, '-74.02': 55, '-73.73': 5, '-74.09': 7, '-74.07': 18, '-74.05': 13, '-74.08': 7, '-74.06': 19, '-73.70': 6,
                #'-73.72': 12, '-74.12': 11, '-74.14': 5, '-74.23': 1, '-73.75': 5, '-73.76': 14, '-74.18': 9, '-73.71': 6, '-74.17': 14,
                #'-74.11': 8, '-74.20': 1, '-74.25': 4, '-74.22': 3, '-74.19': 2, '-74.13': 6, '-74.21': 1}

                # The number of points inside the bounding box for 14776614 pickup longitude is really big number compared to the number of
                # points outside the bounding box:

                #{'-74.00': 1581119, '-73.97': 2576599, '-73.96': 1549802, '-73.99': 2503233, '-73.98': 3567237, '-74.01': 293161,
                # '-73.78': 159632, '-73.95': 1322448, '-73.86': 124359, '-73.94': 360437, '-73.90': 14566, '-73.87': 147130, '-73.79': 29227,
                # '-73.92': 53989, '-73.93': 76041, '-73.91': 35051, '-73.77': 43243, '-73.81': 2331, '-73.88': 21175, '-73.89': 9998,
                # '-73.80': 6042, '-74.10': 189, '-73.85': 3696, '-73.84': 4964, '-74.15': 520, '-74.16': 646, '-73.74': 138, '-74': 1524,
                # '-73.83': 2809, '-73.82': 1783, '-74.04': 1374, '-74.03': 3190, '-74.02': 2449, '-73.73': 228, '-74.09': 216, '-74.07': 446,
                # '-74.05': 566, '-74.08': 235, '-74.06': 591, '-73.70': 168, '-73.72': 248, '-74.12': 138, '-74.14': 146, '-74.23': 53,
                # '-73.75': 132, '-73.76': 226, '-74.18': 356, '-73.71': 114, '-74.17': 724, '-74.11': 183, '-74.20': 78, '-74.25': 42,
                # '-74.22': 96, '-74.19': 103, '-74.13': 118, '-74.21': 145, '-74.24': 37, '-73.69': 15}
                
            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215):
                        if float(line[10]) < float(max_pickup_longitude_bounding):
                            max_pickup_longitude_bounding = line[10]
                        if float(line[10]) > float(min_pickup_longitude_bounding):
                            min_pickup_longitude_bounding = line[10]

                        line_text = line[10]
                        line_text = line_text [0:6]
                        
                        if line_text in mhist_inside_Boundingbox.keys():

                               mhist_inside_Boundingbox[line_text] += 1
                        else:
                               mhist_inside_Boundingbox[line_text] = 1


                # Here, we are working to count the number points of pickup longitude out of bounding box of NYC for 50000 pickup longitude
                # and in the range between -73.699215 and -72.699215. I got only two points {'-73.61': 1, '-73.43': 1}. Thie number of points
                # in this band are very small if it is compared to the points number of pickup longitude inside the bounding box.

                # The number points of pickup longitude out of bounding box of NYC for 500000 pickup longitude
                # The number of points in this band is really small if it is compared to the points number of pickup longitude inside
                # the bounding box.
                
                #{'-73.61': 4, '-73.43': 1, '-73.00': 1, '-73.66': 3, '-73.62': 2, '-73.56': 1, '-73.60': 2, '-73.54': 2, '-73.59': 3,
                #'-73.16': 1, '-73.69': 1, '-72.69': 1, '-73.63': 1, '-72.72': 1, '-73.05': 1, '-73.03': 1, '-73.68': 2, '-73.30': 1,
                #'-73.51': 1, '-73.67': 1, '-73.53': 2, '-73.64': 1, '-73.09': 1}.

                # The number points of pickup longitude out of bounding box of NYC for 14776614 pickup longitude
                # The number of points in this band is really small if it is compared to the points number of pickup longitude inside
                # the bounding box.

                # {'-73.61': 59, '-73.43': 11, '-73.00': 1, '-73.66': 135, '-73.62': 52, '-73.56': 19, '-73.60': 24, '-73.54': 22, '-73.59': 30,
                # '-73.16': 5, '-73.69': 87, '-72.69': 1, '-73.63': 46, '-72.72': 1, '-73.05': 4, '-73.03': 5, '-73.68': 98, '-73.30': 12,
                # '-73.51': 24, '-73.67': 61, '-73.53': 50, '-73.64': 68, '-73.09': 6, '-73.47': 7, '-73.65': 93, '-73.24': 1, '-73.52': 56,
                # '-73.25': 5, '-73.55': 24, '-73.18': 3, '-72.94': 1, '-73.20': 2, '-73.58': 35, '-73.39': 4, '-73.26': 5, '-73.11': 3,
                # '-73.42': 26, '-73.46': 12, '-73.5': 4, '-72.82': 2, '-73.32': 3, '-73.15': 7, '-73.48': 11, '-73.28': 4, '-73.37': 12,
                # '-73.01': 2, '-73.38': 6, '-73.36': 7, '-73.29': 5, '-73.50': 9, '-73.57': 15, '-73.41': 17, '-72.88': 1, '-73.12': 2,
                # '-73.49': 15, '-73.23': 4, '-72.96': 3, '-73.40': 7, '-73.13': 3, '-73.44': 10, '-73.04': 2, '-73.22': 2, '-73.34': 6,
                # '-73.35': 2, '-73.08': 1, '-73.19': 3, '-72.89': 1, '-73.21': 5, '-73.45': 5, '-72.81': 1, '-72.78': 2, '-73.33': 4,
                # '-72.84': 2, '-73': 1, '-73.06': 2, '-73.31': 7, '-72.77': 1, '-73.10': 2, '-73.27': 7, '-72.83': 2, '-72.97': 1}

            if line[10] != "" and float(line[10]) >= float (-73.699215) and float(line[10])<= float(-72.699215):

                        line_text1 = line[10]
                        line_text1 = line_text1 [0:6]

                        if line_text1 in mhist_outside_Boundingbox.keys():

                               mhist_outside_Boundingbox[line_text1] += 1
                        else:
                               mhist_outside_Boundingbox[line_text1] = 1


                ###

                #Longitude is in the range -180 and +180 and latitude is in in the range -90 and +90.
                
            if line[11] != "" and float(line[11]) <= 90 and float(line[11])>=-90:

                        if float(line[11]) > float(max_pickup_latitude):
                            max_pickup_latitude = line[11]
                        if float(line[11]) < float(min_pickup_latitude):
                            min_pickup_latitude = line[11]

                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LATITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LATITUDE 
                #-----------------------------------------------------------------------------------------------------


                # The "mhist1_inside_Boundingbox" containes on a many pick up latitude points inside the box compared the latitude points outside the
                # bounding box

                #{'40.73': 1561073, '40.75': 2637136, '40.74': 2106817, '40.76': 2448920, '40.78': 854074, '40.77': 1699229, '40.79': 330860,
                # '40.72': 1269417, '40.70': 250964, '40.64': 225531, '40.68': 78206, '40.71': 649978, '40.80': 177464, '40.67': 34643,
                # '40.59': 450, '40.69': 61337, '40.81': 47559, '40.82': 19734, '40.85': 3294, '40.88': 721, '40.66': 12269, '40.65': 8336,
                # '40.84': 9019, '40.63': 4946, '40.83': 9666, '40.87': 800, '40.62': 1185, '40.61': 951, '40.58': 780, '40.86': 1639,
                # '40.89': 342, '40.60': 501, '40.90': 196, '40.57': 173, '40.50': 33, '40.51': 24, '40.52': 24, '40.56': 80, '40.5': 7,
                # '40.53': 31, '40.54': 46, '40.91': 88, '40.55': 43, '40.49': 15}
                
                
            if line[11] != "" and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568):

                        if float(line[11]) < float(max_pickup_latitude_bounding):
                            max_pickup_latitude_bounding = line[11]
                        if float(line[11]) > float(min_pickup_latitude_bounding):
                            min_pickup_latitude_bounding = line[11]

                        line_text2 = line[11]
                        line_text2 = line_text2 [0:5]
                        
                        if line_text2 in mhist1_inside_Boundingbox.keys():

                               mhist1_inside_Boundingbox[line_text2] += 1
                        else:
                               mhist1_inside_Boundingbox[line_text2] = 1
                               
                
                # The number points of pickup latitude out of bounding box of NYC for 50000 pickup latitude only two points
                # {'41.34': 2, '41.02': 1}

                # {'40.73': 5376, '40.75': 7647, '40.74': 6742, '40.76': 7541, '40.78': 3612, '40.77': 6252, '40.79': 1685, '40.72': 4307, '40.70': 889, '40.64': 763, '40.68': 288, '40.71': 2271, '40.80': 774, '40.67': 125, '40.59': 2, '40.69': 238, '40.81': 199, '40.82': 109, '40.85': 24, '40.88': 2, '40.66': 65, '40.65': 33, '40.84': 28, '40.63': 34, '40.83': 44, '40.87': 3, '40.62': 2, '40.61': 1, '40.58': 2, '40.86': 9}

                # The number points of pickup latitude out of bounding box of NYC for 500000 pickup latitude are
                #{'41.34': 2, '41.02': 4, '41.06': 4, '41.25': 4, '41.07': 2, '41.45': 17, '41.28': 1, '41.01': 3, '41.10': 1, '41.20': 1,
                # '41.04': 4, '40.97': 6, '40.96': 2, '41.08': 2, '41.16': 2, '40.98': 3, '40.94': 2, '41.05': 2, '41.65': 1, '40.93': 2,
                #'41.03': 1, '40.92': 2, '41.22': 1, '41.18': 1, '41.09': 1, '40.95': 1, '41.11': 1, '41.21': 1, '41.17': 1, '40.99': 1,
                # '40.91': 1}
                

                # The number points of pickup latitude out of bounding box of NYC for 14776614 pickup latitude are below.
                
                # {'41.34': 6, '41.02': 58, '41.06': 66, '41.25': 6, '41.07': 20, '41.45': 278, '41.28': 3, '41.01': 40, '41.10': 18,
                # '41.20': 9, '41.04': 48, '40.97': 46, '40.96': 52, '41.08': 11, '41.16': 10, '40.98': 55, '40.94': 81, '41.05': 41,
                # '41.65': 3, '40.93': 126, '41.03': 51, '40.92': 122, '41.22': 4, '41.18': 8, '41.09': 12, '40.95': 53, '41.11': 17,
                # '41.21': 13, '41.17': 5, '40.99': 32, '40.91': 69, '41.12': 10, '41.24': 3, '41.15': 12, '41.23': 12, '41.44': 3,
                # '41.71': 1, '41.54': 3, '41.00': 32, '41.58': 6, '41.46': 4, '41.50': 2, '41.29': 4, '41.27': 1, '41.73': 1, '41.14': 8,
                # '41.37': 2, '41.53': 2, '41.40': 4, '41.79': 3, '41': 1, '41.56': 3, '41.31': 8, '41.13': 7, '41.66': 1, '41.72': 1,
                # '41.67': 1, '41.69': 2, '41.5': 2, '41.39': 1, '41.51': 3, '41.26': 7, '41.38': 3, '41.30': 1, '41.32': 3, '41.19': 2,
                # '41.62': 1, '41.74': 2, '41.83': 1, '41.70': 2, '41.49': 1, '41.41': 3, '41.61': 1, '41.36': 4, '41.59': 1, '41.78': 1,
                # '41.60': 1, '41.42': 1, '41.48': 1, '41.55': 1, '41.43': 2, '41.90': 5, '41.81': 2, '41.77': 1}

            if line[11] != "" and float(line[11]) >= float (40.915568) and float(line[11])<= float(41.915568):

                        line_text3 = line[11]
                        line_text3 = line_text3 [0:5]

                        if line_text3 in mhist1_outside_Boundingbox.keys():

                               mhist1_outside_Boundingbox[line_text3] += 1
                        else:
                               mhist1_outside_Boundingbox[line_text3] = 1
                

                ####

                #Longitude is in the range -180 and +180 and latitude is in in the range -90 and +90.

            if line[12] != "" and float(line[12]) <= 180 and float(line[12])>=-180:

                        if float(line[12]) < float(max_dropoff_longitude):
                            max_dropoff_longitude = line[12]
                        if float(line[12]) > float(min_dropoff_longitude):
                            min_dropoff_longitude = line[12]

                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF Dropoff LONGITUDE 
                #-----------------------------------------------------------------------------------------------------

                # The "mhist2_inside_Boundingbox" containes on a many dropp off longitude points inside the box compared the longitude points outside the
                # bounding box

                # {'-74.00': 1483241, '-73.98': 3308286, '-73.86': 93859, '-73.95': 1422048, '-73.96': 1503432, '-73.97': 2719811,
                # '-73.99': 2256090, '-73.91': 93736, '-73.93': 173941, '-74.01': 328435, '-73.92': 116127, '-73.94': 527308, '-73.87': 100615,
                # '-73.78': 66614, '-73.84': 13889, '-74.02': 10563, '-73.83': 12086, '-73.85': 18932, '-73.90': 51332, '-73.82': 11259,
                # '-73.89': 30416, '-73.71': 1162, '-73.88': 33875, '-73.70': 889, '-74.17': 12061, '-73.79': 24708, '-73.73': 2337,
                # '-73.81': 8645, '-74.03': 12156, '-74.18': 4869, '-74.09': 542, '-74.15': 878, '-73.77': 17149, '-73.80': 12054,
                # '-74.16': 1094, '-73.75': 2251, '-74.11': 418, '-73.74': 2088, '-74.14': 351, '-74.04': 3139, '-74': 1477, '-74.13': 328,
                # '-73.72': 1725, '-74.12': 375, '-73.76': 2228, '-74.07': 975, '-74.21': 209, '-74.05': 854, '-74.08': 618, '-74.06': 1172,
                # '-73.69': 58, '-74.10': 579, '-74.19': 296, '-74.23': 80, '-74.20': 170, '-74.25': 60, '-74.22': 135, '-74.24': 64}
                
                
            if line[12] != "" and float(line[12]) >= float (-74.257159) and float(line[12])<= float(-73.699215): 

                        if float(line[12]) < float(max_dropoff_longitude_bounding):
                            max_dropoff_longitude_bounding = line[12]
                        if float(line[12]) > float(min_dropoff_longitude_bounding):
                            min_dropoff_longitude_bounding = line[12]

                        line_text4 = line[12]
                        line_text4 = line_text4 [0:6]
                        
                        if line_text4 in mhist2_inside_Boundingbox.keys():

                               mhist2_inside_Boundingbox[line_text4] += 1
                        else:
                               mhist2_inside_Boundingbox[line_text4] = 1

                # The number points of dropp off longitude out of bounding box of NYC for 50000 dropoff longitude only two points
                # {'-73.60': 1, '-73.44': 1}

                # The number points of dropp off longitude out of bounding box of NYC for 500000 dropp off longitude are
                # {'-73.60': 1, '-73.44': 1, '-73.43': 1, '-73.69': 1, '-73.62': 1, '-73.66': 1, '-73.63': 1, '-73.64': 1, '-73.55': 1}

                # The number points of dropoff longitude out of bounding box of NYC for 500000 dropoff longitude
                # The number of points in this band is really small if it is compared to the points number of dropoff longitude inside
                # the bounding box.

                #{'-73.60': 8, '-73.44': 3, '-73.43': 2, '-73.69': 9, '-73.62': 5, '-73.66': 7, '-73.63': 12, '-73.64': 5, '-73.55': 5,
                # '-73': 1, '-73.00': 2, '-73.68': 14, '-73.67': 18, '-73.42': 3, '-73.51': 4, '-73.65': 6, '-73.58': 6, '-73.17': 1,
                # '-73.56': 3, '-73.59': 6, '-73.47': 2, '-73.61': 3, '-73.30': 1, '-73.53': 6, '-73.54': 4, '-73.52': 1, '-73.48': 2,
                # '-73.57': 2, '-73.09': 1, '-73.06': 1, '-73.16': 1, '-73.14': 1, '-73.08': 1, '-73.46': 1, '-73.36': 1, '-73.50': 2,
                # '-73.13': 1, '-73.25': 1, '-73.49': 1}

                # The number points of dropp off longitude out of bounding box of NYC for 14776614 dropp off longitude are below.
                # {'-73.60': 141, '-73.44': 38, '-73.43': 22, '-73.69': 436, '-73.62': 163, '-73.66': 325, '-73.63': 202, '-73.64': 278,
                # '-73.55': 72, '-73': 3, '-73.00': 2, '-73.68': 381, '-73.67': 293, '-73.42': 86, '-73.51': 52, '-73.65': 285, '-73.58': 141,
                # '-73.17': 9, '-73.56': 67, '-73.59': 105, '-73.47': 30, '-73.61': 106, '-73.30': 6, '-73.53': 128, '-73.54': 75, '-73.52': 99,
                # '-73.48': 40, '-73.57': 49, '-73.09': 6, '-73.06': 2, '-73.16': 8, '-73.14': 1, '-73.08': 2, '-73.46': 24, '-73.36': 16, '-73.50': 40,
                # '-73.13': 9, '-73.25': 9, '-73.49': 40, '-73.37': 17, '-73.23': 6, '-73.40': 14, '-72.86': 1, '-73.28': 8, '-73.05': 9, '-73.20': 6,
                # '-73.41': 36, '-73.34': 11, '-73.35': 4, '-73.21': 8, '-73.45': 22, '-73.10': 9, '-73.26': 11, '-73.33': 5, '-73.18': 6, '-73.11': 4,
                # '-73.19': 9, '-73.38': 16, '-73.29': 6, '-72.96': 3, '-73.39': 8, '-72.88': 1, '-73.12': 3, '-73.04': 1, '-73.31': 7, '-72.91': 2,
                # '-72.74': 1, '-73.22': 4, '-73.32': 5, '-73.15': 2, '-73.27': 8, '-73.01': 3, '-72.75': 1, '-73.02': 3, '-72.78': 1, '-73.24': 1,
                # '-73.03': 1, '-72.95': 1, '-72.94': 1, '-72.83': 2, '-72.98': 1}


            if line[12] != "" and float(line[12]) >= float (-73.699215) and float(line[12])<= float(-72.699215):

                        line_text5 = line[12]
                        line_text5 = line_text5[0:6]

                        if line_text5 in mhist2_outside_Boundingbox.keys():

                               mhist2_outside_Boundingbox[line_text5] += 1
                        else:
                               mhist2_outside_Boundingbox[line_text5] = 1


                #####

                #Longitude is in the range -180 and +180 and latitude is in in the range -90 and +90.

            if line[13] != "" and float(line[13]) <= 90 and float(line[13])>=-90:

                        if float(line[13]) > float(max_dropoff_latitude):
                            max_dropoff_latitude = line[13]
                        if float(line[13]) < float(min_dropoff_latitude):
                            min_dropoff_latitude = line[13]

                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LATITUDE) - COMPUTER THE POINTS NUMBER OF Dropoff LATITUDE 
                #-----------------------------------------------------------------------------------------------------
                
                # The "mhist3_inside_Boundingbox" containes on a many dropp off latitude points inside the box compared the latitude points outside the
                # bounding box.

                #{'40.72': 1178901, '40.75': 2640597, '40.74': 1980509, '40.77': 1603294, '40.73': 1406694, '40.80': 232637, '40.76': 2314247,
                # '40.78': 888135, '40.67': 94116, '40.79': 366535, '40.61': 10178, '40.70': 334478, '40.85': 26898, '40.71': 671278,
                # '40.64': 101874, '40.82': 52639, '40.60': 6576, '40.69': 141629, '40.81': 81200, '40.62': 11646, '40.68': 134426,
                # '40.66': 54654, '40.65': 24783, '40.83': 32477, '40.59': 3924, '40.57': 2182, '40.84': 36008, '40.63': 23377,
                #'40.88': 7204, '40.87': 8368, '40.86': 15836, '40.90': 2305, '40.58': 3525, '40.89': 3578, '40.51': 62, '40.54': 164,
                #'40.91': 503, '40.55': 186, '40.56': 232, '40.53': 102, '40.52': 66, '40.49': 16, '40.50': 46, '40.5': 2}
                
                
            if line[13] != "" and float(line[13]) >= float (40.495992) and float(line[13])<= float(40.915568):

                        if float(line[13]) < float(max_dropoff_latitude_bounding):
                            max_dropoff_latitude_bounding = line[13]
                        if float(line[13]) > float(min_dropoff_latitude_bounding):
                            min_dropoff_latitude_bounding = line[13]

                        line_text6 = line[13]
                        line_text6 = line_text6 [0:5]
                        
                        if line_text6 in mhist3_inside_Boundingbox.keys():

                               mhist3_inside_Boundingbox[line_text6] += 1
                        else:
                               mhist3_inside_Boundingbox[line_text6] = 1



               #There is no points for 50000 dropoff longitude only two points

               #The number points of dropp off latitude outside the bounding box of NYC for 50000 dropp off latitude are
               #{'40.92': 1, '41.02': 1, '41.03': 2}

               # The number points of dropoff latitude out of bounding box of NYC for 500000 dropoff latitude
               # The number of points in this band is really small if it is compared to the points number of dropoff latitude inside
               # the bounding box.

               # {'40.92': 14, '41.02': 6, '41.03': 2, '41.06': 12, '41.25': 5, '40.97': 6, '41.07': 5, '41.01': 11, '41.45': 17, '41.15': 2,
               # '40.98': 7, '41.04': 12, '41.54': 1, '40.95': 8, '40.96': 9, '41.41': 1, '41.10': 2, '40.94': 6, '40.93': 11, '41.05': 7,
               # '41.12': 1, '41.18': 2, '40.91': 6, '41.08': 1, '41.23': 1, '41.53': 1, '41.46': 2, '41.49': 1, '41.61': 1, '41.5': 1,
               # '41.14': 1, '41.00': 2, '41.48': 1, '41.29': 1, '41.31': 1, '41.21': 1, '41.09': 1, '41.20': 1, '40.99': 2, '41.11': 1,
               # '41.17': 1, '41.24': 1, '41.13': 1}

               # The number points of dropp off latitude out of bounding box of NYC for 14776614 dropp off latitude are below.
               # {'40.92': 365, '41.02': 123, '41.03': 167, '41.06': 170, '41.25': 10, '40.97': 149, '41.07': 63, '41.01': 119, '41.45': 283,
               # '41.15': 25, '40.98': 132, '41.04': 110, '41.54': 4, '40.95': 163, '40.96': 167, '41.41': 1, '41.10': 37, '40.94': 293,
               # '40.93': 423, '41.05': 116, '41.12': 31, '41.18': 16, '40.91': 215, '41.08': 27, '41.23': 10, '41.53': 3, '41.46': 10,
               #'41.49': 1, '41.61': 4, '41.5': 4, '41.14': 18, '41.00': 76, '41.48': 4, '41.29': 9, '41.31': 14, '41.21': 6, '41.09': 35,
               #'41.20': 18, '40.99': 92, '41.11': 26, '41.17': 8, '41.24': 7, '41.13': 12, '41.33': 7, '41.44': 3, '41.19': 11, '41.56': 5,
               #'41.79': 2, '41.40': 6, '41.22': 8, '41.59': 3, '41.51': 5, '41': 3, '41.63': 4, '41.38': 5, '41.26': 7, '41.50': 2,
               #'41.58': 5, '41.37': 3, '41.30': 2, '41.27': 1, '41.16': 12, '41.64': 1, '41.34': 5, '41.32': 6, '41.39': 1, '41.81': 2,
               #'41.72': 2, '41.73': 1, '41.28': 3, '41.47': 2, '41.77': 3, '41.69': 1, '41.43': 1, '41.36': 1, '41.70': 2, '41.74': 2,
               #'41.65': 3, '41.84': 2, '41.71': 1, '41.86': 1, '41.42': 1, '41.57': 1, '41.75': 1, '41.90': 5}
               
               
            if line[13] != "" and float(line[13]) >= float (40.915568) and float(line[13])<= float(41.915568):

                        line_text7 = line[13]
                        line_text7 = line_text7 [0:5]

                        if line_text7 in mhist3_outside_Boundingbox.keys():

                               mhist3_outside_Boundingbox[line_text7] += 1
                        else:
                               mhist3_outside_Boundingbox[line_text7] = 1
                        
                ####
            if line[3] > max_rate_code:
                        max_rate_code = line[3]
            if line[3] < min_rate_code:
                        min_rate_code = line[3]

                # min and max of the rate code inside the boudning box:

            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215)and int (line[3]) > int (max_rate_code_insidebox):

                        max_rate_code_insidebox = line[3]

            if line[11] != "" and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568) and int (line[3]) > int (max_rate_code_insidebox):

                        max_rate_code_insidebox_Pickuplatitude = line[3]

                ##### 

            if int(line[8]) > int(max_trip_time_in_secs):
                        max_trip_time_in_secs  = line[8]
            if int(line[8]) < int(min_trip_time_in_secs):
                        min_trip_time_in_secs  = line[8]

                # min and max of the rate code inside the boudning box:

            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215) and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568) and int(line[8]) > int(max_trip_time_in_secs_insidebox):

                        max_trip_time_in_secs_insidebox =  line[8]

            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215) and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568) and int(line[8]) < int(min_trip_time_in_secs_insidebox):

                        min_trip_time_in_secs_insidebox =  line[8]


                ######
                                       
            if line[9] > max_trip_distance:
                        max_trip_distance = line[9]

            if line[9] < min_trip_distance :
                        min_trip_distance = line[9]


                ######


            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215) and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568) and float (line[9]) > float (max_trip_distance_insidebox):

                        max_trip_distance_insidebox = line[9]

            if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215) and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568) and float (line[9]) < float (min_trip_distance_insidebox):

                        min_trip_distance_insidebox = line[9]

                                             
        t+=1

                              
                #####


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


        #########

        # The average number of passengers per day (pickup_datetime) 

        Avg_Passengers_Day = pickup_datetime[8:10]
        Avg_Passengers_Day1 = dropoff_datetime[8:10]
      
        if Avg_Passengers_Day in d4.keys():

                d4[Avg_Passengers_Day] += 1
                
        else:
                d4[Avg_Passengers_Day] = 1

        if Avg_Passengers_Day in mhist16.keys():

                mhist16[Avg_Passengers_Day] += int(line[7])
        else:
                mhist16[Avg_Passengers_Day] = int(line[7])

        # Get one out of every thousand rows (packup_datetime)

        if n % 1000 == 0:

                if Avg_Passengers_Day in d5.keys():
                        d5[Avg_Passengers_Day] += 1
                else:
                        d5[Avg_Passengers_Day] = 1

                if Avg_Passengers_Day in mhist17.keys():

                        mhist17[Avg_Passengers_Day] += int(line[7])
                else:
                        mhist17[Avg_Passengers_Day] = int(line[7])

        # The average number of passengers per day (dropoff_datetime)

        if Avg_Passengers_Day1 in d6.keys():

                d6[Avg_Passengers_Day1] += 1
                
        else:
                d6[Avg_Passengers_Day1] = 1


        if Avg_Passengers_Day1 in mhist18.keys():

                mhist18[Avg_Passengers_Day1] += int(line[7])
        else:
                mhist18[Avg_Passengers_Day1] = int(line[7])

       # Get one out of every thousand rows (dropoff_datetime)

        if n % 1000 == 0:

                if Avg_Passengers_Day1 in d7.keys():
                        d7[Avg_Passengers_Day1] += 1
                else:
                        d7[Avg_Passengers_Day1] = 1

                if Avg_Passengers_Day1 in mhist19.keys():

                        mhist19[Avg_Passengers_Day1] += int(line[7])
                else:
                        mhist19[Avg_Passengers_Day1] = int(line[7])
                
        #if n > 5000:        

           # break

        

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

for k in mhist16.keys():
        chist4[k] = int(mhist16.get(k)) / d4[k]

for k in mhist17.keys():
        chist5[k] = int(mhist17.get(k)) / d5[k]

for k in mhist18.keys():
        chist6[k] = int(mhist18.get(k)) / d6[k]

for k in mhist19.keys():
        chist7[k] = int(mhist19.get(k)) / d7[k]

        

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

for key, val in chist4.items():
    line1 = [str(c),key, str(val)]
    c +=1
    writer4.writerow(line1)

for key, val in chist5.items():
    line1 = [str(c),key, str(val)]
    c +=1
    writer5.writerow(line1)

for key, val in chist6.items():
    line1 = [str(c),key, str(val)]
    c +=1
    writer6.writerow(line1)

for key, val in chist7.items():
    line1 = [str(c),key, str(val)]
    c +=1
    writer7.writerow(line1)

f2.close()
f3.close()
f4.close()
f5.close()

f6.close()
f7.close()
f8.close()
f9.close()

print ('Number of rows= ' + str(i))

with open('trip_data_1.csv', 'r') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames


print (headers)
print ('Time in seconds =' + str ((time.time()-start)))


print ("Smallest_date_pickup_datetime = ", Smallest_date_pickup_datetime)
print ("Largest_date_pickup_datetime = ", Largest_date_pickup_datetime)

print ("Smallest_date_dropoff_datetime = ", Smallest_date_dropoff_datetime)
print ("Largest_date_dropoff_datetime = ", Largest_date_dropoff_datetime)



        
print (d)#hour count
print (mhist12)#sum of passengers in each hour
print (chist)#passengers per hour (average)

print (d1)
print (mhist13)
print (chist1)

print (d2)
print (mhist14)
print (chist2)

print (d3)
print (mhist15)
print (chist3)

print (d4)
print (mhist16)
print (chist4)

print (d5)
print (mhist17)
print (chist5)

print (d6)
print (mhist18)
print (chist6)

print (d7)
print (mhist19)
print (chist7)

print (mhist)
print (mhist1)
print (mhist2)



print (mhist3)
print ("mhist3")
print ("mhist3")
print ("mhist3")
print ("mhist3")
print ("mhist3")



print (mhist4)
print (mhist5)
print (mhist6)
print (mhist7)

print (max_passenger_count)
print (min_passenger_count)

print (max_pickup_longitude)
print (min_pickup_longitude)

print (max_pickup_latitude)
print (min_pickup_latitude)

print (max_dropoff_longitude)
print (min_dropoff_longitude)

print (max_dropoff_latitude)
print (min_dropoff_latitude)

print (max_rate_code )
print (min_rate_code)

print (max_trip_time_in_secs)
print (min_trip_time_in_secs)

print (max_trip_distance)
print (min_trip_distance)


###

print (max_passenger_count_bounding)
print (min_passenger_count_bounding)
print (max_pickup_longitude_bounding)
print (min_pickup_longitude_bounding)
print (max_pickup_latitude_bounding)
print (min_pickup_latitude_bounding)
print(mhist_inside_Boundingbox)
print(mhist_outside_Boundingbox)
print(mhist1_inside_Boundingbox)
print(mhist1_outside_Boundingbox)
print (mhist2_inside_Boundingbox)
print (mhist2_outside_Boundingbox)
print (mhist3_inside_Boundingbox)
print (mhist3_outside_Boundingbox)
print (max_rate_code_insidebox)
print (min_rate_code_insidebox)
print (max_trip_time_in_secs_insidebox)
print (min_trip_time_in_secs_insidebox)
print (max_trip_distance_insidebox)
print (min_trip_distance_insidebox)
print (max_passenger_count_insidebox)
print (min_passenger_count_insidebox)


######

print (max_pickup_longitude_big_bounday)
print (min_pickup_longitude_big_bounday)
print (max_pickup_latitude_big_bounday)
print (min_pickup_latitude_big_bounday)
print (max_dropoff_small_longitude_bounding)
print (min_dropoff_small_longitude_bounding)
print (max_dropoff_longitude_big_bounday)
print (min_dropoff_longitude_big_bounday)
print (max_dropoff_latitude_big_bounday)
print (min_dropoff_latitude_big_bounday)
print (max_rate_code_insidebox_Pickuplatitude)




