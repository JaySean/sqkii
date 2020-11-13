# Sqkii Hunt 1
This sub repository corresponds to the Sqkii Hunt on 18 June 2020

## Procedure

### 1. Supermarkets

_Hint #1: It is within a 15-minute walk from a supermarket._

#### Dataset
CSV file retrieved from Data.gov.sg

[List of Supermarket Licences](https://data.gov.sg/dataset/list-of-supermarket-licences?resource_id=3561a136-4ee4-4029-a5cd-ddf591cce643
 "List of Supermarket Licences")

#### Result

+ Average Human Walking Speed: 5km/h
+ 15-min walking radius = 1250m radius
+ Each purple circle corresponds to a supermarket
+ White marker indicates the actual answer

![](https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint1_output.png "Hint 1 Output")


### 2. Historical Sites and Towns

_Hint #2: There is a historical site within the town._

#### Dataset
##### Historical Site:

Historic site data manually retrieved from roots.gov.sg

[Historic Site Markers](https://roots.sg/learn/places/Historic%20Sites "Historic Site Markers")

##### Town:

KML file retrieved from Data.gov.sg

[Master Plan 2019 Planning Area Boundary](https://data.gov.sg/dataset/master-plan-2019-planning-area-boundary-no-sea
 "Master Plan 2019 Planning Area Boundary")

#### Result

+ Each grey marker corresponds to a historial site
+ Each blue polygon/marker corresponds to a town
+ Towns without a historical site are removed
+ White marker indicates the actual answer

![](https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint2_output_1.png "Hint 2 Output 1")

![](https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint2_output_2.png "Hint 2 Output 2")

### 3. MRT

_Hint #3: It is at least a 40-minute MRT ride from Changi Airport._

#### Dataset

KML file retrieved from Data.gov.sg

[Master Plan 2019 Rail Station Name layer](https://data.gov.sg/dataset/master-plan-2019-rail-station-name-layer
 "Master Plan 2019 Rail Station Name layer
")

#### Result

+ Each marker corresponds to an MRT station
+ Travel distance time from Changi Airport is calculated using Google Maps [Distance Matrix API](https://developers.google.com/maps/documentation/distance-matrix/overview
 "Distance Matrix API")
+ Green markers are at least 40 mins away from Changi Airport
+ Red markers are within 40 mins from Changi Airport
+ White marker indicates the actual answer
+ _Note: Travel distance times calculate by the Distance Matrix API are probably longer than reality_

![](https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint3_output.png "Hint 3 Output")

## Hints

<img src="https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint1.jpg" alt="Hint 1" width="500" height="500">
<img src="https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint2.jpg" alt="Hint 2" width="500" height="500">
<img src="https://github.com/JaySean/sqkii/raw/main/sqkii1/images/hint3.jpg" alt="Hint 3" width="500" height="500">
