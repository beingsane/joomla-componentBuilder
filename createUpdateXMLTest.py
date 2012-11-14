﻿#===============================================================================
# @version:        1.0.0
# @summary:        Test script for update server xml creating
# @copyright:      (C) 2012 Mathias Gebhardt
# @license:        GNU General Public License version 2 or later; see LICENSE.txt
#===============================================================================

from xml.dom.minidom import parse, parseString
import zipfile
import os
import sys
import urllib2

updateServer = 'https://github.com/downloads/mgebhardt/osbit/osbit-update.xml'
version = '0.6.0dev5'

file = urllib2.urlopen(updateServer)
dom = parse(file)
update = dom.getElementsByTagName('update')[0].cloneNode(True);
update.getElementsByTagName('version')[0].firstChild = dom.createTextNode(version)

#print update.toxml();

dom.firstChild.appendChild(update)

print dom.toxml()