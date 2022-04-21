# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageSelectors:

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
        'storage_type': 'str',
        'match_labels': 'StorageSelectorsMatchLabels'
    }

    attribute_map = {
        'name': 'name',
        'storage_type': 'storageType',
        'match_labels': 'matchLabels'
    }

    def __init__(self, name=None, storage_type=None, match_labels=None):
        """StorageSelectors

        The model defined in huaweicloud sdk

        :param name: selector的名字，作为storageGroup中selectorNames的索引，因此各个selector间的名字不能重复。
        :type name: str
        :param storage_type: 存储类型，当前仅支持evs（云硬盘）或local（本地盘）；local存储类型不支持磁盘选择，所有本地盘将被组成一个VG，因此也仅允许只有一个local类型的storageSelector。
        :type storage_type: str
        :param match_labels: 
        :type match_labels: :class:`huaweicloudsdkcce.v3.StorageSelectorsMatchLabels`
        """
        
        

        self._name = None
        self._storage_type = None
        self._match_labels = None
        self.discriminator = None

        self.name = name
        self.storage_type = storage_type
        if match_labels is not None:
            self.match_labels = match_labels

    @property
    def name(self):
        """Gets the name of this StorageSelectors.

        selector的名字，作为storageGroup中selectorNames的索引，因此各个selector间的名字不能重复。

        :return: The name of this StorageSelectors.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageSelectors.

        selector的名字，作为storageGroup中selectorNames的索引，因此各个selector间的名字不能重复。

        :param name: The name of this StorageSelectors.
        :type name: str
        """
        self._name = name

    @property
    def storage_type(self):
        """Gets the storage_type of this StorageSelectors.

        存储类型，当前仅支持evs（云硬盘）或local（本地盘）；local存储类型不支持磁盘选择，所有本地盘将被组成一个VG，因此也仅允许只有一个local类型的storageSelector。

        :return: The storage_type of this StorageSelectors.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this StorageSelectors.

        存储类型，当前仅支持evs（云硬盘）或local（本地盘）；local存储类型不支持磁盘选择，所有本地盘将被组成一个VG，因此也仅允许只有一个local类型的storageSelector。

        :param storage_type: The storage_type of this StorageSelectors.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def match_labels(self):
        """Gets the match_labels of this StorageSelectors.


        :return: The match_labels of this StorageSelectors.
        :rtype: :class:`huaweicloudsdkcce.v3.StorageSelectorsMatchLabels`
        """
        return self._match_labels

    @match_labels.setter
    def match_labels(self, match_labels):
        """Sets the match_labels of this StorageSelectors.


        :param match_labels: The match_labels of this StorageSelectors.
        :type match_labels: :class:`huaweicloudsdkcce.v3.StorageSelectorsMatchLabels`
        """
        self._match_labels = match_labels

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
        if not isinstance(other, StorageSelectors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
