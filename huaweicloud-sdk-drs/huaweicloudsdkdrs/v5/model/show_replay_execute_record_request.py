# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayExecuteRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_language': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, job_id=None, x_language=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ShowReplayExecuteRecordRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param start_time: SQL执行记录的起始时间，格式为秒级时间戳。
        :type start_time: int
        :param end_time: SQL执行记录的结束时间，格式为秒级时间戳。
        :type end_time: int
        :param offset: 偏移量，表示查询该偏移量后面的记录，默认为0。
        :type offset: int
        :param limit: 查询返回记录的数量限制，默认为10，最大值为2000。
        :type limit: int
        """
        
        

        self._job_id = None
        self._x_language = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowReplayExecuteRecordRequest.

        任务ID。

        :return: The job_id of this ShowReplayExecuteRecordRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowReplayExecuteRecordRequest.

        任务ID。

        :param job_id: The job_id of this ShowReplayExecuteRecordRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowReplayExecuteRecordRequest.

        请求语言类型。

        :return: The x_language of this ShowReplayExecuteRecordRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowReplayExecuteRecordRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowReplayExecuteRecordRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowReplayExecuteRecordRequest.

        SQL执行记录的起始时间，格式为秒级时间戳。

        :return: The start_time of this ShowReplayExecuteRecordRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowReplayExecuteRecordRequest.

        SQL执行记录的起始时间，格式为秒级时间戳。

        :param start_time: The start_time of this ShowReplayExecuteRecordRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowReplayExecuteRecordRequest.

        SQL执行记录的结束时间，格式为秒级时间戳。

        :return: The end_time of this ShowReplayExecuteRecordRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowReplayExecuteRecordRequest.

        SQL执行记录的结束时间，格式为秒级时间戳。

        :param end_time: The end_time of this ShowReplayExecuteRecordRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowReplayExecuteRecordRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :return: The offset of this ShowReplayExecuteRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowReplayExecuteRecordRequest.

        偏移量，表示查询该偏移量后面的记录，默认为0。

        :param offset: The offset of this ShowReplayExecuteRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowReplayExecuteRecordRequest.

        查询返回记录的数量限制，默认为10，最大值为2000。

        :return: The limit of this ShowReplayExecuteRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowReplayExecuteRecordRequest.

        查询返回记录的数量限制，默认为10，最大值为2000。

        :param limit: The limit of this ShowReplayExecuteRecordRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowReplayExecuteRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
