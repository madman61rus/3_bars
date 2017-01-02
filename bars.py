import json
import os
from geopy.distance import vincenty

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding='cp1251') as data_file:
       bars_info = json.load(data_file)
    return bars_info

def get_biggest_bar(bars):
    result = max(bars, key=lambda tmp: tmp.get("SeatsCount", float('inf')))
    return result['Name']

def get_smallest_bar(bars):
    result = min(bars , key=lambda tmp: tmp.get("SeatsCount", float('inf')))
    return result['Name']

def get_closest_bar(bars_info, longitude, latitude):
    coordinates_array = [{'name': bars['Name'], 'latitude': float(bars['Latitude_WGS84']),
                          'longitude': float(bars['Longitude_WGS84']),
                          'distance': vincenty((float(bars['Latitude_WGS84']), float(bars['Longitude_WGS84'])),
                                               (latitude, longitude)).km}
                         for bars in bars_info]
    return (min(coordinates_array , key=lambda x: x['distance']))['name']


if __name__ == '__main__':
    file_path = input('Введите путь к файлу ')
    json_data = load_data(file_path)
    latitude = float(input('Введите latitude '))
    longitude = float(input('Введите longitude '))
    print('Самый маленький бар - ' + get_smallest_bar(json_data))
    print('Самый большой бар - ' + get_biggest_bar(json_data))
    print('Самый ближайший бар - ' + get_closest_bar(json_data,longitude,latitude))