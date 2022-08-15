# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficMark:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sip': 'list[str]',
        'cookie': 'str',
        'params': 'str'
    }

    attribute_map = {
        'sip': 'sip',
        'cookie': 'cookie',
        'params': 'params'
    }

    def __init__(self, sip=None, cookie=None, params=None):
        """TrafficMark

        The model defined in huaweicloud sdk

        :param sip: IP标记，客户端最原始的IP地址的HTTP请求头字段。
        :type sip: list[str]
        :param cookie: Session标记，用于Cookie恶意请求的攻击惩罚功能。在选择Cookie拦截的攻击惩罚功能前，必须配置该标识
        :type cookie: str
        :param params: User标记，用于Params恶意请求的攻击惩罚功能。在选择Params拦截的攻击惩罚功能前，必须配置该标识。
        :type params: str
        """
        
        

        self._sip = None
        self._cookie = None
        self._params = None
        self.discriminator = None

        if sip is not None:
            self.sip = sip
        if cookie is not None:
            self.cookie = cookie
        if params is not None:
            self.params = params

    @property
    def sip(self):
        """Gets the sip of this TrafficMark.

        IP标记，客户端最原始的IP地址的HTTP请求头字段。

        :return: The sip of this TrafficMark.
        :rtype: list[str]
        """
        return self._sip

    @sip.setter
    def sip(self, sip):
        """Sets the sip of this TrafficMark.

        IP标记，客户端最原始的IP地址的HTTP请求头字段。

        :param sip: The sip of this TrafficMark.
        :type sip: list[str]
        """
        self._sip = sip

    @property
    def cookie(self):
        """Gets the cookie of this TrafficMark.

        Session标记，用于Cookie恶意请求的攻击惩罚功能。在选择Cookie拦截的攻击惩罚功能前，必须配置该标识

        :return: The cookie of this TrafficMark.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """Sets the cookie of this TrafficMark.

        Session标记，用于Cookie恶意请求的攻击惩罚功能。在选择Cookie拦截的攻击惩罚功能前，必须配置该标识

        :param cookie: The cookie of this TrafficMark.
        :type cookie: str
        """
        self._cookie = cookie

    @property
    def params(self):
        """Gets the params of this TrafficMark.

        User标记，用于Params恶意请求的攻击惩罚功能。在选择Params拦截的攻击惩罚功能前，必须配置该标识。

        :return: The params of this TrafficMark.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this TrafficMark.

        User标记，用于Params恶意请求的攻击惩罚功能。在选择Params拦截的攻击惩罚功能前，必须配置该标识。

        :param params: The params of this TrafficMark.
        :type params: str
        """
        self._params = params

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
        if not isinstance(other, TrafficMark):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
