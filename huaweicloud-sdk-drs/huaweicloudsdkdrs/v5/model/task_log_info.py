# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'str',
        'message': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'level': 'level',
        'message': 'message',
        'create_time': 'create_time'
    }

    def __init__(self, level=None, message=None, create_time=None):
        r"""TaskLogInfo

        The model defined in huaweicloud sdk

        :param level: 日志级别。
        :type level: str
        :param message: 日志信息。
        :type message: str
        :param create_time: 日志时间。
        :type create_time: str
        """
        
        

        self._level = None
        self._message = None
        self._create_time = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if message is not None:
            self.message = message
        if create_time is not None:
            self.create_time = create_time

    @property
    def level(self):
        r"""Gets the level of this TaskLogInfo.

        日志级别。

        :return: The level of this TaskLogInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this TaskLogInfo.

        日志级别。

        :param level: The level of this TaskLogInfo.
        :type level: str
        """
        self._level = level

    @property
    def message(self):
        r"""Gets the message of this TaskLogInfo.

        日志信息。

        :return: The message of this TaskLogInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this TaskLogInfo.

        日志信息。

        :param message: The message of this TaskLogInfo.
        :type message: str
        """
        self._message = message

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskLogInfo.

        日志时间。

        :return: The create_time of this TaskLogInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskLogInfo.

        日志时间。

        :param create_time: The create_time of this TaskLogInfo.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, TaskLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
