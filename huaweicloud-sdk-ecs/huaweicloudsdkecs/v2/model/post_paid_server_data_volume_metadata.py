# coding: utf-8

import pprint
import re

import six





class PostPaidServerDataVolumeMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'system_encrypted': 'str',
        'system_cmkid': 'str'
    }

    attribute_map = {
        'system_encrypted': '__system__encrypted',
        'system_cmkid': '__system__cmkid'
    }

    def __init__(self, system_encrypted='0', system_cmkid=None):
        """PostPaidServerDataVolumeMetadata - a model defined in huaweicloud sdk"""
        
        

        self._system_encrypted = None
        self._system_cmkid = None
        self.discriminator = None

        if system_encrypted is not None:
            self.system_encrypted = system_encrypted
        if system_cmkid is not None:
            self.system_cmkid = system_cmkid

    @property
    def system_encrypted(self):
        """Gets the system_encrypted of this PostPaidServerDataVolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。

        :return: The system_encrypted of this PostPaidServerDataVolumeMetadata.
        :rtype: str
        """
        return self._system_encrypted

    @system_encrypted.setter
    def system_encrypted(self, system_encrypted):
        """Sets the system_encrypted of this PostPaidServerDataVolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。

        :param system_encrypted: The system_encrypted of this PostPaidServerDataVolumeMetadata.
        :type: str
        """
        self._system_encrypted = system_encrypted

    @property
    def system_cmkid(self):
        """Gets the system_cmkid of this PostPaidServerDataVolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。

        :return: The system_cmkid of this PostPaidServerDataVolumeMetadata.
        :rtype: str
        """
        return self._system_cmkid

    @system_cmkid.setter
    def system_cmkid(self, system_cmkid):
        """Sets the system_cmkid of this PostPaidServerDataVolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。

        :param system_cmkid: The system_cmkid of this PostPaidServerDataVolumeMetadata.
        :type: str
        """
        self._system_cmkid = system_cmkid

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
        if not isinstance(other, PostPaidServerDataVolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
