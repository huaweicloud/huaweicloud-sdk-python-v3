# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_ids': 'list[str]',
        'total': 'int',
        'next_offset': 'int',
        'previous_offset': 'int'
    }

    attribute_map = {
        'group_ids': 'group_ids',
        'total': 'total',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset'
    }

    def __init__(self, group_ids=None, total=None, next_offset=None, previous_offset=None):
        """ListInstanceConsumerGroupsResponse

        The model defined in huaweicloud sdk

        :param group_ids: 所有的消费组ID
        :type group_ids: list[str]
        :param total: 所有的消费组总数
        :type total: int
        :param next_offset: 下一个消费组序号
        :type next_offset: int
        :param previous_offset: 上一个消费组序号
        :type previous_offset: int
        """
        
        super(ListInstanceConsumerGroupsResponse, self).__init__()

        self._group_ids = None
        self._total = None
        self._next_offset = None
        self._previous_offset = None
        self.discriminator = None

        if group_ids is not None:
            self.group_ids = group_ids
        if total is not None:
            self.total = total
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset

    @property
    def group_ids(self):
        """Gets the group_ids of this ListInstanceConsumerGroupsResponse.

        所有的消费组ID

        :return: The group_ids of this ListInstanceConsumerGroupsResponse.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this ListInstanceConsumerGroupsResponse.

        所有的消费组ID

        :param group_ids: The group_ids of this ListInstanceConsumerGroupsResponse.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def total(self):
        """Gets the total of this ListInstanceConsumerGroupsResponse.

        所有的消费组总数

        :return: The total of this ListInstanceConsumerGroupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceConsumerGroupsResponse.

        所有的消费组总数

        :param total: The total of this ListInstanceConsumerGroupsResponse.
        :type total: int
        """
        self._total = total

    @property
    def next_offset(self):
        """Gets the next_offset of this ListInstanceConsumerGroupsResponse.

        下一个消费组序号

        :return: The next_offset of this ListInstanceConsumerGroupsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ListInstanceConsumerGroupsResponse.

        下一个消费组序号

        :param next_offset: The next_offset of this ListInstanceConsumerGroupsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        """Gets the previous_offset of this ListInstanceConsumerGroupsResponse.

        上一个消费组序号

        :return: The previous_offset of this ListInstanceConsumerGroupsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        """Sets the previous_offset of this ListInstanceConsumerGroupsResponse.

        上一个消费组序号

        :param previous_offset: The previous_offset of this ListInstanceConsumerGroupsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

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
        if not isinstance(other, ListInstanceConsumerGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
