# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IPAuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'auth_type': 'str',
        'ip_auth_list': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'auth_type': 'auth_type',
        'ip_auth_list': 'ip_auth_list'
    }

    def __init__(self, domain=None, auth_type=None, ip_auth_list=None):
        r"""IPAuthInfo

        The model defined in huaweicloud sdk

        :param domain: 推流域名或播放域名
        :type domain: str
        :param auth_type: 鉴权类型。 包含如下取值： - WHITE：IP白名单鉴权。 - BLACK：IP黑名单鉴权。 - NONE：不鉴权。 
        :type auth_type: str
        :param ip_auth_list: IP黑名单列表，IP之间用;分隔，如192.168.0.0;192.168.0.8，最多支持配置100个IP。支持IP网段添加，例如127.0.0.1/24表示采用子网掩码中的前24位为有效位，即用32-24&#x3D;8bit来表示主机号，该子网可以容纳2^8 - 2 &#x3D; 254 台主机。故127.0.0.1/24 表示IP网段范围是：127.0.0.1~127.0.0.255
        :type ip_auth_list: str
        """
        
        

        self._domain = None
        self._auth_type = None
        self._ip_auth_list = None
        self.discriminator = None

        self.domain = domain
        self.auth_type = auth_type
        self.ip_auth_list = ip_auth_list

    @property
    def domain(self):
        r"""Gets the domain of this IPAuthInfo.

        推流域名或播放域名

        :return: The domain of this IPAuthInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this IPAuthInfo.

        推流域名或播放域名

        :param domain: The domain of this IPAuthInfo.
        :type domain: str
        """
        self._domain = domain

    @property
    def auth_type(self):
        r"""Gets the auth_type of this IPAuthInfo.

        鉴权类型。 包含如下取值： - WHITE：IP白名单鉴权。 - BLACK：IP黑名单鉴权。 - NONE：不鉴权。 

        :return: The auth_type of this IPAuthInfo.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this IPAuthInfo.

        鉴权类型。 包含如下取值： - WHITE：IP白名单鉴权。 - BLACK：IP黑名单鉴权。 - NONE：不鉴权。 

        :param auth_type: The auth_type of this IPAuthInfo.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def ip_auth_list(self):
        r"""Gets the ip_auth_list of this IPAuthInfo.

        IP黑名单列表，IP之间用;分隔，如192.168.0.0;192.168.0.8，最多支持配置100个IP。支持IP网段添加，例如127.0.0.1/24表示采用子网掩码中的前24位为有效位，即用32-24=8bit来表示主机号，该子网可以容纳2^8 - 2 = 254 台主机。故127.0.0.1/24 表示IP网段范围是：127.0.0.1~127.0.0.255

        :return: The ip_auth_list of this IPAuthInfo.
        :rtype: str
        """
        return self._ip_auth_list

    @ip_auth_list.setter
    def ip_auth_list(self, ip_auth_list):
        r"""Sets the ip_auth_list of this IPAuthInfo.

        IP黑名单列表，IP之间用;分隔，如192.168.0.0;192.168.0.8，最多支持配置100个IP。支持IP网段添加，例如127.0.0.1/24表示采用子网掩码中的前24位为有效位，即用32-24=8bit来表示主机号，该子网可以容纳2^8 - 2 = 254 台主机。故127.0.0.1/24 表示IP网段范围是：127.0.0.1~127.0.0.255

        :param ip_auth_list: The ip_auth_list of this IPAuthInfo.
        :type ip_auth_list: str
        """
        self._ip_auth_list = ip_auth_list

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
        if not isinstance(other, IPAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
