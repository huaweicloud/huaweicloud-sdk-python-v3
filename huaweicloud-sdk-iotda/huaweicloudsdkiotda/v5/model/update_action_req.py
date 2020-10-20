# coding: utf-8

import pprint
import re

import six





class UpdateActionReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'channel': 'str',
        'channel_detail': 'ChannelDetail'
    }

    attribute_map = {
        'channel': 'channel',
        'channel_detail': 'channel_detail'
    }

    def __init__(self, channel=None, channel_detail=None):
        """UpdateActionReq - a model defined in huaweicloud sdk"""
        
        

        self._channel = None
        self._channel_detail = None
        self.discriminator = None

        if channel is not None:
            self.channel = channel
        if channel_detail is not None:
            self.channel_detail = channel_detail

    @property
    def channel(self):
        """Gets the channel of this UpdateActionReq.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 

        :return: The channel of this UpdateActionReq.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this UpdateActionReq.

        规则动作的类型，取值范围： - HTTP_FORWARDING：HTTP服务消息类型。 - AMQP_FORWARDING：转发AMQP服务消息类型。 

        :param channel: The channel of this UpdateActionReq.
        :type: str
        """
        self._channel = channel

    @property
    def channel_detail(self):
        """Gets the channel_detail of this UpdateActionReq.


        :return: The channel_detail of this UpdateActionReq.
        :rtype: ChannelDetail
        """
        return self._channel_detail

    @channel_detail.setter
    def channel_detail(self, channel_detail):
        """Sets the channel_detail of this UpdateActionReq.


        :param channel_detail: The channel_detail of this UpdateActionReq.
        :type: ChannelDetail
        """
        self._channel_detail = channel_detail

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
