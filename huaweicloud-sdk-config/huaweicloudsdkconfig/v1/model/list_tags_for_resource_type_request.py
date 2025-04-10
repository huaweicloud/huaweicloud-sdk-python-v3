# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTagsForResourceTypeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, resource_type=None, limit=None, offset=None):
        r"""ListTagsForResourceTypeRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param limit: 查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1
        :type limit: int
        :param offset: 索引位置，从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数
        :type offset: int
        """
        
        

        self._resource_type = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.resource_type = resource_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListTagsForResourceTypeRequest.

        资源类型

        :return: The resource_type of this ListTagsForResourceTypeRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListTagsForResourceTypeRequest.

        资源类型

        :param resource_type: The resource_type of this ListTagsForResourceTypeRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def limit(self):
        r"""Gets the limit of this ListTagsForResourceTypeRequest.

        查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1

        :return: The limit of this ListTagsForResourceTypeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTagsForResourceTypeRequest.

        查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1

        :param limit: The limit of this ListTagsForResourceTypeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTagsForResourceTypeRequest.

        索引位置，从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数

        :return: The offset of this ListTagsForResourceTypeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTagsForResourceTypeRequest.

        索引位置，从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数

        :param offset: The offset of this ListTagsForResourceTypeRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListTagsForResourceTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
