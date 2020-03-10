

# Elwakdy-TripData
 

# Time range of datetime 

<br>

# Smallest_date_pickup_datetime =  2013-01-01 00:00:00

# Largest_date_pickup_datetime =  2013-01-31 23:59:59

# Smallest_date_dropoff_datetime =  2013-01-01 00:00:36

# Largest_date_dropoff_datetime =  2013-02-01 10:33:08

<br>

```

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

```

<br>

# Number of rows= 14776615

```

for line in reader:
        
        i+=1

print ('Number of rows= ' + str(i))

```

<br>

# The distinct values for each field


# In this code, the distinct values of some fields suchas pickup_datetime, dropoff_datetime, medallion, hack_license, rate_code, passenger_count, trip_time_in_secs and trip_distance are getting on. I used a dictionary for each field to get the distinct values. Please run the python code to get the distinct values.

# For an example of distint values of some fields explained below: 

<br>

{'1': 14456067, '2': 239160, '4': 22831, '5': 39889, '3': 17655, '6': 315, '8': 10, '0': 667, '210': 11, '28': 2, '7': 2, '9': 1, '65': 1, '128': 4}

{'4': 280992, '1': 10471701, '2': 1986196, '3': 597485, '5': 920006, '6': 520066, '0': 166, '208': 1, '9': 1, '255': 1}

|   Rate Code   | MAX:14456067 , MIN: 1 |
| ------------- | --------------------- |
| passenger_count | MAX:  10471701|
| ------------- | --------------------- |




```
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



```




