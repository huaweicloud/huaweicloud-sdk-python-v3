# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateItemResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        '_from': 'str',
        'to': 'str',
        'status': 'str',
        'process': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'job_id': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_from': 'from',
        'to': 'to',
        'status': 'status',
        'process': 'process',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'job_id': 'job_id',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, id=None, _from=None, to=None, status=None, process=None, start_time=None, end_time=None, job_id=None, failed_reason=None):
        """UpdateItemResp

        The model defined in huaweicloud sdk

        :param id: 升级项ID
        :type id: str
        :param _from: 起始版本
        :type _from: str
        :param to: 目标版本
        :type to: str
        :param status: 升级路径状态
        :type status: str
        :param process: 升级进度
        :type process: str
        :param start_time: 起始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param job_id: 升级任务ID
        :type job_id: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        

        self._id = None
        self.__from = None
        self._to = None
        self._status = None
        self._process = None
        self._start_time = None
        self._end_time = None
        self._job_id = None
        self._failed_reason = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if status is not None:
            self.status = status
        if process is not None:
            self.process = process
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if job_id is not None:
            self.job_id = job_id
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def id(self):
        """Gets the id of this UpdateItemResp.

        升级项ID

        :return: The id of this UpdateItemResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateItemResp.

        升级项ID

        :param id: The id of this UpdateItemResp.
        :type id: str
        """
        self._id = id

    @property
    def _from(self):
        """Gets the _from of this UpdateItemResp.

        起始版本

        :return: The _from of this UpdateItemResp.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this UpdateItemResp.

        起始版本

        :param _from: The _from of this UpdateItemResp.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this UpdateItemResp.

        目标版本

        :return: The to of this UpdateItemResp.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this UpdateItemResp.

        目标版本

        :param to: The to of this UpdateItemResp.
        :type to: str
        """
        self._to = to

    @property
    def status(self):
        """Gets the status of this UpdateItemResp.

        升级路径状态

        :return: The status of this UpdateItemResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateItemResp.

        升级路径状态

        :param status: The status of this UpdateItemResp.
        :type status: str
        """
        self._status = status

    @property
    def process(self):
        """Gets the process of this UpdateItemResp.

        升级进度

        :return: The process of this UpdateItemResp.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this UpdateItemResp.

        升级进度

        :param process: The process of this UpdateItemResp.
        :type process: str
        """
        self._process = process

    @property
    def start_time(self):
        """Gets the start_time of this UpdateItemResp.

        起始时间

        :return: The start_time of this UpdateItemResp.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpdateItemResp.

        起始时间

        :param start_time: The start_time of this UpdateItemResp.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UpdateItemResp.

        结束时间

        :return: The end_time of this UpdateItemResp.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateItemResp.

        结束时间

        :param end_time: The end_time of this UpdateItemResp.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        """Gets the job_id of this UpdateItemResp.

        升级任务ID

        :return: The job_id of this UpdateItemResp.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this UpdateItemResp.

        升级任务ID

        :param job_id: The job_id of this UpdateItemResp.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def failed_reason(self):
        """Gets the failed_reason of this UpdateItemResp.

        失败原因

        :return: The failed_reason of this UpdateItemResp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this UpdateItemResp.

        失败原因

        :param failed_reason: The failed_reason of this UpdateItemResp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, UpdateItemResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
