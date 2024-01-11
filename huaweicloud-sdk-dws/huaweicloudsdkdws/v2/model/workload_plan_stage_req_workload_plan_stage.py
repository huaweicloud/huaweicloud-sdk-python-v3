# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadPlanStageReqWorkloadPlanStage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day': 'str',
        'month': 'str',
        'stage_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'queue_list': 'list[QueueResourceItem]'
    }

    attribute_map = {
        'day': 'day',
        'month': 'month',
        'stage_name': 'stage_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'queue_list': 'queue_list'
    }

    def __init__(self, day=None, month=None, stage_name=None, start_time=None, end_time=None, queue_list=None):
        """WorkloadPlanStageReqWorkloadPlanStage

        The model defined in huaweicloud sdk

        :param day: 日期
        :type day: str
        :param month: 月份
        :type month: str
        :param stage_name: 计划阶段
        :type stage_name: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param queue_list: 资源队列
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        
        

        self._day = None
        self._month = None
        self._stage_name = None
        self._start_time = None
        self._end_time = None
        self._queue_list = None
        self.discriminator = None

        if day is not None:
            self.day = day
        if month is not None:
            self.month = month
        if stage_name is not None:
            self.stage_name = stage_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if queue_list is not None:
            self.queue_list = queue_list

    @property
    def day(self):
        """Gets the day of this WorkloadPlanStageReqWorkloadPlanStage.

        日期

        :return: The day of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: str
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this WorkloadPlanStageReqWorkloadPlanStage.

        日期

        :param day: The day of this WorkloadPlanStageReqWorkloadPlanStage.
        :type day: str
        """
        self._day = day

    @property
    def month(self):
        """Gets the month of this WorkloadPlanStageReqWorkloadPlanStage.

        月份

        :return: The month of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this WorkloadPlanStageReqWorkloadPlanStage.

        月份

        :param month: The month of this WorkloadPlanStageReqWorkloadPlanStage.
        :type month: str
        """
        self._month = month

    @property
    def stage_name(self):
        """Gets the stage_name of this WorkloadPlanStageReqWorkloadPlanStage.

        计划阶段

        :return: The stage_name of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: str
        """
        return self._stage_name

    @stage_name.setter
    def stage_name(self, stage_name):
        """Sets the stage_name of this WorkloadPlanStageReqWorkloadPlanStage.

        计划阶段

        :param stage_name: The stage_name of this WorkloadPlanStageReqWorkloadPlanStage.
        :type stage_name: str
        """
        self._stage_name = stage_name

    @property
    def start_time(self):
        """Gets the start_time of this WorkloadPlanStageReqWorkloadPlanStage.

        开始时间

        :return: The start_time of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this WorkloadPlanStageReqWorkloadPlanStage.

        开始时间

        :param start_time: The start_time of this WorkloadPlanStageReqWorkloadPlanStage.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this WorkloadPlanStageReqWorkloadPlanStage.

        结束时间

        :return: The end_time of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this WorkloadPlanStageReqWorkloadPlanStage.

        结束时间

        :param end_time: The end_time of this WorkloadPlanStageReqWorkloadPlanStage.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def queue_list(self):
        """Gets the queue_list of this WorkloadPlanStageReqWorkloadPlanStage.

        资源队列

        :return: The queue_list of this WorkloadPlanStageReqWorkloadPlanStage.
        :rtype: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, queue_list):
        """Sets the queue_list of this WorkloadPlanStageReqWorkloadPlanStage.

        资源队列

        :param queue_list: The queue_list of this WorkloadPlanStageReqWorkloadPlanStage.
        :type queue_list: list[:class:`huaweicloudsdkdws.v2.QueueResourceItem`]
        """
        self._queue_list = queue_list

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
        if not isinstance(other, WorkloadPlanStageReqWorkloadPlanStage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
