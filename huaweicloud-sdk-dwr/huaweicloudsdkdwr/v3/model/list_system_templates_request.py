# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prefix': 'str',
        'category': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'prefix': 'prefix',
        'category': 'category',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, prefix=None, category=None, offset=None, limit=None):
        """ListSystemTemplatesRequest

        The model defined in huaweicloud sdk

        :param prefix: 模板前缀。
        :type prefix: str
        :param category: 算子模板的分类。
        :type category: str
        :param offset: 查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。
        :type offset: int
        :param limit: 请求返回的最大记录条数。limit取值最小1，最大1000，不设置则取默认值10。
        :type limit: int
        """
        
        

        self._prefix = None
        self._category = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if category is not None:
            self.category = category
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def prefix(self):
        """Gets the prefix of this ListSystemTemplatesRequest.

        模板前缀。

        :return: The prefix of this ListSystemTemplatesRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this ListSystemTemplatesRequest.

        模板前缀。

        :param prefix: The prefix of this ListSystemTemplatesRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def category(self):
        """Gets the category of this ListSystemTemplatesRequest.

        算子模板的分类。

        :return: The category of this ListSystemTemplatesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ListSystemTemplatesRequest.

        算子模板的分类。

        :param category: The category of this ListSystemTemplatesRequest.
        :type category: str
        """
        self._category = category

    @property
    def offset(self):
        """Gets the offset of this ListSystemTemplatesRequest.

        查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。

        :return: The offset of this ListSystemTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSystemTemplatesRequest.

        查询的起始位置。start大于等于1，最大1000，不设置则取默认值1。

        :param offset: The offset of this ListSystemTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSystemTemplatesRequest.

        请求返回的最大记录条数。limit取值最小1，最大1000，不设置则取默认值10。

        :return: The limit of this ListSystemTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSystemTemplatesRequest.

        请求返回的最大记录条数。limit取值最小1，最大1000，不设置则取默认值10。

        :param limit: The limit of this ListSystemTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListSystemTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
