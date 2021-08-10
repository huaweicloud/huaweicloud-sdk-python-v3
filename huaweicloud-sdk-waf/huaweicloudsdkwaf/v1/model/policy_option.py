# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyOption:


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
        'crawler': 'bool',
        'crawler_engine': 'bool',
        'crawler_scanner': 'bool',
        'crawler_script': 'bool',
        'crawler_other': 'bool',
        'webshell': 'bool',
        'cc': 'bool',
        'custom': 'bool',
        'whiteblackip': 'bool',
        'ignore': 'bool',
        'privacy': 'bool',
        'antitamper': 'bool'
    }

    attribute_map = {
        'webattack': 'webattack',
        'common': 'common',
        'crawler': 'crawler',
        'crawler_engine': 'crawler_engine',
        'crawler_scanner': 'crawler_scanner',
        'crawler_script': 'crawler_script',
        'crawler_other': 'crawler_other',
        'webshell': 'webshell',
        'cc': 'cc',
        'custom': 'custom',
        'whiteblackip': 'whiteblackip',
        'ignore': 'ignore',
        'privacy': 'privacy',
        'antitamper': 'antitamper'
    }

    def __init__(self, webattack=None, common=None, crawler=None, crawler_engine=None, crawler_scanner=None, crawler_script=None, crawler_other=None, webshell=None, cc=None, custom=None, whiteblackip=None, ignore=None, privacy=None, antitamper=None):
        """PolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._webattack = None
        self._common = None
        self._crawler = None
        self._crawler_engine = None
        self._crawler_scanner = None
        self._crawler_script = None
        self._crawler_other = None
        self._webshell = None
        self._cc = None
        self._custom = None
        self._whiteblackip = None
        self._ignore = None
        self._privacy = None
        self._antitamper = None
        self.discriminator = None

        if webattack is not None:
            self.webattack = webattack
        if common is not None:
            self.common = common
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
        if whiteblackip is not None:
            self.whiteblackip = whiteblackip
        if ignore is not None:
            self.ignore = ignore
        if privacy is not None:
            self.privacy = privacy
        if antitamper is not None:
            self.antitamper = antitamper

    @property
    def webattack(self):
        """Gets the webattack of this PolicyOption.

        基础防护是否开启

        :return: The webattack of this PolicyOption.
        :rtype: bool
        """
        return self._webattack

    @webattack.setter
    def webattack(self, webattack):
        """Sets the webattack of this PolicyOption.

        基础防护是否开启

        :param webattack: The webattack of this PolicyOption.
        :type: bool
        """
        self._webattack = webattack

    @property
    def common(self):
        """Gets the common of this PolicyOption.

        常规检测是否开启

        :return: The common of this PolicyOption.
        :rtype: bool
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this PolicyOption.

        常规检测是否开启

        :param common: The common of this PolicyOption.
        :type: bool
        """
        self._common = common

    @property
    def crawler(self):
        """Gets the crawler of this PolicyOption.

        反爬虫是否开启

        :return: The crawler of this PolicyOption.
        :rtype: bool
        """
        return self._crawler

    @crawler.setter
    def crawler(self, crawler):
        """Sets the crawler of this PolicyOption.

        反爬虫是否开启

        :param crawler: The crawler of this PolicyOption.
        :type: bool
        """
        self._crawler = crawler

    @property
    def crawler_engine(self):
        """Gets the crawler_engine of this PolicyOption.

        搜索engine是否开启

        :return: The crawler_engine of this PolicyOption.
        :rtype: bool
        """
        return self._crawler_engine

    @crawler_engine.setter
    def crawler_engine(self, crawler_engine):
        """Sets the crawler_engine of this PolicyOption.

        搜索engine是否开启

        :param crawler_engine: The crawler_engine of this PolicyOption.
        :type: bool
        """
        self._crawler_engine = crawler_engine

    @property
    def crawler_scanner(self):
        """Gets the crawler_scanner of this PolicyOption.

        反爬虫检测是否开启

        :return: The crawler_scanner of this PolicyOption.
        :rtype: bool
        """
        return self._crawler_scanner

    @crawler_scanner.setter
    def crawler_scanner(self, crawler_scanner):
        """Sets the crawler_scanner of this PolicyOption.

        反爬虫检测是否开启

        :param crawler_scanner: The crawler_scanner of this PolicyOption.
        :type: bool
        """
        self._crawler_scanner = crawler_scanner

    @property
    def crawler_script(self):
        """Gets the crawler_script of this PolicyOption.

        脚本反爬虫是否开启

        :return: The crawler_script of this PolicyOption.
        :rtype: bool
        """
        return self._crawler_script

    @crawler_script.setter
    def crawler_script(self, crawler_script):
        """Sets the crawler_script of this PolicyOption.

        脚本反爬虫是否开启

        :param crawler_script: The crawler_script of this PolicyOption.
        :type: bool
        """
        self._crawler_script = crawler_script

    @property
    def crawler_other(self):
        """Gets the crawler_other of this PolicyOption.

        其他爬虫是否开启

        :return: The crawler_other of this PolicyOption.
        :rtype: bool
        """
        return self._crawler_other

    @crawler_other.setter
    def crawler_other(self, crawler_other):
        """Sets the crawler_other of this PolicyOption.

        其他爬虫是否开启

        :param crawler_other: The crawler_other of this PolicyOption.
        :type: bool
        """
        self._crawler_other = crawler_other

    @property
    def webshell(self):
        """Gets the webshell of this PolicyOption.

        Webshell检测是否开启

        :return: The webshell of this PolicyOption.
        :rtype: bool
        """
        return self._webshell

    @webshell.setter
    def webshell(self, webshell):
        """Sets the webshell of this PolicyOption.

        Webshell检测是否开启

        :param webshell: The webshell of this PolicyOption.
        :type: bool
        """
        self._webshell = webshell

    @property
    def cc(self):
        """Gets the cc of this PolicyOption.

        cc规则是否开启

        :return: The cc of this PolicyOption.
        :rtype: bool
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this PolicyOption.

        cc规则是否开启

        :param cc: The cc of this PolicyOption.
        :type: bool
        """
        self._cc = cc

    @property
    def custom(self):
        """Gets the custom of this PolicyOption.

        精准防护是否开启

        :return: The custom of this PolicyOption.
        :rtype: bool
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this PolicyOption.

        精准防护是否开启

        :param custom: The custom of this PolicyOption.
        :type: bool
        """
        self._custom = custom

    @property
    def whiteblackip(self):
        """Gets the whiteblackip of this PolicyOption.

        黑白名单防护是否开启

        :return: The whiteblackip of this PolicyOption.
        :rtype: bool
        """
        return self._whiteblackip

    @whiteblackip.setter
    def whiteblackip(self, whiteblackip):
        """Sets the whiteblackip of this PolicyOption.

        黑白名单防护是否开启

        :param whiteblackip: The whiteblackip of this PolicyOption.
        :type: bool
        """
        self._whiteblackip = whiteblackip

    @property
    def ignore(self):
        """Gets the ignore of this PolicyOption.

        误报屏蔽是否开启

        :return: The ignore of this PolicyOption.
        :rtype: bool
        """
        return self._ignore

    @ignore.setter
    def ignore(self, ignore):
        """Sets the ignore of this PolicyOption.

        误报屏蔽是否开启

        :param ignore: The ignore of this PolicyOption.
        :type: bool
        """
        self._ignore = ignore

    @property
    def privacy(self):
        """Gets the privacy of this PolicyOption.

        隐私屏蔽是否开启

        :return: The privacy of this PolicyOption.
        :rtype: bool
        """
        return self._privacy

    @privacy.setter
    def privacy(self, privacy):
        """Sets the privacy of this PolicyOption.

        隐私屏蔽是否开启

        :param privacy: The privacy of this PolicyOption.
        :type: bool
        """
        self._privacy = privacy

    @property
    def antitamper(self):
        """Gets the antitamper of this PolicyOption.

        网页防篡改规则是否开启

        :return: The antitamper of this PolicyOption.
        :rtype: bool
        """
        return self._antitamper

    @antitamper.setter
    def antitamper(self, antitamper):
        """Sets the antitamper of this PolicyOption.

        网页防篡改规则是否开启

        :param antitamper: The antitamper of this PolicyOption.
        :type: bool
        """
        self._antitamper = antitamper

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
        if not isinstance(other, PolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
