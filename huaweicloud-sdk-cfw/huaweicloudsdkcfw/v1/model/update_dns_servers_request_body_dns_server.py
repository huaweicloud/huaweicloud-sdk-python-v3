# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDnsServersRequestBodyDnsServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ip': 'str',
        'is_customized': 'int',
        'is_applied': 'int'
    }

    attribute_map = {
        'server_ip': 'server_ip',
        'is_customized': 'is_customized',
        'is_applied': 'is_applied'
    }

    def __init__(self, server_ip=None, is_customized=None, is_applied=None):
        r"""UpdateDnsServersRequestBodyDnsServer

        The model defined in huaweicloud sdk

        :param server_ip: DNS服务器IP，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.server_ip（.表示各对象之间层级的区分）获得。
        :type server_ip: str
        :param is_customized: 是否是用户自定义的dns服务器，0否 1是
        :type is_customized: int
        :param is_applied: 是否应用，0否 1是
        :type is_applied: int
        """
        
        

        self._server_ip = None
        self._is_customized = None
        self._is_applied = None
        self.discriminator = None

        self.server_ip = server_ip
        self.is_customized = is_customized
        self.is_applied = is_applied

    @property
    def server_ip(self):
        r"""Gets the server_ip of this UpdateDnsServersRequestBodyDnsServer.

        DNS服务器IP，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.server_ip（.表示各对象之间层级的区分）获得。

        :return: The server_ip of this UpdateDnsServersRequestBodyDnsServer.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this UpdateDnsServersRequestBodyDnsServer.

        DNS服务器IP，可通过[查询dns服务器列表接口](ListDnsServers.xml)查询获得，通过返回值中的data.server_ip（.表示各对象之间层级的区分）获得。

        :param server_ip: The server_ip of this UpdateDnsServersRequestBodyDnsServer.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def is_customized(self):
        r"""Gets the is_customized of this UpdateDnsServersRequestBodyDnsServer.

        是否是用户自定义的dns服务器，0否 1是

        :return: The is_customized of this UpdateDnsServersRequestBodyDnsServer.
        :rtype: int
        """
        return self._is_customized

    @is_customized.setter
    def is_customized(self, is_customized):
        r"""Sets the is_customized of this UpdateDnsServersRequestBodyDnsServer.

        是否是用户自定义的dns服务器，0否 1是

        :param is_customized: The is_customized of this UpdateDnsServersRequestBodyDnsServer.
        :type is_customized: int
        """
        self._is_customized = is_customized

    @property
    def is_applied(self):
        r"""Gets the is_applied of this UpdateDnsServersRequestBodyDnsServer.

        是否应用，0否 1是

        :return: The is_applied of this UpdateDnsServersRequestBodyDnsServer.
        :rtype: int
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        r"""Sets the is_applied of this UpdateDnsServersRequestBodyDnsServer.

        是否应用，0否 1是

        :param is_applied: The is_applied of this UpdateDnsServersRequestBodyDnsServer.
        :type is_applied: int
        """
        self._is_applied = is_applied

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
        if not isinstance(other, UpdateDnsServersRequestBodyDnsServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
