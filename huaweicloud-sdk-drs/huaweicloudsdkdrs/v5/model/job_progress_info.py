# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobProgressInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'str',
        'incr_trans_delay': 'str',
        'incr_trans_delay_millis': 'str',
        'task_mode': 'str',
        'transfer_status': 'str',
        'process_time': 'str',
        'remaining_time': 'str',
        'progress_map': 'dict(str, ProgressCompleteInfo)'
    }

    attribute_map = {
        'progress': 'progress',
        'incr_trans_delay': 'incr_trans_delay',
        'incr_trans_delay_millis': 'incr_trans_delay_millis',
        'task_mode': 'task_mode',
        'transfer_status': 'transfer_status',
        'process_time': 'process_time',
        'remaining_time': 'remaining_time',
        'progress_map': 'progress_map'
    }

    def __init__(self, progress=None, incr_trans_delay=None, incr_trans_delay_millis=None, task_mode=None, transfer_status=None, process_time=None, remaining_time=None, progress_map=None):
        r"""JobProgressInfo

        The model defined in huaweicloud sdk

        :param progress: 迁移对比百分比。
        :type progress: str
        :param incr_trans_delay: 增量迁移时延（单位：s）。
        :type incr_trans_delay: str
        :param incr_trans_delay_millis: 增量迁移时延（单位：ms）。
        :type incr_trans_delay_millis: str
        :param task_mode: 迁移模式。
        :type task_mode: str
        :param transfer_status: 迁移状态。
        :type transfer_status: str
        :param process_time: 迁移时间。
        :type process_time: str
        :param remaining_time: 预计剩余时间。
        :type remaining_time: str
        :param progress_map: 全量迁移进度详情。
        :type progress_map: dict(str, ProgressCompleteInfo)
        """
        
        

        self._progress = None
        self._incr_trans_delay = None
        self._incr_trans_delay_millis = None
        self._task_mode = None
        self._transfer_status = None
        self._process_time = None
        self._remaining_time = None
        self._progress_map = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if incr_trans_delay is not None:
            self.incr_trans_delay = incr_trans_delay
        if incr_trans_delay_millis is not None:
            self.incr_trans_delay_millis = incr_trans_delay_millis
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

    @property
    def progress(self):
        r"""Gets the progress of this JobProgressInfo.

        迁移对比百分比。

        :return: The progress of this JobProgressInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this JobProgressInfo.

        迁移对比百分比。

        :param progress: The progress of this JobProgressInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def incr_trans_delay(self):
        r"""Gets the incr_trans_delay of this JobProgressInfo.

        增量迁移时延（单位：s）。

        :return: The incr_trans_delay of this JobProgressInfo.
        :rtype: str
        """
        return self._incr_trans_delay

    @incr_trans_delay.setter
    def incr_trans_delay(self, incr_trans_delay):
        r"""Sets the incr_trans_delay of this JobProgressInfo.

        增量迁移时延（单位：s）。

        :param incr_trans_delay: The incr_trans_delay of this JobProgressInfo.
        :type incr_trans_delay: str
        """
        self._incr_trans_delay = incr_trans_delay

    @property
    def incr_trans_delay_millis(self):
        r"""Gets the incr_trans_delay_millis of this JobProgressInfo.

        增量迁移时延（单位：ms）。

        :return: The incr_trans_delay_millis of this JobProgressInfo.
        :rtype: str
        """
        return self._incr_trans_delay_millis

    @incr_trans_delay_millis.setter
    def incr_trans_delay_millis(self, incr_trans_delay_millis):
        r"""Sets the incr_trans_delay_millis of this JobProgressInfo.

        增量迁移时延（单位：ms）。

        :param incr_trans_delay_millis: The incr_trans_delay_millis of this JobProgressInfo.
        :type incr_trans_delay_millis: str
        """
        self._incr_trans_delay_millis = incr_trans_delay_millis

    @property
    def task_mode(self):
        r"""Gets the task_mode of this JobProgressInfo.

        迁移模式。

        :return: The task_mode of this JobProgressInfo.
        :rtype: str
        """
        return self._task_mode

    @task_mode.setter
    def task_mode(self, task_mode):
        r"""Sets the task_mode of this JobProgressInfo.

        迁移模式。

        :param task_mode: The task_mode of this JobProgressInfo.
        :type task_mode: str
        """
        self._task_mode = task_mode

    @property
    def transfer_status(self):
        r"""Gets the transfer_status of this JobProgressInfo.

        迁移状态。

        :return: The transfer_status of this JobProgressInfo.
        :rtype: str
        """
        return self._transfer_status

    @transfer_status.setter
    def transfer_status(self, transfer_status):
        r"""Sets the transfer_status of this JobProgressInfo.

        迁移状态。

        :param transfer_status: The transfer_status of this JobProgressInfo.
        :type transfer_status: str
        """
        self._transfer_status = transfer_status

    @property
    def process_time(self):
        r"""Gets the process_time of this JobProgressInfo.

        迁移时间。

        :return: The process_time of this JobProgressInfo.
        :rtype: str
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        r"""Sets the process_time of this JobProgressInfo.

        迁移时间。

        :param process_time: The process_time of this JobProgressInfo.
        :type process_time: str
        """
        self._process_time = process_time

    @property
    def remaining_time(self):
        r"""Gets the remaining_time of this JobProgressInfo.

        预计剩余时间。

        :return: The remaining_time of this JobProgressInfo.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        r"""Sets the remaining_time of this JobProgressInfo.

        预计剩余时间。

        :param remaining_time: The remaining_time of this JobProgressInfo.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

    @property
    def progress_map(self):
        r"""Gets the progress_map of this JobProgressInfo.

        全量迁移进度详情。

        :return: The progress_map of this JobProgressInfo.
        :rtype: dict(str, ProgressCompleteInfo)
        """
        return self._progress_map

    @progress_map.setter
    def progress_map(self, progress_map):
        r"""Sets the progress_map of this JobProgressInfo.

        全量迁移进度详情。

        :param progress_map: The progress_map of this JobProgressInfo.
        :type progress_map: dict(str, ProgressCompleteInfo)
        """
        self._progress_map = progress_map

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
        if not isinstance(other, JobProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
