# -*- coding: utf-8 -*-

'''
    iEPCBM Bot (YaLVA-B1) - Wikipedia bot
    Copyright (C) 2017-2019  Rishat Kagirov (iEPCBM)
    
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
'''

from bot_config import *

draft_prefix = u"Участник:IEPCBM Bot/Черновик/"

SubscriberCountAndViewCountList = [
    {
        "ruWikipediaArticleTitle"  : u"Шарий, Анатолий Анатольевич",
        "data"                     : [{
            "channelName"              : u"Анатолий Шарий",
            "channelID"                : u"UCVPYbobPRzz0SjinWekjUBw",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Big Russian Boss",
        "data"                     : [{
            "channelName"              : u"Big Russian Boss Show",
            "channelID"                : u"UCE5dBnwxi9DS7-Ff_VEnITA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"BadComedian",
        "data"                     : [{
            "channelName"              : u"BadComedian",
            "channelID"                : u"UC6cqazSR6CnVMClY0bJI0Lg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Ивангай",
        "data"                     : [{
            "channelName"              : u"Ивангай",
            "channelID"                : u"UCrFiA0hztL9e8zTi_qBuW4w",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Мэддисон, Илья",
        "data"                     : [{
            "channelName"              : u"Maddyblog",
            "channelID"                : u"UCylfxXlnvdvjP3CmfwJN_Jg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Иванов, Дмитрий Сергеевич (видеоблогер)",
        "data"                     : [{
            "channelName"              : u"kamikadzedead",
            "channelID"                : u"UCDbsY8C1eQJ5t6KBv9ds-ag",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Клэп, Катя",
        "data"                     : [{
            "channelName"              : u"TheKateClapp",
            "channelID"                : u"UCC83eap-hc6uFQHRJ2F2LNg",
            "postfix"                  : "TheKateClapp"
        },
        {
            "channelName"              : u"FoggyDisaster",
            "channelID"                : u"UCY_4S0Bb4o3DoPa-OifxA2g",
            "postfix"                  : "FoggyDisaster"
        }]
    },
    {
        
        "ruWikipediaArticleTitle"  : u"Голополосов, Максим Сергеевич",
        "data"                     : [{
            "channelName"              : u"AdamThomasMoran",
            "channelID"                : u"UC-27_Szq7BtHDoC0R2U0zxA",
            "postfix"                  : u"основной канал"
        },
        {
            "channelName"              : u"MoranDays",
            "channelID"                : u"UCHqibHqO1A1F66jHPvNmw_A",
            "postfix"                  : u"MoranDays"
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Соболев, Николай Юрьевич",
        "data"                     : [{
            "channelName"              : u"Rakamakafo",
            "channelID"                : u"UCtHimY-CLBNM_Rn79-T7ZQA",
            "postfix"                  : u"Rakamakafo"
        },
        {
            "channelName"              : u"SOBOLEV",
            "channelID"                : u"UCNb2BkmQu3IfQVcaPExHkvQ",
            "postfix"                  : u"SOBOLEV"
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Саша Спилберг",
        "data"                     : [{
            "channelName"              : u"Sasha Spilberg",
            "channelID"                : u"UCJatXmy5PyaZ6gFs-NEAFWQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Хованский, Юрий Михайлович",
        "data"                     : [{
            "channelName"              : u"Юрий Хованский",
            "channelID"                : u"UCnQBjLBbZ6TXMwM_D_iaXjQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"ЯнГо",
        "data"                     : [{
            "channelName"              : u"YanGo",
            "channelID"                : u"UCkpvU1ZMcg1RVxxvy8ng60w",
            "postfix"                  : NONE
        }]
    },
    {

        "ruWikipediaArticleTitle"  : u"Стримерша Карина",
        "data"                     : [{
            "channelName"              : u"СТРИМЕРША КАРИНА",
            "channelID"                : u"UCxgOetpLyBhtlVBQ70XfIAQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Boxxy",
        "data"                     : [{
            "channelName"              : u"boxxybabee",
            "channelID"                : u"UCzIiTeduaanyEboRfwJJznA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Джонсон, Рэй Уильям",
        "data"                     : [{
            "channelName"              : u"Ray William Johnson",
            "channelID"                : u"UCGt7X90Au6BV8rf49BiM6Dg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Smosh",
        "data"                     : [{
            "channelName"              : u"Smosh",
            "channelID"                : u"UCY30JRSgfhYXA6i6xX1erWg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"PewDiePie",
        "data"                     : [{
            "channelName"              : u"PewDiePie",
            "channelID"                : u"UC-lHJZR3Gqxm24_Vd_AJ5Yw",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Рома Жёлудь",
        "data"                     : [{
            "channelName"              : u"RomaAcorn",
            "channelID"                : u"UCmNvt3clEIdiTIKwCYbceuQ",
            "postfix"                  : NONE
        }]
    },
    
    # {
    # "ruWikipediaArticleTitle"  : draft_prefix,
    # "data"                     : [{
    #     "channelName"              : u"RomaAcorn",
    #     "channelID"                : u"UCmNvt3clEIdiTIKwCYbceuQ",
    #     "postfix"                  : NONE
    # }]
    # },
    
    {
        "ruWikipediaArticleTitle"  : u"Бизоньин, Марция",
        "data"                     : [{
            "channelName"              : u"Marzia",
            "channelID"                : u"UCe9oofjVfJzapRyVlt57x8Q",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Хауэлл, Дэн",
        "data"                     : [{
            "channelName"              : u"Daniel Howell",
            "channelID"                : u"UCGjylN-4QCpn8XJ1uY-UOgA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Ли, Каспар",
        "data"                     : [{
            "channelName"              : u"Caspar",
            "channelID"                : u"UCAaUVu8vYss8zCaC0WuA9jA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"HolaSoyGerman",
        "data"                     : [{
            "channelName"              : u"HolaSoyGerman.",
            "channelID"                : u"UCZJ7m7EnCNodqnu5SAtg8eQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Лестер, Фил",
        "data"                     : [{
            "channelName"              : u"AmazingPhil",
            "channelID"                : u"UCHUE4ypXKp7ZkmdWbGJNgJg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Батлер, Маркус",
        "data"                     : [{
            "channelName"              : u"Marcus Butler",
            "channelID"                : u"UCPeZTzsoQ4iBjfkVbU0ilmg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Франта, Коннор",
        "data"                     : [{
            "channelName"              : u"ConnorFranta",
            "channelID"                : u"UCudeRz9YntRrmKBSqnHyKGQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Найстет, Кейси",
        "data"                     : [{
            "channelName"              : u"CaseyNeistat",
            "channelID"                : u"UCtinbF-Q-fVthA0qrFQTgXQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Ларин, Дмитрий (видеоблогер)",
        "data"                     : [{
            "channelName"              : u"ЛАРИН",
            "channelID"                : u"UCEbpRAmSB6ZWMjyNTvpIkFA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"HowToBasic",
        "data"                     : [{
            "channelName"              : u"HowToBasic",
            "channelID"                : u"UCR4s1DE9J4DHzZYXMltSMAg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"El Rubius",
        "data"                     : [{
            "channelName"              : u"elrubiusOMG",
            "channelID"                : u"UCXazgXDIYyWH-yXLAkcrFxw",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Jacksepticeye",
        "data"                     : [{
            "channelName"              : u"jacksepticeye",
            "channelID"                : u"UCYzPXprvl5Y-Sf0g4vX-m6g",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"FattyPillow",
        "data"                     : [{
            "channelName"              : u"FattyPillowTV",
            "channelID"                : u"UC_c01No6K3fhgPafCUzEf6w",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Markiplier",
        "data"                     : [{
            "channelName"              : u"Markiplier",
            "channelID"                : u"UC7_YxT-KID8kRbqZo7MyscQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Nemagia",
        "data"                     : [{
            "channelName"              : u"NEMAGIA",
            "channelID"                : u"UCGJLJ7p4jWNwWDY4j9OY8QA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Дуглас, Джек",
        "data"                     : [{
            "channelName"              : u"jacksfilms",
            "channelID"                : u"UCPcFg7aBbaVzXoIKSNqwaww",
            "postfix"                  : u"jacksfilms"
        },
        {
            "channelName"              : u"jackisanerd",
            "channelID"                : u"UCTjqo_3046IXFFGZ_M5jedA",
            "postfix"                  : u"jackisanerd"
        },
        {
            "channelName"              : u"SHUTUPDENNIS",
            "channelID"                : u"UCl3NEjerkcJ-Y8IJmipL7vQ",
            "postfix"                  : u"SHUTUPDENNIS"
        },
        {
            "channelName"              : u"featuredfridays",
            "channelID"                : u"UCQ3_JVqgUgaCUMSegxqny5Q",
            "postfix"                  : u"featuredfridays"
        },]
    },
    {
        "ruWikipediaArticleTitle"  : u"Domics",
        "data"                     : [{
            "channelName"              : u"Domics",
            "channelID"                : u"UCn1XB-jvmd9fXMzhiA6IR0w",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Никифоров, Сергей Игоревич",
        "data"                     : [{
            "channelName"              : u"FC KEFIR",
            "channelID"                : u"UCQ2OQ6fnFHaz5-5eJ2mtgFQ",
            "postfix"                  : u"FC KEFIR"
        },
        {
            "channelName"              : u"7F United",
            "channelID"                : u"UCRUvktXBRiqzBh9L7o7fZTA",
            "postfix"                  : u"7F United"
        },
        {
            "channelName"              : u"KEFIR TV",
            "channelID"                : u"UCnoZovmZTEQhthY--JcKhcw",
            "postfix"                  : u"KEFIR TV"
        },]
    },
    {
        "ruWikipediaArticleTitle"  : u"Filthy Frank",
        "data"                     : [{
            "channelName"              : u"TVFilthyFrank",
            "channelID"                : u"UCkitABalXafr-NqceQdDXtg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Лиззка",
        "data"                     : [{
            "channelName"              : u"лиззка",
            "channelID"                : u"UC3XGNDKlaOvXRSMY9cGt6ig",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Пол, Джейк",
        "data"                     : [{
            "channelName"              : u"Jake Paul",
            "channelID"                : u"UCcgVECVN4OKV6DH1jLkqmcA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Лоули, Киан",
        "data"                     : [{
            "channelName"              : u"superkian13",
            "channelID"                : u"UCeTzt8EPd5KZn6ZYH07eUSA",
            "postfix"                  : u"основной канал"
        },
        {
            "channelName"              : u"KianAndJc",
            "channelID"                : u"UC_DptbqTndVt_Im3KkuIK5Q",
            "postfix"                  : u"KianAndJc"
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Стивенс, Майкл",
        "data"                     : [{
            "channelName"              : u"Vsauce",
            "channelID"                : u"UC6nSFpj9HTCZ5t-N3Rm3-HA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Франта, Коннор",
        "data"                     : [{
            "channelName"              : u"ConnorFranta",
            "channelID"                : u"UCudeRz9YntRrmKBSqnHyKGQ",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Ро, Марьяна",
        "data"                     : [{
            "channelName"              : u"Maryana Ro",
            "channelID"                : u"UCcGVrf54UcSyIFKlJic8T8A",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Little Big",
        "data"                     : [{
            "channelName"              : u"Little Big",
            "channelID"                : u"UCu7TZ_ATWgjgD9IrNLdnYDA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Киносита, Юка",
        "data"                     : [{
            "channelName"              : u"Yuka Kinoshita木下ゆうか",
            "channelID"                : u"UCFTVNLC7ysej-sD5lkLqNGA",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Пол, Логан",
        "data"                     : [{
            "channelName"              : u"Logan Paul Vlogs",
            "channelID"                : u"UCG8rbF3g2AMX70yOd8vqIZg",
            "postfix"                  : u"влоговый"
        },
        {
            "channelName"              : u"TheOfficialLoganPaul",
            "channelID"                : u"UCbwMZHCMpBiOWfYLBOH-9Qw",
            "postfix"                  : u"основной"
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Hype Camp",
        "data"                     : [{
            "channelName"              : u"HYPE CAMP",
            "channelID"                : u"UCPL81luS9t6s3Ro6U9pRdWg",
            "postfix"                  : NONE
        }]
    },
    {
        "ruWikipediaArticleTitle"  : u"Сливки шоу",
        "data"                     : [{
            "channelName"              : u"SlivkiShow",
            "channelID"                : u"UCU_yU4xGT9hrVFo6euH8LLw",
            "postfix"                  : NONE
        }]
    },
    # -------------- Тест --------------
    {
        "ruWikipediaArticleTitle"  : u"Успешная группа",
        "data"                     : [{
            "channelName"              : u"УСПЕШНАЯ ГРУППА",
            "channelID"                : u"UCF5LvuL3cqagGSw6WPTs_tg",
            "postfix"                  : NONE
        }]
    },
	{
        "ruWikipediaArticleTitle"  : u"ВДудь",
        "data"                     : [{
            "channelName"              : u"ВДудь",
            "channelID"                : u"UCMCgOm8GZkHp8zJ6l7_hIuA",
            "postfix"                  : NONE
        }]
    },
	{
        "ruWikipediaArticleTitle"  : u"Могилко, Марина Дмитриевна",
        "data"                     : [{
            "channelName"              : u"Marina Mogilko",
            "channelID"                : u"UCLJl8-mbCfolWMkh1F1qfjA",
            "postfix"                  : u"Marina Mogilko"
        },
		{
            "channelName"              : u"linguamarina",
            "channelID"                : u"UCAQg09FkoobmLquNNoO4ulg",
            "postfix"                  : u"linguamarina"
        },
		{
            "channelName"              : u"Silicon Valley Girl",
            "channelID"                : u"UCiq1FIgtEK7LRAOB1JXTPig",
            "postfix"                  : u"Silicon Valley Girl"
        }]
    },
	{
        "ruWikipediaArticleTitle"  : u"Адушкина, Катя",
        "data"                     : [{
            "channelName"              : u"Katya Adushkina",
            "channelID"                : u"UCA0Xum6Bxx-rhmrog1A1ISQ",
            "postfix"                  : NONE
        }]
    }
]
