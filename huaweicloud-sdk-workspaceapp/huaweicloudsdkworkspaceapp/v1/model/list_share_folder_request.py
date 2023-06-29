# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareFolderRequest:

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
        'storage_claim_id': 'str',
        'path': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'storage_id': 'storage_id',
        'storage_claim_id': 'storage_claim_id',
        'path': 'path'
    }

    def __init__(self, offset=None, limit=None, storage_id=None, storage_claim_id=None, path=None):
        """ListShareFolderRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量
        :type offset: int
        :param limit: 单次查询的大小[1-100]
        :type limit: int
        :param storage_id: WKS存储ID
        :type storage_id: str
        :param storage_claim_id: WKS存储目录声明ID
        :type storage_claim_id: str
        :param path: 查询名称需满足如下规则: 1. 可见字符+空格 2. 长度0~128个字符
        :type path: str
        """
        
        

        self._offset = None
        self._limit = None
        self._storage_id = None
        self._storage_claim_id = None
        self._path = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.storage_id = storage_id
        if storage_claim_id is not None:
            self.storage_claim_id = storage_claim_id
        if path is not None:
            self.path = path

    @property
    def offset(self):
        """Gets the offset of this ListShareFolderRequest.

        查询的偏移量

        :return: The offset of this ListShareFolderRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListShareFolderRequest.

        查询的偏移量

        :param offset: The offset of this ListShareFolderRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListShareFolderRequest.

        单次查询的大小[1-100]

        :return: The limit of this ListShareFolderRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListShareFolderRequest.

        单次查询的大小[1-100]

        :param limit: The limit of this ListShareFolderRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def storage_id(self):
        """Gets the storage_id of this ListShareFolderRequest.

        WKS存储ID

        :return: The storage_id of this ListShareFolderRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this ListShareFolderRequest.

        WKS存储ID

        :param storage_id: The storage_id of this ListShareFolderRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def storage_claim_id(self):
        """Gets the storage_claim_id of this ListShareFolderRequest.

        WKS存储目录声明ID

        :return: The storage_claim_id of this ListShareFolderRequest.
        :rtype: str
        """
        return self._storage_claim_id

    @storage_claim_id.setter
    def storage_claim_id(self, storage_claim_id):
        """Sets the storage_claim_id of this ListShareFolderRequest.

        WKS存储目录声明ID

        :param storage_claim_id: The storage_claim_id of this ListShareFolderRequest.
        :type storage_claim_id: str
        """
        self._storage_claim_id = storage_claim_id

    @property
    def path(self):
        """Gets the path of this ListShareFolderRequest.

        查询名称需满足如下规则: 1. 可见字符+空格 2. 长度0~128个字符

        :return: The path of this ListShareFolderRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListShareFolderRequest.

        查询名称需满足如下规则: 1. 可见字符+空格 2. 长度0~128个字符

        :param path: The path of this ListShareFolderRequest.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ListShareFolderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
