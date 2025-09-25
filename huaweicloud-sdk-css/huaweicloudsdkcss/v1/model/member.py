# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Member:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'address': 'str',
        'protocol_port': 'int',
        'operating_status': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'operating_status': 'operating_status',
        'instance_id': 'instance_id'
    }

    def __init__(self, name=None, address=None, protocol_port=None, operating_status=None, instance_id=None):
        r"""Member

        The model defined in huaweicloud sdk

        :param name: 后端服务器名称。
        :type name: str
        :param address: 后端服务器对应的IP地址。
        :type address: str
        :param protocol_port: 后端服务器业务端口号。
        :type protocol_port: int
        :param operating_status: 后端云服务器的健康状态。
        :type operating_status: str
        :param instance_id: member关联的实例ID。
        :type instance_id: str
        """
        
        

        self._name = None
        self._address = None
        self._protocol_port = None
        self._operating_status = None
        self._instance_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if operating_status is not None:
            self.operating_status = operating_status
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this Member.

        后端服务器名称。

        :return: The name of this Member.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Member.

        后端服务器名称。

        :param name: The name of this Member.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        r"""Gets the address of this Member.

        后端服务器对应的IP地址。

        :return: The address of this Member.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this Member.

        后端服务器对应的IP地址。

        :param address: The address of this Member.
        :type address: str
        """
        self._address = address

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this Member.

        后端服务器业务端口号。

        :return: The protocol_port of this Member.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this Member.

        后端服务器业务端口号。

        :param protocol_port: The protocol_port of this Member.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def operating_status(self):
        r"""Gets the operating_status of this Member.

        后端云服务器的健康状态。

        :return: The operating_status of this Member.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this Member.

        后端云服务器的健康状态。

        :param operating_status: The operating_status of this Member.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Member.

        member关联的实例ID。

        :return: The instance_id of this Member.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Member.

        member关联的实例ID。

        :param instance_id: The instance_id of this Member.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
