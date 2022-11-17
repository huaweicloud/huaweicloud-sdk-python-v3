# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'system__encrypted': 'str',
        'system__cmkid': 'str'
    }

    attribute_map = {
        'system__encrypted': '__system__encrypted',
        'system__cmkid': '__system__cmkid'
    }

    def __init__(self, system__encrypted=None, system__cmkid=None):
        """VolumeMetadata

        The model defined in huaweicloud sdk

        :param system__encrypted: 表示云硬盘加密功能的字段，&#39;0&#39;代表不加密，&#39;1&#39;代表加密。  该字段不存在时，云硬盘默认为不加密。
        :type system__encrypted: str
        :param system__cmkid: 用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。
        :type system__cmkid: str
        """
        
        

        self._system__encrypted = None
        self._system__cmkid = None
        self.discriminator = None

        if system__encrypted is not None:
            self.system__encrypted = system__encrypted
        if system__cmkid is not None:
            self.system__cmkid = system__cmkid

    @property
    def system__encrypted(self):
        """Gets the system__encrypted of this VolumeMetadata.

        表示云硬盘加密功能的字段，'0'代表不加密，'1'代表加密。  该字段不存在时，云硬盘默认为不加密。

        :return: The system__encrypted of this VolumeMetadata.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this VolumeMetadata.

        表示云硬盘加密功能的字段，'0'代表不加密，'1'代表加密。  该字段不存在时，云硬盘默认为不加密。

        :param system__encrypted: The system__encrypted of this VolumeMetadata.
        :type system__encrypted: str
        """
        self._system__encrypted = system__encrypted

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this VolumeMetadata.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。

        :return: The system__cmkid of this VolumeMetadata.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this VolumeMetadata.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。

        :param system__cmkid: The system__cmkid of this VolumeMetadata.
        :type system__cmkid: str
        """
        self._system__cmkid = system__cmkid

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
        if not isinstance(other, VolumeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
