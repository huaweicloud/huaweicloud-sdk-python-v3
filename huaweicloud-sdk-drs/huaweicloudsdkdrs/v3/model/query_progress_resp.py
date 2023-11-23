# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryProgressResp:

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
        'progress': 'str',
        'incre_trans_delay': 'str',
        'incre_trans_delay_millis': 'str',
        'task_mode': 'str',
        'transfer_status': 'str',
        'process_time': 'str',
        'remaining_time': 'str',
        'progress_map': 'dict(str, ProgressInfo)',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'progress': 'progress',
        'incre_trans_delay': 'incre_trans_delay',
        'incre_trans_delay_millis': 'incre_trans_delay_millis',
        'task_mode': 'task_mode',
        'transfer_status': 'transfer_status',
        'process_time': 'process_time',
        'remaining_time': 'remaining_time',
        'progress_map': 'progress_map',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, job_id=None, progress=None, incre_trans_delay=None, incre_trans_delay_millis=None, task_mode=None, transfer_status=None, process_time=None, remaining_time=None, progress_map=None, error_code=None, error_msg=None):
        """QueryProgressResp

        The model defined in huaweicloud sdk

        :param job_id: 任务Id
        :type job_id: str
        :param progress: 迁移百分比
        :type progress: str
        :param incre_trans_delay: 增量迁移时延。单位：s
        :type incre_trans_delay: str
        :param incre_trans_delay_millis: 增量迁移时延。单位：ms
        :type incre_trans_delay_millis: str
        :param task_mode: 迁移模式。 - FULL_TRANS: 全量 - INCR_TRANS: 增量 - FULL_INCR_TRANS: 全量+增量
        :type task_mode: str
        :param transfer_status: 任务状态
        :type transfer_status: str
        :param process_time: 迁移时间，时间戳
        :type process_time: str
        :param remaining_time: 预计剩余时间
        :type remaining_time: str
        :param progress_map: 数据，结构，索引迁移进度信息体
        :type progress_map: dict(str, ProgressInfo)
        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误信息
        :type error_msg: str
        """
        
        

        self._job_id = None
        self._progress = None
        self._incre_trans_delay = None
        self._incre_trans_delay_millis = None
        self._task_mode = None
        self._transfer_status = None
        self._process_time = None
        self._remaining_time = None
        self._progress_map = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if progress is not None:
            self.progress = progress
        if incre_trans_delay is not None:
            self.incre_trans_delay = incre_trans_delay
        if incre_trans_delay_millis is not None:
            self.incre_trans_delay_millis = incre_trans_delay_millis
        if task_mode is not None:
            self.task_mode = task_mode
        if transfer_status is not None:
            self.transfer_status = transfer_status
        if process_time is not None:
            self.process_time = process_time
        if remaining_time is not None:
            self.remaining_time = remaining_time
        if progress_map is not None:
            self.progress_map = progress_map
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def job_id(self):
        """Gets the job_id of this QueryProgressResp.

        任务Id

        :return: The job_id of this QueryProgressResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this QueryProgressResp.

        任务Id

        :param job_id: The job_id of this QueryProgressResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def progress(self):
        """Gets the progress of this QueryProgressResp.

        迁移百分比

        :return: The progress of this QueryProgressResp.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this QueryProgressResp.

        迁移百分比

        :param progress: The progress of this QueryProgressResp.
        :type progress: str
        """
        self._progress = progress

    @property
    def incre_trans_delay(self):
        """Gets the incre_trans_delay of this QueryProgressResp.

        增量迁移时延。单位：s

        :return: The incre_trans_delay of this QueryProgressResp.
        :rtype: str
        """
        return self._incre_trans_delay

    @incre_trans_delay.setter
    def incre_trans_delay(self, incre_trans_delay):
        """Sets the incre_trans_delay of this QueryProgressResp.

        增量迁移时延。单位：s

        :param incre_trans_delay: The incre_trans_delay of this QueryProgressResp.
        :type incre_trans_delay: str
        """
        self._incre_trans_delay = incre_trans_delay

    @property
    def incre_trans_delay_millis(self):
        """Gets the incre_trans_delay_millis of this QueryProgressResp.

        增量迁移时延。单位：ms

        :return: The incre_trans_delay_millis of this QueryProgressResp.
        :rtype: str
        """
        return self._incre_trans_delay_millis

    @incre_trans_delay_millis.setter
    def incre_trans_delay_millis(self, incre_trans_delay_millis):
        """Sets the incre_trans_delay_millis of this QueryProgressResp.

        增量迁移时延。单位：ms

        :param incre_trans_delay_millis: The incre_trans_delay_millis of this QueryProgressResp.
        :type incre_trans_delay_millis: str
        """
        self._incre_trans_delay_millis = incre_trans_delay_millis

    @property
    def task_mode(self):
        """Gets the task_mode of this QueryProgressResp.

        迁移模式。 - FULL_TRANS: 全量 - INCR_TRANS: 增量 - FULL_INCR_TRANS: 全量+增量

        :return: The task_mode of this QueryProgressResp.
        :rtype: str
        """
        return self._task_mode

    @task_mode.setter
    def task_mode(self, task_mode):
        """Sets the task_mode of this QueryProgressResp.

        迁移模式。 - FULL_TRANS: 全量 - INCR_TRANS: 增量 - FULL_INCR_TRANS: 全量+增量

        :param task_mode: The task_mode of this QueryProgressResp.
        :type task_mode: str
        """
        self._task_mode = task_mode

    @property
    def transfer_status(self):
        """Gets the transfer_status of this QueryProgressResp.

        任务状态

        :return: The transfer_status of this QueryProgressResp.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        """Sets the transfer_status of this QueryProgressResp.

        任务状态

        :param transfer_status: The transfer_status of this QueryProgressResp.
        :type transfer_status: str
        """
        self._transfer_status = transfer_status

    @property
    def process_time(self):
        """Gets the process_time of this QueryProgressResp.

        迁移时间，时间戳

        :return: The process_time of this QueryProgressResp.
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        """Sets the process_time of this QueryProgressResp.

        迁移时间，时间戳

        :param process_time: The process_time of this QueryProgressResp.
        :type process_time: str
        """
        self._process_time = process_time

    @property
    def remaining_time(self):
        """Gets the remaining_time of this QueryProgressResp.

        预计剩余时间

        :return: The remaining_time of this QueryProgressResp.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        """Sets the remaining_time of this QueryProgressResp.

        预计剩余时间

        :param remaining_time: The remaining_time of this QueryProgressResp.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

    @property
    def progress_map(self):
        """Gets the progress_map of this QueryProgressResp.

        数据，结构，索引迁移进度信息体

        :return: The progress_map of this QueryProgressResp.
        :rtype: dict(str, ProgressInfo)
        """
        return self._progress_map

    @progress_map.setter
    def progress_map(self, progress_map):
        """Sets the progress_map of this QueryProgressResp.

        数据，结构，索引迁移进度信息体

        :param progress_map: The progress_map of this QueryProgressResp.
        :type progress_map: dict(str, ProgressInfo)
        """
        self._progress_map = progress_map

    @property
    def error_code(self):
        """Gets the error_code of this QueryProgressResp.

        错误码

        :return: The error_code of this QueryProgressResp.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this QueryProgressResp.

        错误码

        :param error_code: The error_code of this QueryProgressResp.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this QueryProgressResp.

        错误信息

        :return: The error_msg of this QueryProgressResp.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this QueryProgressResp.

        错误信息

        :param error_msg: The error_msg of this QueryProgressResp.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, QueryProgressResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
