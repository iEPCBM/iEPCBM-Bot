# -*- coding: utf-8 -*-

#    iEPCBM Bot (YaLVA-B1) is Wikipedia bot
#    Copyright (C) 2017, 2018  Rishat Kagirov (iEPCBM)
#    
#    This file is part of iEPCBM Bot.
#    
#    iEPCBM Bot is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    
#    **************************************************************************
#    
#    Program use GoogleAPI.
#    GoogleAPIs Terms of Service - <https://developers.google.com/terms/>
#    
#    **************************************************************************
#    Note:
#        YouTube is Google's trade mark



# doc for program
'''
    iEPCBM Bot (YaLVA-B1) is Wikipedia bot
    Copyright (C) 2017, 2018  Rishat Kagirov (iEPCBM)
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    **************************************************************************
    
    Program use GoogleAPI.
    GoogleAPIs Terms of Service - <https://developers.google.com/terms/>
    
    **************************************************************************
    Note:
        YouTube is Google's trade mark
'''

import os, sys

curDir = os.path.dirname(__file__)
sys.path.append(os.path.join(curDir, "modules"))
sys.path.append(os.path.join(curDir, "conf"))
sys.path.append(os.path.join(curDir, "modules/tools"))

import math
import pywikibot
import datetime
import re
import time

# Подключаем свои скрипты 
from bot_config import *
from getDataFrom_YouTube import *
from list_channels import *
from TemplateYouTubePerson_list import *
from monthsRU import *

from updateViewsAndSubscriberCount import *

site = pywikibot.Site()

def main():
    print (__doc__)
    # Получение данных о каналах, указанных в SubscriberCountAndViewCountList
    data = getAllDataOfSubsAndViewsCount()
    
    # Обновление даннах в соответствующих статьях
    for member in data:
        IEBLogger.info ("Current article: " + member["ruWikipediaArticleTitle"])
        # IEBLogger.debug ("Waiting for user agree...")
        # IEBLogger.debug ("Press <ENTER> to continue...")
        # input ()
        # IEBLogger.info ("Sleeping for " + str(wikiMinQuota) + " seconds (local quota)...")
        # time.sleep (wikiMinQuota)
        updateViewsAndSubscribersCount (member, site)
    IEBLogger.debug ("Done! Press <ENTER> to exit...")
    input ()
    pywikibot.stopme()
    return 0

if __name__ == "__main__":
    main()
