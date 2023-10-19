# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsServersResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'is_applied': 'int',
        'is_customized': 'int',
        'server_ip': 'str',
        'health_check_domain_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'is_applied': 'is_applied',
        'is_customized': 'is_customized',
        'server_ip': 'server_ip',
        'health_check_domain_name': 'health_check_domain_name'
    }

    def __init__(self, id=None, is_applied=None, is_customized=None, server_ip=None, health_check_domain_name=None):
        """DnsServersResponseDTO

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param is_applied: 是否应用，0否 1是
        :type is_applied: int
        :param is_customized: 是否是用户自定义的dns服务器，0否 1是
        :type is_customized: int
        :param server_ip: DNS服务器IP
        :type server_ip: str
        :param health_check_domain_name: 健康检查域名
        :type health_check_domain_name: str
        """
        
        

        self._id = None
        self._is_applied = None
        self._is_customized = None
        self._server_ip = None
        self._health_check_domain_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_applied is not None:
            self.is_applied = is_applied
        if is_customized is not None:
            self.is_customized = is_customized
        if server_ip is not None:
            self.server_ip = server_ip
        if health_check_domain_name is not None:
            self.health_check_domain_name = health_check_domain_name

    @property
    def id(self):
        """Gets the id of this DnsServersResponseDTO.

        id

        :return: The id of this DnsServersResponseDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DnsServersResponseDTO.

        id

        :param id: The id of this DnsServersResponseDTO.
        :type id: int
        """
        self._id = id

    @property
    def is_applied(self):
        """Gets the is_applied of this DnsServersResponseDTO.

        是否应用，0否 1是

        :return: The is_applied of this DnsServersResponseDTO.
        :rtype: int
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        """Sets the is_applied of this DnsServersResponseDTO.

        是否应用，0否 1是

        :param is_applied: The is_applied of this DnsServersResponseDTO.
        :type is_applied: int
        """
        self._is_applied = is_applied

    @property
    def is_customized(self):
        """Gets the is_customized of this DnsServersResponseDTO.

        是否是用户自定义的dns服务器，0否 1是

        :return: The is_customized of this DnsServersResponseDTO.
        :rtype: int
        """
        return self._is_customized

    @is_customized.setter
    def is_customized(self, is_customized):
        """Sets the is_customized of this DnsServersResponseDTO.

        是否是用户自定义的dns服务器，0否 1是

        :param is_customized: The is_customized of this DnsServersResponseDTO.
        :type is_customized: int
        """
        self._is_customized = is_customized

    @property
    def server_ip(self):
        """Gets the server_ip of this DnsServersResponseDTO.

        DNS服务器IP

        :return: The server_ip of this DnsServersResponseDTO.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        """Sets the server_ip of this DnsServersResponseDTO.

        DNS服务器IP

        :param server_ip: The server_ip of this DnsServersResponseDTO.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def health_check_domain_name(self):
        """Gets the health_check_domain_name of this DnsServersResponseDTO.

        健康检查域名

        :return: The health_check_domain_name of this DnsServersResponseDTO.
        :rtype: str
        """
        return self._health_check_domain_name

    @health_check_domain_name.setter
    def health_check_domain_name(self, health_check_domain_name):
        """Sets the health_check_domain_name of this DnsServersResponseDTO.

        健康检查域名

        :param health_check_domain_name: The health_check_domain_name of this DnsServersResponseDTO.
        :type health_check_domain_name: str
        """
        self._health_check_domain_name = health_check_domain_name

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
        if not isinstance(other, DnsServersResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
