# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRocketmqTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'next_offset': 'int',
        'previous_offset': 'int',
        'tags': 'list[TagEntity]'
    }

    attribute_map = {
        'total': 'total',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset',
        'tags': 'tags'
    }

    def __init__(self, total=None, next_offset=None, previous_offset=None, tags=None):
        r"""ShowRocketmqTagsResponse

        The model defined in huaweicloud sdk

        :param total: 总数。
        :type total: float
        :param next_offset: 下个分页的offset。
        :type next_offset: int
        :param previous_offset: 上个分页的offset。
        :type previous_offset: int
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        
        super(ShowRocketmqTagsResponse, self).__init__()

        self._total = None
        self._next_offset = None
        self._previous_offset = None
        self._tags = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset
        if tags is not None:
            self.tags = tags

    @property
    def total(self):
        r"""Gets the total of this ShowRocketmqTagsResponse.

        总数。

        :return: The total of this ShowRocketmqTagsResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowRocketmqTagsResponse.

        总数。

        :param total: The total of this ShowRocketmqTagsResponse.
        :type total: float
        """
        self._total = total

    @property
    def next_offset(self):
        r"""Gets the next_offset of this ShowRocketmqTagsResponse.

        下个分页的offset。

        :return: The next_offset of this ShowRocketmqTagsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        r"""Sets the next_offset of this ShowRocketmqTagsResponse.

        下个分页的offset。

        :param next_offset: The next_offset of this ShowRocketmqTagsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        r"""Gets the previous_offset of this ShowRocketmqTagsResponse.

        上个分页的offset。

        :return: The previous_offset of this ShowRocketmqTagsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        r"""Sets the previous_offset of this ShowRocketmqTagsResponse.

        上个分页的offset。

        :param previous_offset: The previous_offset of this ShowRocketmqTagsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

    @property
    def tags(self):
        r"""Gets the tags of this ShowRocketmqTagsResponse.

        标签列表

        :return: The tags of this ShowRocketmqTagsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowRocketmqTagsResponse.

        标签列表

        :param tags: The tags of this ShowRocketmqTagsResponse.
        :type tags: list[:class:`huaweicloudsdkrocketmq.v2.TagEntity`]
        """
        self._tags = tags

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
        if not isinstance(other, ShowRocketmqTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
