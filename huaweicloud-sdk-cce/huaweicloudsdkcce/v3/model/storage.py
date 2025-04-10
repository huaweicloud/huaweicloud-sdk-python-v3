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
        'storage_selectors': 'list[StorageSelectors]',
        'storage_groups': 'list[StorageGroups]'
    }

    attribute_map = {
        'storage_selectors': 'storageSelectors',
        'storage_groups': 'storageGroups'
    }

    def __init__(self, storage_selectors=None, storage_groups=None):
        r"""Storage

        The model defined in huaweicloud sdk

        :param storage_selectors: 磁盘选择，根据matchLabels和storageType对匹配的磁盘进行管理。磁盘匹配存在先后顺序，靠前的匹配规则优先匹配。
        :type storage_selectors: list[:class:`huaweicloudsdkcce.v3.StorageSelectors`]
        :param storage_groups: 由多个存储设备组成的存储组，用于各个存储空间的划分。
        :type storage_groups: list[:class:`huaweicloudsdkcce.v3.StorageGroups`]
        """
        
        

        self._storage_selectors = None
        self._storage_groups = None
        self.discriminator = None

        self.storage_selectors = storage_selectors
        self.storage_groups = storage_groups

    @property
    def storage_selectors(self):
        r"""Gets the storage_selectors of this Storage.

        磁盘选择，根据matchLabels和storageType对匹配的磁盘进行管理。磁盘匹配存在先后顺序，靠前的匹配规则优先匹配。

        :return: The storage_selectors of this Storage.
        :rtype: list[:class:`huaweicloudsdkcce.v3.StorageSelectors`]
        """
        return self._storage_selectors

    @storage_selectors.setter
    def storage_selectors(self, storage_selectors):
        r"""Sets the storage_selectors of this Storage.

        磁盘选择，根据matchLabels和storageType对匹配的磁盘进行管理。磁盘匹配存在先后顺序，靠前的匹配规则优先匹配。

        :param storage_selectors: The storage_selectors of this Storage.
        :type storage_selectors: list[:class:`huaweicloudsdkcce.v3.StorageSelectors`]
        """
        self._storage_selectors = storage_selectors

    @property
    def storage_groups(self):
        r"""Gets the storage_groups of this Storage.

        由多个存储设备组成的存储组，用于各个存储空间的划分。

        :return: The storage_groups of this Storage.
        :rtype: list[:class:`huaweicloudsdkcce.v3.StorageGroups`]
        """
        return self._storage_groups

    @storage_groups.setter
    def storage_groups(self, storage_groups):
        r"""Sets the storage_groups of this Storage.

        由多个存储设备组成的存储组，用于各个存储空间的划分。

        :param storage_groups: The storage_groups of this Storage.
        :type storage_groups: list[:class:`huaweicloudsdkcce.v3.StorageGroups`]
        """
        self._storage_groups = storage_groups

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
