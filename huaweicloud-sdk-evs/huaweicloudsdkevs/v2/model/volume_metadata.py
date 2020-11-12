# coding: utf-8

import pprint
import re

import six





class VolumeMetadata:


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
        'system__encrypted': 'str',
        'full_clone': 'str',
        'hwpassthrough': 'str',
        'order_id': 'str'
    }

    attribute_map = {
        'system__cmkid': '__system__cmkid',
        'system__encrypted': '__system__encrypted',
        'full_clone': 'full_clone',
        'hwpassthrough': 'hw:passthrough',
        'order_id': 'orderID'
    }

    def __init__(self, system__cmkid=None, system__encrypted=None, full_clone=None, hwpassthrough=None, order_id=None):
        """VolumeMetadata - a model defined in huaweicloud sdk"""
        
        

        self._system__cmkid = None
        self._system__encrypted = None
        self._full_clone = None
        self._hwpassthrough = None
        self._order_id = None
        self.discriminator = None

        if system__cmkid is not None:
            self.system__cmkid = system__cmkid
        if system__encrypted is not None:
            self.system__encrypted = system__encrypted
        if full_clone is not None:
            self.full_clone = full_clone
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if order_id is not None:
            self.order_id = order_id

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this VolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。 > 说明： >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/dew_02_0017.html)\"。

        :return: The system__cmkid of this VolumeMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this VolumeMetadata.

        metadata中的加密cmkid字段，与__system__encrypted配合表示需要加密，cmkid长度固定为36个字节。 > 说明： >  > 请求获取密钥ID的方法请参考：\"[查询密钥列表](https://support.huaweicloud.com/api-dew/dew_02_0017.html)\"。

        :param system__cmkid: The system__cmkid of this VolumeMetadata.
        :type: str
        """
        self._system__cmkid = system__cmkid

    @property
    def system__encrypted(self):
        """Gets the system__encrypted of this VolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。 不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。

        :return: The system__encrypted of this VolumeMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this VolumeMetadata.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。 不指定该字段时，云硬盘的加密属性与数据源保持一致，如果不是从数据源创建的场景，则默认不加密。

        :param system__encrypted: The system__encrypted of this VolumeMetadata.
        :type: str
        """
        self._system__encrypted = system__encrypted

    @property
    def full_clone(self):
        """Gets the full_clone of this VolumeMetadata.

        从快照创建云硬盘时的创建方式。 * 0表示使用链接克隆方式。 * 1表示使用全量克隆方式。

        :return: The full_clone of this VolumeMetadata.
        :rtype: str
        """
        return self._full_clone

    @full_clone.setter
    def full_clone(self, full_clone):
        """Sets the full_clone of this VolumeMetadata.

        从快照创建云硬盘时的创建方式。 * 0表示使用链接克隆方式。 * 1表示使用全量克隆方式。

        :param full_clone: The full_clone of this VolumeMetadata.
        :type: str
        """
        self._full_clone = full_clone

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this VolumeMetadata.

        * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 * 该字段不存在时，云硬盘默认为VBD类型。

        :return: The hwpassthrough of this VolumeMetadata.
        :rtype: str
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this VolumeMetadata.

        * true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 * false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 * 该字段不存在时，云硬盘默认为VBD类型。

        :param hwpassthrough: The hwpassthrough of this VolumeMetadata.
        :type: str
        """
        self._hwpassthrough = hwpassthrough

    @property
    def order_id(self):
        """Gets the order_id of this VolumeMetadata.

        metadata中的表示云硬盘计费类型的字段。 当该字段有值时，表示该云硬盘的计费类型为包周期计费，否则计费类型为按需计费。

        :return: The order_id of this VolumeMetadata.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this VolumeMetadata.

        metadata中的表示云硬盘计费类型的字段。 当该字段有值时，表示该云硬盘的计费类型为包周期计费，否则计费类型为按需计费。

        :param order_id: The order_id of this VolumeMetadata.
        :type: str
        """
        self._order_id = order_id

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
