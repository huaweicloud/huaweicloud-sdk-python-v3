# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReplayProgressResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'int',
        'parse_count': 'int',
        'replay_count': 'int',
        'task_mode': 'str',
        'process_time': 'int',
        'transfer_status': 'str',
        'max_time': 'int',
        'min_time': 'int',
        'now_time': 'int',
        'min_export_time': 'int',
        'max_export_time': 'int',
        'replay_sql_now_list': 'list[ReplaySqlNowInfo]'
    }

    attribute_map = {
        'progress': 'progress',
        'parse_count': 'parse_count',
        'replay_count': 'replay_count',
        'task_mode': 'task_mode',
        'process_time': 'process_time',
        'transfer_status': 'transfer_status',
        'max_time': 'max_time',
        'min_time': 'min_time',
        'now_time': 'now_time',
        'min_export_time': 'min_export_time',
        'max_export_time': 'max_export_time',
        'replay_sql_now_list': 'replay_sql_now_list'
    }

    def __init__(self, progress=None, parse_count=None, replay_count=None, task_mode=None, process_time=None, transfer_status=None, max_time=None, min_time=None, now_time=None, min_export_time=None, max_export_time=None, replay_sql_now_list=None):
        r"""ShowReplayProgressResponse

        The model defined in huaweicloud sdk

        :param progress: 回放进度的百分数
        :type progress: int
        :param parse_count: 需要解析的总数
        :type parse_count: int
        :param replay_count: 回放的总数
        :type replay_count: int
        :param task_mode: 迁移模式
        :type task_mode: str
        :param process_time: 迁移时间
        :type process_time: int
        :param transfer_status: 迁移状态
        :type transfer_status: str
        :param max_time: 回放最大时间
        :type max_time: int
        :param min_time: 回放最小时间
        :type min_time: int
        :param now_time: 回放当前时间
        :type now_time: int
        :param min_export_time: 回放报告最小时间
        :type min_export_time: int
        :param max_export_time: 回放报告最大时间
        :type max_export_time: int
        :param replay_sql_now_list: 正在回放的sql列表
        :type replay_sql_now_list: list[:class:`huaweicloudsdkdrs.v5.ReplaySqlNowInfo`]
        """
        
        super().__init__()

        self._progress = None
        self._parse_count = None
        self._replay_count = None
        self._task_mode = None
        self._process_time = None
        self._transfer_status = None
        self._max_time = None
        self._min_time = None
        self._now_time = None
        self._min_export_time = None
        self._max_export_time = None
        self._replay_sql_now_list = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if parse_count is not None:
            self.parse_count = parse_count
        if replay_count is not None:
            self.replay_count = replay_count
        if task_mode is not None:
            self.task_mode = task_mode
        if process_time is not None:
            self.process_time = process_time
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if max_time is not None:
            self.max_time = max_time
        if min_time is not None:
            self.min_time = min_time
        if now_time is not None:
            self.now_time = now_time
        if min_export_time is not None:
            self.min_export_time = min_export_time
        if max_export_time is not None:
            self.max_export_time = max_export_time
        if replay_sql_now_list is not None:
            self.replay_sql_now_list = replay_sql_now_list

    @property
    def progress(self):
        r"""Gets the progress of this ShowReplayProgressResponse.

        回放进度的百分数

        :return: The progress of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ShowReplayProgressResponse.

        回放进度的百分数

        :param progress: The progress of this ShowReplayProgressResponse.
        :type progress: int
        """
        self._progress = progress

    @property
    def parse_count(self):
        r"""Gets the parse_count of this ShowReplayProgressResponse.

        需要解析的总数

        :return: The parse_count of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._parse_count

    @parse_count.setter
    def parse_count(self, parse_count):
        r"""Sets the parse_count of this ShowReplayProgressResponse.

        需要解析的总数

        :param parse_count: The parse_count of this ShowReplayProgressResponse.
        :type parse_count: int
        """
        self._parse_count = parse_count

    @property
    def replay_count(self):
        r"""Gets the replay_count of this ShowReplayProgressResponse.

        回放的总数

        :return: The replay_count of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._replay_count

    @replay_count.setter
    def replay_count(self, replay_count):
        r"""Sets the replay_count of this ShowReplayProgressResponse.

        回放的总数

        :param replay_count: The replay_count of this ShowReplayProgressResponse.
        :type replay_count: int
        """
        self._replay_count = replay_count

    @property
    def task_mode(self):
        r"""Gets the task_mode of this ShowReplayProgressResponse.

        迁移模式

        :return: The task_mode of this ShowReplayProgressResponse.
        :rtype: str
        """
        return self._task_mode

    @task_mode.setter
    def task_mode(self, task_mode):
        r"""Sets the task_mode of this ShowReplayProgressResponse.

        迁移模式

        :param task_mode: The task_mode of this ShowReplayProgressResponse.
        :type task_mode: str
        """
        self._task_mode = task_mode

    @property
    def process_time(self):
        r"""Gets the process_time of this ShowReplayProgressResponse.

        迁移时间

        :return: The process_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        r"""Sets the process_time of this ShowReplayProgressResponse.

        迁移时间

        :param process_time: The process_time of this ShowReplayProgressResponse.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def transfer_status(self):
        r"""Gets the transfer_status of this ShowReplayProgressResponse.

        迁移状态

        :return: The transfer_status of this ShowReplayProgressResponse.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        r"""Sets the transfer_status of this ShowReplayProgressResponse.

        迁移状态

        :param transfer_status: The transfer_status of this ShowReplayProgressResponse.
        :type transfer_status: str
        """
        self._transfer_status = transfer_status

    @property
    def max_time(self):
        r"""Gets the max_time of this ShowReplayProgressResponse.

        回放最大时间

        :return: The max_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        r"""Sets the max_time of this ShowReplayProgressResponse.

        回放最大时间

        :param max_time: The max_time of this ShowReplayProgressResponse.
        :type max_time: int
        """
        self._max_time = max_time

    @property
    def min_time(self):
        r"""Gets the min_time of this ShowReplayProgressResponse.

        回放最小时间

        :return: The min_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time):
        r"""Sets the min_time of this ShowReplayProgressResponse.

        回放最小时间

        :param min_time: The min_time of this ShowReplayProgressResponse.
        :type min_time: int
        """
        self._min_time = min_time

    @property
    def now_time(self):
        r"""Gets the now_time of this ShowReplayProgressResponse.

        回放当前时间

        :return: The now_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._now_time

    @now_time.setter
    def now_time(self, now_time):
        r"""Sets the now_time of this ShowReplayProgressResponse.

        回放当前时间

        :param now_time: The now_time of this ShowReplayProgressResponse.
        :type now_time: int
        """
        self._now_time = now_time

    @property
    def min_export_time(self):
        r"""Gets the min_export_time of this ShowReplayProgressResponse.

        回放报告最小时间

        :return: The min_export_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._min_export_time

    @min_export_time.setter
    def min_export_time(self, min_export_time):
        r"""Sets the min_export_time of this ShowReplayProgressResponse.

        回放报告最小时间

        :param min_export_time: The min_export_time of this ShowReplayProgressResponse.
        :type min_export_time: int
        """
        self._min_export_time = min_export_time

    @property
    def max_export_time(self):
        r"""Gets the max_export_time of this ShowReplayProgressResponse.

        回放报告最大时间

        :return: The max_export_time of this ShowReplayProgressResponse.
        :rtype: int
        """
        return self._max_export_time

    @max_export_time.setter
    def max_export_time(self, max_export_time):
        r"""Sets the max_export_time of this ShowReplayProgressResponse.

        回放报告最大时间

        :param max_export_time: The max_export_time of this ShowReplayProgressResponse.
        :type max_export_time: int
        """
        self._max_export_time = max_export_time

    @property
    def replay_sql_now_list(self):
        r"""Gets the replay_sql_now_list of this ShowReplayProgressResponse.

        正在回放的sql列表

        :return: The replay_sql_now_list of this ShowReplayProgressResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.ReplaySqlNowInfo`]
        """
        return self._replay_sql_now_list

    @replay_sql_now_list.setter
    def replay_sql_now_list(self, replay_sql_now_list):
        r"""Sets the replay_sql_now_list of this ShowReplayProgressResponse.

        正在回放的sql列表

        :param replay_sql_now_list: The replay_sql_now_list of this ShowReplayProgressResponse.
        :type replay_sql_now_list: list[:class:`huaweicloudsdkdrs.v5.ReplaySqlNowInfo`]
        """
        self._replay_sql_now_list = replay_sql_now_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowReplayProgressResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowReplayProgressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
