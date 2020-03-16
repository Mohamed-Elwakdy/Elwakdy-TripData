

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

####  INSIDE THE BOUNDING BOX (MAX AND MINIMUM LONGITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LONGITUDE 
#### -----------------------------------------------------------------------------------------------------

###  The number of points inside the bounding box for 14776614 pickup longitude is really a big number compared to the number of points outside the bounding box:

```
    
                
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


```

# The number points of pickup longitude out of bounding box of NYC for 14776614 pickup longitude The number of points in this band is really small if it is compared to the points number of pickup longitude inside the bounding box.

```

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
   
```

#### INSIDE THE BOUNDING BOX (MAX AND MINIMUM LATITUDE) - COMPUTER THE POINTS NUMBER OF PICKUP LATITUDE 
#### -----------------------------------------------------------------------------------------------------

### There are many pick up latitude points inside the box compared the latitude points outside the bounding box 

```

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
                               mhist1_inside_Boundingbox[line_text2] = 

```

### The number points of pickup latitude out of bounding box of NYC for 14776614 pickup latitude are few whether it is compared to the number of points inside the bounding box 

```

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


```

<br>

# Question 6

<br>

### In this code, the distinct values of some fields suchas pickup_datetime, dropoff_datetime, medallion, hack_license, rate_code, passenger_count, trip_time_in_secs and trip_distance are getting on. 

### I used a dictionary to get the total number of values for each field. Please run the python code to get the distinct values of other fields. 

### For an example of distint values of some fields explained below: 

<br>

### min and max of the rate code and passenger account:

|   Field Name   | Distinct Values |
| ------------- | --------------------- |
|   rate_code   | MAX: 14456067, MIN:  1|
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


```

<br>

# Question 7

<br>

### The values of trip_time_in_secs, trip_distance and Rate Code outside the bounding box

|   Field Name   | Max/Min Values |
| ------------- | --------------------- |
| trip_time_in_secs| MAX  10800, Min 0|
|  trip_distance   |MAX 99.90, Min 0|
|  Rate Code   |MAX 9 , Min 0|


```
                min_rate_code = line[3]
                max_rate_code = line[3]


                if line[3] > max_rate_code:
                        max_rate_code = line[3]
                if line[3] < min_rate_code:
                        min_rate_code = line[3]

```

<br>

# Question 8

<br>

### Pickup Datetime

### The average number of passengers each hour of the day 

<br>

```
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

```

###  The average number of passengers per day (pickup_datetime) 

``` 

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


```
### The average of passengers per hour (Puckup)
![Image of screencapture](images/AVGPassengersPickup.JPG)

### The average of passengers per hour (Droopoff)
![Image of screencapture](images/Droppoff.JPG)



