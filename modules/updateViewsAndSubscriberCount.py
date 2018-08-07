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
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "tools"))

import math
import pywikibot
import datetime
import re

from bot_config import *
from list_channels import *
from TemplateYouTubePerson_list import *
from monthsRU import *

from getDataFrom_YouTube import *
from sortByTemplate import *


def notFoundUsedParams (foundUsedParams):
    nApr = memberOfParamsUsed
    for index, memberOfParamsUsed in enumerate(TemplateYouTubePerson_list_used):
        for memberFUP in foundUsedParams:
            if memberOfParamsUsed["name"] == memberFUP:
                del nApr[index]
    return nApr

def updateViewsAndSubscribersCount (member, site):
    if member["ruWikipediaArticleTitle"] == NONAME:
        return False
    page = pywikibot.Page(site, member["ruWikipediaArticleTitle"])
    if re.search(r'\{\{(nobots|bots\|(allow=none|deny=.*?[iI]EPCBM Bot.*?|optout=all|deny=all))\}\}', page.text):
        IEBLogger.warn ("Denied for editing article " + "[[" +member["ruWikipediaArticleTitle"] + "]]")
        return False
    isFormatted = False
    isRemNParams = False
    isCorrected = False
    listOfChannelsToInvite = u""
    fParams = []
    templateParams = []
    KTIsFound = False
    for template in page.templatesWithParams():
        if template[0].title() == keyTemplate:
            KTIsFound = True
            for templateMember in template[1]:
                for memberNameOfParamsUsed in TemplateYouTubePerson_list_used_names:
                    if templateMember.split('=', 1)[0] == memberNameOfParamsUsed:
                        fParams.append (templateMember.split('=', 1)[0])
            for param2Add in list(set(TemplateYouTubePerson_list_used_names) - set(fParams)):
                template[1].append(param2Add + "=")
            foundUsedParams = []
            for templateMember in template[1]:
                for memberOfParamsUsed in TemplateYouTubePerson_list_used:
                    if templateMember.split('=', 1)[0] == memberOfParamsUsed["name"]:
                        isCurMonth = memberOfParamsUsed["idToGetVal"] == CURMOUNTH
                        isCurDate = memberOfParamsUsed["idToGetVal"] == CURDATE
                        CurVal = ""
                        for memberData in member["data"]:
                            isUnknownRelData = (isCurDate or isCurMonth) and memberOfParamsUsed["idToCheck"] != NONE and memberData[memberOfParamsUsed["idToCheck"]] == UNKNOWN
                            if not (isCurDate or isCurMonth) and memberData[memberOfParamsUsed["idToGetVal"]] != UNKNOWN:
                                if len(member["data"]) > 1:
                                    CurVal += prefixListMember
                                CurVal += memberData[memberOfParamsUsed["idToGetVal"]]
                                if memberData["postfix"] != NONE:
                                    CurVal += " (" + memberData["postfix"] + ")"
                            elif isCurMonth and not isUnknownRelData:
                                CurVal = months[int(datetime.datetime.now().strftime("%m"))-1] + " " + datetime.datetime.now().strftime("%Y")
                            elif isCurDate and not isUnknownRelData:
                                CurVal = datetime.datetime.now().strftime("%#d") + " " + months_inGenitiveCase[int(datetime.datetime.now().strftime("%m"))-1] + " " + datetime.datetime.now().strftime("%Y")
                        if (not (isCurDate or isCurMonth) and  memberData[memberOfParamsUsed["idToGetVal"]] == UNKNOWN) or isUnknownRelData:
                            templateParams.append ({"name": templateMember.split('=', 1)[0],
                                                    "value": templateMember.split('=', 1)[1]})
                        else:
                            templateParams.append ({"name": templateMember.split('=', 1)[0],
                                                    "value": CurVal})
                        break
                else:
                    templateParams.append ({"name": templateMember.split('=', 1)[0],
                                            "value": templateMember.split('=', 1)[1]})
    if (not KTIsFound):
        IEBLogger.warn ("[[" + keyTemplate + "]]" + " not found in article " + "[[" + member["ruWikipediaArticleTitle"] + "]]");
        return False
    newTemplateConf = keyOpenTemplate + u"\n"
    for memberTplParams2FWP in templateParams:
        for tplWPParam in TemplateYouTubePersonWrongParams_list:
            if tplWPParam["name"] == memberTplParams2FWP["name"]:
                memberTplParams2FWP["name"] = tplWPParam["correctlyName"]
                isCorrected = True
    for index, memberTplParams in enumerate(templateParams):
        isFound = False
        for tplParam in TemplateYouTubePerson_list:
            if tplParam["name"] == memberTplParams["name"]:
                isFound = True
                break
        if not isFound:
            del templateParams[index]
            isRemNParams = True
    templateParams.sort (key = lambda listMember: sortByTemplate(listMember, TemplateYouTubePerson_list))
    curMaxLen = 0
    for memberData in templateParams:
        if curMaxLen < len(memberData["name"]):
            curMaxLen = len(memberData["name"])
        if curMaxLen > maxLen:
            curMaxLen = maxLen
    curMaxLen += minPaddingBefore
    for memberData in templateParams:
        i = 0
        spacePaddingBefore = ""
        while i < curMaxLen - len (memberData["name"]):
            spacePaddingBefore += paddingSymbol
            i += 1
        i = 0
        spacePaddingAfter = ""
        while i < minPaddingBefore:
            spacePaddingAfter += paddingSymbol
            i += 1
        newTemplateConf += u"| " + memberData["name"] + spacePaddingBefore + u"=" + spacePaddingAfter + memberData["value"] + u"\n"
    newTemplateConf += closeTemplate
    basePos = page.text.find(keyOpenTemplate)
    openedBrakets = 0
    i = basePos
    while True:
        isOpenBrakets = page.text[i] == openTemplate[0] and \
                        page.text[i+1] == openTemplate[1]
        isCloseBrakets = page.text[i] == closeTemplate[0] and \
                        page.text[i+1] == closeTemplate[1]
        if isOpenBrakets:
            openedBrakets += 1
            i += 1
        elif isCloseBrakets:
            openedBrakets -= 1
            i += 1
        i += 1
        isAllBraketsClosed = openedBrakets <= 0
        isIndexOverflow = i >= len(page.text)
        if isIndexOverflow or isAllBraketsClosed:
            break
    page.text = page.text[:basePos] + newTemplateConf + page.text[i:]
    saveDesc = u""
    saveDesc += saveDescPrefix
    if isRemNParams:
        saveDesc += saveDescStrBaseRemParamsNNTPL
    if isFormatted:
        saveDesc += saveDescStrBaseFormatParamsBTPL
        if isCorrected:
            saveDesc += saveDescAnd
    if isCorrected:
        saveDesc += saveDescStrBaseCorrectedParamsTPL
    if isFormatted or isCorrected:
        saveDesc += saveDescStrContentGC
    if isRemNParams or isFormatted or isCorrected:
        saveDesc += saveDescPointerTPL_GC + saveDescSeparator
    saveDesc += saveDescStrBaseUPD
    if len(member["data"]) > 1:
        saveDesc += saveDescStrUPDEndMany
    else:
        saveDesc += saveDescStrUPDEndOne
    for memberData in member["data"]:
        listOfChannelsToInvite += memberData["channelName"]
        if memberData != member["data"][-1]:
             listOfChannelsToInvite += saveDescSeparator
    saveDesc += listOfChannelsToInvite
    saveDesc = (saveDesc[:saveDescMaxLen-len(dots)] + dots) if len(saveDesc) > saveDescMaxLen else saveDesc
    IEBLogger.info ("Save description: " + saveDesc)
    page.save(saveDesc)
    return True
