# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Address:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intranet_ip': 'str',
        'access_ip': 'str',
        'server_ip': 'str',
        'public_ip': 'str'
    }

    attribute_map = {
        'intranet_ip': 'intranet_ip',
        'access_ip': 'access_ip',
        'server_ip': 'server_ip',
        'public_ip': 'public_ip'
    }

    def __init__(self, intranet_ip=None, access_ip=None, server_ip=None, public_ip=None):
        r"""Address

        The model defined in huaweicloud sdk

        :param intranet_ip: 云手机服务器的内网IP，过期字段。
        :type intranet_ip: str
        :param access_ip: 云手机服务器的公网IP，过期字段。
        :type access_ip: str
        :param server_ip: 云手机服务器的内网IP，新增字段。
        :type server_ip: str
        :param public_ip: 云手机服务器的公网IP，新增字段。
        :type public_ip: str
        """
        
        

        self._intranet_ip = None
        self._access_ip = None
        self._server_ip = None
        self._public_ip = None
        self.discriminator = None

        if intranet_ip is not None:
            self.intranet_ip = intranet_ip
        if access_ip is not None:
            self.access_ip = access_ip
        if server_ip is not None:
            self.server_ip = server_ip
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def intranet_ip(self):
        r"""Gets the intranet_ip of this Address.

        云手机服务器的内网IP，过期字段。

        :return: The intranet_ip of this Address.
        :rtype: str
        """
        return self._intranet_ip

    @intranet_ip.setter
    def intranet_ip(self, intranet_ip):
        r"""Sets the intranet_ip of this Address.

        云手机服务器的内网IP，过期字段。

        :param intranet_ip: The intranet_ip of this Address.
        :type intranet_ip: str
        """
        self._intranet_ip = intranet_ip

    @property
    def access_ip(self):
        r"""Gets the access_ip of this Address.

        云手机服务器的公网IP，过期字段。

        :return: The access_ip of this Address.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        r"""Sets the access_ip of this Address.

        云手机服务器的公网IP，过期字段。

        :param access_ip: The access_ip of this Address.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def server_ip(self):
        r"""Gets the server_ip of this Address.

        云手机服务器的内网IP，新增字段。

        :return: The server_ip of this Address.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this Address.

        云手机服务器的内网IP，新增字段。

        :param server_ip: The server_ip of this Address.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this Address.

        云手机服务器的公网IP，新增字段。

        :return: The public_ip of this Address.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this Address.

        云手机服务器的公网IP，新增字段。

        :param public_ip: The public_ip of this Address.
        :type public_ip: str
        """
        self._public_ip = public_ip

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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
