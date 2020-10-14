# coding: utf-8

import pprint
import re

import six





class AddReplicationBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'az_code': 'str'
    }

    attribute_map = {
        'az_code': 'az_code'
    }

    def __init__(self, az_code=None):
        """AddReplicationBody - a model defined in huaweicloud sdk"""
        
        

        self._az_code = None
        self.discriminator = None

        if az_code is not None:
            self.az_code = az_code

    @property
    def az_code(self):
        """Gets the az_code of this AddReplicationBody.

        表示指定副本所在的可用区编码。 可用区编码可通过[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html)接口查询，可用区必须是有资源的，否则添加失败。 

        :return: The az_code of this AddReplicationBody.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this AddReplicationBody.

        表示指定副本所在的可用区编码。 可用区编码可通过[查询可用区信息](https://support.huaweicloud.com/api-dcs/ListAvailableZones.html)接口查询，可用区必须是有资源的，否则添加失败。 

        :param az_code: The az_code of this AddReplicationBody.
        :type: str
        """
        self._az_code = az_code

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
        if not isinstance(other, AddReplicationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
