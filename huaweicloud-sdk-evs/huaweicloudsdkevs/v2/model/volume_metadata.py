# coding: utf-8

import pprint
import re

import six


class VolumeMetadata(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'system_cmkid': 'str',
        'system_encrypted': 'str',
        'full_clone': 'str',
        'hwpassthrough': 'str'
    }

    attribute_map = {
        'system_cmkid': '__system__cmkid',
        'system_encrypted': '__system__encrypted',
        'full_clone': 'full_clone',
        'hwpassthrough': 'hw:passthrough'
    }

    def __init__(self, system_cmkid=None, system_encrypted=None, full_clone=None, hwpassthrough=None):  # noqa: E501
        """VolumeMetadata - a model defined in huaweicloud sdk"""

        self._system_cmkid = None
        self._system_encrypted = None
        self._full_clone = None
        self._hwpassthrough = None
        self.discriminator = None

        if system_cmkid is not None:
            self.system_cmkid = system_cmkid
        if system_encrypted is not None:
            self.system_encrypted = system_encrypted
        if full_clone is not None:
            self.full_clone = full_clone
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough

    @property
    def system_cmkid(self):
        """Gets the system_cmkid of this VolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。  说明： 请参考 [查询密钥列表](https://support.huaweicloud.com/api-dew/dew_02_0017.html)，通过HTTPS请求获取密钥ID。

        :return: The system_cmkid of this VolumeMetadata.
        :rtype: str
        """
        return self._system_cmkid

    @system_cmkid.setter
    def system_cmkid(self, system_cmkid):
        """Sets the system_cmkid of this VolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。  说明： 请参考 [查询密钥列表](https://support.huaweicloud.com/api-dew/dew_02_0017.html)，通过HTTPS请求获取密钥ID。

        :param system_cmkid: The system_cmkid of this VolumeMetadata.
        :type: str
        """
        self._system_cmkid = system_cmkid

    @property
    def system_encrypted(self):
        """Gets the system_encrypted of this VolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。 该字段不存在时，云硬盘默认为不加密。

        :return: The system_encrypted of this VolumeMetadata.
        :rtype: str
        """
        return self._system_encrypted

    @system_encrypted.setter
    def system_encrypted(self, system_encrypted):
        """Sets the system_encrypted of this VolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。 该字段不存在时，云硬盘默认为不加密。

        :param system_encrypted: The system_encrypted of this VolumeMetadata.
        :type: str
        """
        self._system_encrypted = system_encrypted

    @property
    def full_clone(self):
        """Gets the full_clone of this VolumeMetadata.

        从快照创建云硬盘时，如需使用link克隆方式，请指定该字段的值为0。

        :return: The full_clone of this VolumeMetadata.
        :rtype: str
        """
        return self._full_clone

    @full_clone.setter
    def full_clone(self, full_clone):
        """Sets the full_clone of this VolumeMetadata.

        从快照创建云硬盘时，如需使用link克隆方式，请指定该字段的值为0。

        :param full_clone: The full_clone of this VolumeMetadata.
        :type: str
        """
        self._full_clone = full_clone

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this VolumeMetadata.

        true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 该字段不存在时，云硬盘默认为VBD类型。  >说明： >当shareable参数值设置为true，不指定hw:passthrough参数值时，创建的云硬盘为VBD类型共享云硬盘。

        :return: The hwpassthrough of this VolumeMetadata.
        :rtype: str
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this VolumeMetadata.

        true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 该字段不存在时，云硬盘默认为VBD类型。  >说明： >当shareable参数值设置为true，不指定hw:passthrough参数值时，创建的云硬盘为VBD类型共享云硬盘。

        :param hwpassthrough: The hwpassthrough of this VolumeMetadata.
        :type: str
        """
        self._hwpassthrough = hwpassthrough

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
        if not isinstance(other, VolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
