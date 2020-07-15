# coding: utf-8

import pprint
import re

import six





class CorpBasicDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain': 'str',
        'phone': 'str',
        'country': 'str',
        'fax': 'str',
        'email': 'str',
        'address': 'str',
        'description': 'str',
        'sp_id': 'str',
        'language': 'str',
        'time_zone_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain': 'domain',
        'phone': 'phone',
        'country': 'country',
        'fax': 'fax',
        'email': 'email',
        'address': 'address',
        'description': 'description',
        'sp_id': 'spId',
        'language': 'language',
        'time_zone_id': 'timeZoneId'
    }

    def __init__(self, name=None, domain=None, phone=None, country='chinaPR', fax=None, email=None, address=None, description=None, sp_id=None, language='zh-CN', time_zone_id='56'):
        """CorpBasicDTO - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._domain = None
        self._phone = None
        self._country = None
        self._fax = None
        self._email = None
        self._address = None
        self._description = None
        self._sp_id = None
        self._language = None
        self._time_zone_id = None
        self.discriminator = None

        self.name = name
        if domain is not None:
            self.domain = domain
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if sp_id is not None:
            self.sp_id = sp_id
        if language is not None:
            self.language = language
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id

    @property
    def name(self):
        """Gets the name of this CorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\"'？?\\\\……/]*$

        :return: The name of this CorpBasicDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\"'？?\\\\……/]*$

        :param name: The name of this CorpBasicDTO.
        :type: str
        """
        self._name = name

    @property
    def domain(self):
        """Gets the domain of this CorpBasicDTO.

        企业域名

        :return: The domain of this CorpBasicDTO.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CorpBasicDTO.

        企业域名

        :param domain: The domain of this CorpBasicDTO.
        :type: str
        """
        self._domain = domain

    @property
    def phone(self):
        """Gets the phone of this CorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时， “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)

        :return: The phone of this CorpBasicDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时， “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)

        :param phone: The phone of this CorpBasicDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this CorpBasicDTO.

        手机号所属的国家, 如果国家为中国大陆则country参数取值为chinaPR,国家和国家码的对应关系如下chinaPR: +86(中国大陆); chinaHKG: +852（中国香港）; chinaOMA: +853(中国澳门);  chinaTPE: +886(中国台湾地区); BVl: +1284 (英属维尔京群岛); Bolivia: +591(玻利维亚); CZ: +420(捷克共和国); GB: +245(几内亚比绍); SVGrenadines: +1784(圣文森特和格林纳丁斯); TAT: +1868(特立尼达和多巴哥); UK: +44(英国); afghanistan: +93(阿富汗); albania: +355(阿尔巴尼亚); algeria: +213(阿尔及利亚); andorra: +376(安道尔共和国); angola: +244(安哥拉); argentina: +54(阿根廷); armenia: +374(亚美尼亚); australia: +61(澳大利亚); austria: +43(奥地利); azerbaijan: +994(阿塞拜疆); bahamas: +1242(巴哈马); bahrain: +973(巴林); bangladesh: +880(孟加拉国); belarus: +375(白俄罗斯); belgium: +32(比利时); belize: +501(伯利兹); benin: +229(贝宁); bosniaAndHerzegovina: +387(波斯尼亚和黑塞哥维那); botswana: +267(博茨瓦纳); brazil: +55(巴西); brunei: +673(文莱); bulgaria: +359(保加利亚); burkinaFaso: +226(布基纳法索); burundi: +257(布隆迪); cambodia: +855(柬埔寨); cameroon: +237(喀麦隆); canada: +1(加拿大); capeVerde: +238(佛得角); caymanIslands: +1345(开曼群岛); centralAfrican: +236(中非); chad: +235(乍得); chile: +56(智利);  columbia: +57(哥伦比亚); comoros: +269(科摩罗); congoB: +242(刚果.布); congoJ: +243(刚果.金); costarica: +506(哥斯达黎加); croatia: +385(克罗地亚); curacao: +599(库拉索岛); cyprus: +357(塞浦路斯); denmark: +45(丹麦); djibouti: +253(吉布提); dominica: +1809(多米尼加共和国); ecuador: +593(厄瓜多尔); egypt: +20(埃及); equatorialGuinea: +240(赤道几内亚); estonia: +372(爱沙尼亚); finland: +358(芬兰); france: +33(法国); gabon: +241(加蓬); gambia: +220(冈比亚); georgia: +995(格鲁吉亚); germany: +49(德国); ghana: +233(加纳); greece: +30(希腊); grenada: +1473(格林纳达); guatemala: +502(危地马拉); guinea: +224(几内亚); guyana: +592(圭亚那); honduras: +504(洪都拉斯); hungary: +36(匈牙利); india: +91(印度); indonesia: +62(印度尼西亚); iraq: +964(伊拉克); ireland: +353(爱尔兰); israel: +972( 以色列); italy: +39(意大利); ivoryCoast: +225(科特迪瓦); jamaica: +1876(牙买加); japan: +81(日本); jordan: +962(约旦); kazakhstan: +7(哈萨克斯坦); kenya: +254(肯尼亚); kosovo: +383(科索沃); kuwait: +965(科威特); kyrgyzstan: +996(吉尔吉斯斯坦); laos: +856(老挝); latvia: +371(拉脱维亚); lebanon: +961(黎巴嫩); lesotho: +266(莱索托); liberia: +231(利比里亚); libya: +218(利比亚); lithuania: +370(立陶宛); luxembourg: +352(卢森堡); macedonia: +389(马其顿); madagascar: +261(马达加斯加); malawi: +265(马拉维); malaysia: +60(马来西亚); maldives: +960(马尔代夫); mali: +223(马里); malta: +356(马耳他); mauritania: +222(毛里塔尼亚); mauritius: +230(毛里求斯); mexico: +52(墨西哥); moldova: +373(摩尔多瓦); mongolia: +976(蒙古); montenegro: +382 (黑山共和国); morocco: +212(摩洛哥); mozambique: +258(莫桑比克); myanmar: +95(缅甸); namibia: +264(纳米比亚); nepal: +977(尼泊尔); netherlands: +31(荷兰); newZealand: +64(新西兰); nicaragua: +505(尼加拉瓜); niger: +227(尼日尔); nigeria: +234(尼日利亚); norway: +47(挪威); oman: +968(阿曼); pakistan: +92(巴基斯坦); palestine: +970(巴勒斯坦); panama: +507(巴拿马); papuaNewGuinea: +675(巴布亚新几内亚); peru: +51(秘鲁); philippines: +63(菲律宾); poland: +48(波兰); portugal: +351(葡萄牙); puertoRico: +1787(波多黎各); qatar: +974(卡塔尔); romania: +40(罗马尼亚); russia: +7(俄罗斯); rwanda: +250(卢旺达); saintMartin: +590(圣马丁); salvatore: +503(萨尔瓦多); saudiArabia: +966(沙特阿拉伯); senegal: +221(塞内加尔); serbia: +381(塞尔维亚); seychelles: +248(塞舌尔); sierraLeone: +232(塞拉利昂); singapore: +65(新加坡); slovakia: +421(斯洛伐克); slovenia: +386(斯洛文尼亚); somalia: +252(索马里); southAfrica: +27(南非); southKorea: +82(韩国); spain: +34(西班牙); sriLanka: +94(斯里兰卡); suriname: +597(苏里南); swaziland: +268(斯威士兰); sweden: +46(瑞典); switzerland: +41(瑞士); tajikistan: +992(塔吉克斯坦); tanzania: +255(坦桑尼亚); thailand: +66(泰国); togo: +228(多哥); tunisia: +216(突尼斯); turkey: +90(土耳其); turkmenistan: +993(土库曼斯坦); uae: +971(阿联酋); uganda: +256(乌干达); ukraine: +380(乌克兰); uruguay: +598(乌拉圭); usa: +1(美国); uzbekistan: +998(乌兹别克斯坦); venezuela: +58(委内瑞拉); vietNam: +84(越南); yemen: +967(也门); zambia: +260(赞比亚); zimbabwe: +263(津巴布韦)

        :return: The country of this CorpBasicDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CorpBasicDTO.

        手机号所属的国家, 如果国家为中国大陆则country参数取值为chinaPR,国家和国家码的对应关系如下chinaPR: +86(中国大陆); chinaHKG: +852（中国香港）; chinaOMA: +853(中国澳门);  chinaTPE: +886(中国台湾地区); BVl: +1284 (英属维尔京群岛); Bolivia: +591(玻利维亚); CZ: +420(捷克共和国); GB: +245(几内亚比绍); SVGrenadines: +1784(圣文森特和格林纳丁斯); TAT: +1868(特立尼达和多巴哥); UK: +44(英国); afghanistan: +93(阿富汗); albania: +355(阿尔巴尼亚); algeria: +213(阿尔及利亚); andorra: +376(安道尔共和国); angola: +244(安哥拉); argentina: +54(阿根廷); armenia: +374(亚美尼亚); australia: +61(澳大利亚); austria: +43(奥地利); azerbaijan: +994(阿塞拜疆); bahamas: +1242(巴哈马); bahrain: +973(巴林); bangladesh: +880(孟加拉国); belarus: +375(白俄罗斯); belgium: +32(比利时); belize: +501(伯利兹); benin: +229(贝宁); bosniaAndHerzegovina: +387(波斯尼亚和黑塞哥维那); botswana: +267(博茨瓦纳); brazil: +55(巴西); brunei: +673(文莱); bulgaria: +359(保加利亚); burkinaFaso: +226(布基纳法索); burundi: +257(布隆迪); cambodia: +855(柬埔寨); cameroon: +237(喀麦隆); canada: +1(加拿大); capeVerde: +238(佛得角); caymanIslands: +1345(开曼群岛); centralAfrican: +236(中非); chad: +235(乍得); chile: +56(智利);  columbia: +57(哥伦比亚); comoros: +269(科摩罗); congoB: +242(刚果.布); congoJ: +243(刚果.金); costarica: +506(哥斯达黎加); croatia: +385(克罗地亚); curacao: +599(库拉索岛); cyprus: +357(塞浦路斯); denmark: +45(丹麦); djibouti: +253(吉布提); dominica: +1809(多米尼加共和国); ecuador: +593(厄瓜多尔); egypt: +20(埃及); equatorialGuinea: +240(赤道几内亚); estonia: +372(爱沙尼亚); finland: +358(芬兰); france: +33(法国); gabon: +241(加蓬); gambia: +220(冈比亚); georgia: +995(格鲁吉亚); germany: +49(德国); ghana: +233(加纳); greece: +30(希腊); grenada: +1473(格林纳达); guatemala: +502(危地马拉); guinea: +224(几内亚); guyana: +592(圭亚那); honduras: +504(洪都拉斯); hungary: +36(匈牙利); india: +91(印度); indonesia: +62(印度尼西亚); iraq: +964(伊拉克); ireland: +353(爱尔兰); israel: +972( 以色列); italy: +39(意大利); ivoryCoast: +225(科特迪瓦); jamaica: +1876(牙买加); japan: +81(日本); jordan: +962(约旦); kazakhstan: +7(哈萨克斯坦); kenya: +254(肯尼亚); kosovo: +383(科索沃); kuwait: +965(科威特); kyrgyzstan: +996(吉尔吉斯斯坦); laos: +856(老挝); latvia: +371(拉脱维亚); lebanon: +961(黎巴嫩); lesotho: +266(莱索托); liberia: +231(利比里亚); libya: +218(利比亚); lithuania: +370(立陶宛); luxembourg: +352(卢森堡); macedonia: +389(马其顿); madagascar: +261(马达加斯加); malawi: +265(马拉维); malaysia: +60(马来西亚); maldives: +960(马尔代夫); mali: +223(马里); malta: +356(马耳他); mauritania: +222(毛里塔尼亚); mauritius: +230(毛里求斯); mexico: +52(墨西哥); moldova: +373(摩尔多瓦); mongolia: +976(蒙古); montenegro: +382 (黑山共和国); morocco: +212(摩洛哥); mozambique: +258(莫桑比克); myanmar: +95(缅甸); namibia: +264(纳米比亚); nepal: +977(尼泊尔); netherlands: +31(荷兰); newZealand: +64(新西兰); nicaragua: +505(尼加拉瓜); niger: +227(尼日尔); nigeria: +234(尼日利亚); norway: +47(挪威); oman: +968(阿曼); pakistan: +92(巴基斯坦); palestine: +970(巴勒斯坦); panama: +507(巴拿马); papuaNewGuinea: +675(巴布亚新几内亚); peru: +51(秘鲁); philippines: +63(菲律宾); poland: +48(波兰); portugal: +351(葡萄牙); puertoRico: +1787(波多黎各); qatar: +974(卡塔尔); romania: +40(罗马尼亚); russia: +7(俄罗斯); rwanda: +250(卢旺达); saintMartin: +590(圣马丁); salvatore: +503(萨尔瓦多); saudiArabia: +966(沙特阿拉伯); senegal: +221(塞内加尔); serbia: +381(塞尔维亚); seychelles: +248(塞舌尔); sierraLeone: +232(塞拉利昂); singapore: +65(新加坡); slovakia: +421(斯洛伐克); slovenia: +386(斯洛文尼亚); somalia: +252(索马里); southAfrica: +27(南非); southKorea: +82(韩国); spain: +34(西班牙); sriLanka: +94(斯里兰卡); suriname: +597(苏里南); swaziland: +268(斯威士兰); sweden: +46(瑞典); switzerland: +41(瑞士); tajikistan: +992(塔吉克斯坦); tanzania: +255(坦桑尼亚); thailand: +66(泰国); togo: +228(多哥); tunisia: +216(突尼斯); turkey: +90(土耳其); turkmenistan: +993(土库曼斯坦); uae: +971(阿联酋); uganda: +256(乌干达); ukraine: +380(乌克兰); uruguay: +598(乌拉圭); usa: +1(美国); uzbekistan: +998(乌兹别克斯坦); venezuela: +58(委内瑞拉); vietNam: +84(越南); yemen: +967(也门); zambia: +260(赞比亚); zimbabwe: +263(津巴布韦)

        :param country: The country of this CorpBasicDTO.
        :type: str
        """
        self._country = country

    @property
    def fax(self):
        """Gets the fax of this CorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)

        :return: The fax of this CorpBasicDTO.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this CorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)

        :param fax: The fax of this CorpBasicDTO.
        :type: str
        """
        self._fax = fax

    @property
    def email(self):
        """Gets the email of this CorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\w-+]+(\\.[\\w-+]+)*@[\\w-]+(\\.[\\w-]+)*(\\.[\\w-]{1,})$)

        :return: The email of this CorpBasicDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\w-+]+(\\.[\\w-+]+)*@[\\w-]+(\\.[\\w-]+)*(\\.[\\w-]{1,})$)

        :param email: The email of this CorpBasicDTO.
        :type: str
        """
        self._email = email

    @property
    def address(self):
        """Gets the address of this CorpBasicDTO.

        地址

        :return: The address of this CorpBasicDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CorpBasicDTO.

        地址

        :param address: The address of this CorpBasicDTO.
        :type: str
        """
        self._address = address

    @property
    def description(self):
        """Gets the description of this CorpBasicDTO.

        备注

        :return: The description of this CorpBasicDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CorpBasicDTO.

        备注

        :param description: The description of this CorpBasicDTO.
        :type: str
        """
        self._description = description

    @property
    def sp_id(self):
        """Gets the sp_id of this CorpBasicDTO.

        仅在查询时返回

        :return: The sp_id of this CorpBasicDTO.
        :rtype: str
        """
        return self._sp_id

    @sp_id.setter
    def sp_id(self, sp_id):
        """Sets the sp_id of this CorpBasicDTO.

        仅在查询时返回

        :param sp_id: The sp_id of this CorpBasicDTO.
        :type: str
        """
        self._sp_id = sp_id

    @property
    def language(self):
        """Gets the language of this CorpBasicDTO.

        企业提示音语言设置,zh-CN或en-US

        :return: The language of this CorpBasicDTO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CorpBasicDTO.

        企业提示音语言设置,zh-CN或en-US

        :param language: The language of this CorpBasicDTO.
        :type: str
        """
        self._language = language

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this CorpBasicDTO.

        时区Id设置,例如北京东8区timeZoneId值为56,时区Id和时区的对应关系如下:   1代表(GMT-12:00) Eniwetok, Kwajalein/(GMT-12:00) 埃尼威托克, 夸贾林   2代表(GMT-11:00) Midway Island, Samoa/(GMT-11:00) 中途岛, 萨摩亚群岛   3代表(GMT-10:00) Hawaii/(GMT-10:00) 夏威夷   4代表(GMT-09:00) Alaska/(GMT-09:00) 阿拉斯加   5代表(GMT-08:00) Pacific Time(US&Canada);Tijuana/(GMT-08:00) 太平洋时间（美国和加拿大）;蒂华纳   6代表(GMT-07:00) Arizona/(GMT-07:00) 亚利桑那州   7代表(GMT-07:00) Mountain Time(US&Canada)/(GMT-07:00) 山地时间（美国和加拿大）   8代表(GMT-06:00) Central America/(GMT-06:00) 中美洲   9代表(GMT-06:00) Central Time(US&Canada)/(GMT-06:00) 中部标准时间（美国和加拿大）   10代表(GMT-06:00) Mexico City/(GMT-06:00) 墨西哥城   11代表(GMT-06:00) Saskatchewan/(GMT-06:00) 萨斯喀彻温   12代表(GMT-05:00) Bogota, Lima, Quito/(GMT-05:00) 波哥大, 利马, 基多   13代表(GMT-05:00) Eastern Time(US&Canada)/(GMT-05:00) 东部时间（美国和加拿大）   14代表(GMT-05:00) Indiana(East)/(GMT-05:00) 印地安那州（东部）   15代表(GMT-04:00) Atlantic time(Canada)/(GMT-04:00) 大西洋时间（加拿大）   16代表(GMT-04:00) Caracas, La Paz/(GMT-04:00) 加拉加斯, 拉巴斯   17代表(GMT-04:00) Santiago/(GMT-04:00) 圣地亚哥   18代表(GMT-03:30) Newfoundland/(GMT-03:30) 纽芬兰   19代表(GMT-03:00) Brasilia/(GMT-03:00) 巴西利亚   20代表(GMT-03:00) Buenos Aires, Georgetown/(GMT-03:00) 布宜诺斯艾利斯, 乔治敦   21代表(GMT-03:00) Greenland/(GMT-03:00) 格陵兰   22代表(GMT-02:00) Mid-Atlantic/(GMT-02:00) 中大西洋   23代表(GMT-01:00) Azores/(GMT-01:00) 亚速尔群岛   24代表(GMT-01:00) Cape Verde Is./(GMT-01:00) 佛得角群岛   25代表(GMT) Casablanca, Monrovia/(GMT) 卡萨布兰卡, 蒙罗维亚   26代表(GMT) Greenwich Mean Time:Dublin, Edinburgh, Lisbon, London/(GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦   27代表(GMT+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna/(GMT+01:00) 阿姆斯特丹, 柏林, 伯尔尼, 罗马, 斯德哥尔摩, 维也纳   28代表(GMT+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague/(GMT+01:00) 贝尔格莱德, 布拉迪斯拉发, 布达佩斯, 卢布尔雅那, 布拉格   29代表(GMT+01:00) Brussels, Copenhagen, Madrid, Paris/(GMT+01:00) 布鲁塞尔, 哥本哈根, 马德里, 巴黎   30代表(GMT+01:00) Sarajevo, Skopje, Sofija, Warsaw, Zagreb/(GMT+01:00) 萨拉热窝, 斯科普里, 索菲娅, 华沙, 萨格勒布   31代表(GMT+01:00) West Central Africa/(GMT+01:00) 中非西部   32代表(GMT+02:00) Athens, Vilnius/(GMT+02:00) 雅典, 维尔纽斯   33代表(GMT+02:00) Bucharest/(GMT+02:00) 布加勒斯特   34代表(GMT+02:00) Cairo/(GMT+02:00) 开罗   35代表(GMT+02:00) Harare, Pretoria/(GMT+02:00) 哈拉雷, 比勒陀利亚   36代表(GMT+02:00) Helsinki, Riga, Tallinn/(GMT+02:00) 赫尔辛基, 里加, 塔林   37代表(GMT+02:00) Jerusalem/(GMT+02:00) 耶路撒冷   38代表(GMT+03:00) Baghdad, Minsk/(GMT+03:00) 巴格达, 明斯克市   39代表(GMT+03:00) Kuwait, Riyadh/(GMT+03:00) 科威特, 利雅得   40(GMT+03:00) Moscow, St. Petersburg/(GMT+03:00) 莫斯科, 圣彼得堡   41代表(GMT+03:00) Nairobi, Istanbul/(GMT+03:00) 内罗毕, 伊斯坦布尔   42代表(GMT+03:30) Tehran/(GMT+03:30) 德黑兰   43代表(GMT+04:00) Abu Dhabi, Muscat, Volgograd/(GMT+04:00) 阿布达比, 马斯喀特, 伏尔加格勒   44代表(GMT+04:00) Baku, Tbilisi, Yerevan/(GMT+04:00) 巴库, 第比利斯, 埃里温   45代表(GMT+04:30) Kabul/(GMT+04:30) 喀布尔   46代表(GMT+05:00) Ekaterinburg/(GMT+05:00) 叶卡捷林堡   47代表(GMT+05:00) Islamabad, Karachi, Tashkent/(GMT+05:00) 伊斯兰堡, 卡拉奇, 塔什干   48代表(GMT+05:30) Calcutta, Chennai, Mumbai, New Delhi/(GMT+05:30) 加尔各答, 钦奈, 孟买, 新德里   49代表(GMT+05:45) Kathmandu/(GMT+05:45) 加德满都   50代表(GMT+06:00) Almaty/(GMT+06:00) 阿拉木图   51代表(GMT+06:00) Astana, Dhaka/(GMT+06:00) 阿斯塔纳, 达卡   52代表(GMT+05:30) Sri Jayawardenepura/(GMT+05:30) 斯里贾亚瓦登普拉   53代表(GMT+06:30) Rangoon/(GMT+06:30) 仰光   54代表(GMT+07:00) Bangkok, Hanoi, Jakarta/(GMT+07:00) 曼谷, 河内, 雅加达   55代表(GMT+07:00) Novosibirsk, Krasnoyarsk/(GMT+07:00) 新西伯利亚, 克拉斯诺亚尔斯克   56代表(GMT+08:00) Beijing, Chongqing, Hong Kong, Urumqi, Taipei/(GMT+08:00) 北京, 重庆, 香港特别行政区, 乌鲁木齐, 台北   57代表(GMT+08:00) Ulaan Bataar/(GMT+08:00) 乌兰巴托   58代表(GMT+08:00) Kuala Lumpur, Singapore/(GMT+08:00) 吉隆坡, 新加坡   59代表(GMT+08:00) Perth/(GMT+08:00) 珀斯   60代表(GMT+09:00) Osaka, Sapporo, Tokyo/(GMT+09:00) 大阪, 札幌, 东京   61代表(GMT+09:00) Seoul/(GMT+09:00) 首尔   62代表(GMT+09:00) Yakutsk/(GMT+09:00) 雅库茨克   63代表(GMT+09:30) Adelaide/(GMT+09:30) 阿德莱德   64代表(GMT+09:30) Darwin/(GMT+09:30) 达尔文   65代表(GMT+10:00) Brisbane/(GMT+10:00) 布利斯班   66代表(GMT+10:00) Canberra, Melbourne, Sydney/(GMT+10:00) 堪培拉, 墨尔本, 悉尼    67代表(GMT+10:00) Guam, Port Moresby/(GMT+10:00) 关岛, 莫尔兹比港   68代表(GMT+10:00) Hobart/(GMT+10:00) 霍巴特   69代表(GMT+10:00) Vladivostok/(GMT+10:00) 海参威   70代表(GMT+11:00) Magadan, Solomon Is., New Caledonia/(GMT+11:00) 马加丹, 所罗门群岛, 新喀里多尼亚   71代表(GMT+12:00) Auckland, Welington/(GMT+12:00) 奥克兰, 惠灵顿   72代表(GMT+12:00) Fiji/(GMT+12:00) 斐济   73代表(GMT+13:00) Nuku'alofa/(GMT+13:00) 努库阿洛法   74代表(GMT+08:00) Irkutsk/(GMT+08:00) 伊尔库次克   75代表(GMT) Casablanca/(GMT) 卡萨布兰卡   76代表(GMT+04:00) Baku/(GMT+04:00) 巴库   77代表(GMT+12:00) Kamchatka, Marshall Is./(GMT+12:00) 堪察加半岛, 马绍尔群岛

        :return: The time_zone_id of this CorpBasicDTO.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this CorpBasicDTO.

        时区Id设置,例如北京东8区timeZoneId值为56,时区Id和时区的对应关系如下:   1代表(GMT-12:00) Eniwetok, Kwajalein/(GMT-12:00) 埃尼威托克, 夸贾林   2代表(GMT-11:00) Midway Island, Samoa/(GMT-11:00) 中途岛, 萨摩亚群岛   3代表(GMT-10:00) Hawaii/(GMT-10:00) 夏威夷   4代表(GMT-09:00) Alaska/(GMT-09:00) 阿拉斯加   5代表(GMT-08:00) Pacific Time(US&Canada);Tijuana/(GMT-08:00) 太平洋时间（美国和加拿大）;蒂华纳   6代表(GMT-07:00) Arizona/(GMT-07:00) 亚利桑那州   7代表(GMT-07:00) Mountain Time(US&Canada)/(GMT-07:00) 山地时间（美国和加拿大）   8代表(GMT-06:00) Central America/(GMT-06:00) 中美洲   9代表(GMT-06:00) Central Time(US&Canada)/(GMT-06:00) 中部标准时间（美国和加拿大）   10代表(GMT-06:00) Mexico City/(GMT-06:00) 墨西哥城   11代表(GMT-06:00) Saskatchewan/(GMT-06:00) 萨斯喀彻温   12代表(GMT-05:00) Bogota, Lima, Quito/(GMT-05:00) 波哥大, 利马, 基多   13代表(GMT-05:00) Eastern Time(US&Canada)/(GMT-05:00) 东部时间（美国和加拿大）   14代表(GMT-05:00) Indiana(East)/(GMT-05:00) 印地安那州（东部）   15代表(GMT-04:00) Atlantic time(Canada)/(GMT-04:00) 大西洋时间（加拿大）   16代表(GMT-04:00) Caracas, La Paz/(GMT-04:00) 加拉加斯, 拉巴斯   17代表(GMT-04:00) Santiago/(GMT-04:00) 圣地亚哥   18代表(GMT-03:30) Newfoundland/(GMT-03:30) 纽芬兰   19代表(GMT-03:00) Brasilia/(GMT-03:00) 巴西利亚   20代表(GMT-03:00) Buenos Aires, Georgetown/(GMT-03:00) 布宜诺斯艾利斯, 乔治敦   21代表(GMT-03:00) Greenland/(GMT-03:00) 格陵兰   22代表(GMT-02:00) Mid-Atlantic/(GMT-02:00) 中大西洋   23代表(GMT-01:00) Azores/(GMT-01:00) 亚速尔群岛   24代表(GMT-01:00) Cape Verde Is./(GMT-01:00) 佛得角群岛   25代表(GMT) Casablanca, Monrovia/(GMT) 卡萨布兰卡, 蒙罗维亚   26代表(GMT) Greenwich Mean Time:Dublin, Edinburgh, Lisbon, London/(GMT) 格林威治标准时间:都柏林, 爱丁堡, 里斯本, 伦敦   27代表(GMT+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna/(GMT+01:00) 阿姆斯特丹, 柏林, 伯尔尼, 罗马, 斯德哥尔摩, 维也纳   28代表(GMT+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague/(GMT+01:00) 贝尔格莱德, 布拉迪斯拉发, 布达佩斯, 卢布尔雅那, 布拉格   29代表(GMT+01:00) Brussels, Copenhagen, Madrid, Paris/(GMT+01:00) 布鲁塞尔, 哥本哈根, 马德里, 巴黎   30代表(GMT+01:00) Sarajevo, Skopje, Sofija, Warsaw, Zagreb/(GMT+01:00) 萨拉热窝, 斯科普里, 索菲娅, 华沙, 萨格勒布   31代表(GMT+01:00) West Central Africa/(GMT+01:00) 中非西部   32代表(GMT+02:00) Athens, Vilnius/(GMT+02:00) 雅典, 维尔纽斯   33代表(GMT+02:00) Bucharest/(GMT+02:00) 布加勒斯特   34代表(GMT+02:00) Cairo/(GMT+02:00) 开罗   35代表(GMT+02:00) Harare, Pretoria/(GMT+02:00) 哈拉雷, 比勒陀利亚   36代表(GMT+02:00) Helsinki, Riga, Tallinn/(GMT+02:00) 赫尔辛基, 里加, 塔林   37代表(GMT+02:00) Jerusalem/(GMT+02:00) 耶路撒冷   38代表(GMT+03:00) Baghdad, Minsk/(GMT+03:00) 巴格达, 明斯克市   39代表(GMT+03:00) Kuwait, Riyadh/(GMT+03:00) 科威特, 利雅得   40(GMT+03:00) Moscow, St. Petersburg/(GMT+03:00) 莫斯科, 圣彼得堡   41代表(GMT+03:00) Nairobi, Istanbul/(GMT+03:00) 内罗毕, 伊斯坦布尔   42代表(GMT+03:30) Tehran/(GMT+03:30) 德黑兰   43代表(GMT+04:00) Abu Dhabi, Muscat, Volgograd/(GMT+04:00) 阿布达比, 马斯喀特, 伏尔加格勒   44代表(GMT+04:00) Baku, Tbilisi, Yerevan/(GMT+04:00) 巴库, 第比利斯, 埃里温   45代表(GMT+04:30) Kabul/(GMT+04:30) 喀布尔   46代表(GMT+05:00) Ekaterinburg/(GMT+05:00) 叶卡捷林堡   47代表(GMT+05:00) Islamabad, Karachi, Tashkent/(GMT+05:00) 伊斯兰堡, 卡拉奇, 塔什干   48代表(GMT+05:30) Calcutta, Chennai, Mumbai, New Delhi/(GMT+05:30) 加尔各答, 钦奈, 孟买, 新德里   49代表(GMT+05:45) Kathmandu/(GMT+05:45) 加德满都   50代表(GMT+06:00) Almaty/(GMT+06:00) 阿拉木图   51代表(GMT+06:00) Astana, Dhaka/(GMT+06:00) 阿斯塔纳, 达卡   52代表(GMT+05:30) Sri Jayawardenepura/(GMT+05:30) 斯里贾亚瓦登普拉   53代表(GMT+06:30) Rangoon/(GMT+06:30) 仰光   54代表(GMT+07:00) Bangkok, Hanoi, Jakarta/(GMT+07:00) 曼谷, 河内, 雅加达   55代表(GMT+07:00) Novosibirsk, Krasnoyarsk/(GMT+07:00) 新西伯利亚, 克拉斯诺亚尔斯克   56代表(GMT+08:00) Beijing, Chongqing, Hong Kong, Urumqi, Taipei/(GMT+08:00) 北京, 重庆, 香港特别行政区, 乌鲁木齐, 台北   57代表(GMT+08:00) Ulaan Bataar/(GMT+08:00) 乌兰巴托   58代表(GMT+08:00) Kuala Lumpur, Singapore/(GMT+08:00) 吉隆坡, 新加坡   59代表(GMT+08:00) Perth/(GMT+08:00) 珀斯   60代表(GMT+09:00) Osaka, Sapporo, Tokyo/(GMT+09:00) 大阪, 札幌, 东京   61代表(GMT+09:00) Seoul/(GMT+09:00) 首尔   62代表(GMT+09:00) Yakutsk/(GMT+09:00) 雅库茨克   63代表(GMT+09:30) Adelaide/(GMT+09:30) 阿德莱德   64代表(GMT+09:30) Darwin/(GMT+09:30) 达尔文   65代表(GMT+10:00) Brisbane/(GMT+10:00) 布利斯班   66代表(GMT+10:00) Canberra, Melbourne, Sydney/(GMT+10:00) 堪培拉, 墨尔本, 悉尼    67代表(GMT+10:00) Guam, Port Moresby/(GMT+10:00) 关岛, 莫尔兹比港   68代表(GMT+10:00) Hobart/(GMT+10:00) 霍巴特   69代表(GMT+10:00) Vladivostok/(GMT+10:00) 海参威   70代表(GMT+11:00) Magadan, Solomon Is., New Caledonia/(GMT+11:00) 马加丹, 所罗门群岛, 新喀里多尼亚   71代表(GMT+12:00) Auckland, Welington/(GMT+12:00) 奥克兰, 惠灵顿   72代表(GMT+12:00) Fiji/(GMT+12:00) 斐济   73代表(GMT+13:00) Nuku'alofa/(GMT+13:00) 努库阿洛法   74代表(GMT+08:00) Irkutsk/(GMT+08:00) 伊尔库次克   75代表(GMT) Casablanca/(GMT) 卡萨布兰卡   76代表(GMT+04:00) Baku/(GMT+04:00) 巴库   77代表(GMT+12:00) Kamchatka, Marshall Is./(GMT+12:00) 堪察加半岛, 马绍尔群岛

        :param time_zone_id: The time_zone_id of this CorpBasicDTO.
        :type: str
        """
        self._time_zone_id = time_zone_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CorpBasicDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
