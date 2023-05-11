# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories': 'str',
        'key_word': 'str',
        'labels': 'str',
        'limit': 'int',
        'offset': 'int',
        'publishers': 'str',
        'scope': 'str',
        'vendor_ids': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'key_word': 'key_word',
        'labels': 'labels',
        'limit': 'limit',
        'offset': 'offset',
        'publishers': 'publishers',
        'scope': 'scope',
        'vendor_ids': 'vendor_ids'
    }

    def __init__(self, categories=None, key_word=None, labels=None, limit=None, offset=None, publishers=None, scope=None, vendor_ids=None):
        """ListAssetRequest

        The model defined in huaweicloud sdk

        :param categories: 资产类别，支持IMAGE/APP/WORKFLOW/DATASET，支持查询多个，以&#39;,&#39;分割
        :type categories: str
        :param key_word: 关键字，支持在资产名、资产标题、短描述、长描述中搜索
        :type key_word: str
        :param labels: 标签，支持查询多个，以&#39;,&#39;分割
        :type labels: str
        :param limit: 返回记录限制
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param publishers: 发布者，支持查询多个，以&#39;,&#39;分割
        :type publishers: str
        :param scope: 查询范围，支持PUBLIC/INTERNAL/SELF
        :type scope: str
        :param vendor_ids: 供应商，支持查询多个，以&#39;,&#39;分割
        :type vendor_ids: str
        """
        
        

        self._categories = None
        self._key_word = None
        self._labels = None
        self._limit = None
        self._offset = None
        self._publishers = None
        self._scope = None
        self._vendor_ids = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if key_word is not None:
            self.key_word = key_word
        if labels is not None:
            self.labels = labels
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if publishers is not None:
            self.publishers = publishers
        self.scope = scope
        if vendor_ids is not None:
            self.vendor_ids = vendor_ids

    @property
    def categories(self):
        """Gets the categories of this ListAssetRequest.

        资产类别，支持IMAGE/APP/WORKFLOW/DATASET，支持查询多个，以','分割

        :return: The categories of this ListAssetRequest.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ListAssetRequest.

        资产类别，支持IMAGE/APP/WORKFLOW/DATASET，支持查询多个，以','分割

        :param categories: The categories of this ListAssetRequest.
        :type categories: str
        """
        self._categories = categories

    @property
    def key_word(self):
        """Gets the key_word of this ListAssetRequest.

        关键字，支持在资产名、资产标题、短描述、长描述中搜索

        :return: The key_word of this ListAssetRequest.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this ListAssetRequest.

        关键字，支持在资产名、资产标题、短描述、长描述中搜索

        :param key_word: The key_word of this ListAssetRequest.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def labels(self):
        """Gets the labels of this ListAssetRequest.

        标签，支持查询多个，以','分割

        :return: The labels of this ListAssetRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ListAssetRequest.

        标签，支持查询多个，以','分割

        :param labels: The labels of this ListAssetRequest.
        :type labels: str
        """
        self._labels = labels

    @property
    def limit(self):
        """Gets the limit of this ListAssetRequest.

        返回记录限制

        :return: The limit of this ListAssetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAssetRequest.

        返回记录限制

        :param limit: The limit of this ListAssetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListAssetRequest.

        偏移量

        :return: The offset of this ListAssetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAssetRequest.

        偏移量

        :param offset: The offset of this ListAssetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def publishers(self):
        """Gets the publishers of this ListAssetRequest.

        发布者，支持查询多个，以','分割

        :return: The publishers of this ListAssetRequest.
        :rtype: str
        """
        return self._publishers

    @publishers.setter
    def publishers(self, publishers):
        """Sets the publishers of this ListAssetRequest.

        发布者，支持查询多个，以','分割

        :param publishers: The publishers of this ListAssetRequest.
        :type publishers: str
        """
        self._publishers = publishers

    @property
    def scope(self):
        """Gets the scope of this ListAssetRequest.

        查询范围，支持PUBLIC/INTERNAL/SELF

        :return: The scope of this ListAssetRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ListAssetRequest.

        查询范围，支持PUBLIC/INTERNAL/SELF

        :param scope: The scope of this ListAssetRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def vendor_ids(self):
        """Gets the vendor_ids of this ListAssetRequest.

        供应商，支持查询多个，以','分割

        :return: The vendor_ids of this ListAssetRequest.
        :rtype: str
        """
        return self._vendor_ids

    @vendor_ids.setter
    def vendor_ids(self, vendor_ids):
        """Sets the vendor_ids of this ListAssetRequest.

        供应商，支持查询多个，以','分割

        :param vendor_ids: The vendor_ids of this ListAssetRequest.
        :type vendor_ids: str
        """
        self._vendor_ids = vendor_ids

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
        if not isinstance(other, ListAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
