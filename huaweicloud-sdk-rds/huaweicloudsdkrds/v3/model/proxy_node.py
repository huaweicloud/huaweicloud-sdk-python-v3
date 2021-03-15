# coding: utf-8

import pprint
import re

import six





class ProxyNode:


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
        'name': 'str',
        'role': 'str',
        'az_code': 'str',
        'status': 'str',
        'frozen_flag': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'az_code': 'az_code',
        'status': 'status',
        'frozen_flag': 'frozen_flag'
    }

    def __init__(self, id=None, name=None, role=None, az_code=None, status=None, frozen_flag=None):
        """ProxyNode - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._role = None
        self._az_code = None
        self._status = None
        self._frozen_flag = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.role = role
        self.az_code = az_code
        self.status = status
        self.frozen_flag = frozen_flag

    @property
    def id(self):
        """Gets the id of this ProxyNode.

        Proxy节点ID。

        :return: The id of this ProxyNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyNode.

        Proxy节点ID。

        :param id: The id of this ProxyNode.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProxyNode.

        Proxy节点名称。

        :return: The name of this ProxyNode.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProxyNode.

        Proxy节点名称。

        :param name: The name of this ProxyNode.
        :type: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this ProxyNode.

        Proxy节点角色。 包括master和slave。

        :return: The role of this ProxyNode.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ProxyNode.

        Proxy节点角色。 包括master和slave。

        :param role: The role of this ProxyNode.
        :type: str
        """
        self._role = role

    @property
    def az_code(self):
        """Gets the az_code of this ProxyNode.

        可用区。

        :return: The az_code of this ProxyNode.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this ProxyNode.

        可用区。

        :param az_code: The az_code of this ProxyNode.
        :type: str
        """
        self._az_code = az_code

    @property
    def status(self):
        """Gets the status of this ProxyNode.

        Proxy节点状态。

        :return: The status of this ProxyNode.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProxyNode.

        Proxy节点状态。

        :param status: The status of this ProxyNode.
        :type: str
        """
        self._status = status

    @property
    def frozen_flag(self):
        """Gets the frozen_flag of this ProxyNode.

        Proxy节点是否被冻结。 0表示未冻结，1表示冻结，2表示冻结删除。

        :return: The frozen_flag of this ProxyNode.
        :rtype: int
        """
        return self._frozen_flag

    @frozen_flag.setter
    def frozen_flag(self, frozen_flag):
        """Sets the frozen_flag of this ProxyNode.

        Proxy节点是否被冻结。 0表示未冻结，1表示冻结，2表示冻结删除。

        :param frozen_flag: The frozen_flag of this ProxyNode.
        :type: int
        """
        self._frozen_flag = frozen_flag

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProxyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
