# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateSubscriptionResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str',
        'subject': 'Subject',
        'callbackurl': 'str',
        'channel': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscription_id',
        'subject': 'subject',
        'callbackurl': 'callbackurl',
        'channel': 'channel'
    }

    def __init__(self, subscription_id=None, subject=None, callbackurl=None, channel=None):
        """UpdateSubscriptionResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._subscription_id = None
        self._subject = None
        self._callbackurl = None
        self._channel = None
        self.discriminator = None

        if subscription_id is not None:
            self.subscription_id = subscription_id
        if subject is not None:
            self.subject = subject
        if callbackurl is not None:
            self.callbackurl = callbackurl
        if channel is not None:
            self.channel = channel

    @property
    def subscription_id(self):
        """Gets the subscription_id of this UpdateSubscriptionResponse.

        订阅ID，用于唯一标识一个订阅，在创建订阅时由物联网平台分配获得。

        :return: The subscription_id of this UpdateSubscriptionResponse.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this UpdateSubscriptionResponse.

        订阅ID，用于唯一标识一个订阅，在创建订阅时由物联网平台分配获得。

        :param subscription_id: The subscription_id of this UpdateSubscriptionResponse.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def subject(self):
        """Gets the subject of this UpdateSubscriptionResponse.


        :return: The subject of this UpdateSubscriptionResponse.
        :rtype: Subject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this UpdateSubscriptionResponse.


        :param subject: The subject of this UpdateSubscriptionResponse.
        :type: Subject
        """
        self._subject = subject

    @property
    def callbackurl(self):
        """Gets the callbackurl of this UpdateSubscriptionResponse.

        订阅的回调地址，用于接收对应资源事件的通知消息。

        :return: The callbackurl of this UpdateSubscriptionResponse.
        :rtype: str
        """
        return self._callbackurl

    @callbackurl.setter
    def callbackurl(self, callbackurl):
        """Sets the callbackurl of this UpdateSubscriptionResponse.

        订阅的回调地址，用于接收对应资源事件的通知消息。

        :param callbackurl: The callbackurl of this UpdateSubscriptionResponse.
        :type: str
        """
        self._callbackurl = callbackurl

    @property
    def channel(self):
        """Gets the channel of this UpdateSubscriptionResponse.

        物联网平台推送通知消息时使用的协议通道。使用“http”填充，表示该订阅推送协议通道为http(s)协议。

        :return: The channel of this UpdateSubscriptionResponse.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this UpdateSubscriptionResponse.

        物联网平台推送通知消息时使用的协议通道。使用“http”填充，表示该订阅推送协议通道为http(s)协议。

        :param channel: The channel of this UpdateSubscriptionResponse.
        :type: str
        """
        self._channel = channel

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
        if not isinstance(other, UpdateSubscriptionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
