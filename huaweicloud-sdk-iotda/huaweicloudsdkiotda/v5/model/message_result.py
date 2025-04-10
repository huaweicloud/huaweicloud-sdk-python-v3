# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MessageResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'created_time': 'str',
        'finished_time': 'str'
    }

    attribute_map = {
        'status': 'status',
        'created_time': 'created_time',
        'finished_time': 'finished_time'
    }

    def __init__(self, status=None, created_time=None, finished_time=None):
        r"""MessageResult

        The model defined in huaweicloud sdk

        :param status: 消息状态, PENDING，DELIVERED，FAILED和TIMEOUT。如果设备不在线，则平台缓存消息，并且返回PENDING，等设备数据上报之后再下发；如果设备在线，则消息直接进行下发，下发成功后接口返回DELIVERED，失败返回FAILED；如果消息在平台默认时间内（1天）还没有下发给设备，则平台会将消息设置为超时，状态为TIMEOUT。另外应用可以订阅消息的执行结果，平台会将消息结果推送给订阅的应用。
        :type status: str
        :param created_time: 消息的创建时间，\&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串。
        :type created_time: str
        :param finished_time: 消息结束时间, \&quot;yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;\&quot;格式的UTC字符串，包含消息转换到DELIVERED，FAILED和TIMEOUT状态的时间。
        :type finished_time: str
        """
        
        

        self._status = None
        self._created_time = None
        self._finished_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if finished_time is not None:
            self.finished_time = finished_time

    @property
    def status(self):
        r"""Gets the status of this MessageResult.

        消息状态, PENDING，DELIVERED，FAILED和TIMEOUT。如果设备不在线，则平台缓存消息，并且返回PENDING，等设备数据上报之后再下发；如果设备在线，则消息直接进行下发，下发成功后接口返回DELIVERED，失败返回FAILED；如果消息在平台默认时间内（1天）还没有下发给设备，则平台会将消息设置为超时，状态为TIMEOUT。另外应用可以订阅消息的执行结果，平台会将消息结果推送给订阅的应用。

        :return: The status of this MessageResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MessageResult.

        消息状态, PENDING，DELIVERED，FAILED和TIMEOUT。如果设备不在线，则平台缓存消息，并且返回PENDING，等设备数据上报之后再下发；如果设备在线，则消息直接进行下发，下发成功后接口返回DELIVERED，失败返回FAILED；如果消息在平台默认时间内（1天）还没有下发给设备，则平台会将消息设置为超时，状态为TIMEOUT。另外应用可以订阅消息的执行结果，平台会将消息结果推送给订阅的应用。

        :param status: The status of this MessageResult.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this MessageResult.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :return: The created_time of this MessageResult.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this MessageResult.

        消息的创建时间，\"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串。

        :param created_time: The created_time of this MessageResult.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def finished_time(self):
        r"""Gets the finished_time of this MessageResult.

        消息结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串，包含消息转换到DELIVERED，FAILED和TIMEOUT状态的时间。

        :return: The finished_time of this MessageResult.
        :rtype: str
        """
        return self._finished_time

    @finished_time.setter
    def finished_time(self, finished_time):
        r"""Sets the finished_time of this MessageResult.

        消息结束时间, \"yyyyMMdd'T'HHmmss'Z'\"格式的UTC字符串，包含消息转换到DELIVERED，FAILED和TIMEOUT状态的时间。

        :param finished_time: The finished_time of this MessageResult.
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
        if not isinstance(other, MessageResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
