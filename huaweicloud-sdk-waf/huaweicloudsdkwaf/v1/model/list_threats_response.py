# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""ListThreatsResponse

        The model defined in huaweicloud sdk

        :param xss: 时间区间内xss攻击数量
        :type xss: int
        :param sqli: 时间区间内sqli攻击数量
        :type sqli: int
        :param cmdi: 时间区间内cmdi攻击数量
        :type cmdi: int
        :param lfi: 时间区间内lfi攻击数量
        :type lfi: int
        :param rfi: 时间区间内rfi攻击数量
        :type rfi: int
        :param webshell: 时间区间内webshell攻击数量
        :type webshell: int
        :param robot: 时间区间内恶意爬虫数量
        :type robot: int
        :param cc: 时间区间内cc攻击数量
        :type cc: int
        :param custom: 时间区间内对自定义规则攻击数量
        :type custom: int
        :param whiteblackip: 时间区间内对黑白名单规则攻击数量
        :type whiteblackip: int
        :param antileakage: 时间区间内反泄漏数量
        :type antileakage: int
        :param antitamper: 时间区间内防篡改数量
        :type antitamper: int
        """
        
        super().__init__()

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
        r"""Gets the xss of this ListThreatsResponse.

        时间区间内xss攻击数量

        :return: The xss of this ListThreatsResponse.
        :rtype: int
        """
        return self._xss

    @xss.setter
    def xss(self, xss):
        r"""Sets the xss of this ListThreatsResponse.

        时间区间内xss攻击数量

        :param xss: The xss of this ListThreatsResponse.
        :type xss: int
        """
        self._xss = xss

    @property
    def sqli(self):
        r"""Gets the sqli of this ListThreatsResponse.

        时间区间内sqli攻击数量

        :return: The sqli of this ListThreatsResponse.
        :rtype: int
        """
        return self._sqli

    @sqli.setter
    def sqli(self, sqli):
        r"""Sets the sqli of this ListThreatsResponse.

        时间区间内sqli攻击数量

        :param sqli: The sqli of this ListThreatsResponse.
        :type sqli: int
        """
        self._sqli = sqli

    @property
    def cmdi(self):
        r"""Gets the cmdi of this ListThreatsResponse.

        时间区间内cmdi攻击数量

        :return: The cmdi of this ListThreatsResponse.
        :rtype: int
        """
        return self._cmdi

    @cmdi.setter
    def cmdi(self, cmdi):
        r"""Sets the cmdi of this ListThreatsResponse.

        时间区间内cmdi攻击数量

        :param cmdi: The cmdi of this ListThreatsResponse.
        :type cmdi: int
        """
        self._cmdi = cmdi

    @property
    def lfi(self):
        r"""Gets the lfi of this ListThreatsResponse.

        时间区间内lfi攻击数量

        :return: The lfi of this ListThreatsResponse.
        :rtype: int
        """
        return self._lfi

    @lfi.setter
    def lfi(self, lfi):
        r"""Sets the lfi of this ListThreatsResponse.

        时间区间内lfi攻击数量

        :param lfi: The lfi of this ListThreatsResponse.
        :type lfi: int
        """
        self._lfi = lfi

    @property
    def rfi(self):
        r"""Gets the rfi of this ListThreatsResponse.

        时间区间内rfi攻击数量

        :return: The rfi of this ListThreatsResponse.
        :rtype: int
        """
        return self._rfi

    @rfi.setter
    def rfi(self, rfi):
        r"""Sets the rfi of this ListThreatsResponse.

        时间区间内rfi攻击数量

        :param rfi: The rfi of this ListThreatsResponse.
        :type rfi: int
        """
        self._rfi = rfi

    @property
    def webshell(self):
        r"""Gets the webshell of this ListThreatsResponse.

        时间区间内webshell攻击数量

        :return: The webshell of this ListThreatsResponse.
        :rtype: int
        """
        return self._webshell

    @webshell.setter
    def webshell(self, webshell):
        r"""Sets the webshell of this ListThreatsResponse.

        时间区间内webshell攻击数量

        :param webshell: The webshell of this ListThreatsResponse.
        :type webshell: int
        """
        self._webshell = webshell

    @property
    def robot(self):
        r"""Gets the robot of this ListThreatsResponse.

        时间区间内恶意爬虫数量

        :return: The robot of this ListThreatsResponse.
        :rtype: int
        """
        return self._robot

    @robot.setter
    def robot(self, robot):
        r"""Sets the robot of this ListThreatsResponse.

        时间区间内恶意爬虫数量

        :param robot: The robot of this ListThreatsResponse.
        :type robot: int
        """
        self._robot = robot

    @property
    def cc(self):
        r"""Gets the cc of this ListThreatsResponse.

        时间区间内cc攻击数量

        :return: The cc of this ListThreatsResponse.
        :rtype: int
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this ListThreatsResponse.

        时间区间内cc攻击数量

        :param cc: The cc of this ListThreatsResponse.
        :type cc: int
        """
        self._cc = cc

    @property
    def custom(self):
        r"""Gets the custom of this ListThreatsResponse.

        时间区间内对自定义规则攻击数量

        :return: The custom of this ListThreatsResponse.
        :rtype: int
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        r"""Sets the custom of this ListThreatsResponse.

        时间区间内对自定义规则攻击数量

        :param custom: The custom of this ListThreatsResponse.
        :type custom: int
        """
        self._custom = custom

    @property
    def whiteblackip(self):
        r"""Gets the whiteblackip of this ListThreatsResponse.

        时间区间内对黑白名单规则攻击数量

        :return: The whiteblackip of this ListThreatsResponse.
        :rtype: int
        """
        return self._whiteblackip

    @whiteblackip.setter
    def whiteblackip(self, whiteblackip):
        r"""Sets the whiteblackip of this ListThreatsResponse.

        时间区间内对黑白名单规则攻击数量

        :param whiteblackip: The whiteblackip of this ListThreatsResponse.
        :type whiteblackip: int
        """
        self._whiteblackip = whiteblackip

    @property
    def antileakage(self):
        r"""Gets the antileakage of this ListThreatsResponse.

        时间区间内反泄漏数量

        :return: The antileakage of this ListThreatsResponse.
        :rtype: int
        """
        return self._antileakage

    @antileakage.setter
    def antileakage(self, antileakage):
        r"""Sets the antileakage of this ListThreatsResponse.

        时间区间内反泄漏数量

        :param antileakage: The antileakage of this ListThreatsResponse.
        :type antileakage: int
        """
        self._antileakage = antileakage

    @property
    def antitamper(self):
        r"""Gets the antitamper of this ListThreatsResponse.

        时间区间内防篡改数量

        :return: The antitamper of this ListThreatsResponse.
        :rtype: int
        """
        return self._antitamper

    @antitamper.setter
    def antitamper(self, antitamper):
        r"""Sets the antitamper of this ListThreatsResponse.

        时间区间内防篡改数量

        :param antitamper: The antitamper of this ListThreatsResponse.
        :type antitamper: int
        """
        self._antitamper = antitamper

    def to_dict(self):
        import warnings
        warnings.warn("ListThreatsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListThreatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
