# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'job_id': 'str',
        'report_time': 'int'
    }

    attribute_map = {
        'order_id': 'order_id',
        'job_id': 'job_id',
        'report_time': 'report_time'
    }

    def __init__(self, order_id=None, job_id=None, report_time=None):
        r"""ExecutionSummary

        The model defined in huaweicloud sdk

        :param order_id: 工单Id
        :type order_id: str
        :param job_id: 脚本执行Id
        :type job_id: str
        :param report_time: 报告时间
        :type report_time: int
        """
        
        

        self._order_id = None
        self._job_id = None
        self._report_time = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if job_id is not None:
            self.job_id = job_id
        if report_time is not None:
            self.report_time = report_time

    @property
    def order_id(self):
        r"""Gets the order_id of this ExecutionSummary.

        工单Id

        :return: The order_id of this ExecutionSummary.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ExecutionSummary.

        工单Id

        :param order_id: The order_id of this ExecutionSummary.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ExecutionSummary.

        脚本执行Id

        :return: The job_id of this ExecutionSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ExecutionSummary.

        脚本执行Id

        :param job_id: The job_id of this ExecutionSummary.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def report_time(self):
        r"""Gets the report_time of this ExecutionSummary.

        报告时间

        :return: The report_time of this ExecutionSummary.
        :rtype: int
        """
        return self._report_time

    @report_time.setter
    def report_time(self, report_time):
        r"""Sets the report_time of this ExecutionSummary.

        报告时间

        :param report_time: The report_time of this ExecutionSummary.
        :type report_time: int
        """
        self._report_time = report_time

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
        if not isinstance(other, ExecutionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
