# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePersistentStorageReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'storage_metadata': 'Storage'
    }

    attribute_map = {
        'name': 'name',
        'storage_metadata': 'storage_metadata'
    }

    def __init__(self, name=None, storage_metadata=None):
        """CreatePersistentStorageReq

        The model defined in huaweicloud sdk

        :param name: WKS存储名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~128个字符
        :type name: str
        :param storage_metadata: 
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.Storage`
        """
        
        

        self._name = None
        self._storage_metadata = None
        self.discriminator = None

        self.name = name
        self.storage_metadata = storage_metadata

    @property
    def name(self):
        """Gets the name of this CreatePersistentStorageReq.

        WKS存储名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~128个字符

        :return: The name of this CreatePersistentStorageReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreatePersistentStorageReq.

        WKS存储名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~128个字符

        :param name: The name of this CreatePersistentStorageReq.
        :type name: str
        """
        self._name = name

    @property
    def storage_metadata(self):
        """Gets the storage_metadata of this CreatePersistentStorageReq.

        :return: The storage_metadata of this CreatePersistentStorageReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Storage`
        """
        return self._storage_metadata

    @storage_metadata.setter
    def storage_metadata(self, storage_metadata):
        """Sets the storage_metadata of this CreatePersistentStorageReq.

        :param storage_metadata: The storage_metadata of this CreatePersistentStorageReq.
        :type storage_metadata: :class:`huaweicloudsdkworkspaceapp.v1.Storage`
        """
        self._storage_metadata = storage_metadata

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
        if not isinstance(other, CreatePersistentStorageReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
