# coding: utf-8

import pprint
import re

import six





class DataVolumeMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'system__cmkid': 'str',
        'system__encrypted': 'str'
    }

    attribute_map = {
        'system__cmkid': '__system__cmkid',
        'system__encrypted': '__system__encrypted'
    }

    def __init__(self, system__cmkid=None, system__encrypted=None):
        """DataVolumeMetadata - a model defined in huaweicloud sdk"""
        
        

        self._system__cmkid = None
        self._system__encrypted = None
        self.discriminator = None

        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if system__encrypted is not None:
            self.system__encrypted = system__encrypted

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this DataVolumeMetadata.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。

        :return: The system__cmkid of this DataVolumeMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this DataVolumeMetadata.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。

        :param system__cmkid: The system__cmkid of this DataVolumeMetadata.
        :type: str
        """
        self._system__cmkid = system__cmkid

    @property
    def system__encrypted(self):
        """Gets the system__encrypted of this DataVolumeMetadata.

        表示云硬盘加密功能的字段，'0'代表不加密，'1'代表加密。  该字段不存在时，云硬盘默认为不加密。

        :return: The system__encrypted of this DataVolumeMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this DataVolumeMetadata.

        表示云硬盘加密功能的字段，'0'代表不加密，'1'代表加密。  该字段不存在时，云硬盘默认为不加密。

        :param system__encrypted: The system__encrypted of this DataVolumeMetadata.
        :type: str
        """
        self._system__encrypted = system__encrypted

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
        if not isinstance(other, DataVolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
