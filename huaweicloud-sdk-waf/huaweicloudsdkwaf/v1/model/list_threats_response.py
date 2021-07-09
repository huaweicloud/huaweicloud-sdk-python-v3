# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListThreatsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'xss': 'int',
        'sqli': 'int',
        'cmdi': 'int',
        'lfi': 'int',
        'rfi': 'int',
        'webshell': 'int',
        'robot': 'int',
        'cc': 'int',
        'custom': 'int',
        'whiteblackip': 'int',
        'antileakage': 'int',
        'antitamper': 'int'
    }

    attribute_map = {
        'xss': 'xss',
        'sqli': 'sqli',
        'cmdi': 'cmdi',
        'lfi': 'lfi',
        'rfi': 'rfi',
        'webshell': 'webshell',
        'robot': 'robot',
        'cc': 'cc',
        'custom': 'custom',
        'whiteblackip': 'whiteblackip',
        'antileakage': 'antileakage',
        'antitamper': 'antitamper'
    }

    def __init__(self, xss=None, sqli=None, cmdi=None, lfi=None, rfi=None, webshell=None, robot=None, cc=None, custom=None, whiteblackip=None, antileakage=None, antitamper=None):
        """ListThreatsResponse - a model defined in huaweicloud sdk"""
        
        super(ListThreatsResponse, self).__init__()

        self._xss = None
        self._sqli = None
        self._cmdi = None
        self._lfi = None
        self._rfi = None
        self._webshell = None
        self._robot = None
        self._cc = None
        self._custom = None
        self._whiteblackip = None
        self._antileakage = None
        self._antitamper = None
        self.discriminator = None

        if xss is not None:
            self.xss = xss
        if sqli is not None:
            self.sqli = sqli
        if cmdi is not None:
            self.cmdi = cmdi
        if lfi is not None:
            self.lfi = lfi
        if rfi is not None:
            self.rfi = rfi
        if webshell is not None:
            self.webshell = webshell
        if robot is not None:
            self.robot = robot
        if cc is not None:
            self.cc = cc
        if custom is not None:
            self.custom = custom
        if whiteblackip is not None:
            self.whiteblackip = whiteblackip
        if antileakage is not None:
            self.antileakage = antileakage
        if antitamper is not None:
            self.antitamper = antitamper

    @property
    def xss(self):
        """Gets the xss of this ListThreatsResponse.

        时间区间内xss攻击数量

        :return: The xss of this ListThreatsResponse.
        :rtype: int
        """
        return self._xss

    @xss.setter
    def xss(self, xss):
        """Sets the xss of this ListThreatsResponse.

        时间区间内xss攻击数量

        :param xss: The xss of this ListThreatsResponse.
        :type: int
        """
        self._xss = xss

    @property
    def sqli(self):
        """Gets the sqli of this ListThreatsResponse.

        时间区间内sqli攻击数量

        :return: The sqli of this ListThreatsResponse.
        :rtype: int
        """
        return self._sqli

    @sqli.setter
    def sqli(self, sqli):
        """Sets the sqli of this ListThreatsResponse.

        时间区间内sqli攻击数量

        :param sqli: The sqli of this ListThreatsResponse.
        :type: int
        """
        self._sqli = sqli

    @property
    def cmdi(self):
        """Gets the cmdi of this ListThreatsResponse.

        时间区间内cmdi攻击数量

        :return: The cmdi of this ListThreatsResponse.
        :rtype: int
        """
        return self._cmdi

    @cmdi.setter
    def cmdi(self, cmdi):
        """Sets the cmdi of this ListThreatsResponse.

        时间区间内cmdi攻击数量

        :param cmdi: The cmdi of this ListThreatsResponse.
        :type: int
        """
        self._cmdi = cmdi

    @property
    def lfi(self):
        """Gets the lfi of this ListThreatsResponse.

        时间区间内lfi攻击数量

        :return: The lfi of this ListThreatsResponse.
        :rtype: int
        """
        return self._lfi

    @lfi.setter
    def lfi(self, lfi):
        """Sets the lfi of this ListThreatsResponse.

        时间区间内lfi攻击数量

        :param lfi: The lfi of this ListThreatsResponse.
        :type: int
        """
        self._lfi = lfi

    @property
    def rfi(self):
        """Gets the rfi of this ListThreatsResponse.

        时间区间内rfi攻击数量

        :return: The rfi of this ListThreatsResponse.
        :rtype: int
        """
        return self._rfi

    @rfi.setter
    def rfi(self, rfi):
        """Sets the rfi of this ListThreatsResponse.

        时间区间内rfi攻击数量

        :param rfi: The rfi of this ListThreatsResponse.
        :type: int
        """
        self._rfi = rfi

    @property
    def webshell(self):
        """Gets the webshell of this ListThreatsResponse.

        时间区间内webshell攻击数量

        :return: The webshell of this ListThreatsResponse.
        :rtype: int
        """
        return self._webshell

    @webshell.setter
    def webshell(self, webshell):
        """Sets the webshell of this ListThreatsResponse.

        时间区间内webshell攻击数量

        :param webshell: The webshell of this ListThreatsResponse.
        :type: int
        """
        self._webshell = webshell

    @property
    def robot(self):
        """Gets the robot of this ListThreatsResponse.

        时间区间内恶意爬虫数量

        :return: The robot of this ListThreatsResponse.
        :rtype: int
        """
        return self._robot

    @robot.setter
    def robot(self, robot):
        """Sets the robot of this ListThreatsResponse.

        时间区间内恶意爬虫数量

        :param robot: The robot of this ListThreatsResponse.
        :type: int
        """
        self._robot = robot

    @property
    def cc(self):
        """Gets the cc of this ListThreatsResponse.

        时间区间内cc攻击数量

        :return: The cc of this ListThreatsResponse.
        :rtype: int
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ListThreatsResponse.

        时间区间内cc攻击数量

        :param cc: The cc of this ListThreatsResponse.
        :type: int
        """
        self._cc = cc

    @property
    def custom(self):
        """Gets the custom of this ListThreatsResponse.

        时间区间内对自定义规则攻击数量

        :return: The custom of this ListThreatsResponse.
        :rtype: int
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this ListThreatsResponse.

        时间区间内对自定义规则攻击数量

        :param custom: The custom of this ListThreatsResponse.
        :type: int
        """
        self._custom = custom

    @property
    def whiteblackip(self):
        """Gets the whiteblackip of this ListThreatsResponse.

        时间区间内对黑白名单规则攻击数量

        :return: The whiteblackip of this ListThreatsResponse.
        :rtype: int
        """
        return self._whiteblackip

    @whiteblackip.setter
    def whiteblackip(self, whiteblackip):
        """Sets the whiteblackip of this ListThreatsResponse.

        时间区间内对黑白名单规则攻击数量

        :param whiteblackip: The whiteblackip of this ListThreatsResponse.
        :type: int
        """
        self._whiteblackip = whiteblackip

    @property
    def antileakage(self):
        """Gets the antileakage of this ListThreatsResponse.

        时间区间内反泄漏数量

        :return: The antileakage of this ListThreatsResponse.
        :rtype: int
        """
        return self._antileakage

    @antileakage.setter
    def antileakage(self, antileakage):
        """Sets the antileakage of this ListThreatsResponse.

        时间区间内反泄漏数量

        :param antileakage: The antileakage of this ListThreatsResponse.
        :type: int
        """
        self._antileakage = antileakage

    @property
    def antitamper(self):
        """Gets the antitamper of this ListThreatsResponse.

        时间区间内防篡改数量

        :return: The antitamper of this ListThreatsResponse.
        :rtype: int
        """
        return self._antitamper

    @antitamper.setter
    def antitamper(self, antitamper):
        """Sets the antitamper of this ListThreatsResponse.

        时间区间内防篡改数量

        :param antitamper: The antitamper of this ListThreatsResponse.
        :type: int
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListThreatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
