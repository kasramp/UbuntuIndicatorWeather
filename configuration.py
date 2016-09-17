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
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

class Configuration:

    def __init__(self):
        self.config_file_name = self.__get_config_file_path()
        self.start_up_file_name = self.__get_start_up_file_path()
        self.json_configuration = self.__create_folder_and_config_file_if_not_exist()
        self.ini_start_up = self.__create_start_up_script_if_not_exist()
        self.__apply_change_log()

    def __create_folder_and_config_file_if_not_exist(self):
        if not os.path.exists(os.path.dirname(self.config_file_name)):
            try:
                os.makedirs(os.path.dirname(self.config_file_name))
                return self.__create_default_configuration_and_save_to_disk()
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        else:
            return self.__load_configuration_from_disk()

    def __create_start_up_script_if_not_exist(self):
        if not os.path.exists(self.start_up_file_name):
            try:
                return self.__create_default_start_up_script_and_save_to_disk()
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        else:
            return self.__load_start_up_script_from_disk()

    def __load_configuration_from_disk(self):
        with open(self.config_file_name, "r") as f:
            return json.load(f)

    def __load_start_up_script_from_disk(self):
        config = ConfigParser()
        config.optionxform = str
        config.read(self.start_up_file_name)
        return config

    def __save_configuration_to_disk(self, content):
        with open(self.config_file_name, 'w') as f:
            json.dump(content, f)

    def __save_ini_start_up_script_to_disk(self, content):
        with open(self.start_up_file_name, 'w') as config_file:
            content.write(config_file)

    def __create_default_configuration_and_save_to_disk(self):
        config = { 
        	Parameter.TEMPERATURE_SCALE: '0', 
        	Parameter.AUTOMATIC_LOCATION_DETECTION: 'True', 
        	Parameter.LATITUDE: '0.00000', 
        	Parameter.LONGITUDE: '0.00000',
            Parameter.HIDE_LOCATION: 'False',
            Parameter.ROUND_TEMPERATURE: 'False'
        }
        self.__save_configuration_to_disk(config)
        return self.__load_configuration_from_disk()

    def __create_default_start_up_script_and_save_to_disk(self):
        config = ConfigParser()
        config.optionxform = str
        config.add_section(Startup.SECTION_DESKTOP_ENTRY)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_NAME, Startup.SETTING_VALUE_NAME)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_COMMENT, Startup.SETTING_VALUE_COMMENT)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_EXEC, Startup.SETTING_VALUE_EXEC)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_TERMINAL, Startup.SETTING_VALUE_TERMINAL)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_TYPE, Startup.SETTING_VALUE_TYPE)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_ICON, Startup.SETTING_VALUE_ICON)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_CATEGORIES, Startup.SETTING_VALUE_CATEGORIES)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_NO_DISPLAY, Startup.SETTING_VALUE_NO_DISPLAY)        
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_ONLY_SHOW_IN, Startup.SETTING_VALUE_ONLY_SHOW_IN)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_X_GNOME_AUTO_START_ENABLED, Startup.SETTING_VALUE_X_GNOME_AUTO_START_ENABLED)
        config.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_X_UBUNTU_GET_TEXT_DOMAIN, Startup.SETTING_VALUE_X_UBUNTU_GET_TEXT_DOMAIN) 
        self.__save_ini_start_up_script_to_disk(config)
        return self.__load_start_up_script_from_disk()

    def __get_config_file_path(self):
        return self.__get_home_directory() + '/.indicator-weather/config.json'

    def __get_start_up_file_path(self):
        return self.__get_home_directory() + '/.config/autostart/indicator-weather.desktop'

    def __get_home_directory(self):
        return expanduser('~')
    
    def __apply_change_log(self):
        if Parameter.HIDE_LOCATION not in self.json_configuration:
            self.json_configuration[Parameter.HIDE_LOCATION] = 'False'
            self.save_reload_configuration()
        if Parameter.ROUND_TEMPERATURE not in self.json_configuration:
            self.json_configuration[Parameter.ROUND_TEMPERATURE] = 'False'
            self.save_reload_configuration()

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

    def get_hide_location(self):
        return self.is_hide_location()
    
    def set_hide_location(self, value):
        self.json_configuration[Parameter.HIDE_LOCATION] = value

    def is_hide_location(self):
        return ast.literal_eval(self.json_configuration[Parameter.HIDE_LOCATION])

    def get_round_temperature(self):
        return self.is_round_temperature()
    
    def set_round_temperature(self, value):
        self.json_configuration[Parameter.ROUND_TEMPERATURE] = value

    def is_round_temperature(self):
        return ast.literal_eval(self.json_configuration[Parameter.ROUND_TEMPERATURE])

    def get_auto_start(self):
        return self.ini_start_up.getboolean(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_X_GNOME_AUTO_START_ENABLED)

    def set_auto_start(self, value):
        return self.ini_start_up.set(Startup.SECTION_DESKTOP_ENTRY, Startup.SETTING_NAME_X_GNOME_AUTO_START_ENABLED, value.lower())

    def save_configuration(self):
        self.__save_configuration_to_disk(self.json_configuration)

    def save_ini_start_up_script(self):
        self.__save_ini_start_up_script_to_disk(self.ini_start_up)

    def reload_configuration(self):
    	self.json_configuration = self.__load_configuration_from_disk()

    def save_reload_configuration(self):
        self.save_configuration()
        self.reload_configuration()

class Parameter:
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    AUTOMATIC_LOCATION_DETECTION = 'automatic_location_detection'
    TEMPERATURE_SCALE = 'temperature_scale'
    HIDE_LOCATION = 'hide_location'
    ROUND_TEMPERATURE = 'round_temperature'

class Startup:
    SECTION_DESKTOP_ENTRY = 'Desktop Entry'
    SETTING_NAME_NAME = 'Name'
    SETTING_VALUE_NAME = 'Simple Weather Indicator'
    SETTING_NAME_COMMENT = 'Comment'
    SETTING_VALUE_COMMENT = 'Simple Weather Indicator'
    SETTING_NAME_EXEC = 'Exec'
    SETTING_VALUE_EXEC = 'indicator-weather'
    SETTING_NAME_TERMINAL = 'Terminal'
    SETTING_VALUE_TERMINAL = 'False'
    SETTING_NAME_TYPE = 'Type'
    SETTING_VALUE_TYPE = 'Application'
    SETTING_NAME_ICON = 'Icon'
    SETTING_VALUE_ICON = '/usr/share/icons/hicolor/32x32/apps/indicator-weather.png'
    SETTING_NAME_CATEGORIES = 'Categories'
    SETTING_VALUE_CATEGORIES = 'GNOME;Weather;'
    SETTING_NAME_NO_DISPLAY = 'Nodisplay'
    SETTING_VALUE_NO_DISPLAY = 'true'
    SETTING_NAME_ONLY_SHOW_IN = 'Onlyshowin'
    SETTING_VALUE_ONLY_SHOW_IN = 'Unity;GNOME;'
    SETTING_NAME_X_GNOME_AUTO_START_ENABLED = 'X-GNOME-Autostart-enabled'
    SETTING_VALUE_X_GNOME_AUTO_START_ENABLED = 'true'
    SETTING_NAME_X_UBUNTU_GET_TEXT_DOMAIN = 'X-Ubuntu-Gettext-domain'
    SETTING_VALUE_X_UBUNTU_GET_TEXT_DOMAIN = 'indicator-weather'
    