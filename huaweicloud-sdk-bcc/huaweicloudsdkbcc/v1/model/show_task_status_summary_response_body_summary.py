# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskStatusSummaryResponseBodySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_task_count': 'int',
        'completed_task_count': 'int',
        'failed_task_count': 'int',
        'running_task_count': 'int',
        'skipped_task_count': 'int',
        'timeout_task_count': 'int'
    }

    attribute_map = {
        'total_task_count': 'total_task_count',
        'completed_task_count': 'completed_task_count',
        'failed_task_count': 'failed_task_count',
        'running_task_count': 'running_task_count',
        'skipped_task_count': 'skipped_task_count',
        'timeout_task_count': 'timeout_task_count'
    }

    def __init__(self, total_task_count=None, completed_task_count=None, failed_task_count=None, running_task_count=None, skipped_task_count=None, timeout_task_count=None):
        r"""ShowTaskStatusSummaryResponseBodySummary

        The model defined in huaweicloud sdk

        :param total_task_count: 总任务数据
        :type total_task_count: int
        :param completed_task_count: 已完成的总任务数
        :type completed_task_count: int
        :param failed_task_count: 失败的总任务数
        :type failed_task_count: int
        :param running_task_count: 运行中的总任务数
        :type running_task_count: int
        :param skipped_task_count: 跳过的总任务数
        :type skipped_task_count: int
        :param timeout_task_count: 超时的总任务数
        :type timeout_task_count: int
        """
        
        

        self._total_task_count = None
        self._completed_task_count = None
        self._failed_task_count = None
        self._running_task_count = None
        self._skipped_task_count = None
        self._timeout_task_count = None
        self.discriminator = None

        self.total_task_count = total_task_count
        self.completed_task_count = completed_task_count
        self.failed_task_count = failed_task_count
        self.running_task_count = running_task_count
        self.skipped_task_count = skipped_task_count
        self.timeout_task_count = timeout_task_count

    @property
    def total_task_count(self):
        r"""Gets the total_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        总任务数据

        :return: The total_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._total_task_count

    @total_task_count.setter
    def total_task_count(self, total_task_count):
        r"""Sets the total_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        总任务数据

        :param total_task_count: The total_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type total_task_count: int
        """
        self._total_task_count = total_task_count

    @property
    def completed_task_count(self):
        r"""Gets the completed_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        已完成的总任务数

        :return: The completed_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._completed_task_count

    @completed_task_count.setter
    def completed_task_count(self, completed_task_count):
        r"""Sets the completed_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        已完成的总任务数

        :param completed_task_count: The completed_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type completed_task_count: int
        """
        self._completed_task_count = completed_task_count

    @property
    def failed_task_count(self):
        r"""Gets the failed_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        失败的总任务数

        :return: The failed_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._failed_task_count

    @failed_task_count.setter
    def failed_task_count(self, failed_task_count):
        r"""Sets the failed_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        失败的总任务数

        :param failed_task_count: The failed_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type failed_task_count: int
        """
        self._failed_task_count = failed_task_count

    @property
    def running_task_count(self):
        r"""Gets the running_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        运行中的总任务数

        :return: The running_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._running_task_count

    @running_task_count.setter
    def running_task_count(self, running_task_count):
        r"""Sets the running_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        运行中的总任务数

        :param running_task_count: The running_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type running_task_count: int
        """
        self._running_task_count = running_task_count

    @property
    def skipped_task_count(self):
        r"""Gets the skipped_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        跳过的总任务数

        :return: The skipped_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._skipped_task_count

    @skipped_task_count.setter
    def skipped_task_count(self, skipped_task_count):
        r"""Sets the skipped_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        跳过的总任务数

        :param skipped_task_count: The skipped_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type skipped_task_count: int
        """
        self._skipped_task_count = skipped_task_count

    @property
    def timeout_task_count(self):
        r"""Gets the timeout_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        超时的总任务数

        :return: The timeout_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :rtype: int
        """
        return self._timeout_task_count

    @timeout_task_count.setter
    def timeout_task_count(self, timeout_task_count):
        r"""Sets the timeout_task_count of this ShowTaskStatusSummaryResponseBodySummary.

        超时的总任务数

        :param timeout_task_count: The timeout_task_count of this ShowTaskStatusSummaryResponseBodySummary.
        :type timeout_task_count: int
        """
        self._timeout_task_count = timeout_task_count

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
        if not isinstance(other, ShowTaskStatusSummaryResponseBodySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
