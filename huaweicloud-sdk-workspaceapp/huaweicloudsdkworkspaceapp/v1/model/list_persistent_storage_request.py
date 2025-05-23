# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPersistentStorageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'storage_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'storage_id': 'storage_id',
        'name': 'name'
    }

    def __init__(self, offset=None, limit=None, storage_id=None, name=None):
        r"""ListPersistentStorageRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param storage_id: WKS存储ID。
        :type storage_id: str
        :param name: 查询名称，模糊匹配。
        :type name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._storage_id = None
        self._name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if storage_id is not None:
            self.storage_id = storage_id
        if name is not None:
            self.name = name

    @property
    def offset(self):
        r"""Gets the offset of this ListPersistentStorageRequest.

        查询的偏移量。

        :return: The offset of this ListPersistentStorageRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPersistentStorageRequest.

        查询的偏移量。

        :param offset: The offset of this ListPersistentStorageRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPersistentStorageRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListPersistentStorageRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPersistentStorageRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListPersistentStorageRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def storage_id(self):
        r"""Gets the storage_id of this ListPersistentStorageRequest.

        WKS存储ID。

        :return: The storage_id of this ListPersistentStorageRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        r"""Sets the storage_id of this ListPersistentStorageRequest.

        WKS存储ID。

        :param storage_id: The storage_id of this ListPersistentStorageRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def name(self):
        r"""Gets the name of this ListPersistentStorageRequest.

        查询名称，模糊匹配。

        :return: The name of this ListPersistentStorageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPersistentStorageRequest.

        查询名称，模糊匹配。

        :param name: The name of this ListPersistentStorageRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListPersistentStorageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
