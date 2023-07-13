# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'message': 'object',
        'encoding': 'str',
        'payload_format': 'str',
        'topic': 'str',
        'properties': 'PropertiesDTO',
        'status': 'str',
        'error_info': 'ErrorInfoDTO',
        'created_time': 'str',
        'finished_time': 'str'
    }

    attribute_map = {
        'message_id': 'message_id',
        'name': 'name',
        'message': 'message',
        'encoding': 'encoding',
        'payload_format': 'payload_format',
        'topic': 'topic',
        'properties': 'properties',
        'status': 'status',
        'error_info': 'error_info',
        'created_time': 'created_time',
        'finished_time': 'finished_time'
    }

    def __init__(self, message_id=None, name=None, message=None, encoding=None, payload_format=None, topic=None, properties=None, status=None, error_info=None, created_time=None, finished_time=None):
        """ShowDeviceMessageResponse

        The model defined in huaweicloud sdk

        :param message_id: 设备消息ID，用于唯一标识一条消息，在下发设备消息时由物联网平台分配获得。
        :type message_id: str
        :param name: 消息名称,在下发消息时由用户指定。
        :type name: str
        :param message: 消息内容。
        :type message: object
        :param encoding: 消息内容编码格式，取值范围none|base64,默认值none, base64格式仅支持透传。
        :type encoding: str
        :param payload_format: 有效负载格式，在消息内容编码格式为none时有效，取值范围standard|raw，默认值standard（平台封装的标准格式），取值为raw时直接将消息内容作为有效负载下发。
        :type payload_format: str
        :param topic: 消息topic
        :type topic: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        :param status: 消息状态，包含PENDING，DELIVERED，FAILED和TIMEOUT，PENDING指设备不在线，消息被缓存起来，等设备上线之后下发； DELIVERED指消息发送成功；FAILED消息发送失败；TIMEOUT指消息在平台默认时间内（1天）还没有下发送给设备，则平台会将消息设置为超时，状态为TIMEOUT。
        :type status: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkiotda.v5.ErrorInfoDTO`
        :param created_time: 消息的创建时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type created_time: str
        :param finished_time: 消息结束时间, \&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串，包含消息转换到DELIVERED和TIMEOUT两个状态的时间。
        :type finished_time: str
        """
        
        super(ShowDeviceMessageResponse, self).__init__()

        self._message_id = None
        self._name = None
        self._message = None
        self._encoding = None
        self._payload_format = None
        self._topic = None
        self._properties = None
        self._status = None
        self._error_info = None
        self._created_time = None
        self._finished_time = None
        self.discriminator = None

        if message_id is not None:
            self.message_id = message_id
        if name is not None:
            self.name = name
        if message is not None:
            self.message = message
        if encoding is not None:
            self.encoding = encoding
        if payload_format is not None:
            self.payload_format = payload_format
        if topic is not None:
            self.topic = topic
        if properties is not None:
            self.properties = properties
        if status is not None:
            self.status = status
        if error_info is not None:
            self.error_info = error_info
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
        :type message_id: str
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
        :type name: str
        """
        self._name = name

    @property
    def message(self):
        """Gets the message of this ShowDeviceMessageResponse.

        消息内容。

        :return: The message of this ShowDeviceMessageResponse.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowDeviceMessageResponse.

        消息内容。

        :param message: The message of this ShowDeviceMessageResponse.
        :type message: object
        """
        self._message = message

    @property
    def encoding(self):
        """Gets the encoding of this ShowDeviceMessageResponse.

        消息内容编码格式，取值范围none|base64,默认值none, base64格式仅支持透传。

        :return: The encoding of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ShowDeviceMessageResponse.

        消息内容编码格式，取值范围none|base64,默认值none, base64格式仅支持透传。

        :param encoding: The encoding of this ShowDeviceMessageResponse.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def payload_format(self):
        """Gets the payload_format of this ShowDeviceMessageResponse.

        有效负载格式，在消息内容编码格式为none时有效，取值范围standard|raw，默认值standard（平台封装的标准格式），取值为raw时直接将消息内容作为有效负载下发。

        :return: The payload_format of this ShowDeviceMessageResponse.
        :rtype: str
        """
        return self._payload_format

    @payload_format.setter
    def payload_format(self, payload_format):
        """Sets the payload_format of this ShowDeviceMessageResponse.

        有效负载格式，在消息内容编码格式为none时有效，取值范围standard|raw，默认值standard（平台封装的标准格式），取值为raw时直接将消息内容作为有效负载下发。

        :param payload_format: The payload_format of this ShowDeviceMessageResponse.
        :type payload_format: str
        """
        self._payload_format = payload_format

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
        :type topic: str
        """
        self._topic = topic

    @property
    def properties(self):
        """Gets the properties of this ShowDeviceMessageResponse.

        :return: The properties of this ShowDeviceMessageResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ShowDeviceMessageResponse.

        :param properties: The properties of this ShowDeviceMessageResponse.
        :type properties: :class:`huaweicloudsdkiotda.v5.PropertiesDTO`
        """
        self._properties = properties

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
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        """Gets the error_info of this ShowDeviceMessageResponse.

        :return: The error_info of this ShowDeviceMessageResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.ErrorInfoDTO`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this ShowDeviceMessageResponse.

        :param error_info: The error_info of this ShowDeviceMessageResponse.
        :type error_info: :class:`huaweicloudsdkiotda.v5.ErrorInfoDTO`
        """
        self._error_info = error_info

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
        :type created_time: str
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
        :type finished_time: str
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
        if not isinstance(other, ShowDeviceMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
