# -*- coding: utf-8 -*-

'''
    iEPCBM Bot (YaLVA-B1) is Wikipedia bot
    Copyright (C) 2017, 2018  Rishat Kagirov (iEPCBM)
	
	This file is part of iEPCBM Bot.
    
    iEPCBM Bot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../conf"))

from bot_config import *

def getStrCascLev (cascLevel):
    retVal = ""
    i = 0
    while i < cascLevel:
        retVal += cascadeStep
        i += 1
    return retVal