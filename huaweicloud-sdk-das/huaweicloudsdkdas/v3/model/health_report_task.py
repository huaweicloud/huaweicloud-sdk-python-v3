# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'instance_id': 'str',
        'create_at': 'int',
        'report_status': 'str',
        'risk_count': 'int',
        'origin': 'str',
        'start_at': 'int',
        'end_at': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'instance_id': 'instance_id',
        'create_at': 'create_at',
        'report_status': 'report_status',
        'risk_count': 'risk_count',
        'origin': 'origin',
        'start_at': 'start_at',
        'end_at': 'end_at'
    }

    def __init__(self, task_id=None, instance_id=None, create_at=None, report_status=None, risk_count=None, origin=None, start_at=None, end_at=None):
        r"""HealthReportTask

        The model defined in huaweicloud sdk

        :param task_id: 报告ID
        :type task_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param create_at: 创建时间（Unix timestamp），单位：毫秒。
        :type create_at: int
        :param report_status: 诊断状态
        :type report_status: str
        :param risk_count: 风险点数量
        :type risk_count: int
        :param origin: 触发源
        :type origin: str
        :param start_at: 日报诊断区间的起始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 日报诊断区间的结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        """
        
        

        self._task_id = None
        self._instance_id = None
        self._create_at = None
        self._report_status = None
        self._risk_count = None
        self._origin = None
        self._start_at = None
        self._end_at = None
        self.discriminator = None

        self.task_id = task_id
        self.instance_id = instance_id
        self.create_at = create_at
        self.report_status = report_status
        self.risk_count = risk_count
        self.origin = origin
        self.start_at = start_at
        self.end_at = end_at

    @property
    def task_id(self):
        r"""Gets the task_id of this HealthReportTask.

        报告ID

        :return: The task_id of this HealthReportTask.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this HealthReportTask.

        报告ID

        :param task_id: The task_id of this HealthReportTask.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this HealthReportTask.

        实例ID

        :return: The instance_id of this HealthReportTask.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this HealthReportTask.

        实例ID

        :param instance_id: The instance_id of this HealthReportTask.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def create_at(self):
        r"""Gets the create_at of this HealthReportTask.

        创建时间（Unix timestamp），单位：毫秒。

        :return: The create_at of this HealthReportTask.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this HealthReportTask.

        创建时间（Unix timestamp），单位：毫秒。

        :param create_at: The create_at of this HealthReportTask.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def report_status(self):
        r"""Gets the report_status of this HealthReportTask.

        诊断状态

        :return: The report_status of this HealthReportTask.
        :rtype: str
        """
        return self._report_status

    @report_status.setter
    def report_status(self, report_status):
        r"""Sets the report_status of this HealthReportTask.

        诊断状态

        :param report_status: The report_status of this HealthReportTask.
        :type report_status: str
        """
        self._report_status = report_status

    @property
    def risk_count(self):
        r"""Gets the risk_count of this HealthReportTask.

        风险点数量

        :return: The risk_count of this HealthReportTask.
        :rtype: int
        """
        return self._risk_count

    @risk_count.setter
    def risk_count(self, risk_count):
        r"""Sets the risk_count of this HealthReportTask.

        风险点数量

        :param risk_count: The risk_count of this HealthReportTask.
        :type risk_count: int
        """
        self._risk_count = risk_count

    @property
    def origin(self):
        r"""Gets the origin of this HealthReportTask.

        触发源

        :return: The origin of this HealthReportTask.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this HealthReportTask.

        触发源

        :param origin: The origin of this HealthReportTask.
        :type origin: str
        """
        self._origin = origin

    @property
    def start_at(self):
        r"""Gets the start_at of this HealthReportTask.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this HealthReportTask.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this HealthReportTask.

        日报诊断区间的起始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this HealthReportTask.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this HealthReportTask.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this HealthReportTask.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this HealthReportTask.

        日报诊断区间的结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this HealthReportTask.
        :type end_at: int
        """
        self._end_at = end_at

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
        if not isinstance(other, HealthReportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
