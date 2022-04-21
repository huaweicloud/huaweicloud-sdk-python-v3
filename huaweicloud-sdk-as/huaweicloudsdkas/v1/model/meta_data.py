# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaData:

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
        """MetaData

        The model defined in huaweicloud sdk

        :param system__encrypted: metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。 说明： 系统盘不支持加密。
        :type system__encrypted: str
        :param system__cmkid: 用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。 说明： - 系统盘不支持加密。 - 请参考[查询密钥列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;KMS&amp;api&#x3D;ListKeys&amp;version&#x3D;v2)，通过HTTPS请求获取密钥ID。
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
        """Gets the system__encrypted of this MetaData.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。 说明： 系统盘不支持加密。

        :return: The system__encrypted of this MetaData.
        :rtype: str
        """
        return self._system__encrypted

    @system__encrypted.setter
    def system__encrypted(self, system__encrypted):
        """Sets the system__encrypted of this MetaData.

        metadata中的表示加密功能的字段，0代表不加密，1代表加密。  该字段不存在时，云硬盘默认为不加密。 说明： 系统盘不支持加密。

        :param system__encrypted: The system__encrypted of this MetaData.
        :type system__encrypted: str
        """
        self._system__encrypted = system__encrypted

    @property
    def system__cmkid(self):
        """Gets the system__cmkid of this MetaData.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。 说明： - 系统盘不支持加密。 - 请参考[查询密钥列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=KMS&api=ListKeys&version=v2)，通过HTTPS请求获取密钥ID。

        :return: The system__cmkid of this MetaData.
        :rtype: str
        """
        return self._system__cmkid

    @system__cmkid.setter
    def system__cmkid(self, system__cmkid):
        """Sets the system__cmkid of this MetaData.

        用户主密钥ID，是metadata中的表示加密功能的字段，与__system__encrypted配合使用。 说明： - 系统盘不支持加密。 - 请参考[查询密钥列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=KMS&api=ListKeys&version=v2)，通过HTTPS请求获取密钥ID。

        :param system__cmkid: The system__cmkid of this MetaData.
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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
