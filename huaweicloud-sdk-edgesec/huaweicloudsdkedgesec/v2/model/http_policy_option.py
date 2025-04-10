# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpPolicyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'webattack': 'bool',
        'common': 'bool',
        'bot_enable': 'bool',
        'crawler': 'bool',
        'crawler_engine': 'bool',
        'crawler_scanner': 'bool',
        'crawler_script': 'bool',
        'crawler_other': 'bool',
        'webshell': 'bool',
        'cc': 'bool',
        'custom': 'bool',
        'followed_action': 'bool',
        'whiteblackip': 'bool',
        'geoip': 'bool',
        'ignore': 'bool',
        'privacy': 'bool',
        'antitamper': 'bool',
        'antileakage': 'bool',
        'anticrawler': 'bool',
        'third_bot_river': 'bool'
    }

    attribute_map = {
        'webattack': 'webattack',
        'common': 'common',
        'bot_enable': 'bot_enable',
        'crawler': 'crawler',
        'crawler_engine': 'crawler_engine',
        'crawler_scanner': 'crawler_scanner',
        'crawler_script': 'crawler_script',
        'crawler_other': 'crawler_other',
        'webshell': 'webshell',
        'cc': 'cc',
        'custom': 'custom',
        'followed_action': 'followed_action',
        'whiteblackip': 'whiteblackip',
        'geoip': 'geoip',
        'ignore': 'ignore',
        'privacy': 'privacy',
        'antitamper': 'antitamper',
        'antileakage': 'antileakage',
        'anticrawler': 'anticrawler',
        'third_bot_river': 'third_bot_river'
    }

    def __init__(self, webattack=None, common=None, bot_enable=None, crawler=None, crawler_engine=None, crawler_scanner=None, crawler_script=None, crawler_other=None, webshell=None, cc=None, custom=None, followed_action=None, whiteblackip=None, geoip=None, ignore=None, privacy=None, antitamper=None, antileakage=None, anticrawler=None, third_bot_river=None):
        r"""HttpPolicyOption

        The model defined in huaweicloud sdk

        :param webattack: 基础防护是否开启
        :type webattack: bool
        :param common: 常规检测是否开启
        :type common: bool
        :param bot_enable: 所有反爬虫是否开启
        :type bot_enable: bool
        :param crawler: 特征反爬虫是否开启
        :type crawler: bool
        :param crawler_engine: 搜索engine是否开启
        :type crawler_engine: bool
        :param crawler_scanner: 扫描器是否开启
        :type crawler_scanner: bool
        :param crawler_script: 脚本反爬虫是否开启
        :type crawler_script: bool
        :param crawler_other: 其他爬虫是否开启
        :type crawler_other: bool
        :param webshell: Webshell检测是否开启
        :type webshell: bool
        :param cc: cc规则是否开启
        :type cc: bool
        :param custom: 精准防护是否开启
        :type custom: bool
        :param followed_action: 攻击惩罚是否开启
        :type followed_action: bool
        :param whiteblackip: 黑白名单防护是否开启
        :type whiteblackip: bool
        :param geoip: 地理位置规则是否开启
        :type geoip: bool
        :param ignore: 误报屏蔽是否开启
        :type ignore: bool
        :param privacy: 隐私屏蔽是否开启
        :type privacy: bool
        :param antitamper: 网页防篡改规则是否开启
        :type antitamper: bool
        :param antileakage: 防敏感信息泄露规则是否开启
        :type antileakage: bool
        :param anticrawler: 脚本反爬虫规则是否开启
        :type anticrawler: bool
        :param third_bot_river: 三方BOT是否开启
        :type third_bot_river: bool
        """
        
        

        self._webattack = None
        self._common = None
        self._bot_enable = None
        self._crawler = None
        self._crawler_engine = None
        self._crawler_scanner = None
        self._crawler_script = None
        self._crawler_other = None
        self._webshell = None
        self._cc = None
        self._custom = None
        self._followed_action = None
        self._whiteblackip = None
        self._geoip = None
        self._ignore = None
        self._privacy = None
        self._antitamper = None
        self._antileakage = None
        self._anticrawler = None
        self._third_bot_river = None
        self.discriminator = None

        if webattack is not None:
            self.webattack = webattack
        if common is not None:
            self.common = common
        if bot_enable is not None:
            self.bot_enable = bot_enable
        if crawler is not None:
            self.crawler = crawler
        if crawler_engine is not None:
            self.crawler_engine = crawler_engine
        if crawler_scanner is not None:
            self.crawler_scanner = crawler_scanner
        if crawler_script is not None:
            self.crawler_script = crawler_script
        if crawler_other is not None:
            self.crawler_other = crawler_other
        if webshell is not None:
            self.webshell = webshell
        if cc is not None:
            self.cc = cc
        if custom is not None:
            self.custom = custom
        if followed_action is not None:
            self.followed_action = followed_action
        if whiteblackip is not None:
            self.whiteblackip = whiteblackip
        if geoip is not None:
            self.geoip = geoip
        if ignore is not None:
            self.ignore = ignore
        if privacy is not None:
            self.privacy = privacy
        if antitamper is not None:
            self.antitamper = antitamper
        if antileakage is not None:
            self.antileakage = antileakage
        if anticrawler is not None:
            self.anticrawler = anticrawler
        if third_bot_river is not None:
            self.third_bot_river = third_bot_river

    @property
    def webattack(self):
        r"""Gets the webattack of this HttpPolicyOption.

        基础防护是否开启

        :return: The webattack of this HttpPolicyOption.
        :rtype: bool
        """
        return self._webattack

    @webattack.setter
    def webattack(self, webattack):
        r"""Sets the webattack of this HttpPolicyOption.

        基础防护是否开启

        :param webattack: The webattack of this HttpPolicyOption.
        :type webattack: bool
        """
        self._webattack = webattack

    @property
    def common(self):
        r"""Gets the common of this HttpPolicyOption.

        常规检测是否开启

        :return: The common of this HttpPolicyOption.
        :rtype: bool
        """
        return self._common

    @common.setter
    def common(self, common):
        r"""Sets the common of this HttpPolicyOption.

        常规检测是否开启

        :param common: The common of this HttpPolicyOption.
        :type common: bool
        """
        self._common = common

    @property
    def bot_enable(self):
        r"""Gets the bot_enable of this HttpPolicyOption.

        所有反爬虫是否开启

        :return: The bot_enable of this HttpPolicyOption.
        :rtype: bool
        """
        return self._bot_enable

    @bot_enable.setter
    def bot_enable(self, bot_enable):
        r"""Sets the bot_enable of this HttpPolicyOption.

        所有反爬虫是否开启

        :param bot_enable: The bot_enable of this HttpPolicyOption.
        :type bot_enable: bool
        """
        self._bot_enable = bot_enable

    @property
    def crawler(self):
        r"""Gets the crawler of this HttpPolicyOption.

        特征反爬虫是否开启

        :return: The crawler of this HttpPolicyOption.
        :rtype: bool
        """
        return self._crawler

    @crawler.setter
    def crawler(self, crawler):
        r"""Sets the crawler of this HttpPolicyOption.

        特征反爬虫是否开启

        :param crawler: The crawler of this HttpPolicyOption.
        :type crawler: bool
        """
        self._crawler = crawler

    @property
    def crawler_engine(self):
        r"""Gets the crawler_engine of this HttpPolicyOption.

        搜索engine是否开启

        :return: The crawler_engine of this HttpPolicyOption.
        :rtype: bool
        """
        return self._crawler_engine

    @crawler_engine.setter
    def crawler_engine(self, crawler_engine):
        r"""Sets the crawler_engine of this HttpPolicyOption.

        搜索engine是否开启

        :param crawler_engine: The crawler_engine of this HttpPolicyOption.
        :type crawler_engine: bool
        """
        self._crawler_engine = crawler_engine

    @property
    def crawler_scanner(self):
        r"""Gets the crawler_scanner of this HttpPolicyOption.

        扫描器是否开启

        :return: The crawler_scanner of this HttpPolicyOption.
        :rtype: bool
        """
        return self._crawler_scanner

    @crawler_scanner.setter
    def crawler_scanner(self, crawler_scanner):
        r"""Sets the crawler_scanner of this HttpPolicyOption.

        扫描器是否开启

        :param crawler_scanner: The crawler_scanner of this HttpPolicyOption.
        :type crawler_scanner: bool
        """
        self._crawler_scanner = crawler_scanner

    @property
    def crawler_script(self):
        r"""Gets the crawler_script of this HttpPolicyOption.

        脚本反爬虫是否开启

        :return: The crawler_script of this HttpPolicyOption.
        :rtype: bool
        """
        return self._crawler_script

    @crawler_script.setter
    def crawler_script(self, crawler_script):
        r"""Sets the crawler_script of this HttpPolicyOption.

        脚本反爬虫是否开启

        :param crawler_script: The crawler_script of this HttpPolicyOption.
        :type crawler_script: bool
        """
        self._crawler_script = crawler_script

    @property
    def crawler_other(self):
        r"""Gets the crawler_other of this HttpPolicyOption.

        其他爬虫是否开启

        :return: The crawler_other of this HttpPolicyOption.
        :rtype: bool
        """
        return self._crawler_other

    @crawler_other.setter
    def crawler_other(self, crawler_other):
        r"""Sets the crawler_other of this HttpPolicyOption.

        其他爬虫是否开启

        :param crawler_other: The crawler_other of this HttpPolicyOption.
        :type crawler_other: bool
        """
        self._crawler_other = crawler_other

    @property
    def webshell(self):
        r"""Gets the webshell of this HttpPolicyOption.

        Webshell检测是否开启

        :return: The webshell of this HttpPolicyOption.
        :rtype: bool
        """
        return self._webshell

    @webshell.setter
    def webshell(self, webshell):
        r"""Sets the webshell of this HttpPolicyOption.

        Webshell检测是否开启

        :param webshell: The webshell of this HttpPolicyOption.
        :type webshell: bool
        """
        self._webshell = webshell

    @property
    def cc(self):
        r"""Gets the cc of this HttpPolicyOption.

        cc规则是否开启

        :return: The cc of this HttpPolicyOption.
        :rtype: bool
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this HttpPolicyOption.

        cc规则是否开启

        :param cc: The cc of this HttpPolicyOption.
        :type cc: bool
        """
        self._cc = cc

    @property
    def custom(self):
        r"""Gets the custom of this HttpPolicyOption.

        精准防护是否开启

        :return: The custom of this HttpPolicyOption.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        r"""Sets the custom of this HttpPolicyOption.

        精准防护是否开启

        :param custom: The custom of this HttpPolicyOption.
        :type custom: bool
        """
        self._custom = custom

    @property
    def followed_action(self):
        r"""Gets the followed_action of this HttpPolicyOption.

        攻击惩罚是否开启

        :return: The followed_action of this HttpPolicyOption.
        :rtype: bool
        """
        return self._followed_action

    @followed_action.setter
    def followed_action(self, followed_action):
        r"""Sets the followed_action of this HttpPolicyOption.

        攻击惩罚是否开启

        :param followed_action: The followed_action of this HttpPolicyOption.
        :type followed_action: bool
        """
        self._followed_action = followed_action

    @property
    def whiteblackip(self):
        r"""Gets the whiteblackip of this HttpPolicyOption.

        黑白名单防护是否开启

        :return: The whiteblackip of this HttpPolicyOption.
        :rtype: bool
        """
        return self._whiteblackip

    @whiteblackip.setter
    def whiteblackip(self, whiteblackip):
        r"""Sets the whiteblackip of this HttpPolicyOption.

        黑白名单防护是否开启

        :param whiteblackip: The whiteblackip of this HttpPolicyOption.
        :type whiteblackip: bool
        """
        self._whiteblackip = whiteblackip

    @property
    def geoip(self):
        r"""Gets the geoip of this HttpPolicyOption.

        地理位置规则是否开启

        :return: The geoip of this HttpPolicyOption.
        :rtype: bool
        """
        return self._geoip

    @geoip.setter
    def geoip(self, geoip):
        r"""Sets the geoip of this HttpPolicyOption.

        地理位置规则是否开启

        :param geoip: The geoip of this HttpPolicyOption.
        :type geoip: bool
        """
        self._geoip = geoip

    @property
    def ignore(self):
        r"""Gets the ignore of this HttpPolicyOption.

        误报屏蔽是否开启

        :return: The ignore of this HttpPolicyOption.
        :rtype: bool
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        r"""Sets the ignore of this HttpPolicyOption.

        误报屏蔽是否开启

        :param ignore: The ignore of this HttpPolicyOption.
        :type ignore: bool
        """
        self._ignore = ignore

    @property
    def privacy(self):
        r"""Gets the privacy of this HttpPolicyOption.

        隐私屏蔽是否开启

        :return: The privacy of this HttpPolicyOption.
        :rtype: bool
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        r"""Sets the privacy of this HttpPolicyOption.

        隐私屏蔽是否开启

        :param privacy: The privacy of this HttpPolicyOption.
        :type privacy: bool
        """
        self._privacy = privacy

    @property
    def antitamper(self):
        r"""Gets the antitamper of this HttpPolicyOption.

        网页防篡改规则是否开启

        :return: The antitamper of this HttpPolicyOption.
        :rtype: bool
        """
        return self._antitamper

    @antitamper.setter
    def antitamper(self, antitamper):
        r"""Sets the antitamper of this HttpPolicyOption.

        网页防篡改规则是否开启

        :param antitamper: The antitamper of this HttpPolicyOption.
        :type antitamper: bool
        """
        self._antitamper = antitamper

    @property
    def antileakage(self):
        r"""Gets the antileakage of this HttpPolicyOption.

        防敏感信息泄露规则是否开启

        :return: The antileakage of this HttpPolicyOption.
        :rtype: bool
        """
        return self._antileakage

    @antileakage.setter
    def antileakage(self, antileakage):
        r"""Sets the antileakage of this HttpPolicyOption.

        防敏感信息泄露规则是否开启

        :param antileakage: The antileakage of this HttpPolicyOption.
        :type antileakage: bool
        """
        self._antileakage = antileakage

    @property
    def anticrawler(self):
        r"""Gets the anticrawler of this HttpPolicyOption.

        脚本反爬虫规则是否开启

        :return: The anticrawler of this HttpPolicyOption.
        :rtype: bool
        """
        return self._anticrawler

    @anticrawler.setter
    def anticrawler(self, anticrawler):
        r"""Sets the anticrawler of this HttpPolicyOption.

        脚本反爬虫规则是否开启

        :param anticrawler: The anticrawler of this HttpPolicyOption.
        :type anticrawler: bool
        """
        self._anticrawler = anticrawler

    @property
    def third_bot_river(self):
        r"""Gets the third_bot_river of this HttpPolicyOption.

        三方BOT是否开启

        :return: The third_bot_river of this HttpPolicyOption.
        :rtype: bool
        """
        return self._third_bot_river

    @third_bot_river.setter
    def third_bot_river(self, third_bot_river):
        r"""Sets the third_bot_river of this HttpPolicyOption.

        三方BOT是否开启

        :param third_bot_river: The third_bot_river of this HttpPolicyOption.
        :type third_bot_river: bool
        """
        self._third_bot_river = third_bot_river

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
        if not isinstance(other, HttpPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
