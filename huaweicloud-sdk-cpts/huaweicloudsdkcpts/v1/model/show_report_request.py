# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReportRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_id': 'int',
        'case_run_id': 'int',
        'brokens_limit_count': 'int'
    }

    attribute_map = {
        'task_run_id': 'task_run_id',
        'case_run_id': 'case_run_id',
        'brokens_limit_count': 'brokens_limit_count'
    }

    def __init__(self, task_run_id=None, case_run_id=None, brokens_limit_count=None):
        """ShowReportRequest

        The model defined in huaweicloud sdk

        :param task_run_id: 运行任务id
        :type task_run_id: int
        :param case_run_id: 运行用例id
        :type case_run_id: int
        :param brokens_limit_count: 曲线图点数
        :type brokens_limit_count: int
        """
        
        

        self._task_run_id = None
        self._case_run_id = None
        self._brokens_limit_count = None
        self.discriminator = None

        self.task_run_id = task_run_id
        self.case_run_id = case_run_id
        self.brokens_limit_count = brokens_limit_count

    @property
    def task_run_id(self):
        """Gets the task_run_id of this ShowReportRequest.

        运行任务id

        :return: The task_run_id of this ShowReportRequest.
        :rtype: int
        """
        return self._task_run_id

    @task_run_id.setter
    def task_run_id(self, task_run_id):
        """Sets the task_run_id of this ShowReportRequest.

        运行任务id

        :param task_run_id: The task_run_id of this ShowReportRequest.
        :type task_run_id: int
        """
        self._task_run_id = task_run_id

    @property
    def case_run_id(self):
        """Gets the case_run_id of this ShowReportRequest.

        运行用例id

        :return: The case_run_id of this ShowReportRequest.
        :rtype: int
        """
        return self._case_run_id

    @case_run_id.setter
    def case_run_id(self, case_run_id):
        """Sets the case_run_id of this ShowReportRequest.

        运行用例id

        :param case_run_id: The case_run_id of this ShowReportRequest.
        :type case_run_id: int
        """
        self._case_run_id = case_run_id

    @property
    def brokens_limit_count(self):
        """Gets the brokens_limit_count of this ShowReportRequest.

        曲线图点数

        :return: The brokens_limit_count of this ShowReportRequest.
        :rtype: int
        """
        return self._brokens_limit_count

    @brokens_limit_count.setter
    def brokens_limit_count(self, brokens_limit_count):
        """Sets the brokens_limit_count of this ShowReportRequest.

        曲线图点数

        :param brokens_limit_count: The brokens_limit_count of this ShowReportRequest.
        :type brokens_limit_count: int
        """
        self._brokens_limit_count = brokens_limit_count

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
        if not isinstance(other, ShowReportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
