# coding: utf-8

import pprint
import re

import six





class CreateSubReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'subject': 'Subject',
        'callbackurl': 'str',
        'app_id': 'str',
        'channel': 'str'
    }

    attribute_map = {
        'subject': 'subject',
        'callbackurl': 'callbackurl',
        'app_id': 'app_id',
        'channel': 'channel'
    }

    def __init__(self, subject=None, callbackurl=None, app_id=None, channel=None):
        """CreateSubReq - a model defined in huaweicloud sdk"""
        
        

        self._subject = None
        self._callbackurl = None
        self._app_id = None
        self._channel = None
        self.discriminator = None

        self.subject = subject
        self.callbackurl = callbackurl
        if app_id is not None:
            self.app_id = app_id
        self.channel = channel

    @property
    def subject(self):
        """Gets the subject of this CreateSubReq.


        :return: The subject of this CreateSubReq.
        :rtype: Subject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CreateSubReq.


        :param subject: The subject of this CreateSubReq.
        :type: Subject
        """
        self._subject = subject

    @property
    def callbackurl(self):
        """Gets the callbackurl of this CreateSubReq.

        订阅的回调地址，用于接收对应资源事件的通知消息，例如：https://10.10.10.10:443/callbackurltest。

        :return: The callbackurl of this CreateSubReq.
        :rtype: str
        """
        return self._callbackurl

    @callbackurl.setter
    def callbackurl(self, callbackurl):
        """Sets the callbackurl of this CreateSubReq.

        订阅的回调地址，用于接收对应资源事件的通知消息，例如：https://10.10.10.10:443/callbackurltest。

        :param callbackurl: The callbackurl of this CreateSubReq.
        :type: str
        """
        self._callbackurl = callbackurl

    @property
    def app_id(self):
        """Gets the app_id of this CreateSubReq.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定订阅哪个资源空间下的消息通知，否则订阅的消息通知将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this CreateSubReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateSubReq.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定订阅哪个资源空间下的消息通知，否则订阅的消息通知将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this CreateSubReq.
        :type: str
        """
        self._app_id = app_id

    @property
    def channel(self):
        """Gets the channel of this CreateSubReq.

        物联网平台推送通知消息时使用的协议通道。使用“http”填充，表示该订阅推送协议通道为http(s)协议。

        :return: The channel of this CreateSubReq.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this CreateSubReq.

        物联网平台推送通知消息时使用的协议通道。使用“http”填充，表示该订阅推送协议通道为http(s)协议。

        :param channel: The channel of this CreateSubReq.
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
        if not isinstance(other, CreateSubReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
