# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EncryptDataNodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'state': 'str',
        'name': 'str',
        'host_name': 'str',
        'host_ips': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'name': 'name',
        'host_name': 'host_name',
        'host_ips': 'host_ips'
    }

    def __init__(self, id=None, state=None, name=None, host_name=None, host_ips=None):
        """EncryptDataNodes

        The model defined in huaweicloud sdk

        :param id: 边缘节点ID
        :type id: str
        :param state: 边缘节点状态
        :type state: str
        :param name: 边缘节点名称
        :type name: str
        :param host_name: 边缘节点主机名
        :type host_name: str
        :param host_ips: 边缘节点主机IP地址列表
        :type host_ips: list[str]
        """
        
        

        self._id = None
        self._state = None
        self._name = None
        self._host_name = None
        self._host_ips = None
        self.discriminator = None

        self.id = id
        self.state = state
        self.name = name
        self.host_name = host_name
        self.host_ips = host_ips

    @property
    def id(self):
        """Gets the id of this EncryptDataNodes.

        边缘节点ID

        :return: The id of this EncryptDataNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EncryptDataNodes.

        边缘节点ID

        :param id: The id of this EncryptDataNodes.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this EncryptDataNodes.

        边缘节点状态

        :return: The state of this EncryptDataNodes.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EncryptDataNodes.

        边缘节点状态

        :param state: The state of this EncryptDataNodes.
        :type state: str
        """
        self._state = state

    @property
    def name(self):
        """Gets the name of this EncryptDataNodes.

        边缘节点名称

        :return: The name of this EncryptDataNodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EncryptDataNodes.

        边缘节点名称

        :param name: The name of this EncryptDataNodes.
        :type name: str
        """
        self._name = name

    @property
    def host_name(self):
        """Gets the host_name of this EncryptDataNodes.

        边缘节点主机名

        :return: The host_name of this EncryptDataNodes.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this EncryptDataNodes.

        边缘节点主机名

        :param host_name: The host_name of this EncryptDataNodes.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ips(self):
        """Gets the host_ips of this EncryptDataNodes.

        边缘节点主机IP地址列表

        :return: The host_ips of this EncryptDataNodes.
        :rtype: list[str]
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        """Sets the host_ips of this EncryptDataNodes.

        边缘节点主机IP地址列表

        :param host_ips: The host_ips of this EncryptDataNodes.
        :type host_ips: list[str]
        """
        self._host_ips = host_ips

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
        if not isinstance(other, EncryptDataNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
