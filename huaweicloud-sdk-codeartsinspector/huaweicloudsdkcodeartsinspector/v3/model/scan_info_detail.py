# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanInfoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'enable_weak_passwd': 'bool',
        'end_time': 'int',
        'progress': 'int',
        'reason': 'str',
        'status': 'int'
    }

    attribute_map = {
        'create_time': 'create_time',
        'enable_weak_passwd': 'enable_weak_passwd',
        'end_time': 'end_time',
        'progress': 'progress',
        'reason': 'reason',
        'status': 'status'
    }

    def __init__(self, create_time=None, enable_weak_passwd=None, end_time=None, progress=None, reason=None, status=None):
        r"""ScanInfoDetail

        The model defined in huaweicloud sdk

        :param create_time: 扫描任务创建时间
        :type create_time: int
        :param enable_weak_passwd: 弱密码检查
        :type enable_weak_passwd: bool
        :param end_time: 扫描任务结束时间
        :type end_time: int
        :param progress: 任务进度
        :type progress: int
        :param reason: 任务描述
        :type reason: str
        :param status: 扫描任务状态:   * 0 运行中   * 1 已完成   * 2 手动取消   * 3 等待中   * 4 扫描失败   * 5 等待定时调度 
        :type status: int
        """
        
        

        self._create_time = None
        self._enable_weak_passwd = None
        self._end_time = None
        self._progress = None
        self._reason = None
        self._status = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if enable_weak_passwd is not None:
            self.enable_weak_passwd = enable_weak_passwd
        if end_time is not None:
            self.end_time = end_time
        if progress is not None:
            self.progress = progress
        if reason is not None:
            self.reason = reason
        if status is not None:
            self.status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ScanInfoDetail.

        扫描任务创建时间

        :return: The create_time of this ScanInfoDetail.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScanInfoDetail.

        扫描任务创建时间

        :param create_time: The create_time of this ScanInfoDetail.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def enable_weak_passwd(self):
        r"""Gets the enable_weak_passwd of this ScanInfoDetail.

        弱密码检查

        :return: The enable_weak_passwd of this ScanInfoDetail.
        :rtype: bool
        """
        return self._enable_weak_passwd

    @enable_weak_passwd.setter
    def enable_weak_passwd(self, enable_weak_passwd):
        r"""Sets the enable_weak_passwd of this ScanInfoDetail.

        弱密码检查

        :param enable_weak_passwd: The enable_weak_passwd of this ScanInfoDetail.
        :type enable_weak_passwd: bool
        """
        self._enable_weak_passwd = enable_weak_passwd

    @property
    def end_time(self):
        r"""Gets the end_time of this ScanInfoDetail.

        扫描任务结束时间

        :return: The end_time of this ScanInfoDetail.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScanInfoDetail.

        扫描任务结束时间

        :param end_time: The end_time of this ScanInfoDetail.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def progress(self):
        r"""Gets the progress of this ScanInfoDetail.

        任务进度

        :return: The progress of this ScanInfoDetail.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ScanInfoDetail.

        任务进度

        :param progress: The progress of this ScanInfoDetail.
        :type progress: int
        """
        self._progress = progress

    @property
    def reason(self):
        r"""Gets the reason of this ScanInfoDetail.

        任务描述

        :return: The reason of this ScanInfoDetail.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ScanInfoDetail.

        任务描述

        :param reason: The reason of this ScanInfoDetail.
        :type reason: str
        """
        self._reason = reason

    @property
    def status(self):
        r"""Gets the status of this ScanInfoDetail.

        扫描任务状态:   * 0 运行中   * 1 已完成   * 2 手动取消   * 3 等待中   * 4 扫描失败   * 5 等待定时调度 

        :return: The status of this ScanInfoDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScanInfoDetail.

        扫描任务状态:   * 0 运行中   * 1 已完成   * 2 手动取消   * 3 等待中   * 4 扫描失败   * 5 等待定时调度 

        :param status: The status of this ScanInfoDetail.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ScanInfoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
