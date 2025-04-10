# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogGroupResponse(SdkResponse):

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
        'log_group_name': 'str',
        'log_group_id': 'str',
        'ttl_in_days': 'int'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'log_group_name': 'log_group_name',
        'log_group_id': 'log_group_id',
        'ttl_in_days': 'ttl_in_days'
    }

    def __init__(self, creation_time=None, log_group_name=None, log_group_id=None, ttl_in_days=None):
        r"""UpdateLogGroupResponse

        The model defined in huaweicloud sdk

        :param creation_time: 创建该日志组的时间， 毫秒级。
        :type creation_time: int
        :param log_group_name: 日志组的名称。
        :type log_group_name: str
        :param log_group_id: 日志组ID。
        :type log_group_id: str
        :param ttl_in_days: 日志存储时间（天）。
        :type ttl_in_days: int
        """
        
        super(UpdateLogGroupResponse, self).__init__()

        self._creation_time = None
        self._log_group_name = None
        self._log_group_id = None
        self._ttl_in_days = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if ttl_in_days is not None:
            self.ttl_in_days = ttl_in_days

    @property
    def creation_time(self):
        r"""Gets the creation_time of this UpdateLogGroupResponse.

        创建该日志组的时间， 毫秒级。

        :return: The creation_time of this UpdateLogGroupResponse.
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this UpdateLogGroupResponse.

        创建该日志组的时间， 毫秒级。

        :param creation_time: The creation_time of this UpdateLogGroupResponse.
        :type creation_time: int
        """
        self._creation_time = creation_time

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this UpdateLogGroupResponse.

        日志组的名称。

        :return: The log_group_name of this UpdateLogGroupResponse.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this UpdateLogGroupResponse.

        日志组的名称。

        :param log_group_name: The log_group_name of this UpdateLogGroupResponse.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this UpdateLogGroupResponse.

        日志组ID。

        :return: The log_group_id of this UpdateLogGroupResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this UpdateLogGroupResponse.

        日志组ID。

        :param log_group_id: The log_group_id of this UpdateLogGroupResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def ttl_in_days(self):
        r"""Gets the ttl_in_days of this UpdateLogGroupResponse.

        日志存储时间（天）。

        :return: The ttl_in_days of this UpdateLogGroupResponse.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        r"""Sets the ttl_in_days of this UpdateLogGroupResponse.

        日志存储时间（天）。

        :param ttl_in_days: The ttl_in_days of this UpdateLogGroupResponse.
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
        if not isinstance(other, UpdateLogGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
