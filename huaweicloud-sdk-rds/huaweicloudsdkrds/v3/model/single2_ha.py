# coding: utf-8

import pprint
import re

import six





class Single2Ha:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'az_code_new_node': 'str',
        'password': 'str',
        'dsspool_id': 'str'
    }

    attribute_map = {
        'az_code_new_node': 'az_code_new_node',
        'password': 'password',
        'dsspool_id': 'dsspool_id'
    }

    def __init__(self, az_code_new_node=None, password=None, dsspool_id=None):
        """Single2Ha - a model defined in huaweicloud sdk"""
        
        

        self._az_code_new_node = None
        self._password = None
        self._dsspool_id = None
        self.discriminator = None

        self.az_code_new_node = az_code_new_node
        if password is not None:
            self.password = password
        if dsspool_id is not None:
            self.dsspool_id = dsspool_id

    @property
    def az_code_new_node(self):
        """Gets the az_code_new_node of this Single2Ha.

        实例节点可用区码（AZ）。

        :return: The az_code_new_node of this Single2Ha.
        :rtype: str
        """
        return self._az_code_new_node

    @az_code_new_node.setter
    def az_code_new_node(self, az_code_new_node):
        """Sets the az_code_new_node of this Single2Ha.

        实例节点可用区码（AZ）。

        :param az_code_new_node: The az_code_new_node of this Single2Ha.
        :type: str
        """
        self._az_code_new_node = az_code_new_node

    @property
    def password(self):
        """Gets the password of this Single2Ha.

        仅在支持SQL Server数据库实例进行单机转主备时必选，有效。

        :return: The password of this Single2Ha.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Single2Ha.

        仅在支持SQL Server数据库实例进行单机转主备时必选，有效。

        :param password: The password of this Single2Ha.
        :type: str
        """
        self._password = password

    @property
    def dsspool_id(self):
        """Gets the dsspool_id of this Single2Ha.

        创建新节点所在专属存储池ID，仅专属云创建实例时有效。

        :return: The dsspool_id of this Single2Ha.
        :rtype: str
        """
        return self._dsspool_id

    @dsspool_id.setter
    def dsspool_id(self, dsspool_id):
        """Sets the dsspool_id of this Single2Ha.

        创建新节点所在专属存储池ID，仅专属云创建实例时有效。

        :param dsspool_id: The dsspool_id of this Single2Ha.
        :type: str
        """
        self._dsspool_id = dsspool_id

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
        if not isinstance(other, Single2Ha):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
