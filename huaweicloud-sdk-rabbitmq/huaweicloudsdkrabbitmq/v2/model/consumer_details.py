# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumerDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consumer_tag': 'str',
        'channel_details': 'ChannelDetails',
        'ack_required': 'bool',
        'prefetch_count': 'int'
    }

    attribute_map = {
        'consumer_tag': 'consumer_tag',
        'channel_details': 'channel_details',
        'ack_required': 'ack_required',
        'prefetch_count': 'prefetch_count'
    }

    def __init__(self, consumer_tag=None, channel_details=None, ack_required=None, prefetch_count=None):
        r"""ConsumerDetails

        The model defined in huaweicloud sdk

        :param consumer_tag: 消费者标识
        :type consumer_tag: str
        :param channel_details: 
        :type channel_details: :class:`huaweicloudsdkrabbitmq.v2.ChannelDetails`
        :param ack_required: 消费者客户端是否设置手动ack
        :type ack_required: bool
        :param prefetch_count: 消费者客户端预取值
        :type prefetch_count: int
        """
        
        

        self._consumer_tag = None
        self._channel_details = None
        self._ack_required = None
        self._prefetch_count = None
        self.discriminator = None

        if consumer_tag is not None:
            self.consumer_tag = consumer_tag
        if channel_details is not None:
            self.channel_details = channel_details
        if ack_required is not None:
            self.ack_required = ack_required
        if prefetch_count is not None:
            self.prefetch_count = prefetch_count

    @property
    def consumer_tag(self):
        r"""Gets the consumer_tag of this ConsumerDetails.

        消费者标识

        :return: The consumer_tag of this ConsumerDetails.
        :rtype: str
        """
        return self._consumer_tag

    @consumer_tag.setter
    def consumer_tag(self, consumer_tag):
        r"""Sets the consumer_tag of this ConsumerDetails.

        消费者标识

        :param consumer_tag: The consumer_tag of this ConsumerDetails.
        :type consumer_tag: str
        """
        self._consumer_tag = consumer_tag

    @property
    def channel_details(self):
        r"""Gets the channel_details of this ConsumerDetails.

        :return: The channel_details of this ConsumerDetails.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.ChannelDetails`
        """
        return self._channel_details

    @channel_details.setter
    def channel_details(self, channel_details):
        r"""Sets the channel_details of this ConsumerDetails.

        :param channel_details: The channel_details of this ConsumerDetails.
        :type channel_details: :class:`huaweicloudsdkrabbitmq.v2.ChannelDetails`
        """
        self._channel_details = channel_details

    @property
    def ack_required(self):
        r"""Gets the ack_required of this ConsumerDetails.

        消费者客户端是否设置手动ack

        :return: The ack_required of this ConsumerDetails.
        :rtype: bool
        """
        return self._ack_required

    @ack_required.setter
    def ack_required(self, ack_required):
        r"""Sets the ack_required of this ConsumerDetails.

        消费者客户端是否设置手动ack

        :param ack_required: The ack_required of this ConsumerDetails.
        :type ack_required: bool
        """
        self._ack_required = ack_required

    @property
    def prefetch_count(self):
        r"""Gets the prefetch_count of this ConsumerDetails.

        消费者客户端预取值

        :return: The prefetch_count of this ConsumerDetails.
        :rtype: int
        """
        return self._prefetch_count

    @prefetch_count.setter
    def prefetch_count(self, prefetch_count):
        r"""Sets the prefetch_count of this ConsumerDetails.

        消费者客户端预取值

        :param prefetch_count: The prefetch_count of this ConsumerDetails.
        :type prefetch_count: int
        """
        self._prefetch_count = prefetch_count

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
        if not isinstance(other, ConsumerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
