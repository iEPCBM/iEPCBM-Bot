# -*- coding: utf-8 -*-

'''
    iEPCBM Bot (YaLVA-B1) - Wikipedia bot
    Copyright (C) 2017  Rishat Kagirov (iEPCBM)
    
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
    
    ***********************************************************************
    Note:
        Used Google's trade mark: YouTube
'''

from bot_config import *

TemplateYouTubePerson_list = [
    {"name": u"имя"},
    {"name": u"место_жительства"},
    {"name": u"изображение"},
    {"name": u"размер_изображения"},
    {"name": u"alt"},
    {"name": u"описание_изображения"},
    {"name": u"описание"},
    {"name": u"подпись"},
    {"name": u"имя_при_рождении"},
    {"name": u"дата_рождения"},
    {"name": u"место_рождения"},
    {"name": u"место_смерти"},
    {"name": u"дата_смерти"},
    {"name": u"проживание"},
    {"name": u"происхождение"},
    {"name": u"рост"},
    {"name": u"вес"},
    {"name": u"национальность"},
    {"name": u"местонахождение"},
    {"name": u"род_деятельности"},
    {"name": u"род_занятий"},
    {"name": u"религия"},
    {"name": u"веб-сайт"},
    {"name": u"ссылка"},
    {"name": u"URL"},
    {"name": u"псевдоним"},
    {"name": u"название_канала"},
    {"name": u"ссылка_на_канал"},
    {"name": u"создатель"},
    {"name": u"дата_создания"},
    {"name": u"годы_активности"},
    {"name": u"псевдонимы"},
    {"name": u"жанр"},
    #===============================#\
    {"name": u"подписчики"},        ##\
    {"name": u"подписчики_дата"},   ###\ Обновляемые
    {"name": u"просмотры"},         ###/ данные
    {"name": u"просмотры_дата"},    ##/
    #===============================#/
    {"name": u"сеть"},
    {"name": u"коллективы"},
    {"name": u"коронные_фразы"},
    {"name": u"почетный_префикс"},
    {"name": u"почетный_суффикс"},
    {"name": u"раскрыть"},
    {"name": u"серебряная_кнопка"},
    {"name": u"серебряная_кнопка_год"},
    {"name": u"золотая_кнопка"},
    {"name": u"золотая_кнопка_год"},
    {"name": u"бриллиантовая_кнопка"},
    {"name": u"бриллиантовая_кнопка_год"},
    {"name": u"рубиновая_кнопка"},
    {"name": u"рубиновая_кнопка_год"},
    {"name": u"статистика_обновлена"}, # Это тоже обновляемые данные
    {"name": u"дополнительная_информация"}
]

TemplateYouTubePersonWrongParams_list = [
    {
        "name":          u"размер изображения",
        "correctlyName": u"размер_изображения"
    },
    {
        "name":          u"image size",
        "correctlyName": u"imagesize"
    },
    {
        "name":          u"описание изображения",
        "correctlyName": u"описание_изображения"
    },
    {
        "name":          u"имя при_рождении",
        "correctlyName": u"имя_при_рождении",
    },
    {
        "name":          u"имя_при рождении",
        "correctlyName": u"имя_при_рождении",
    },
    {
        "name":          u"имя при рождении",
        "correctlyName": u"имя_при_рождении",
    },
    {
        "name":          u"дата рождения",
        "correctlyName": u"дата_рождения",
    },
    {
        "name":          u"место рождения",
        "correctlyName": u"место_рождения",
    },
    {
        "name":          u"дата смерти",
        "correctlyName": u"дата_смерти",
    },
    {
        "name":          u"место смерти",
        "correctlyName": u"место_смерти",
    },
    {
        "name":          u"род деятельности",
        "correctlyName": u"род_деятельности",
    },
    {
        "name":          u"род занятий",
        "correctlyName": u"род_занятий",
    },
    {
        "name":          u"веб сайт",
        "correctlyName": u"веб-сайт",
    },
    {
        "name":          u"веб_сайт",
        "correctlyName": u"веб-сайт",
    },
    {
        "name":          u"название канала",
        "correctlyName": u"название_канала",
    },
    {
        "name":          u"ссылка на_канал",
        "correctlyName": u"ссылка_на_канал",
    },
    {
        "name":          u"ссылка_на канал",
        "correctlyName": u"ссылка_на_канал",
    },
    {
        "name":          u"ссылка на канал",
        "correctlyName": u"ссылка_на_канал",
    },
    {
        "name":          u"годы активности",
        "correctlyName": u"годы_активности",
    },
    {
        "name":          u"годыактивности",
        "correctlyName": u"годы_активности",
    },
    {
        "name":          u"подписчики дата",
        "correctlyName": u"подписчики_дата",
    },
    {
        "name":          u"просмотры дата",
        "correctlyName": u"просмотры_дата",
    },
    {
        "name":          u"коронные фразы",
        "correctlyName": u"коронные_фразы",
    },
    {
        "name":          u"почетный префикс",
        "correctlyName": u"почетный_префикс",
    },
    {
        "name":          u"почетный суффикс",
        "correctlyName": u"почетный_суффикс",
    },
    {
        "name":          u"серебряная кнопка",
        "correctlyName": u"серебряная_кнопка",
    },
    {
        "name":          u"серебряная кнопка_год",
        "correctlyName": u"серебряная_кнопка_год",
    },
    {
        "name":          u"серебряная_кнопка год",
        "correctlyName": u"серебряная_кнопка_год",
    },
    {
        "name":          u"серебряная кнопка год",
        "correctlyName": u"серебряная_кнопка_год",
    },
    {
        "name":          u"золотая кнопка",
        "correctlyName": u"золотая_кнопка",
    },
    {
        "name":          u"золотая кнопка_год",
        "correctlyName": u"золотая_кнопка_год",
    },
    {
        "name":          u"золотая_кнопка год",
        "correctlyName": u"золотая_кнопка_год",
    },
    {
        "name":          u"золотая кнопка год",
        "correctlyName": u"золотая_кнопка_год",
    },
    {
        "name":          u"бриллиантовая кнопка",
        "correctlyName": u"бриллиантовая_кнопка",
    },
    {
        "name":          u"бриллиантовая кнопка_год",
        "correctlyName": u"бриллиантовая_кнопка_год",
    },
    {
        "name":          u"бриллиантовая_кнопка год",
        "correctlyName": u"бриллиантовая_кнопка_год",
    },
    {
        "name":          u"бриллиантовая кнопка год",
        "correctlyName": u"бриллиантовая_кнопка_год",
    },
    {
        "name":          u"рубиновая кнопка",
        "correctlyName": u"рубиновая_кнопка",
    },
    {
        "name":          u"рубиновая кнопка_год",
        "correctlyName": u"рубиновая_кнопка_год",
    },
    {
        "name":          u"рубиновая_кнопка год",
        "correctlyName": u"рубиновая_кнопка_год",
    },
    {
        "name":          u"рубиновая кнопка год",
        "correctlyName": u"рубиновая_кнопка_год",
    },
    {
        "name":          u"статистика обновлена",
        "correctlyName": u"статистика_обновлена",
    },
    {
        "name":          u"дополнительная информация",
        "correctlyName": u"дополнительная_информация",
    },
]

TemplateYouTubePerson_list_used = [
    {
        "name": u"подписчики",
        "idToGetVal": "strRSubscriberCount",
        "relativeMemName": u"подписчики_дата",
        "idToCheck": NONE,
        "relativeMemIndex": 1
    },
    {
        "name": u"подписчики_дата",
        "idToGetVal": CURMOUNTH,
        "relativeMemName": u"подписчики",
        "idToCheck": "strRSubscriberCount",
        "relativeMemIndex": 0
    },
    {
        "name": u"просмотры",
        "idToGetVal": "strRViewCount",
        "relativeMemName": u"просмотры_дата",
        "idToCheck": NONE,
        "relativeMemIndex": 3
    },
    {
        "name": u"просмотры_дата",
        "idToGetVal": CURMOUNTH,
        "relativeMemName": u"просмотры",
        "idToCheck": "strRViewCount",
        "relativeMemIndex": 2
    },
    {
        "name": u"статистика_обновлена",
        "idToGetVal": CURDATE,
        "relativeMemName": NONE,
        "idToCheck": NONE,
        "relativeMemIndex": NONE
    }
]

TemplateYouTubePerson_list_used_names = [
    u"подписчики",
    u"подписчики_дата",
    u"просмотры",
    u"просмотры_дата",
    u"статистика_обновлена"
]

maxLen = 49
