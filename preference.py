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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from configuration import Configuration

class Dialog:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('/usr/share/ubuntu-indicator-weather/ui.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('dialog_preferences')
        self.window.set_transient_for(None)
        self.window.show_all()
        self.configuration = Configuration()
        self.load_user_preferences_to_ui()

    def load_user_preferences_to_ui(self):
        combo_temperature_scale, combo_wind_scale, switch_automatic_location_detection, latitude, longitude, switch_hide_location, switch_round_temperature, switch_autostart = self.get_ui_objects()
        combo_temperature_scale.set_active(self.configuration.get_temperature_scale())
        combo_wind_scale.set_active(self.configuration.get_wind_scale())
        switch_automatic_location_detection.set_state(self.configuration.get_automatic_location_detection())
        latitude.set_sensitive(not switch_automatic_location_detection.get_state())
        longitude.set_sensitive(not switch_automatic_location_detection.get_state())
        latitude.set_value(self.configuration.get_latitude())
        longitude.set_value(self.configuration.get_longitude())
        switch_hide_location.set_state(self.configuration.get_hide_location())
        switch_round_temperature.set_state(self.configuration.get_round_temperature())
        switch_autostart.set_state(self.configuration.get_auto_start())
    
    def get_ui_objects(self):
        combo_temperature_scale = self.builder.get_object('combo_temperature_scale')
        combo_wind_scale = self.builder.get_object('combo_wind_scale')
        switch_automatic_location_detection = self.builder.get_object('switch_automatic_location_detection')
        latitude = self.builder.get_object('spin_latitude')
        longitude = self.builder.get_object('spin_longitude')
        switch_hide_location = self.builder.get_object('switch_hide_location')
        switch_round_temperature = self.builder.get_object('switch_round_temperature')
        switch_autostart = self.builder.get_object('switch_autostart')
        return combo_temperature_scale, combo_wind_scale, switch_automatic_location_detection, latitude, longitude, switch_hide_location, switch_round_temperature, switch_autostart

    def on_cancel_button_clicked(self, widget, data=None):
        self.window.destroy()
        Gtk.main_quit()

    def on_ok_button_clicked(self, widget, data=None):
        combo_temperature_scale, combo_wind_scale, switch_automatic_location_detection, latitude, longitude, switch_hide_location, switch_round_temperature, switch_autostart = self.get_ui_objects()
        self.configuration.set_temperature_scale(combo_temperature_scale.get_active())
        self.configuration.set_wind_scale(combo_wind_scale.get_active())
        self.configuration.set_automatic_location_detection(str(switch_automatic_location_detection.get_active()).title())
        self.configuration.set_latitude(latitude.get_value())
        self.configuration.set_longitude(longitude.get_value())
        self.configuration.set_hide_location(str(switch_hide_location.get_active()).title())
        self.configuration.set_round_temperature(str(switch_round_temperature.get_active()).title())
        self.configuration.set_auto_start(str(switch_autostart.get_active()).title())
        self.configuration.save_configuration()
        self.configuration.save_ini_start_up_script()
        self.on_cancel_button_clicked(widget)

    def on_switch_automatic_location_detection_activated(self, switch_automatic_location_detection, data):
        longitude = self.builder.get_object('spin_longitude')
        latitude = self.builder.get_object('spin_latitude')
        latitude.set_sensitive(not switch_automatic_location_detection.get_active())
        longitude.set_sensitive(not switch_automatic_location_detection.get_active())

    def main(self):
        Gtk.main()
