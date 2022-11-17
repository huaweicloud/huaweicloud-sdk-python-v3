# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyTokenDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_token': 'str',
        'long_access_token': 'str',
        'valid_period': 'int',
        'middle_end_url': 'str',
        'middle_end_inner_url': 'str',
        'enable_rerouting': 'bool'
    }

    attribute_map = {
        'access_token': 'accessToken',
        'long_access_token': 'longAccessToken',
        'valid_period': 'validPeriod',
        'middle_end_url': 'middleEndUrl',
        'middle_end_inner_url': 'middleEndInnerUrl',
        'enable_rerouting': 'enableRerouting'
    }

    def __init__(self, access_token=None, long_access_token=None, valid_period=None, middle_end_url=None, middle_end_inner_url=None, enable_rerouting=None):
        """ProxyTokenDTO

        The model defined in huaweicloud sdk

        :param access_token: 代理鉴权服务器的短token字符串。
        :type access_token: str
        :param long_access_token: 代理鉴权服务器的长token字符串。
        :type long_access_token: str
        :param valid_period: Token有效时长，单位：秒。
        :type valid_period: int
        :param middle_end_url: 中台地址。
        :type middle_end_url: str
        :param middle_end_inner_url: 中台内网地址。
        :type middle_end_inner_url: str
        :param enable_rerouting: 是否开启二次路由。
        :type enable_rerouting: bool
        """
        
        

        self._access_token = None
        self._long_access_token = None
        self._valid_period = None
        self._middle_end_url = None
        self._middle_end_inner_url = None
        self._enable_rerouting = None
        self.discriminator = None

        self.access_token = access_token
        if long_access_token is not None:
            self.long_access_token = long_access_token
        if valid_period is not None:
            self.valid_period = valid_period
        if middle_end_url is not None:
            self.middle_end_url = middle_end_url
        if middle_end_inner_url is not None:
            self.middle_end_inner_url = middle_end_inner_url
        if enable_rerouting is not None:
            self.enable_rerouting = enable_rerouting

    @property
    def access_token(self):
        """Gets the access_token of this ProxyTokenDTO.

        代理鉴权服务器的短token字符串。

        :return: The access_token of this ProxyTokenDTO.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ProxyTokenDTO.

        代理鉴权服务器的短token字符串。

        :param access_token: The access_token of this ProxyTokenDTO.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def long_access_token(self):
        """Gets the long_access_token of this ProxyTokenDTO.

        代理鉴权服务器的长token字符串。

        :return: The long_access_token of this ProxyTokenDTO.
        :rtype: str
        """
        return self._long_access_token

    @long_access_token.setter
    def long_access_token(self, long_access_token):
        """Sets the long_access_token of this ProxyTokenDTO.

        代理鉴权服务器的长token字符串。

        :param long_access_token: The long_access_token of this ProxyTokenDTO.
        :type long_access_token: str
        """
        self._long_access_token = long_access_token

    @property
    def valid_period(self):
        """Gets the valid_period of this ProxyTokenDTO.

        Token有效时长，单位：秒。

        :return: The valid_period of this ProxyTokenDTO.
        :rtype: int
        """
        return self._valid_period

    @valid_period.setter
    def valid_period(self, valid_period):
        """Sets the valid_period of this ProxyTokenDTO.

        Token有效时长，单位：秒。

        :param valid_period: The valid_period of this ProxyTokenDTO.
        :type valid_period: int
        """
        self._valid_period = valid_period

    @property
    def middle_end_url(self):
        """Gets the middle_end_url of this ProxyTokenDTO.

        中台地址。

        :return: The middle_end_url of this ProxyTokenDTO.
        :rtype: str
        """
        return self._middle_end_url

    @middle_end_url.setter
    def middle_end_url(self, middle_end_url):
        """Sets the middle_end_url of this ProxyTokenDTO.

        中台地址。

        :param middle_end_url: The middle_end_url of this ProxyTokenDTO.
        :type middle_end_url: str
        """
        self._middle_end_url = middle_end_url

    @property
    def middle_end_inner_url(self):
        """Gets the middle_end_inner_url of this ProxyTokenDTO.

        中台内网地址。

        :return: The middle_end_inner_url of this ProxyTokenDTO.
        :rtype: str
        """
        return self._middle_end_inner_url

    @middle_end_inner_url.setter
    def middle_end_inner_url(self, middle_end_inner_url):
        """Sets the middle_end_inner_url of this ProxyTokenDTO.

        中台内网地址。

        :param middle_end_inner_url: The middle_end_inner_url of this ProxyTokenDTO.
        :type middle_end_inner_url: str
        """
        self._middle_end_inner_url = middle_end_inner_url

    @property
    def enable_rerouting(self):
        """Gets the enable_rerouting of this ProxyTokenDTO.

        是否开启二次路由。

        :return: The enable_rerouting of this ProxyTokenDTO.
        :rtype: bool
        """
        return self._enable_rerouting

    @enable_rerouting.setter
    def enable_rerouting(self, enable_rerouting):
        """Sets the enable_rerouting of this ProxyTokenDTO.

        是否开启二次路由。

        :param enable_rerouting: The enable_rerouting of this ProxyTokenDTO.
        :type enable_rerouting: bool
        """
        self._enable_rerouting = enable_rerouting

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
        if not isinstance(other, ProxyTokenDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
