# coding: utf-8

import pprint
import re

import six





class SecurityGroupsInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        """SecurityGroupsInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self.discriminator = None

        if id is not None:
            self.id = id

    @property
    def id(self):
        """Gets the id of this SecurityGroupsInfo.

        裸金属服务器对应的安全组ID，对创建裸金属服务器中配置的所有网卡生效。当该参数未指定时默认给裸金属服务器绑定default安全组。当该参数传值（UUID格式）时需要指定已有安全组的ID。获取已有安全组的方法请参见《虚拟私有云API参考》的“查询安全组列表”章节。

        :return: The id of this SecurityGroupsInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SecurityGroupsInfo.

        裸金属服务器对应的安全组ID，对创建裸金属服务器中配置的所有网卡生效。当该参数未指定时默认给裸金属服务器绑定default安全组。当该参数传值（UUID格式）时需要指定已有安全组的ID。获取已有安全组的方法请参见《虚拟私有云API参考》的“查询安全组列表”章节。

        :param id: The id of this SecurityGroupsInfo.
        :type: str
        """
        self._id = id

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
        if not isinstance(other, SecurityGroupsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
