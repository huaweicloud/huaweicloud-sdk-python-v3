# coding: utf-8

import pprint
import re

import six





class PublicIp:


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
        'eip': 'Eip'
    }

    attribute_map = {
        'id': 'id',
        'eip': 'eip'
    }

    def __init__(self, id=None, eip=None):
        """PublicIp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._eip = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if eip is not None:
            self.eip = eip

    @property
    def id(self):
        """Gets the id of this PublicIp.

        创建裸金属服务器分配已有弹性公网IP时，分配的弹性公网IP的ID，UUID格式。弹性公网IP的ID可以从网络控制台或者参考《虚拟私有云API参考》的“查询弹性公网IP列表”章节获取。约束：只能分配状态（status）为DOWN的弹性公网IP。批量创建裸金属服务器时，不能使用已有弹性公网IP，即不支持此参数。

        :return: The id of this PublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicIp.

        创建裸金属服务器分配已有弹性公网IP时，分配的弹性公网IP的ID，UUID格式。弹性公网IP的ID可以从网络控制台或者参考《虚拟私有云API参考》的“查询弹性公网IP列表”章节获取。约束：只能分配状态（status）为DOWN的弹性公网IP。批量创建裸金属服务器时，不能使用已有弹性公网IP，即不支持此参数。

        :param id: The id of this PublicIp.
        :type: str
        """
        self._id = id

    @property
    def eip(self):
        """Gets the eip of this PublicIp.


        :return: The eip of this PublicIp.
        :rtype: Eip
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        """Sets the eip of this PublicIp.


        :param eip: The eip of this PublicIp.
        :type: Eip
        """
        self._eip = eip

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
        if not isinstance(other, PublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
