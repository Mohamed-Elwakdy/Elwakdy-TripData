

# Elwakdy-TripData
 

<br>

# Question 1:

<br>

### Time range of datetime 

### Smallest_date_pickup_datetime =  2013-01-01 00:00:00

### Largest_date_pickup_datetime =  2013-01-31 23:59:59

### Smallest_date_dropoff_datetime =  2013-01-01 00:00:36

### Largest_date_dropoff_datetime =  2013-02-01 10:33:08

<br>

### Here, I will chech all the datatime out before I start work on datatime in "Packup Datetime" and "Dropoff Datetime". 
### This means that I match format below of %Y_%m_%d %H:%M:%S and see if there is any invalid datetime. 

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

        # The smallest and largest date of pickup_datetime

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

### Number of rows= 14776615

```

for line in reader:
        
        i+=1

print ('Number of rows= ' + str(i))

```

<br>

# Question: 2

<br>

### The field names are: 

### medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude.


|    Field Name  | Description |
| ------------- | --------------------- |
|   medallion   |A transferable permit in the United States allowing a taxicab driver to operate|
| hack_license | Hack license is known as a New York City Taxi Operators License. The license allows the holder / driver to operate a Yellow Medallion Taxicab in the Five Boroughs of the City of New York|
|   vendor_id  | The Vendor ID is a ten-digit identifier issued by New York State when the vendor is registered on the Statewide Vendor File|
| rate_code |The final rate code in effect at the end of the trip|
| store_and_fwd_flag  | Store and fwd flag indicates whether the trip record was held in vehicle memory before sending to the vendor |
| pickup_datetime |The date and time to pick up the passenger |
|   dropoff_datetime |The date and time to drop off the passenger |
| passenger_count |The number of passengers in the vehicle|
|  trip_time_in_secs  |The trip time per seconds  |
| trip_distance |The trip distance is the difference between the pickup time and drop off time of the passenger(s)|
|   pickup_longitude  |The longitude of the point where the taximeter was engaged|
|  pickup_latitude |The latitude of the point where the taximeter was engaged|
|   dropoff_longitude |The longitude of the point where the taximeter was disengaged|
| dropoff_latitude |The latitude of the point where the taximeter was disengaged|

```
with open('C:/Users/elwakdmf/Desktop/trip_data_1.csv', 'r') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
```

<br>

# Question 3

<br>

### Some sample data for each field

### Sample 1



|   Field Name | Description |
| ------------- | --------------------- |
| medallion | DFD2202EE08F7A8DC9A57B02ACB81FE2|
|hack_license |51EE87E3205C985EF8431D850C786310|
|vendor_id |CMT|
|rate_code |1|
|store_and_fwd_flag |N|
|pickup_datetime |2013-01-07 23:25:03|
|dropoff_datetime | 2013-01-07 23:34:24|
|passenger_count |1|
|trip_time_in_secs| 560|
|trip_distance |2.10|
|pickup_longitude| -73.97625|
|pickup_latitude  |40.748528|
|dropoff_longitude |-74.002586|
|dropoff_latitude |40.747868|

<br>

### Sample 2

|    Field Name  | Description |
| ------------- | --------------------- |
|medallion | 2D4B95E2FA7B2E85118EC5CA4570FA58|
|hack_license |CD2F522EEE1FF5F5A8D8B679E23576B3|
|vendor_id |CMT|
|rate_code |1|
|store_and_fwd_flag |N|
|pickup_datetime |2013-01-07 15:33:28|
|dropoff_datetime | 2013-01-07 15:49:26|
|passenger_count |2|
|trip_time_in_secs| 957|
|trip_distance |2.50|
|pickup_longitude| -73.977936|
|pickup_latitude  |40.786983|
|dropoff_longitude |-73.952919|
|dropoff_latitude |40.80637|

<br>

### Sample 3

|    Field Name  | Description |
| ------------- | --------------------- |
|medallion | 3349F919AA8AE5DC9C50A3773EA45BD8|
|hack_license|7CE849FEF67514F080AF80D990F7EF7F|
|vendor_id |CMT|
|rate_code|1|
|store_and_fwd_flag |N|
|pickup_datetime |2013-01-10 15:42:29|
|dropoff_datetime |2013-01-10 16:04:02|
|passenger_count |1|
|trip_time_in_secs|1293|
|trip_distance |3.20|
|pickup_longitude|-73.994911|
|pickup_latitude  |40.723221|
|dropoff_longitude |-73.971558|
|dropoff_latitude |40.761612|

<br>

# Question 4

<br>

### MySQL data types that I need to store each of the fields are:



|    Field Name  | Data Type |
| ------------- | --------------------- |
|medallion | varchar(32)|
|hack_license |varchar(32)|
|vendor_id|text|
|rate_code |int(3)|
|store_and_fwd_flag |varchar(1)|
|pickup_datetime |datetime|
|dropoff_datetime |datetime|
|passenger_count |int(3)|
|trip_time_in_secs|int(18)|
|trip_distance|decimal (5.3)|
|pickup_longitude|decimal (9.7)|
|pickup_latitude  |decimal (9.7)|
|dropoff_longitude |decimal (9.7)|
|dropoff_latitude |decimal (9.7)|

<br>

# Question 5

<br> 

### The geographic range of my data (min/max - X/Y)

### Here, I take the logitude and latitude points into consideration into a big boundary box and then calculate the max and min values.


|  Longitude/Latitude   | Geographic range of my data (min/max - X/Y) |
| ------------- | --------------------- |
| Max Pickup Longitude/Pickup  | -179.36124|
| Min Pickup Longitude/Pickup| 112.40418 |
|  Max Pickup Latitude/Pickup   | 82.514046|
| Min Packup latitude/Pickup| -39.762348 |
| Max Dropoff Longitude/Dropoff  | |
| Min Dropoff Longitude/Dropoff|  |
|  Max Dropoff Latitude/Dropoff   | |
| Min Dropoff latitude/Dropoff|  |

<br>

### Plot Max Pickup Longitude/Pickup against Min latitude/Pickup on a map
### 
![Image of screencapture](images/New-MaxLong-MinLatitudepickup.jpg)

### Plot Min Pickup Longitude/Pickup against Max latitude/Pickup on a map
![Image of screencapture](images/New-MinLong-MaxLatitudepickup.jpg)

### Plot Max Dropoff Longitude/Pickup against Min latitude/Droppoff on a map 

### Plot Min Dropoff Longitude/Pickup against Max latitude/Droppoff on a map 

```
if line[10] != "" and float(line[10]) <= 180 and float(line[10])>= -180 and line[11] != "" and float(line[11]) <= 90 and float(line[11])>=-90:

                     if float(line[10]) < float(max_pickup_longitude_big_bounday):
                            max_pickup_longitude_big_bounday = line[10]
                     if float(line[10]) > float(min_pickup_longitude_big_bounday):
                            min_pickup_longitude_big_bounday = line[10]
        

                     if float(line[11]) > float(max_pickup_latitude_big_bounday):
                            max_pickup_latitude_big_bounday = line[11]
                     if float(line[11]) < float(min_pickup_latitude_big_bounday):
                            min_pickup_latitude_big_bounday = line[11]

```

<br>

### I take all points into the bounding box based on the longitude and litiude of NYC with computing the max and min values.

###  INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LONGITUDE 
### -----------------------------------------------------------------------------------------------------

###  The number of points inside the bounding box for 14776614 pickup longitude is really a big number compared to the number of points outside the bounding box:

```
    
                
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


     #{'-74.00': 1581119, '-73.97': 2576599, '-73.96': 1549802, '-73.99': 2503233, '-73.98': 3567237, '-74.01': 293161,
     # '-73.78': 159632, '-73.95': 1322448, '-73.86': 124359, '-73.94': 360437, '-73.90': 14566, '-73.87': 147130, '-73.79': 29227,
     # '-73.92': 53989, '-73.93': 76041, '-73.91': 35051, '-73.77': 43243, '-73.81': 2331, '-73.88': 21175, '-73.89': 9998,
     # '-73.80': 6042, '-74.10': 189, '-73.85': 3696, '-73.84': 4964, '-74.15': 520, '-74.16': 646, '-73.74': 138, '-74': 1524,
     # '-73.83': 2809, '-73.82': 1783, '-74.04': 1374, '-74.03': 3190, '-74.02': 2449, '-73.73': 228, '-74.09': 216, '-74.07': 446,
     # '-74.05': 566, '-74.08': 235, '-74.06': 591, '-73.70': 168, '-73.72': 248, '-74.12': 138, '-74.14': 146, '-74.23': 53,
     # '-73.75': 132, '-73.76': 226, '-74.18': 356, '-73.71': 114, '-74.17': 724, '-74.11': 183, '-74.20': 78, '-74.25': 42,
     # '-74.22': 96, '-74.19': 103, '-74.13': 118, '-74.21': 145, '-74.24': 37, '-73.69': 15}       



```
<br>

# Question 6

<br>

# In this code, the distinct values of some fields suchas pickup_datetime, dropoff_datetime, medallion, hack_license, rate_code, passenger_count, trip_time_in_secs and trip_distance are getting on. 

# I used a dictionary to get the total number of values for each field. Please run the python code to get the distinct values of other fields. 

# For an example of distint values of some fields explained below: 

<br>

|   Field Name   | Distinct Values |
| ------------- | --------------------- |
|   Rate Code   | MAX: 14456067, MIN:  1|
| passenger_count | MAX:  10471701, MIN: |

<br>


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


```

<br>

# Question 7

<br>

|   Field Name   | Max/Min Values |
| ------------- | --------------------- |
| trip_time_in_secs| MAX  10800, Min 0|
|  trip_distance   |MAX 99.90, Min 0|
|  Rate Code   |MAX 9 , Min 0|


```

                min_rate_code = line[3]
                max_rate_code = line[3]

                min_rate_code = line[8]
                max_rate_code = line[8]

                min_trip_distance   = line[9]
                max_trip_distance   = line[9]


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


```

<br>

# Question 8

<br>

# Pickup Ddatetime
# The average number of passengers each hour of the day 

|   Hour   | Avarage  |
| ------------- | --------------------- |
| 15| 1.7161581455566817|
| 00| 1.7674645758797922|
| 18| 1.7012934622800804|
| 23| 1.7540406583168833|
| 11| 1.6736848030241087|
| 12| 1.6811567347356455|
| 13| 1.688445186465027|
| 09| 1.6280298565816753|
| 07| 1.5957135230796233|
|14|1.695371301700947|
|22|1.7441527481804624|
|17|1.7042513525845773|
|06|1.5543789390756302|
|21|1.723739471842693|
|08|1.6261664483250076|
|19|1.7074959246849928|
|03|1.7749906599564864|
|04|1.7498726500909643|
|20|1.7098300345053143|
|01|1.7650990993235585|
|10|1.7715300962533436|
|02|1.7715300962533436|
|16|1.7186234442907942|
|05|1.620607966457023|

<br>

```
if Hour_datetime in d.keys():
                d[Hour_datetime] += 1
        else:
                d[Hour_datetime] = 1

        if Hour_datetime in mhist12.keys():

                mhist12[Hour_datetime] += int(line[7])
        else:
                mhist12[Hour_datetime] = int(line[7])


        # Get one out of every thousand rows (pickup_datetime)


```

![Image of screencapture](images/AVGPassengersPickup.JPG)



