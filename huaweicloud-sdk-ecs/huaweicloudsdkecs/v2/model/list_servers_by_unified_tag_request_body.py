# coding: utf-8

import pprint
import re

import six


class ListServersByUnifiedTagRequestBody(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'limit': 'str',
        'offset': 'str',
        'action': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'action': 'action'
    }

    def __init__(self, limit=None, offset=None, action=None):  # noqa: E501
        """ListServersByUnifiedTagRequestBody - a model defined in huaweicloud sdk"""

        self._limit = None
        self._offset = None
        self._action = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.action = action

    @property
    def limit(self):
        """Gets the limit of this ListServersByUnifiedTagRequestBody.

        查询返回的云服务器数量限制，最多为1000，不能为负数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter，limit默认为1000。

        :return: The limit of this ListServersByUnifiedTagRequestBody.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListServersByUnifiedTagRequestBody.

        查询返回的云服务器数量限制，最多为1000，不能为负数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter，limit默认为1000。

        :param limit: The limit of this ListServersByUnifiedTagRequestBody.
        :type: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListServersByUnifiedTagRequestBody.

        索引位置，从offset指定的下一条数据开始查询。必须为数字，不能为负数。  查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter，offset默认为0。

        :return: The offset of this ListServersByUnifiedTagRequestBody.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListServersByUnifiedTagRequestBody.

        索引位置，从offset指定的下一条数据开始查询。必须为数字，不能为负数。  查询第一页数据时，不需要传入此参数。查询后续页码数据时，将查询前一页数据时响应体中的值带入此参数。  - 如果action的值为count，此参数无效。 - 如果action的值为filter，offset默认为0。

        :param offset: The offset of this ListServersByUnifiedTagRequestBody.
        :type: str
        """
        self._offset = offset

    @property
    def action(self):
        """Gets the action of this ListServersByUnifiedTagRequestBody.

        操作标识，包括filter和count两种。  - filter：表示按标签过滤弹性云服务器，返回符合条件的云服务器列表。此时，为分页查询。 - count：表示按标签搜索弹性云服务器，返回符合条件的云服务器个数。

        :return: The action of this ListServersByUnifiedTagRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListServersByUnifiedTagRequestBody.

        操作标识，包括filter和count两种。  - filter：表示按标签过滤弹性云服务器，返回符合条件的云服务器列表。此时，为分页查询。 - count：表示按标签搜索弹性云服务器，返回符合条件的云服务器个数。

        :param action: The action of this ListServersByUnifiedTagRequestBody.
        :type: str
        """
        self._action = action

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListServersByUnifiedTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
