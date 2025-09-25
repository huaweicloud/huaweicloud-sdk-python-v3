# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskEncryptionInfo:

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
        'system_encrypted': 'systemEncrypted',
        'system_cmkid': 'systemCmkid'
    }

    def __init__(self, system_encrypted=None, system_cmkid=None):
        r"""DiskEncryptionInfo

        The model defined in huaweicloud sdk

        :param system_encrypted: 是否开启磁盘加密。通过磁盘加密对集群节点的数据盘进行KMS加密，保障数据存储的安全性。
        :type system_encrypted: str
        :param system_cmkid: 磁盘密钥ID。
        :type system_cmkid: str
        """
        
        

        self._system_encrypted = None
        self._system_cmkid = None
        self.discriminator = None

        if system_encrypted is not None:
            self.system_encrypted = system_encrypted
        if system_cmkid is not None:
            self.system_cmkid = system_cmkid

    @property
    def system_encrypted(self):
        r"""Gets the system_encrypted of this DiskEncryptionInfo.

        是否开启磁盘加密。通过磁盘加密对集群节点的数据盘进行KMS加密，保障数据存储的安全性。

        :return: The system_encrypted of this DiskEncryptionInfo.
        :rtype: str
        """
        return self._system_encrypted

    @system_encrypted.setter
    def system_encrypted(self, system_encrypted):
        r"""Sets the system_encrypted of this DiskEncryptionInfo.

        是否开启磁盘加密。通过磁盘加密对集群节点的数据盘进行KMS加密，保障数据存储的安全性。

        :param system_encrypted: The system_encrypted of this DiskEncryptionInfo.
        :type system_encrypted: str
        """
        self._system_encrypted = system_encrypted

    @property
    def system_cmkid(self):
        r"""Gets the system_cmkid of this DiskEncryptionInfo.

        磁盘密钥ID。

        :return: The system_cmkid of this DiskEncryptionInfo.
        :rtype: str
        """
        return self._system_cmkid

    @system_cmkid.setter
    def system_cmkid(self, system_cmkid):
        r"""Sets the system_cmkid of this DiskEncryptionInfo.

        磁盘密钥ID。

        :param system_cmkid: The system_cmkid of this DiskEncryptionInfo.
        :type system_cmkid: str
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
        if not isinstance(other, DiskEncryptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
