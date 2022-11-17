# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryLogKeyWordCountRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'step_interval': 'int',
        'group_id': 'str',
        'stream_id': 'str',
        'key_word': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'step_interval': 'step_interval',
        'group_id': 'group_id',
        'stream_id': 'stream_id',
        'key_word': 'key_word'
    }

    def __init__(self, start_time=None, end_time=None, step_interval=None, group_id=None, stream_id=None, key_word=None):
        """QueryLogKeyWordCountRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param step_interval: 步长间隔
        :type step_interval: int
        :param group_id: 日志组ID
        :type group_id: str
        :param stream_id: 日志流ID
        :type stream_id: str
        :param key_word: 关键词
        :type key_word: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._step_interval = None
        self._group_id = None
        self._stream_id = None
        self._key_word = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.step_interval = step_interval
        self.group_id = group_id
        self.stream_id = stream_id
        self.key_word = key_word

    @property
    def start_time(self):
        """Gets the start_time of this QueryLogKeyWordCountRequestBody.

        开始时间

        :return: The start_time of this QueryLogKeyWordCountRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryLogKeyWordCountRequestBody.

        开始时间

        :param start_time: The start_time of this QueryLogKeyWordCountRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryLogKeyWordCountRequestBody.

        结束时间

        :return: The end_time of this QueryLogKeyWordCountRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryLogKeyWordCountRequestBody.

        结束时间

        :param end_time: The end_time of this QueryLogKeyWordCountRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def step_interval(self):
        """Gets the step_interval of this QueryLogKeyWordCountRequestBody.

        步长间隔

        :return: The step_interval of this QueryLogKeyWordCountRequestBody.
        :rtype: int
        """
        return self._step_interval

    @step_interval.setter
    def step_interval(self, step_interval):
        """Sets the step_interval of this QueryLogKeyWordCountRequestBody.

        步长间隔

        :param step_interval: The step_interval of this QueryLogKeyWordCountRequestBody.
        :type step_interval: int
        """
        self._step_interval = step_interval

    @property
    def group_id(self):
        """Gets the group_id of this QueryLogKeyWordCountRequestBody.

        日志组ID

        :return: The group_id of this QueryLogKeyWordCountRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this QueryLogKeyWordCountRequestBody.

        日志组ID

        :param group_id: The group_id of this QueryLogKeyWordCountRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def stream_id(self):
        """Gets the stream_id of this QueryLogKeyWordCountRequestBody.

        日志流ID

        :return: The stream_id of this QueryLogKeyWordCountRequestBody.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """Sets the stream_id of this QueryLogKeyWordCountRequestBody.

        日志流ID

        :param stream_id: The stream_id of this QueryLogKeyWordCountRequestBody.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def key_word(self):
        """Gets the key_word of this QueryLogKeyWordCountRequestBody.

        关键词

        :return: The key_word of this QueryLogKeyWordCountRequestBody.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this QueryLogKeyWordCountRequestBody.

        关键词

        :param key_word: The key_word of this QueryLogKeyWordCountRequestBody.
        :type key_word: str
        """
        self._key_word = key_word

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
        if not isinstance(other, QueryLogKeyWordCountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
