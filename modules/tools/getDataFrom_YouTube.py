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
    
    **************************************************************************
    
    Program use GoogleAPI.
    GoogleAPIs Terms of Service - <https://developers.google.com/terms/>
    
    **************************************************************************
    Note:
        YouTube is Google's trade mark
'''

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

import urllib.request
import json
import logging
import math
import time

from bot_config import *
from list_channels import *
from getStrCascLev import *
from postRound import *

URL_get_channel_data = "https://www.googleapis.com/youtube/v3/channels"

cascadeLevel = 0

def getSubscriberCountAndViewCount (ChannelID):
    try:
        response = urllib.request.urlopen(URL_get_channel_data+"?part=statistics&id="+ChannelID+"&key="+GoogleAPI_key_code)
    except urllib.error.URLError as err:
        return "Server returned error code: " + str(err.code)
    json_data = response.read().decode('utf8')
    list_data = json.loads(json_data)
    returnObject = {}
    if list_data['pageInfo']['totalResults'] > 0:
        if list_data['items'][0]['statistics']['hiddenSubscriberCount'] is False:
            returnObject = {"subscriberCount": list_data['items'][0]['statistics']['subscriberCount'],
                            "viewCount": list_data['items'][0]['statistics']['viewCount']}
        else:
            returnObject = {"subscriberCount": UNKNOWN,
                            "viewCount": list_data['items'][0]['statistics']['viewCount']}
    else:
        return "unknownChannel"
    return returnObject

def getStrOfRoundedDataFromSingleChannel (chMem):
    global cascadeLevel
    for dataMem in chMem["data"]:
        IEBLogger.info (getStrCascLev(cascadeLevel) + "Getting subscriber count and view count for channel: " + dataMem["channelName"])
        cascadeLevel += 1
        response = getSubscriberCountAndViewCount (dataMem["channelID"])
        if type(response) is str:
            if response is "unknownChannel":
                IEBLogger.warn (getStrCascLev(cascadeLevel) + "Unknown channel with ID " + dataMem["channelID"])
            else:
                IEBLogger.error (getStrCascLev(cascadeLevel) + response)
        else:
            IEBLogger.info (getStrCascLev(cascadeLevel) + "Subscribers:             " + response["subscriberCount"])
            IEBLogger.info (getStrCascLev(cascadeLevel) + "Views:                   " + response["viewCount"])
            subscriberPostfix = ""
            viewPostfix = ""
            strRSubscriberCount = ""
            strRViewCount = ""
            subscriberCount = 0
            viewCount = 0
            rSubscriberCount = 0
            rViewCount = 0
            isSubsUnknown = response["subscriberCount"] == UNKNOWN
            if not isSubsUnknown:
                if int(response["subscriberCount"])>million:
                    subscriberPostfix = millionsPostfix
                    subscriberCount = int(response["subscriberCount"]) / 100000
                    rSubscriberCount = math.floor(subscriberCount)
                    rSubscriberCount /= 10
                elif int(response["subscriberCount"])>thousand:
                    subscriberPostfix = thousandsPostfix
                    subscriberCount = int(response["subscriberCount"]) / 100
                    rSubscriberCount = math.floor(subscriberCount)
                    rSubscriberCount /= 10
                else:
                    rSubscriberCount = subscriberCount
            else:
                subscriberCount = UNKNOWN
                rSubscriberCount = UNKNOWN
            if int(response["viewCount"])>billion:
                viewPostfix = billionsPostfix
                viewCount = int(response["viewCount"]) / 100000000
                rViewCount = math.floor(viewCount)
                rViewCount /= 10
            elif int(response["viewCount"])>million:
                viewPostfix = millionsPostfix
                viewCount = int(response["viewCount"]) / 1000000
                rViewCount = math.floor(viewCount)
                rViewCount /= 1
            elif int(response["viewCount"])>thousand:
                viewPostfix = thousandsPostfix
                viewCount = int(response["viewCount"]) / 1000
                rViewCount = math.floor(viewCount)
                rViewCount /= 1
            strRSubscriberCount = str(rSubscriberCount).replace(".", ",") + subscriberPostfix
            strRViewCount = str(rViewCount).replace(".", ",") + viewPostfix
            IEBLogger.info (getStrCascLev(cascadeLevel) + "Rounded subscribers:     " + strRSubscriberCount)
            IEBLogger.info (getStrCascLev(cascadeLevel) + "Rounded views:           " + strRViewCount)
            strRSubscriberCount = (str(postRound (rSubscriberCount)).replace(".", ",") + subscriberPostfix) if not isSubsUnknown else UNKNOWN
            strRViewCount = (str(postRound (rViewCount)).replace(".", ",") + viewPostfix)
            IEBLogger.info (getStrCascLev(cascadeLevel) + "PostRounded subscribers: " + strRSubscriberCount)
            IEBLogger.info (getStrCascLev(cascadeLevel) + "PostRounded views:       " + strRViewCount)
            dataMem.update ({"strRSubscriberCount"    : strRSubscriberCount,
                            "strRViewCount"            : strRViewCount})
            cascadeLevel -= 1
    return chMem

def getAllDataOfSubsAndViewsCount ():
    global cascadeLevel
    IEBLogger.info (log_TitleSeparator + " Get subscriber count and view count from all channels " + log_TitleSeparator)
    cascadeLevel += 1
    returnVal = []
    for index, i in enumerate(SubscriberCountAndViewCountList):
        IEBLogger.info (getStrCascLev(cascadeLevel) + "ruWikipedia article title: " + i["ruWikipediaArticleTitle"])
        IEBLogger.info (getStrCascLev(cascadeLevel) + "Index: " + str(index))
        cascadeLevel += 1
        returnVal.append (getStrOfRoundedDataFromSingleChannel (i))
        # IEBLogger.info (getStrCascLev(cascadeLevel) + "Sleeping for " + str(GoogleAPI_MinQuota) + " seconds (local quota)...")
        # time.sleep (GoogleAPI_MinQuota)
        cascadeLevel -= 1
    cascadeLevel -= 1
    return returnVal
