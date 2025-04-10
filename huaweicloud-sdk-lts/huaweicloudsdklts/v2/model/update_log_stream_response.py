# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogStreamResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'int',
        'log_topic_name': 'str',
        'log_topic_id': 'str',
        'ttl_in_days': 'int'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_topic_name': 'log_topic_name',
        'log_topic_id': 'log_topic_id',
        'ttl_in_days': 'ttl_in_days'
    }

    def __init__(self, creation_time=None, log_topic_name=None, log_topic_id=None, ttl_in_days=None):
        r"""UpdateLogStreamResponse

        The model defined in huaweicloud sdk

        :param creation_time: 创建该日志流的时间
        :type creation_time: int
        :param log_topic_name: 日志流的名称。
        :type log_topic_name: str
        :param log_topic_id: 日志流ID。
        :type log_topic_id: str
        :param ttl_in_days: 日志存储时间（天）。
        :type ttl_in_days: int
        """
        
        super(UpdateLogStreamResponse, self).__init__()

        self._creation_time = None
        self._log_topic_name = None
        self._log_topic_id = None
        self._ttl_in_days = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if log_topic_name is not None:
            self.log_topic_name = log_topic_name
        if log_topic_id is not None:
            self.log_topic_id = log_topic_id
        if ttl_in_days is not None:
            self.ttl_in_days = ttl_in_days

    @property
    def creation_time(self):
        r"""Gets the creation_time of this UpdateLogStreamResponse.

        创建该日志流的时间

        :return: The creation_time of this UpdateLogStreamResponse.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this UpdateLogStreamResponse.

        创建该日志流的时间

        :param creation_time: The creation_time of this UpdateLogStreamResponse.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_topic_name(self):
        r"""Gets the log_topic_name of this UpdateLogStreamResponse.

        日志流的名称。

        :return: The log_topic_name of this UpdateLogStreamResponse.
        :rtype: str
        """
        return self._log_topic_name

    @log_topic_name.setter
    def log_topic_name(self, log_topic_name):
        r"""Sets the log_topic_name of this UpdateLogStreamResponse.

        日志流的名称。

        :param log_topic_name: The log_topic_name of this UpdateLogStreamResponse.
        :type log_topic_name: str
        """
        self._log_topic_name = log_topic_name

    @property
    def log_topic_id(self):
        r"""Gets the log_topic_id of this UpdateLogStreamResponse.

        日志流ID。

        :return: The log_topic_id of this UpdateLogStreamResponse.
        :rtype: str
        """
        return self._log_topic_id

    @log_topic_id.setter
    def log_topic_id(self, log_topic_id):
        r"""Sets the log_topic_id of this UpdateLogStreamResponse.

        日志流ID。

        :param log_topic_id: The log_topic_id of this UpdateLogStreamResponse.
        :type log_topic_id: str
        """
        self._log_topic_id = log_topic_id

    @property
    def ttl_in_days(self):
        r"""Gets the ttl_in_days of this UpdateLogStreamResponse.

        日志存储时间（天）。

        :return: The ttl_in_days of this UpdateLogStreamResponse.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        r"""Sets the ttl_in_days of this UpdateLogStreamResponse.

        日志存储时间（天）。

        :param ttl_in_days: The ttl_in_days of this UpdateLogStreamResponse.
        :type ttl_in_days: int
        """
        self._ttl_in_days = ttl_in_days

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
        if not isinstance(other, UpdateLogStreamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
