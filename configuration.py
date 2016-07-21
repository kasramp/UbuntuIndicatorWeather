# This file is part of indicator-weather.
# Indicator Weather is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3
# as published by the Free Software Foundation.
#
# Indicator Weather is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.  <http://www.gnu.org/licenses/>
#
# Author(s):
# (C) 2015 Kasra Madadipouya <kasra@madadipouya.com>

import json
import ast
import os
from os.path import expanduser

class Configuration:

    def __init__(self):
        self.file_name = self.__get_home_directory() + '/config.json'
        self.json_configuration = self.__create_folder_and_config_file_if_not_exist()

    def __create_folder_and_config_file_if_not_exist(self):
        if not os.path.exists(os.path.dirname(self.file_name)):
            try:
                os.makedirs(os.path.dirname(self.file_name))
                return self.__create_default_configuration_and_save_to_disk()
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        else:
            return self.__load_configuration_from_disk()

    def __load_configuration_from_disk(self):
        with open(self.file_name, "r") as f:
            return json.load(f)

    def __save_configuration_to_disk(self, content):
        with open(self.file_name, 'w') as f:
            json.dump(content, f)

    def __create_default_configuration_and_save_to_disk(self):
        config = { 
        	Parameter.TEMPERATURE_SCALE: '0', 
        	Parameter.AUTOMATIC_LOCATION_DETECTION: 'True', 
        	Parameter.LATITUDE: '0.00000', 
        	Parameter.LONGITUDE: '0.00000'
        }
        self.__save_configuration_to_disk(config)
        return self.__load_configuration_from_disk()

    def __get_home_directory(self):
        return expanduser('~') + '/.indicator-weather'
    
    def get_temperature_scale(self):
        return int(self.json_configuration[Parameter.TEMPERATURE_SCALE])

    def set_temperature_scale(self, value):
        self.json_configuration[Parameter.TEMPERATURE_SCALE] = int(value)

    def get_automatic_location_detection(self):
        return self.is_automatic_location_detection()
    
    def set_automatic_location_detection(self, value):
        self.json_configuration[Parameter.AUTOMATIC_LOCATION_DETECTION] = value

    def is_automatic_location_detection(self):
        return ast.literal_eval(self.json_configuration[Parameter.AUTOMATIC_LOCATION_DETECTION])

    def get_latitude(self):
        return float(self.json_configuration[Parameter.LATITUDE])

    def set_latitude(self, value):
        self.json_configuration[Parameter.LATITUDE] = float(value)

    def get_longitude(self):
        return float(self.json_configuration[Parameter.LONGITUDE])

    def set_longitude(self, value):
        self.json_configuration[Parameter.LONGITUDE] = float(value)

    def get_coordinates(self):
        return self.get_latitude(), self.get_longitude()

    def set_coordinates(self, latitude, longitude):
        self.set_latitude(latitude)
        self.set_longitude(longitude)

    def save_configuration(self):
        self.__save_configuration_to_disk(self.json_configuration)

    def reload_configuration(self):
    	self.json_configuration = self.__load_configuration_from_disk()

class Parameter:
		LATITUDE = 'latitude'
		LONGITUDE = 'longitude'
		AUTOMATIC_LOCATION_DETECTION = 'automatic_location_detection'
		TEMPERATURE_SCALE = 'temperature_scale'
    