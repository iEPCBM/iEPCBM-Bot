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
    
    **************************************************************************
    
    Program use GoogleAPI.
    GoogleAPIs Terms of Service - <https://developers.google.com/terms/>
    
    ***********************************************************************
    Note:
        Used Google's trade mark: YouTube
'''

# == GoogleAPI ключ == 
GoogleAPI_key_code = "AIzaSyAYPAswlVbs7fKoP0QFj6kazqzdLS9MJ9o" # Здесь всё прикрыто крестиками :P

# == Круглые числа ==
thousand = 1000
million  = 1000000
billion  = 1000000000

# == Логи. Они нужны для отладки == 
import logging
import datetime
import sys

logFormatter = logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
# IEB значит iEPCBM Bot
IEBLogger = logging.getLogger()
IEBLogger.setLevel(logging.DEBUG)

SH = logging.StreamHandler(sys.stdout)
SH.setLevel(logging.DEBUG)
SH.setFormatter(logFormatter)
IEBLogger.addHandler(SH)

FH = logging.FileHandler("{0}/{1}.log".format("logs", "logger("+datetime.datetime.now().strftime("%H-%M-%S %d-%m-%Y")+")"))
FH.setLevel(logging.DEBUG)
FH.setFormatter(logFormatter)
IEBLogger.addHandler(FH)

# === Форматирование логов ===
log_TitleSeparator = "===" # Для выделения основных стадий работы бота
cascadeStep = u"  " # При нулевом значении ("") отступы убираются совсем

# == Описание изменений ==
saveDescPrefix = u"Бот: " # То, что будет стоять в начале строки описания изменений
saveDescMaxLen = 255 # Максимально допустимая длина описания изменений
dots = u"…" # Символ(ы) для вставки в случае превышения максимально допустимой длины описания изменений
# Описание изменений для обновления количества просмотров и подписчиков
saveDescStrUPDEndMany = u"ов: " # Окончание для множественного числа
saveDescStrUPDEndOne = u"а "    # Окончание для единственного числа
saveDescStrBaseUPD = u"обновление статистики для канал"
# saveDescStrBaseSortedParamsBTPL = u"сортировка параметров"
saveDescStrBaseRemParamsNNTPL = u"удаление несуществующих параметров"
saveDescStrBaseFormatParamsBTPL = u"оформление "
saveDescStrBaseCorrectedParamsTPL = u"исправление "
saveDescStrContentGC = "содержимого "
# saveDescStrBaseAlignContent  = u"выравнивание значений"
saveDescPointerTPL_GC = u"в шаблоне о видеоблогере"
saveDescSeparator = u", "
saveDescAnd = u"и "

# == Шаблоны ==
openTemplate = u"{{" # Открытие шаблонов
closeTemplate = u"}}" # Закрытие шаблонов
nsTemplate = u"Шаблон:"

keyTemplate1 = u"YouTube персона" # Искомый шаблон 1
keyOpenTemplate1 = openTemplate + u"YouTube персона" # Открытие искомого шаблона 1

keyTemplate2 = u"Ютубер" # Искомый шаблон 2
keyOpenTemplate2 = openTemplate + u"Ютубер" # Открытие искомого шаблона 2

keyTemplate3 = u"Канал YouTube" # Искомый шаблон 3
keyOpenTemplate3 = openTemplate + u"Канал YouTube" # Открытие искомого шаблона 3

keyTemplate4 = u"Видеоблогеры" # Искомый шаблон 4
keyOpenTemplate4 = openTemplate + u"Видеоблогеры" # Открытие искомого шаблона 4

keyTemplate5 = u"Видеоблогер" # Искомый шаблон 5
keyOpenTemplate5 = openTemplate + u"Видеоблогер" # Открытие искомого шаблона 5

# === Форматирование содержимого шаблонов ===
prefixListMember = u"\n* " # Используется в случае, если в значении аргумента шаблона должен использоваться список
paddingSymbol = u" "; # То чем заполняется пространство между названием аргумента и символом "=" для выравнивания значений. Может использоваться пробел и табуляция (не рекомендую). При нулевом значении ("") отступы убираются совсем
minPaddingBefore = 1 # Минимальный отступ от названия аргумента до знака равенства (=)
minPaddingAfter = 1 # Минимальный отступ от знака равенства (=) до значения аргумента

# == Оформление чисел (согласно ВП:ОС) ==
billionsPostfix  = u" млрд" # Миллиарды
millionsPostfix  = u" млн"  # Миллионы
thousandsPostfix = u" тыс." # Тысячи

permissibleRoundedTo = 0.1  # Выводить дробную часть, если она больше или равна этому числу (см. postRound.py)

# == Временные квоты ==
wikiMinQuota = 3 # Минимальная квота на сохранение изменений в вики (в сек.)
GoogleAPI_MinQuota = 0.5 # Минимальная квота на получение данных о YouTube канале (в сек.)

# == Служебные строки. Для работы бота и оформления логов ==
NONAME      = "__NONAME__"
NONE        = "__NONE__"
UNKNOWN     = "__UNKNOWN__"
CURDATE     = "__CURDATE__"   # текущая дата (день, месяц, год)
CURMOUNTH   = "__CURMOUNTH__" # текущий месяц (месяц, год)
