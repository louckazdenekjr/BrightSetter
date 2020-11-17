#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os
import sys


#if os.getuid() != 0:
    #os.execl(sys.executable, sys.executable, *sys.argv)

class mainwindow(Gtk.Window):

    def __init__(self):
        
        Gtk.Window.__init__(self, title="BrightSetter")
        Gtk.Window.set_default_size(self, 200,100)
        Gtk.Window.set_resizable(self, False)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        box1 = Gtk.VButtonBox(spacing=10)
        
        button1 = Gtk.Button.new_with_mnemonic("Brighter")
        button1.connect("clicked", self.whenbutton1_clicked)
        button1.set_property("width-request", 200)
        
        button2 = Gtk.Button.new_with_mnemonic("Darker")
        button2.connect("clicked", self.whenbutton2_clicked)
        button2.set_property("width-request", 200)
		
        box1.pack_start(button1, True, True, 0)
        box1.pack_start(button2, True, True, 0)
        box1.set_border_width(20)

        self.add(box1)
        
    def whenbutton1_clicked(self, button):
        bashCommandUp = "brightnessctl set +10"
        output = subprocess.check_output(['bash','-c', bashCommandUp])
      
    def whenbutton2_clicked(self, button):
        bashCommandDown = "brightnessctl set 10-"
        output = subprocess.check_output(['bash','-c', bashCommandDown])


    def backToNormal():
        bashCommandReset = "brightnessctl set 100"
        output = subprocess.check_output(['bash','-c', bashCommandReset])
        return
    
window = mainwindow()
#window.connect("delete-event", backToNormal())
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
