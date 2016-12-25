#!/usr/bin/python
# -*- coding: utf8 -*-

import json
import os
from geopy.distance import vincenty

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r',encoding='cp1251') as data_file:
       data = json.load(data_file)
    return data

def get_biggest_bar(data):
    sorted_data = sorted(data, key=lambda x: x['SeatsCount'])
    return sorted_data[len(sorted_data)-1]['Name']

def get_smallest_bar(data):
    sorted_data = sorted(data, key=lambda x: x['SeatsCount'])
    return sorted_data[0]['Name']

def get_closest_bar(data, longitude, latitude):
    coordinates_array = [{'name': dt['Name'], 'latitude': float(dt['Latitude_WGS84']),
                          'longitude': float(dt['Longitude_WGS84']),
                          'distance': vincenty((float(dt['Latitude_WGS84']), float(dt['Longitude_WGS84'])),
                                               (latitude, longitude)).km}
                         for dt in data]
    return (min(coordinates_array , key=lambda x: x['distance']))['name']


if __name__ == '__main__':
    file_path = input('Введите путь к файлу ')
    data = load_data(file_path)
    latitude = float(input('Введите latitude '))
    longitude = float(input('Введите longitude '))
    print('Самый маленький бар - ' + get_smallest_bar(data))
    print('Самый большой бар - ' + get_biggest_bar(data))
    print('Самый ближайший бар - ' + get_closest_bar(data,longitude,latitude))