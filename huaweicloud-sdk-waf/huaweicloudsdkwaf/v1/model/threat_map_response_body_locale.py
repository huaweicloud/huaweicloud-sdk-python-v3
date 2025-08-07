# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThreatMapResponseBodyLocale:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmdi': 'str',
        'llm_prompt_injection': 'str',
        'anticrawler': 'str',
        'custom_custom': 'str',
        'third_bot_river': 'str',
        'robot': 'str',
        'custom_idc_ip': 'str',
        'antiscan_dir_traversal': 'str',
        'advanced_bot': 'str',
        'xss': 'str',
        'antiscan_high_freq_scan': 'str',
        'webshell': 'str',
        'cc': 'str',
        'botm': 'str',
        'illegal': 'str',
        'llm_prompt_sensitive': 'str',
        'sqli': 'str',
        'lfi': 'str',
        'antitamper': 'str',
        'custom_geoip': 'str',
        'rfi': 'str',
        'vuln': 'str',
        'llm_response_sensitive': 'str',
        'custom_whiteblackip': 'str',
        'leakage': 'str'
    }

    attribute_map = {
        'cmdi': 'cmdi',
        'llm_prompt_injection': 'llm_prompt_injection',
        'anticrawler': 'anticrawler',
        'custom_custom': 'custom_custom',
        'third_bot_river': 'third_bot_river',
        'robot': 'robot',
        'custom_idc_ip': 'custom_idc_ip',
        'antiscan_dir_traversal': 'antiscan_dir_traversal',
        'advanced_bot': 'advanced_bot',
        'xss': 'xss',
        'antiscan_high_freq_scan': 'antiscan_high_freq_scan',
        'webshell': 'webshell',
        'cc': 'cc',
        'botm': 'botm',
        'illegal': 'illegal',
        'llm_prompt_sensitive': 'llm_prompt_sensitive',
        'sqli': 'sqli',
        'lfi': 'lfi',
        'antitamper': 'antitamper',
        'custom_geoip': 'custom_geoip',
        'rfi': 'rfi',
        'vuln': 'vuln',
        'llm_response_sensitive': 'llm_response_sensitive',
        'custom_whiteblackip': 'custom_whiteblackip',
        'leakage': 'leakage'
    }

    def __init__(self, cmdi=None, llm_prompt_injection=None, anticrawler=None, custom_custom=None, third_bot_river=None, robot=None, custom_idc_ip=None, antiscan_dir_traversal=None, advanced_bot=None, xss=None, antiscan_high_freq_scan=None, webshell=None, cc=None, botm=None, illegal=None, llm_prompt_sensitive=None, sqli=None, lfi=None, antitamper=None, custom_geoip=None, rfi=None, vuln=None, llm_response_sensitive=None, custom_whiteblackip=None, leakage=None):
        r"""ThreatMapResponseBodyLocale

        The model defined in huaweicloud sdk

        :param cmdi: **参数解释：** 命令注入攻击，攻击者通过注入恶意命令来执行非授权操作 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cmdi: str
        :param llm_prompt_injection: **参数解释：** 大模型提示词注入攻击，攻击者通过构造特殊输入来篡改AI模型的提示词 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type llm_prompt_injection: str
        :param anticrawler: **参数解释：** 网站反爬虫策略，用于阻止自动化程序非法获取网站内容 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type anticrawler: str
        :param custom_custom: **参数解释：** 精准防护，基于特定规则的定制化安全防护策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_custom: str
        :param third_bot_river: **参数解释：** 第三方BOT，来自第三方服务的自动化交互程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type third_bot_river: str
        :param robot: **参数解释：** 恶意爬虫，用于非法获取数据或进行攻击的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type robot: str
        :param custom_idc_ip: **参数解释：** IDC情报，基于数据中心IP地址的威胁情报 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_idc_ip: str
        :param antiscan_dir_traversal: **参数解释：** 目录遍历防护，防止攻击者通过目录遍历访问系统文件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type antiscan_dir_traversal: str
        :param advanced_bot: **参数解释：** 高级BOT，具有复杂行为模式的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type advanced_bot: str
        :param xss: **参数解释：** XSS攻击，跨站脚本攻击，攻击者通过注入恶意脚本获取用户信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type xss: str
        :param antiscan_high_freq_scan: **参数解释：** 高频扫描封锁，对异常高频请求进行识别和拦截 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type antiscan_high_freq_scan: str
        :param webshell: **参数解释：** 网站木马，攻击者上传的用于远程控制网站的恶意程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type webshell: str
        :param cc: **参数解释：** CC攻击，挑战型攻击，通过大量请求耗尽服务器资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cc: str
        :param botm: **参数解释：** BOT攻击，利用自动化程序进行的恶意攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type botm: str
        :param illegal: **参数解释：** 非法请求，违反安全策略或业务规则的请求 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type illegal: str
        :param llm_prompt_sensitive: **参数解释：** 大模型提示词合规检测，识别提示词中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type llm_prompt_sensitive: str
        :param sqli: **参数解释：** SQL注入，攻击者通过注入恶意SQL语句来获取或篡改数据 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sqli: str
        :param lfi: **参数解释：** 本地文件包含，攻击者利用漏洞包含本地文件获取信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type lfi: str
        :param antitamper: **参数解释：** 网页防篡改，保护网站内容不被非法修改 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type antitamper: str
        :param custom_geoip: **参数解释：** 地理位置访问控制，基于地理位置的访问限制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_geoip: str
        :param rfi: **参数解释：** 远程文件包含，攻击者利用漏洞包含远程文件执行恶意代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rfi: str
        :param vuln: **参数解释：** 其他类型攻击，未归类的安全漏洞或攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vuln: str
        :param llm_response_sensitive: **参数解释：** 大模型响应合规检测，识别AI模型输出中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type llm_response_sensitive: str
        :param custom_whiteblackip: **参数解释：** IP黑白名单，基于IP地址的访问控制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_whiteblackip: str
        :param leakage: **参数解释：** 网站信息泄露，敏感信息意外暴露的安全事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type leakage: str
        """
        
        

        self._cmdi = None
        self._llm_prompt_injection = None
        self._anticrawler = None
        self._custom_custom = None
        self._third_bot_river = None
        self._robot = None
        self._custom_idc_ip = None
        self._antiscan_dir_traversal = None
        self._advanced_bot = None
        self._xss = None
        self._antiscan_high_freq_scan = None
        self._webshell = None
        self._cc = None
        self._botm = None
        self._illegal = None
        self._llm_prompt_sensitive = None
        self._sqli = None
        self._lfi = None
        self._antitamper = None
        self._custom_geoip = None
        self._rfi = None
        self._vuln = None
        self._llm_response_sensitive = None
        self._custom_whiteblackip = None
        self._leakage = None
        self.discriminator = None

        if cmdi is not None:
            self.cmdi = cmdi
        if llm_prompt_injection is not None:
            self.llm_prompt_injection = llm_prompt_injection
        if anticrawler is not None:
            self.anticrawler = anticrawler
        if custom_custom is not None:
            self.custom_custom = custom_custom
        if third_bot_river is not None:
            self.third_bot_river = third_bot_river
        if robot is not None:
            self.robot = robot
        if custom_idc_ip is not None:
            self.custom_idc_ip = custom_idc_ip
        if antiscan_dir_traversal is not None:
            self.antiscan_dir_traversal = antiscan_dir_traversal
        if advanced_bot is not None:
            self.advanced_bot = advanced_bot
        if xss is not None:
            self.xss = xss
        if antiscan_high_freq_scan is not None:
            self.antiscan_high_freq_scan = antiscan_high_freq_scan
        if webshell is not None:
            self.webshell = webshell
        if cc is not None:
            self.cc = cc
        if botm is not None:
            self.botm = botm
        if illegal is not None:
            self.illegal = illegal
        if llm_prompt_sensitive is not None:
            self.llm_prompt_sensitive = llm_prompt_sensitive
        if sqli is not None:
            self.sqli = sqli
        if lfi is not None:
            self.lfi = lfi
        if antitamper is not None:
            self.antitamper = antitamper
        if custom_geoip is not None:
            self.custom_geoip = custom_geoip
        if rfi is not None:
            self.rfi = rfi
        if vuln is not None:
            self.vuln = vuln
        if llm_response_sensitive is not None:
            self.llm_response_sensitive = llm_response_sensitive
        if custom_whiteblackip is not None:
            self.custom_whiteblackip = custom_whiteblackip
        if leakage is not None:
            self.leakage = leakage

    @property
    def cmdi(self):
        r"""Gets the cmdi of this ThreatMapResponseBodyLocale.

        **参数解释：** 命令注入攻击，攻击者通过注入恶意命令来执行非授权操作 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cmdi of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._cmdi

    @cmdi.setter
    def cmdi(self, cmdi):
        r"""Sets the cmdi of this ThreatMapResponseBodyLocale.

        **参数解释：** 命令注入攻击，攻击者通过注入恶意命令来执行非授权操作 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cmdi: The cmdi of this ThreatMapResponseBodyLocale.
        :type cmdi: str
        """
        self._cmdi = cmdi

    @property
    def llm_prompt_injection(self):
        r"""Gets the llm_prompt_injection of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型提示词注入攻击，攻击者通过构造特殊输入来篡改AI模型的提示词 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The llm_prompt_injection of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._llm_prompt_injection

    @llm_prompt_injection.setter
    def llm_prompt_injection(self, llm_prompt_injection):
        r"""Sets the llm_prompt_injection of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型提示词注入攻击，攻击者通过构造特殊输入来篡改AI模型的提示词 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param llm_prompt_injection: The llm_prompt_injection of this ThreatMapResponseBodyLocale.
        :type llm_prompt_injection: str
        """
        self._llm_prompt_injection = llm_prompt_injection

    @property
    def anticrawler(self):
        r"""Gets the anticrawler of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站反爬虫策略，用于阻止自动化程序非法获取网站内容 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The anticrawler of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._anticrawler

    @anticrawler.setter
    def anticrawler(self, anticrawler):
        r"""Sets the anticrawler of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站反爬虫策略，用于阻止自动化程序非法获取网站内容 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param anticrawler: The anticrawler of this ThreatMapResponseBodyLocale.
        :type anticrawler: str
        """
        self._anticrawler = anticrawler

    @property
    def custom_custom(self):
        r"""Gets the custom_custom of this ThreatMapResponseBodyLocale.

        **参数解释：** 精准防护，基于特定规则的定制化安全防护策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_custom of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._custom_custom

    @custom_custom.setter
    def custom_custom(self, custom_custom):
        r"""Sets the custom_custom of this ThreatMapResponseBodyLocale.

        **参数解释：** 精准防护，基于特定规则的定制化安全防护策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_custom: The custom_custom of this ThreatMapResponseBodyLocale.
        :type custom_custom: str
        """
        self._custom_custom = custom_custom

    @property
    def third_bot_river(self):
        r"""Gets the third_bot_river of this ThreatMapResponseBodyLocale.

        **参数解释：** 第三方BOT，来自第三方服务的自动化交互程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The third_bot_river of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._third_bot_river

    @third_bot_river.setter
    def third_bot_river(self, third_bot_river):
        r"""Sets the third_bot_river of this ThreatMapResponseBodyLocale.

        **参数解释：** 第三方BOT，来自第三方服务的自动化交互程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param third_bot_river: The third_bot_river of this ThreatMapResponseBodyLocale.
        :type third_bot_river: str
        """
        self._third_bot_river = third_bot_river

    @property
    def robot(self):
        r"""Gets the robot of this ThreatMapResponseBodyLocale.

        **参数解释：** 恶意爬虫，用于非法获取数据或进行攻击的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The robot of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._robot

    @robot.setter
    def robot(self, robot):
        r"""Sets the robot of this ThreatMapResponseBodyLocale.

        **参数解释：** 恶意爬虫，用于非法获取数据或进行攻击的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param robot: The robot of this ThreatMapResponseBodyLocale.
        :type robot: str
        """
        self._robot = robot

    @property
    def custom_idc_ip(self):
        r"""Gets the custom_idc_ip of this ThreatMapResponseBodyLocale.

        **参数解释：** IDC情报，基于数据中心IP地址的威胁情报 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_idc_ip of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._custom_idc_ip

    @custom_idc_ip.setter
    def custom_idc_ip(self, custom_idc_ip):
        r"""Sets the custom_idc_ip of this ThreatMapResponseBodyLocale.

        **参数解释：** IDC情报，基于数据中心IP地址的威胁情报 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_idc_ip: The custom_idc_ip of this ThreatMapResponseBodyLocale.
        :type custom_idc_ip: str
        """
        self._custom_idc_ip = custom_idc_ip

    @property
    def antiscan_dir_traversal(self):
        r"""Gets the antiscan_dir_traversal of this ThreatMapResponseBodyLocale.

        **参数解释：** 目录遍历防护，防止攻击者通过目录遍历访问系统文件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The antiscan_dir_traversal of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._antiscan_dir_traversal

    @antiscan_dir_traversal.setter
    def antiscan_dir_traversal(self, antiscan_dir_traversal):
        r"""Sets the antiscan_dir_traversal of this ThreatMapResponseBodyLocale.

        **参数解释：** 目录遍历防护，防止攻击者通过目录遍历访问系统文件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param antiscan_dir_traversal: The antiscan_dir_traversal of this ThreatMapResponseBodyLocale.
        :type antiscan_dir_traversal: str
        """
        self._antiscan_dir_traversal = antiscan_dir_traversal

    @property
    def advanced_bot(self):
        r"""Gets the advanced_bot of this ThreatMapResponseBodyLocale.

        **参数解释：** 高级BOT，具有复杂行为模式的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The advanced_bot of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._advanced_bot

    @advanced_bot.setter
    def advanced_bot(self, advanced_bot):
        r"""Sets the advanced_bot of this ThreatMapResponseBodyLocale.

        **参数解释：** 高级BOT，具有复杂行为模式的自动化程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param advanced_bot: The advanced_bot of this ThreatMapResponseBodyLocale.
        :type advanced_bot: str
        """
        self._advanced_bot = advanced_bot

    @property
    def xss(self):
        r"""Gets the xss of this ThreatMapResponseBodyLocale.

        **参数解释：** XSS攻击，跨站脚本攻击，攻击者通过注入恶意脚本获取用户信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The xss of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._xss

    @xss.setter
    def xss(self, xss):
        r"""Sets the xss of this ThreatMapResponseBodyLocale.

        **参数解释：** XSS攻击，跨站脚本攻击，攻击者通过注入恶意脚本获取用户信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param xss: The xss of this ThreatMapResponseBodyLocale.
        :type xss: str
        """
        self._xss = xss

    @property
    def antiscan_high_freq_scan(self):
        r"""Gets the antiscan_high_freq_scan of this ThreatMapResponseBodyLocale.

        **参数解释：** 高频扫描封锁，对异常高频请求进行识别和拦截 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The antiscan_high_freq_scan of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._antiscan_high_freq_scan

    @antiscan_high_freq_scan.setter
    def antiscan_high_freq_scan(self, antiscan_high_freq_scan):
        r"""Sets the antiscan_high_freq_scan of this ThreatMapResponseBodyLocale.

        **参数解释：** 高频扫描封锁，对异常高频请求进行识别和拦截 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param antiscan_high_freq_scan: The antiscan_high_freq_scan of this ThreatMapResponseBodyLocale.
        :type antiscan_high_freq_scan: str
        """
        self._antiscan_high_freq_scan = antiscan_high_freq_scan

    @property
    def webshell(self):
        r"""Gets the webshell of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站木马，攻击者上传的用于远程控制网站的恶意程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The webshell of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._webshell

    @webshell.setter
    def webshell(self, webshell):
        r"""Sets the webshell of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站木马，攻击者上传的用于远程控制网站的恶意程序 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param webshell: The webshell of this ThreatMapResponseBodyLocale.
        :type webshell: str
        """
        self._webshell = webshell

    @property
    def cc(self):
        r"""Gets the cc of this ThreatMapResponseBodyLocale.

        **参数解释：** CC攻击，挑战型攻击，通过大量请求耗尽服务器资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cc of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this ThreatMapResponseBodyLocale.

        **参数解释：** CC攻击，挑战型攻击，通过大量请求耗尽服务器资源 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cc: The cc of this ThreatMapResponseBodyLocale.
        :type cc: str
        """
        self._cc = cc

    @property
    def botm(self):
        r"""Gets the botm of this ThreatMapResponseBodyLocale.

        **参数解释：** BOT攻击，利用自动化程序进行的恶意攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The botm of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._botm

    @botm.setter
    def botm(self, botm):
        r"""Sets the botm of this ThreatMapResponseBodyLocale.

        **参数解释：** BOT攻击，利用自动化程序进行的恶意攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param botm: The botm of this ThreatMapResponseBodyLocale.
        :type botm: str
        """
        self._botm = botm

    @property
    def illegal(self):
        r"""Gets the illegal of this ThreatMapResponseBodyLocale.

        **参数解释：** 非法请求，违反安全策略或业务规则的请求 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The illegal of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._illegal

    @illegal.setter
    def illegal(self, illegal):
        r"""Sets the illegal of this ThreatMapResponseBodyLocale.

        **参数解释：** 非法请求，违反安全策略或业务规则的请求 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param illegal: The illegal of this ThreatMapResponseBodyLocale.
        :type illegal: str
        """
        self._illegal = illegal

    @property
    def llm_prompt_sensitive(self):
        r"""Gets the llm_prompt_sensitive of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型提示词合规检测，识别提示词中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The llm_prompt_sensitive of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._llm_prompt_sensitive

    @llm_prompt_sensitive.setter
    def llm_prompt_sensitive(self, llm_prompt_sensitive):
        r"""Sets the llm_prompt_sensitive of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型提示词合规检测，识别提示词中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param llm_prompt_sensitive: The llm_prompt_sensitive of this ThreatMapResponseBodyLocale.
        :type llm_prompt_sensitive: str
        """
        self._llm_prompt_sensitive = llm_prompt_sensitive

    @property
    def sqli(self):
        r"""Gets the sqli of this ThreatMapResponseBodyLocale.

        **参数解释：** SQL注入，攻击者通过注入恶意SQL语句来获取或篡改数据 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sqli of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._sqli

    @sqli.setter
    def sqli(self, sqli):
        r"""Sets the sqli of this ThreatMapResponseBodyLocale.

        **参数解释：** SQL注入，攻击者通过注入恶意SQL语句来获取或篡改数据 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sqli: The sqli of this ThreatMapResponseBodyLocale.
        :type sqli: str
        """
        self._sqli = sqli

    @property
    def lfi(self):
        r"""Gets the lfi of this ThreatMapResponseBodyLocale.

        **参数解释：** 本地文件包含，攻击者利用漏洞包含本地文件获取信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The lfi of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._lfi

    @lfi.setter
    def lfi(self, lfi):
        r"""Sets the lfi of this ThreatMapResponseBodyLocale.

        **参数解释：** 本地文件包含，攻击者利用漏洞包含本地文件获取信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param lfi: The lfi of this ThreatMapResponseBodyLocale.
        :type lfi: str
        """
        self._lfi = lfi

    @property
    def antitamper(self):
        r"""Gets the antitamper of this ThreatMapResponseBodyLocale.

        **参数解释：** 网页防篡改，保护网站内容不被非法修改 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The antitamper of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._antitamper

    @antitamper.setter
    def antitamper(self, antitamper):
        r"""Sets the antitamper of this ThreatMapResponseBodyLocale.

        **参数解释：** 网页防篡改，保护网站内容不被非法修改 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param antitamper: The antitamper of this ThreatMapResponseBodyLocale.
        :type antitamper: str
        """
        self._antitamper = antitamper

    @property
    def custom_geoip(self):
        r"""Gets the custom_geoip of this ThreatMapResponseBodyLocale.

        **参数解释：** 地理位置访问控制，基于地理位置的访问限制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_geoip of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._custom_geoip

    @custom_geoip.setter
    def custom_geoip(self, custom_geoip):
        r"""Sets the custom_geoip of this ThreatMapResponseBodyLocale.

        **参数解释：** 地理位置访问控制，基于地理位置的访问限制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_geoip: The custom_geoip of this ThreatMapResponseBodyLocale.
        :type custom_geoip: str
        """
        self._custom_geoip = custom_geoip

    @property
    def rfi(self):
        r"""Gets the rfi of this ThreatMapResponseBodyLocale.

        **参数解释：** 远程文件包含，攻击者利用漏洞包含远程文件执行恶意代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rfi of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._rfi

    @rfi.setter
    def rfi(self, rfi):
        r"""Sets the rfi of this ThreatMapResponseBodyLocale.

        **参数解释：** 远程文件包含，攻击者利用漏洞包含远程文件执行恶意代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rfi: The rfi of this ThreatMapResponseBodyLocale.
        :type rfi: str
        """
        self._rfi = rfi

    @property
    def vuln(self):
        r"""Gets the vuln of this ThreatMapResponseBodyLocale.

        **参数解释：** 其他类型攻击，未归类的安全漏洞或攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vuln of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._vuln

    @vuln.setter
    def vuln(self, vuln):
        r"""Sets the vuln of this ThreatMapResponseBodyLocale.

        **参数解释：** 其他类型攻击，未归类的安全漏洞或攻击 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vuln: The vuln of this ThreatMapResponseBodyLocale.
        :type vuln: str
        """
        self._vuln = vuln

    @property
    def llm_response_sensitive(self):
        r"""Gets the llm_response_sensitive of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型响应合规检测，识别AI模型输出中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The llm_response_sensitive of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._llm_response_sensitive

    @llm_response_sensitive.setter
    def llm_response_sensitive(self, llm_response_sensitive):
        r"""Sets the llm_response_sensitive of this ThreatMapResponseBodyLocale.

        **参数解释：** 大模型响应合规检测，识别AI模型输出中的敏感信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param llm_response_sensitive: The llm_response_sensitive of this ThreatMapResponseBodyLocale.
        :type llm_response_sensitive: str
        """
        self._llm_response_sensitive = llm_response_sensitive

    @property
    def custom_whiteblackip(self):
        r"""Gets the custom_whiteblackip of this ThreatMapResponseBodyLocale.

        **参数解释：** IP黑白名单，基于IP地址的访问控制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_whiteblackip of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._custom_whiteblackip

    @custom_whiteblackip.setter
    def custom_whiteblackip(self, custom_whiteblackip):
        r"""Sets the custom_whiteblackip of this ThreatMapResponseBodyLocale.

        **参数解释：** IP黑白名单，基于IP地址的访问控制策略 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_whiteblackip: The custom_whiteblackip of this ThreatMapResponseBodyLocale.
        :type custom_whiteblackip: str
        """
        self._custom_whiteblackip = custom_whiteblackip

    @property
    def leakage(self):
        r"""Gets the leakage of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站信息泄露，敏感信息意外暴露的安全事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The leakage of this ThreatMapResponseBodyLocale.
        :rtype: str
        """
        return self._leakage

    @leakage.setter
    def leakage(self, leakage):
        r"""Sets the leakage of this ThreatMapResponseBodyLocale.

        **参数解释：** 网站信息泄露，敏感信息意外暴露的安全事件 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param leakage: The leakage of this ThreatMapResponseBodyLocale.
        :type leakage: str
        """
        self._leakage = leakage

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ThreatMapResponseBodyLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
