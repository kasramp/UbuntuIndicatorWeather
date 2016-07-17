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
        config = {'temperature_scale': '0', 
        'automatic_location_detection': 'True', 
        'latitude': '0.00000', 
        'longitude': '0.00000'}
        self.__save_configuration_to_disk(config)
        return self.__load_configuration_from_disk()

    def __get_home_directory(self):
        return expanduser('~') + '/.indicator-weather'
    
    def get_temperature_scale(self):
        return int(self.json_configuration['temperature_scale'])

    def set_temperature_scale(self, value):
        self.json_configuration['temperature_scale'] = int(value)

    def get_automatic_location_detection(self):
        return self.is_automatic_location_detection()
    
    def set_automatic_location_detection(self, value):
        self.json_configuration['automatic_location_detection'] = value

    def is_automatic_location_detection(self):
        return ast.literal_eval(self.json_configuration['automatic_location_detection'])

    def get_latitude(self):
        return float(self.json_configuration['latitude'])

    def set_latitude(self, value):
        self.json_configuration['latitude'] = float(value)

    def get_longitude(self):
        return float(self.json_configuration['longitude'])

    def set_longitude(self, value):
        self.json_configuration['longitude'] = float(value)

    def save_configuration(self):
        self.__save_configuration_to_disk(self.json_configuration)