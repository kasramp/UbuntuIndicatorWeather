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
        self.builder.add_from_file('ui.glade')
        self.builder.connect_signals(self)
        self.window = self.builder.get_object('dialog_preferences')
        self.window.set_transient_for(None)
        self.window.show_all()
        self.configuration = Configuration()
        self.load_user_preferences_to_ui()

    def load_user_preferences_to_ui(self):
        combo, switch, latitude, longitude = self.get_ui_objects()
        combo.set_active(self.configuration.get_temperature_scale())
        switch.set_state(self.configuration.get_automatic_location_detection())
        latitude.set_sensitive(not switch.get_state())
        longitude.set_sensitive(not switch.get_state())
        latitude.set_value(self.configuration.get_latitude())
        longitude.set_value(self.configuration.get_longitude())
    
    def get_ui_objects(self):
        combo = self.builder.get_object('combo_temperature_scale')
        switch = self.builder.get_object('switch_automatic_location_detection')
        latitude = self.builder.get_object('spin_latitude')
        longitude = self.builder.get_object('spin_longitude')
        return combo, switch, latitude, longitude

    def on_cancel_button_clicked(self, widget, data=None):
        self.window.destroy()
        Gtk.main_quit()

    def on_ok_button_clicked(self, widget, data=None):
        combo, switch, latitude, longitude = self.get_ui_objects()
        self.configuration.set_temperature_scale(combo.get_active())
        self.configuration.set_automatic_location_detection(str(switch.get_active()).title())
        self.configuration.set_latitude(latitude.get_value())
        self.configuration.set_longitude(longitude.get_value())
        self.configuration.save_configuration()
        self.on_cancel_button_clicked(widget)

    def on_switch_automatic_location_detection_activated(self, switch, data):
        longitude = self.builder.get_object('spin_longitude')
        latitude = self.builder.get_object('spin_latitude')
        latitude.set_sensitive(not switch.get_active())
        longitude.set_sensitive(not switch.get_active())

    def main(self):
        Gtk.main()