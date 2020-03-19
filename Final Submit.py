
#Documentation:
#https://github.com/Mohamed-Elwakdy/Elwakdy-TripData

#################
import csv
import time
import datetime
import math
import operator

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
mhist8 = {}
mhist9 = {}

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

####

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

max_passenger = 0
min_passenger = 0
 
min_pickup_longitude = 0
max_pickup_longitude = 0

min_pickup_latitude = 0
max_pickup_latitude = 0

min_dropoff_longitude = 0
max_dropoff_longitude = 0

min_pickup_latitude1 = 0
max_pickup_latitude1 = 0

min_dropoff_latitude1 = 0
max_dropoff_latitude1 = 0

min_rate_code  = 0
max_rate_code  = 0

min_trip_time_in_secs  = 0
max_trip_time_in_secs  = 0

min_trip_time_in_secs_put_in_range = 0
min_trip_distance_put_in_range = 0

min_trip_distance  = 0
max_trip_distance  = 0


###

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

        # The smallest and lasrgest date of pickup_datetimemax_dropoff_latitude_bounding
        # ------------------------------------------------------------------------------

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

        # Some sample data for each field in the dataset
        # ----------------------------------------------

        if n % 1000000 == 0:
                print (line)
        

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

        ###

        vendor_id = line [2]

        if vendor_id in mhist8.keys():
             mhist8[vendor_id] += 1
        else:
             mhist8[vendor_id] = 1

        if 'vendor_id' in mhist8:
             del mhist8['vendor_id']

        ###

        store_and_fwd_flag = line [4]

        if store_and_fwd_flag in mhist9.keys():
             mhist9[store_and_fwd_flag] += 1
        else:
             mhist9[store_and_fwd_flag] = 1

        if 'store_and_fwd_flag' in mhist9:
             del mhist9['store_and_fwd_flag']

        ### 
             
                
        # The min and max values
        # ----------------------
     
        if t>0:
                
            if t == 1:
                min_passenger_count = line[7]
                max_passenger_count = line[7]

                max_passenger = line [7]
                min_passenger = line [7]

                #Longitude is in the range -180 and +180. The North pole has a latitude of 90° north (written 90° N or +90°),
                #and the South pole has a latitude of -90°.

                min_pickup_longitude = line[10]
                min_pickup_longitude = min_pickup_longitude                                                                                                                                   
                max_pickup_longitude = line[10]
                max_pickup_longitude = max_pickup_longitude

                ###
                '''
                min_pickup_latitude = line[11]
                min_pickup_latitude = min_pickup_latitude 
                max_pickup_latitude = line[11]
                max_pickup_latitude = max_pickup_latitude

                '''

                min_pickup_latitude1 = line [11]
                min_pickup_latitude1 = min_pickup_latitude1
                max_pickup_latitude1 = line [11]
                max_pickup_latitude1 = max_pickup_latitude1 
                
                ###
                min_dropoff_longitude = line[12]
                min_dropoff_longitude = min_dropoff_longitude 
                max_dropoff_longitude = line[12]
                max_dropoff_longitude = max_dropoff_longitude

                ###

                min_dropoff_latitude1 = line[13]
                min_dropoff_latitude1 = min_dropoff_latitude1
                max_dropoff_latitude1 = line[13]
                max_dropoff_latitude1 = max_dropoff_latitude1 


                # Longitude and Latitude for big bounding box.

                max_pickup_longitude_big_bounday = line[10]
                max_pickup_longitude_big_bounday= max_pickup_longitude_big_bounday
                min_pickup_longitude_big_bounday = line[10]
                min_pickup_longitude_big_bounday= min_pickup_longitude_big_bounday

                max_pickup_latitude_big_bounday = line [11]
                max_pickup_latitude_big_bounday = max_pickup_latitude_big_bounday
                min_pickup_latitude_big_bounday = line [11]
                min_pickup_latitude_big_bounday = min_pickup_latitude_big_bounday


                max_dropoff_longitude_big_bounday = line[12]
                max_dropoff_longitude_big_bounday = max_dropoff_longitude_big_bounday
                min_dropoff_longitude_big_bounday = line[12]
                min_dropoff_longitude_big_bounday = min_dropoff_longitude_big_bounday
                

                max_dropoff_latitude_big_bounday = line[13]
                max_dropoff_latitude_big_bounday = max_dropoff_latitude_big_bounday
                min_dropoff_latitude_big_bounday = line[13]
                min_dropoff_latitude_big_bounday = min_dropoff_latitude_big_bounday

        
                # Longitude and Latitude (inside the bounding box) 

                min_pickup_longitude_bounding = line[10]
                min_pickup_longitude_bounding = min_pickup_longitude_bounding                                                                                                                                   
                max_pickup_longitude_bounding = line[10]
                max_pickup_longitude_bounding = max_pickup_longitude_bounding

                min_pickup_latitude_bounding = line[11]
                min_pickup_latitude_bounding = min_pickup_latitude_bounding                                                                                                                               
                max_pickup_latitude_bounding = line[11]
                max_pickup_latitude_bounding = min_pickup_latitude_bounding

                max_dropoff_longitude_bounding = line [12]
                max_dropoff_longitude_bounding = max_dropoff_longitude_bounding
                min_dropoff_longitude_bounding = line[12]
                min_dropoff_longitude_bounding = min_dropoff_longitude_bounding

                max_dropoff_latitude_bounding = line [13]
                max_dropoff_latitude_bounding = max_dropoff_latitude_bounding
                min_dropoff_latitude_bounding = line [13]
                min_dropoff_latitude_bounding = min_dropoff_latitude_bounding


                ###

                min_rate_code = line[3]
                max_rate_code = line[3]

                min_trip_time_in_secs = line[8]
                max_trip_time_in_secs = line[8]

                min_trip_time_in_secs_put_in_range = line[8]
                #min_trip_time_in_secs_put_in_range= min_trip_time_in_secs_put_in_range

                min_trip_distance   = line[9]
                max_trip_distance   = line[9]

                min_trip_distance_put_in_range= line[9]
                #min_trip_distance_put_in_range = min_trip_distance_put_in_range
                
            else:

                #The number of passenger should be not greather than 5 and the minimum passanger is "Zero" and this is
                #unlogic because the minimum number of passengers should be not less than 1 and not greather than 5.
                #The maximum number of the passengers in that dataset is 255 and this is unlogic, as the mimimum number of
                # passengers is 0 and this is unlogic too. 

                # In this code, I put the maximum number of passengers is 5 and the minimum number of passengers is 1.   

                if int (line[7]) > int (max_passenger):
                        max_passenger = line [7]

                if int (line[7]) < int (min_passenger):
                        min_passenger = line [7]
                        

                # The maximum number of passengers in a vehicle is 5 and minimum number is 1.
                
                if line[7] > max_passenger_count and int (line[7]) < 6 :
                    max_passenger_count = line[7]
                if line[7] < min_passenger_count and int (line [7]) > 0 and int (line [7]) < 6:
                    min_passenger_count = line[7]               


                ######

                # Getting the maximum and minimum longitude and latitude.
                # The minimum and maximum latitude is invalid:
                # max_pickup_latitude1: 3310.3645
                # min_pickup_latitude1: -3547.9207
                # The maximum pickup longitude is invalid as well:
                # maximum pickup longitude: -2771.2854
                # The maximum and minimum longitude
                # max_dropoff_longitude =  -2350.9556
                # min_dropoff_longitude =  2228.7375
                
                if float(line[10]) > float(max_pickup_longitude):
                            max_pickup_longitude = line[10]
                if float(line[10]) < float(min_pickup_longitude):
                            min_pickup_longitude = line[10]
                            
        
                if float(line[11]) > float(max_pickup_latitude1):
                            max_pickup_latitude1 = line[11]
                if float(line[11]) < float(min_pickup_latitude1):
                            min_pickup_latitude1 = line[11]

                if line[12] != "":
                             if float(line[12]) > float(max_dropoff_longitude):
                                     max_dropoff_longitude = line[12]
                             if float(line[12]) < float(min_dropoff_longitude):
                                     min_dropoff_longitude = line[12]

                if line[13] != "":
                             if float(line[13]) > float(max_dropoff_latitude1):
                                     max_dropoff_latitude1 = line[13]
                             if float(line[13]) < float(min_dropoff_latitude1):
                                     min_dropoff_latitude1 = line[13]
                
                ############################################################

                # Because there are some maximum and minimum latitude/longitude points are invalid, I create a big bounding box
                # where Longitude is in the range -180 and +180 and latitude is in in the range -90 and +90.
                
                # Getting the max and min values inside the bounding box for longitude and latitude points.  

                if line[10] != "" and float(line[10]) <= 180 and float(line[10])>= -180:                  

                     if float(line[10]) > float(max_pickup_longitude_big_bounday):
                            max_pickup_longitude_big_bounday = line[10]
                     if float(line[10]) < float(min_pickup_longitude_big_bounday):
                            min_pickup_longitude_big_bounday = line[10]

                if line[11] != "" and float(line[11]) <= 90 and float(line[11])>=-90:

                     if float(line[11]) > float(max_pickup_latitude_big_bounday):
                            max_pickup_latitude_big_bounday = line[11]
                     if float(line[11]) < float(min_pickup_latitude_big_bounday):
                            min_pickup_latitude_big_bounday = line[11]

                if line[12] != "" and float(line[12]) <= 180 and float(line[12])>= -180:
                        
                             if float(line[12]) > float(max_dropoff_longitude_big_bounday):
                                     max_dropoff_longitude_big_bounday = line[12]
                             if float(line[12]) < float(min_dropoff_longitude_big_bounday):
                                     min_dropoff_longitude_big_bounday = line[12]

                if line[13] != "" and float(line[13]) <= 90 and float(line[13])>=-90:
                
                             if float(line[13]) > float(max_dropoff_latitude_big_bounday):
                                     max_dropoff_latitude_big_bounday = line[13]
                             if float(line[13]) < float(min_dropoff_latitude_big_bounday):
                                     min_dropoff_latitude_big_bounday = line[13]


                #############################################################

                # Although all the latitude and longitude pickup/dropoff points are valid points, these points are out of the
                # New York city. 
                # Because of this, I need to create another bounding box includes the maximum and minimum pickup/dropoff
                # longitude and latitude for New York city.                              
    
                # The the maximum and minimum logitude and latitude for a New York city is:
                # Minimum longitude -74.257159 and maximum longitude -73.699215.
                # Maximum latitude 40.915568 and minimum latuitude 40.495992. 

                                     
                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LONGITUDE 
                #-----------------------------------------------------------------------------------------------------
                
                # compute the number points of pickup longitude inside the bounding box

                # The number of points inside the bounding box for 14776614 pickup longitude is really big number compared to the number of
                # points outside the bounding box. 
                
                if line[10] != "" and float(line[10]) >= float (-74.257159) and float(line[10])<= float(-73.699215):
                    
                        if float(line[10]) > float(max_pickup_longitude_bounding):
                            max_pickup_longitude_bounding = line[10]
                        if float(line[10]) < float(min_pickup_longitude_bounding):
                            min_pickup_longitude_bounding = line[10]

                        line_text = line[10]
                        line_text = line_text [0:6]
                        
                        if line_text in mhist_inside_Boundingbox.keys():

                               mhist_inside_Boundingbox[line_text] += 1
                        else:
                               mhist_inside_Boundingbox[line_text] = 1

                # The number points of pickup longitude out of bounding box of NYC for 14776614 pickup longitude.
                # The number of points in this band is really small if it is compared to the points number of pickup longitude inside
                # the bounding box.

                if line[10] != "" and float(line[10]) >= float (-73.699215) and float(line[10])<= float(-72.699215):

                        line_text1 = line[10]
                        line_text1 = line_text1 [0:6]

                        if line_text1 in mhist_outside_Boundingbox.keys():

                               mhist_outside_Boundingbox[line_text1] += 1
                        else:
                               mhist_outside_Boundingbox[line_text1] = 1


                ###
                               
            
                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LATITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LATITUDE 
                #-----------------------------------------------------------------------------------------------------

                
                # The "mhist1_inside_Boundingbox" containes on a many pick up latitude points inside the box compared the latitude points outside the
                # bounding box                
                
                if line[11] != "" and float(line[11]) >= float (40.495992) and float(line[11])<= float(40.915568):

                        if float(line[11]) > float(max_pickup_latitude_bounding):
                            max_pickup_latitude_bounding = line[11]
                        if float(line[11]) < float(min_pickup_latitude_bounding):
                            min_pickup_latitude_bounding = line[11]

                        line_text2 = line[11]
                        line_text2 = line_text2 [0:5]
                        
                        if line_text2 in mhist1_inside_Boundingbox.keys():

                               mhist1_inside_Boundingbox[line_text2] += 1
                        else:
                               mhist1_inside_Boundingbox[line_text2] = 1
                

                if line[11] != "" and float(line[11]) >= float (40.915568) and float(line[11])<= float(41.915568):

                        line_text3 = line[11]
                        line_text3 = line_text3 [0:5]

                        if line_text3 in mhist1_outside_Boundingbox.keys():

                               mhist1_outside_Boundingbox[line_text3] += 1
                        else:
                               mhist1_outside_Boundingbox[line_text3] = 1
                

                ####


                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF Dropoff LONGITUDE 
                #-----------------------------------------------------------------------------------------------------

                # The "mhist2_inside_Boundingbox" containes on a many dropp off longitude points inside the box compared the longitude points outside the
                # bounding box                
                
                if line[12] != "" and float(line[12]) >= float (-74.257159) and float(line[12])<= float(-73.699215): 

                        if float(line[12]) > float(max_dropoff_longitude_bounding):
                            max_dropoff_longitude_bounding = line[12]
                        if float(line[12]) < float(min_dropoff_longitude_bounding):
                            min_dropoff_longitude_bounding = line[12]

                        line_text4 = line[12]
                        line_text4 = line_text4 [0:6]
                        
                        if line_text4 in mhist2_inside_Boundingbox.keys():

                               mhist2_inside_Boundingbox[line_text4] += 1
                        else:
                               mhist2_inside_Boundingbox[line_text4] = 1


            if line[12] != "" and float(line[12]) >= float (-73.699215) and float(line[12])<= float(-72.699215):

                        line_text5 = line[12]
                        line_text5 = line_text5[0:6]

                        if line_text5 in mhist2_outside_Boundingbox.keys():

                               mhist2_outside_Boundingbox[line_text5] += 1
                        else:
                               mhist2_outside_Boundingbox[line_text5] = 1


                #####

                # INSIDE THE BOUNDING BOX (MAX AND MINIMUM LATITUDE) - COMPUTER THE POINTS NUMBER OF Dropoff LATITUDE 
                #-----------------------------------------------------------------------------------------------------
                
                

                # The "mhist3_inside_Boundingbox" containes on a many dropp off latitude points inside the box compared the latitude points outside the
                # bounding box.
                
                
            if line[13] != "" and float(line[13]) >= float (40.495992) and float(line[13])<= float(40.915568):

                        if float(line[13]) > float(max_dropoff_latitude_bounding):
                            max_dropoff_latitude_bounding = line[13]
                        if float(line[13]) < float(min_dropoff_latitude_bounding):
                            min_dropoff_latitude_bounding = line[13]

                        line_text6 = line[13]
                        line_text6 = line_text6 [0:5]
                        
                        if line_text6 in mhist3_inside_Boundingbox.keys():

                               mhist3_inside_Boundingbox[line_text6] += 1
                        else:
                               mhist3_inside_Boundingbox[line_text6] = 1
               
               
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

                #####
            # The maximum trip time is seconds is 10800 seconds and the minimum is 0. The mimimum trip time in seconds are "Zero" and
            # this is unlogic.  

            if int(line[8]) > int(max_trip_time_in_secs):
                        max_trip_time_in_secs  = line[8]
            if int(line[8]) < int(min_trip_time_in_secs):
                        min_trip_time_in_secs  = line[8]

            # Here, I put the minimum trip time in seconds is 5 minutes which equivalent to 300 seconds

            if int(line[8]) < int(min_trip_time_in_secs_put_in_range) and int(line[8]) >= 300:
                        min_trip_time_in_secs_put_in_range  = line[8]

                ######

           # in trip_distance field, the max trip distance is 99.90 and the minimum trip distance .00 is unlogic number. 
                                       
            if line[9] > max_trip_distance:
                        max_trip_distance = line[9]

            if line[9] < min_trip_distance :
                        min_trip_distance = line[9]

            # Here, I put a limit to the mim trip distance to be not less than 2 mile.

            if line[9] < min_trip_distance_put_in_range and float (line[9]) >= 2 :
                        min_trip_distance_put_in_range = line[9]

                                             
        t+=1

                              
                #####


        # The average number of passengers per hour (pickup_datetime) 

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


        # The average number of passengers by taking one out of every thousand rows (pickup_datetime)

        if n % 1000 == 0:

                if Hour_datetime in d1.keys():
                        d1[Hour_datetime] += 1
                else:
                        d1[Hour_datetime] = 1

                if Hour_datetime in mhist13.keys():

                        mhist13[Hour_datetime] += int(line[7])
                else:
                        mhist13[Hour_datetime] = int(line[7])
                        
        # The average number of passengers per hour (dropoff_datetime) 

        if Hour_datetime1 in d2.keys():
                d2[Hour_datetime1] += 1
        else:
                d2[Hour_datetime1] = 1


        if Hour_datetime1 in mhist14.keys():
                mhist14[Hour_datetime1] += int(line[7])

        else:
                mhist14[Hour_datetime1] = int(line[7])

        # The average number of passengers per hour by taking one out of every thousand rows (dropoff_datetime)
        
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

        # The average number of passengers per day by taking one out of every thousand rows (packup_datetime)

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

       # The average number of passengers per day by taking one out of every thousand rows (dropoff_datetime)

        if n % 1000 == 0:

                if Avg_Passengers_Day1 in d7.keys():
                        d7[Avg_Passengers_Day1] += 1
                else:
                        d7[Avg_Passengers_Day1] = 1

                if Avg_Passengers_Day1 in mhist19.keys():

                        mhist19[Avg_Passengers_Day1] += int(line[7])
                else:
                        mhist19[Avg_Passengers_Day1] = int(line[7])
                
        #if n > 500000:        

            #break

        

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

# The number of rows 

print ('Number of rows= ' + str(i))

# The Field names

with open('trip_data_1.csv', 'r') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames


print (headers)
print ('Time in seconds =' + str ((time.time()-start)))


List_max_values_longitude_pickup = dict (sorted(mhist_inside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_longitude_pickup =", List_max_values_longitude_pickup)
List_max_values_latitude_pickup = dict (sorted(mhist1_inside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_latitude_pickup =", List_max_values_latitude_pickup)
List_max_values_longitude_dropoff = dict (sorted(mhist2_inside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_longitude_dropoff =", List_max_values_longitude_dropoff)
List_max_values_latitude_dropoff = dict (sorted(mhist3_inside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_latitude_dropoff =", List_max_values_latitude_dropoff)


List_max_values_longitude_pickup_band = dict (sorted(mhist_outside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_longitude_pickup_band =", List_max_values_longitude_pickup_band)
List_max_values_latitude_pickup_latitude = dict (sorted(mhist1_outside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_latitude_pickup_latitude =", List_max_values_latitude_pickup_latitude)
List_max_values_longitude_dropoff_band = dict (sorted(mhist2_outside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_longitude_dropoff_band =", List_max_values_longitude_dropoff_band)
List_max_values_latitude_dropoff_band = dict (sorted(mhist3_outside_Boundingbox.items(), key=operator.itemgetter(1), reverse=True)[:5])
print ("List_max_values_latitude_dropoff_band =", List_max_values_latitude_dropoff_band)




print ("Smallest_date_pickup_datetime = ", Smallest_date_pickup_datetime)
print ("Largest_date_pickup_datetime = ", Largest_date_pickup_datetime)
print ("Smallest_date_dropoff_datetime = ", Smallest_date_dropoff_datetime)
print ("Largest_date_dropoff_datetime = ", Largest_date_dropoff_datetime)
        
print ("d =", d)#hour count
print ("mhist12 =", mhist12)#sum of passengers in each hour
print ("chist =", chist)#passengers per hour (average)

print ("d1 =",d1)
print ("mhist13 =", mhist13)
print ("chist1 =",chist1)

print ("d2 = ", d2)
print ("mhist14 =", mhist14)
print ("chist2 =", chist2)


print ("d3 =", d3)
print ("mhist15 =", mhist15)
print ("chist3 =", chist3)

print ("d4 =", d4)
print ("mhist16 =", mhist16)
print ("chist4 =", chist4)

print ("d5 =", d5)
print ("mhist17 =",mhist17)
print ("chist5 =", chist5)

print ("d6 =", d6)
print ("mhist18 =", mhist18)
print ("chist6 =", chist6)

print ("d7 =", d7)
print ("mhist19 =", mhist19)
print ("chist7 =", chist7)

print ("mhist =", mhist)
print ("mhist1 =", mhist1)
print ("mhist2 =", mhist2)
print ("mhist3 =", mhist3)
print ("mhist4 =", mhist4)
print ("mhist5 =", mhist5)
print ("mhist6", mhist6)
print ("mhist7 =", mhist7)
print ("mhist8 = ", mhist8)
print ("mhist9 = ", mhist9)

print ("max_passenger =", max_passenger)
print ("min_passenger =", min_passenger)

print ("max_passenger_count =", max_passenger_count)
print ("min_passenger_count =", min_passenger_count)


print ("max_pickup_longitude =", max_pickup_longitude)
print ("min_pickup_longitude =", min_pickup_longitude)
print ("max_pickup_latitude1 =", max_pickup_latitude1)
print ("min_pickup_latitude1 =", min_pickup_latitude1)

print ("max_dropoff_longitude = ", max_dropoff_longitude)
print ("min_dropoff_longitude = ", min_dropoff_longitude)

print ("max_dropoff_latitude1 =", max_dropoff_latitude1)
print ("min_dropoff_latitude1 =", min_dropoff_latitude1)

print ("min_rate_code= ", min_rate_code)
print ("max_rate_code= ", max_rate_code )

print ("max_trip_time_in_secs= ", max_trip_time_in_secs)
print ("min_trip_time_in_secs= ", min_trip_time_in_secs)
print ("min_trip_time_in_secs_put_in_range = ", min_trip_time_in_secs_put_in_range)

print ("max_trip_distance = ", max_trip_distance)
print ("min_trip_distance = ", min_trip_distance)
print ("min_trip_distance_put_in_range", min_trip_distance_put_in_range)

###

print ("max_pickup_longitude_bounding =",max_pickup_longitude_bounding)
print ("min_pickup_longitude_bounding =", min_pickup_longitude_bounding)
print ("max_pickup_latitude_bounding ", max_pickup_latitude_bounding)
print ("min_pickup_latitude_bounding =", min_pickup_latitude_bounding)
print("mhist_inside_Boundingbox =", mhist_inside_Boundingbox)
print("mhist_outside_Boundingbox =", mhist_outside_Boundingbox)
print("mhist1_inside_Boundingbox =", mhist1_inside_Boundingbox)
print("mhist1_outside_Boundingbox =", mhist1_outside_Boundingbox)
print ("mhist2_inside_Boundingbox =", mhist2_inside_Boundingbox)
print ("mhist2_outside_Boundingbox =", mhist2_outside_Boundingbox)
print ("mhist3_inside_Boundingbox =", mhist3_inside_Boundingbox)
print ("mhist3_outside_Boundingbox =", mhist3_outside_Boundingbox)



###

print ("max_pickup_longitude_big_bounday =", max_pickup_longitude_big_bounday)
print ("min_pickup_longitude_big_bounday =", min_pickup_longitude_big_bounday)
print ("max_pickup_latitude_big_bounday = ", max_pickup_latitude_big_bounday)
print ("min_pickup_latitude_big_bounday = ", min_pickup_latitude_big_bounday)

print ("max_dropoff_longitude_bounding =", max_dropoff_longitude_bounding)
print ("min_dropoff_longitude_bounding = ", min_dropoff_longitude_bounding)
print ("max_dropoff_latitude_bounding =", max_dropoff_latitude_bounding)
print ("min_dropoff_latitude_bounding =", min_dropoff_latitude_bounding)

print ("max_dropoff_longitude_big_bounday =", max_dropoff_longitude_big_bounday)
print ("min_dropoff_longitude_big_bounday =", min_dropoff_longitude_big_bounday)
print ("max_dropoff_latitude_big_bounday =", max_dropoff_latitude_big_bounday)
print ("min_dropoff_latitude_big_bounday =", min_dropoff_latitude_big_bounday)




