# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowDeviceMessageResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message_id': 'str',
        'name': 'str',
        'message': 'str',
        'topic': 'str',
        'status': 'str',
        'created_time': 'str',
        'finished_time': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'name': 'name',
        'message': 'message',
        'topic': 'topic',
        'status': 'status',
        'created_time': 'created_time',
        'finished_time': 'finished_time'
    }

    def __init__(self, message_id=None, name=None, message=None, topic=None, status=None, created_time=None, finished_time=None):
        """ShowDeviceMessageResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._message_id = None
        self._name = None
        self._message = None
        self._topic = None
        self._status = None
        self._created_time = None
        self._finished_time = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if topic is not None:
            self.topic = topic
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if finished_time is not None:
            self.finished_time = finished_time

    @property
    def message_id(self):
        """Gets the message_id of this ShowDeviceMessageResponse.

        设备消息ID，用于唯一标识一条消息，在下发设备消息时由物联网平台分配获得。

        :return: The message_id of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ShowDeviceMessageResponse.

        设备消息ID，用于唯一标识一条消息，在下发设备消息时由物联网平台分配获得。

        :param message_id: The message_id of this ShowDeviceMessageResponse.
        :type: str
        """
        self._message_id = message_id

    @property
    def name(self):
        """Gets the name of this ShowDeviceMessageResponse.

        消息名称,在下发消息时由用户指定。

        :return: The name of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowDeviceMessageResponse.

        消息名称,在下发消息时由用户指定。

        :param name: The name of this ShowDeviceMessageResponse.
        :type: str
        """
        self._name = name

    @property
    def message(self):
        """Gets the message of this ShowDeviceMessageResponse.

        消息内容

        :return: The message of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowDeviceMessageResponse.

        消息内容

        :param message: The message of this ShowDeviceMessageResponse.
        :type: str
        """
        self._message = message

    @property
    def topic(self):
        """Gets the topic of this ShowDeviceMessageResponse.

        消息topic

        :return: The topic of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowDeviceMessageResponse.

        消息topic

        :param topic: The topic of this ShowDeviceMessageResponse.
        :type: str
        """
        self._topic = topic

    @property
    def status(self):
        """Gets the status of this ShowDeviceMessageResponse.

        消息状态，包含PENDING，DELIVERED，FAILED和TIMEOUT，PENDING指设备不在线，消息被缓存起来，等设备上线之后下发； DELIVERED指消息发送成功；FAILED消息发送失败；TIMEOUT指消息在平台默认时间内（1天）还没有下发送给设备，则平台会将消息设置为超时，状态为TIMEOUT。

        :return: The status of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDeviceMessageResponse.

        消息状态，包含PENDING，DELIVERED，FAILED和TIMEOUT，PENDING指设备不在线，消息被缓存起来，等设备上线之后下发； DELIVERED指消息发送成功；FAILED消息发送失败；TIMEOUT指消息在平台默认时间内（1天）还没有下发送给设备，则平台会将消息设置为超时，状态为TIMEOUT。

        :param status: The status of this ShowDeviceMessageResponse.
        :type: str
        """
        self._status = status

    @property
    def created_time(self):
        """Gets the created_time of this ShowDeviceMessageResponse.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ShowDeviceMessageResponse.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this ShowDeviceMessageResponse.
        :type: str
        """
        self._created_time = created_time

    @property
    def finished_time(self):
        """Gets the finished_time of this ShowDeviceMessageResponse.

        消息结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串，包含消息转换到DELIVERED和TIMEOUT两个状态的时间。

        :return: The finished_time of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        """Sets the finished_time of this ShowDeviceMessageResponse.

        消息结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串，包含消息转换到DELIVERED和TIMEOUT两个状态的时间。

        :param finished_time: The finished_time of this ShowDeviceMessageResponse.
        :type: str
        """
        self._finished_time = finished_time

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
        if not isinstance(other, ShowDeviceMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
