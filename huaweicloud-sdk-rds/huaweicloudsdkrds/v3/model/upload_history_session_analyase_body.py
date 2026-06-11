# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadHistorySessionAnalyaseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, type=None, start_time=None, end_time=None):
        r"""UploadHistorySessionAnalyaseBody

        The model defined in huaweicloud sdk

        :param type: 类型。 session    表示下载历史会话 wait_event    表示下载历史等待事件 top_sql    表示下载历史top sql
        :type type: str
        :param start_time: 参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type start_time: int
        :param end_time: 参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type end_time: int
        """
        
        

        self._type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.type = type
        self.start_time = start_time
        self.end_time = end_time

    @property
    def type(self):
        r"""Gets the type of this UploadHistorySessionAnalyaseBody.

        类型。 session    表示下载历史会话 wait_event    表示下载历史等待事件 top_sql    表示下载历史top sql

        :return: The type of this UploadHistorySessionAnalyaseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UploadHistorySessionAnalyaseBody.

        类型。 session    表示下载历史会话 wait_event    表示下载历史等待事件 top_sql    表示下载历史top sql

        :param type: The type of this UploadHistorySessionAnalyaseBody.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this UploadHistorySessionAnalyaseBody.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The start_time of this UploadHistorySessionAnalyaseBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this UploadHistorySessionAnalyaseBody.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param start_time: The start_time of this UploadHistorySessionAnalyaseBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UploadHistorySessionAnalyaseBody.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The end_time of this UploadHistorySessionAnalyaseBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UploadHistorySessionAnalyaseBody.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param end_time: The end_time of this UploadHistorySessionAnalyaseBody.
        :type end_time: int
        """
        self._end_time = end_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UploadHistorySessionAnalyaseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
