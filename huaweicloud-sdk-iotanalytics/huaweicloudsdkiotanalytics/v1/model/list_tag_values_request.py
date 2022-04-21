# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagValuesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'data_store_id': 'str',
        'tag_name': 'str',
        'filters': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'data_store_id': 'data_store_id',
        'tag_name': 'tag_name',
        'filters': 'filters',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, data_store_id=None, tag_name=None, filters=None, offset=None, limit=None):
        """ListTagValuesRequest

        The model defined in huaweicloud sdk

        :param data_store_id: 存储ID
        :type data_store_id: str
        :param tag_name: tag 名称
        :type tag_name: str
        :param filters: 查询标签的值的过滤条件，例如: {\&quot;deviceCategory\&quot;: \&quot;class1\&quot;}，注意特殊字符需要 urlencode
        :type filters: str
        :param offset: 查询起始元素的偏移
        :type offset: int
        :param limit: 返回的元素列表大小限制,默认为 100
        :type limit: int
        """
        
        

        self._data_store_id = None
        self._tag_name = None
        self._filters = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.data_store_id = data_store_id
        self.tag_name = tag_name
        if filters is not None:
            self.filters = filters
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def data_store_id(self):
        """Gets the data_store_id of this ListTagValuesRequest.

        存储ID

        :return: The data_store_id of this ListTagValuesRequest.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this ListTagValuesRequest.

        存储ID

        :param data_store_id: The data_store_id of this ListTagValuesRequest.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def tag_name(self):
        """Gets the tag_name of this ListTagValuesRequest.

        tag 名称

        :return: The tag_name of this ListTagValuesRequest.
        :rtype: str
        """
        return self._tag_name

    @tag_name.setter
    def tag_name(self, tag_name):
        """Sets the tag_name of this ListTagValuesRequest.

        tag 名称

        :param tag_name: The tag_name of this ListTagValuesRequest.
        :type tag_name: str
        """
        self._tag_name = tag_name

    @property
    def filters(self):
        """Gets the filters of this ListTagValuesRequest.

        查询标签的值的过滤条件，例如: {\"deviceCategory\": \"class1\"}，注意特殊字符需要 urlencode

        :return: The filters of this ListTagValuesRequest.
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ListTagValuesRequest.

        查询标签的值的过滤条件，例如: {\"deviceCategory\": \"class1\"}，注意特殊字符需要 urlencode

        :param filters: The filters of this ListTagValuesRequest.
        :type filters: str
        """
        self._filters = filters

    @property
    def offset(self):
        """Gets the offset of this ListTagValuesRequest.

        查询起始元素的偏移

        :return: The offset of this ListTagValuesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTagValuesRequest.

        查询起始元素的偏移

        :param offset: The offset of this ListTagValuesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTagValuesRequest.

        返回的元素列表大小限制,默认为 100

        :return: The limit of this ListTagValuesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTagValuesRequest.

        返回的元素列表大小限制,默认为 100

        :param limit: The limit of this ListTagValuesRequest.
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
        if not isinstance(other, ListTagValuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
