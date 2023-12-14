import csv
import xml.etree.ElementTree as ET

SPEED = 8; # m/s, drone speed between waypoints
kml_file = "Tianqin_MS-v2.kml"
output_csv = 'output_MS_DJI.csv'
output_csv_UGCS = 'output_MS_UGCS.csv'

def extract_waypoint_to_DJI_csv(kml_file, output_csv):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    placemarks = root.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)        
        writer.writerow(['point_name','lon',	'lat'	,'height',	'heading',	'gimbal'	,'speed',	'turnmode',	'actions_sequence'])

        for placemark in placemarks:
            lookat = placemark.find('.//{http://www.opengis.net/kml/2.2}LookAt')

            name = placemark.find('.//{http://www.opengis.net/kml/2.2}name').text
            longitude = lookat.find('.//{http://www.opengis.net/kml/2.2}longitude').text
            latitude = lookat.find('.//{http://www.opengis.net/kml/2.2}latitude').text
            altitude = lookat.find('.//{http://www.opengis.net/kml/2.2}altitude').text
            heading = lookat.find('.//{http://www.opengis.net/kml/2.2}heading').text
            tilt = int(float(lookat.find('.//{http://www.opengis.net/kml/2.2}tilt').text))
            range_value = lookat.find('.//{http://www.opengis.net/kml/2.2}range').text
            # altitude_mode = lookat.find('.//{http://www.opengis.net/kml/2.2}altitudeMode').text
            tilt = -tilt # DJI uses opposite sign for tilt

            writer.writerow([name, longitude, latitude, altitude, heading, tilt,SPEED, 'AUTO','SHOOT'])

def extract_waypoint_to_UGCS_csv(kml_file, output_csv):
    tree = ET.parse(kml_file)
    root = tree.getroot()

    placemarks = root.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)        
        # writer.writerow(['point_name','lon',	'lat'	,'height',	'heading',	'gimbal'	,'speed',	'turnmode',	'actions_sequence'])

        for placemark in placemarks:
            lookat = placemark.find('.//{http://www.opengis.net/kml/2.2}LookAt')

            name = placemark.find('.//{http://www.opengis.net/kml/2.2}name').text
            longitude = lookat.find('.//{http://www.opengis.net/kml/2.2}longitude').text
            latitude = lookat.find('.//{http://www.opengis.net/kml/2.2}latitude').text
            altitude = lookat.find('.//{http://www.opengis.net/kml/2.2}altitude').text
            heading = lookat.find('.//{http://www.opengis.net/kml/2.2}heading').text
            tilt = int(float(lookat.find('.//{http://www.opengis.net/kml/2.2}tilt').text))
            range_value = lookat.find('.//{http://www.opengis.net/kml/2.2}range').text
            # altitude_mode = lookat.find('.//{http://www.opengis.net/kml/2.2}altitudeMode').text
            tilt = -tilt # DJI uses opposite sign for tilt

            writer.writerow([latitude,longitude, altitude, '0',-tilt, heading])


if __name__ == '__main__':
    extract_waypoint_to_DJI_csv(kml_file, output_csv)
    extract_waypoint_to_UGCS_csv(kml_file, output_csv_UGCS)
    print("Done")