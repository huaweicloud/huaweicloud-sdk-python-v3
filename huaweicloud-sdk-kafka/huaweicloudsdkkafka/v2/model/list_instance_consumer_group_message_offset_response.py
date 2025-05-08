# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupMessageOffsetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_message_offsets': 'list[GroupMessageOffsetsDetailEntity]',
        'total': 'int'
    }

    attribute_map = {
        'group_message_offsets': 'group_message_offsets',
        'total': 'total'
    }

    def __init__(self, group_message_offsets=None, total=None):
        r"""ListInstanceConsumerGroupMessageOffsetResponse

        The model defined in huaweicloud sdk

        :param group_message_offsets: 消费组消息位点详情
        :type group_message_offsets: list[:class:`huaweicloudsdkkafka.v2.GroupMessageOffsetsDetailEntity`]
        :param total: 总数
        :type total: int
        """
        
        super(ListInstanceConsumerGroupMessageOffsetResponse, self).__init__()

        self._group_message_offsets = None
        self._total = None
        self.discriminator = None

        if group_message_offsets is not None:
            self.group_message_offsets = group_message_offsets
        if total is not None:
            self.total = total

    @property
    def group_message_offsets(self):
        r"""Gets the group_message_offsets of this ListInstanceConsumerGroupMessageOffsetResponse.

        消费组消息位点详情

        :return: The group_message_offsets of this ListInstanceConsumerGroupMessageOffsetResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.GroupMessageOffsetsDetailEntity`]
        """
        return self._group_message_offsets

    @group_message_offsets.setter
    def group_message_offsets(self, group_message_offsets):
        r"""Sets the group_message_offsets of this ListInstanceConsumerGroupMessageOffsetResponse.

        消费组消息位点详情

        :param group_message_offsets: The group_message_offsets of this ListInstanceConsumerGroupMessageOffsetResponse.
        :type group_message_offsets: list[:class:`huaweicloudsdkkafka.v2.GroupMessageOffsetsDetailEntity`]
        """
        self._group_message_offsets = group_message_offsets

    @property
    def total(self):
        r"""Gets the total of this ListInstanceConsumerGroupMessageOffsetResponse.

        总数

        :return: The total of this ListInstanceConsumerGroupMessageOffsetResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceConsumerGroupMessageOffsetResponse.

        总数

        :param total: The total of this ListInstanceConsumerGroupMessageOffsetResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceConsumerGroupMessageOffsetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
