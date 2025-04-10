# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainRealServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'real_server_type': 'int',
        'real_servers': 'str'
    }

    attribute_map = {
        'real_server_type': 'real_server_type',
        'real_servers': 'real_servers'
    }

    def __init__(self, real_server_type=None, real_servers=None):
        r"""DomainRealServerInfo

        The model defined in huaweicloud sdk

        :param real_server_type: 源站类型
        :type real_server_type: int
        :param real_servers: 源站
        :type real_servers: str
        """
        
        

        self._real_server_type = None
        self._real_servers = None
        self.discriminator = None

        if real_server_type is not None:
            self.real_server_type = real_server_type
        if real_servers is not None:
            self.real_servers = real_servers

    @property
    def real_server_type(self):
        r"""Gets the real_server_type of this DomainRealServerInfo.

        源站类型

        :return: The real_server_type of this DomainRealServerInfo.
        :rtype: int
        """
        return self._real_server_type

    @real_server_type.setter
    def real_server_type(self, real_server_type):
        r"""Sets the real_server_type of this DomainRealServerInfo.

        源站类型

        :param real_server_type: The real_server_type of this DomainRealServerInfo.
        :type real_server_type: int
        """
        self._real_server_type = real_server_type

    @property
    def real_servers(self):
        r"""Gets the real_servers of this DomainRealServerInfo.

        源站

        :return: The real_servers of this DomainRealServerInfo.
        :rtype: str
        """
        return self._real_servers

    @real_servers.setter
    def real_servers(self, real_servers):
        r"""Sets the real_servers of this DomainRealServerInfo.

        源站

        :param real_servers: The real_servers of this DomainRealServerInfo.
        :type real_servers: str
        """
        self._real_servers = real_servers

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
        if not isinstance(other, DomainRealServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
