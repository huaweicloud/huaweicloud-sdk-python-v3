# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Storage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_handle': 'str',
        'storage_class': 'str'
    }

    attribute_map = {
        'storage_handle': 'storage_handle',
        'storage_class': 'storage_class'
    }

    def __init__(self, storage_handle=None, storage_class=None):
        """Storage

        The model defined in huaweicloud sdk

        :param storage_handle: SFS文件系统名称
        :type storage_handle: str
        :param storage_class: 存储类型 * &#x60;sfs&#x60; - sfs3.0存储
        :type storage_class: str
        """
        
        

        self._storage_handle = None
        self._storage_class = None
        self.discriminator = None

        self.storage_handle = storage_handle
        self.storage_class = storage_class

    @property
    def storage_handle(self):
        """Gets the storage_handle of this Storage.

        SFS文件系统名称

        :return: The storage_handle of this Storage.
        :rtype: str
        """
        return self._storage_handle

    @storage_handle.setter
    def storage_handle(self, storage_handle):
        """Sets the storage_handle of this Storage.

        SFS文件系统名称

        :param storage_handle: The storage_handle of this Storage.
        :type storage_handle: str
        """
        self._storage_handle = storage_handle

    @property
    def storage_class(self):
        """Gets the storage_class of this Storage.

        存储类型 * `sfs` - sfs3.0存储

        :return: The storage_class of this Storage.
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this Storage.

        存储类型 * `sfs` - sfs3.0存储

        :param storage_class: The storage_class of this Storage.
        :type storage_class: str
        """
        self._storage_class = storage_class

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
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
