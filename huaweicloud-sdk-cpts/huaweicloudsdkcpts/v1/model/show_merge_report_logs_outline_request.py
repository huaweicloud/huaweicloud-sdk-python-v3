# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMergeReportLogsOutlineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_run_id': 'int'
    }

    attribute_map = {
        'task_run_id': 'task_run_id'
    }

    def __init__(self, task_run_id=None):
        r"""ShowMergeReportLogsOutlineRequest

        The model defined in huaweicloud sdk

        :param task_run_id: 运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。
        :type task_run_id: int
        """
        
        

        self._task_run_id = None
        self.discriminator = None

        self.task_run_id = task_run_id

    @property
    def task_run_id(self):
        r"""Gets the task_run_id of this ShowMergeReportLogsOutlineRequest.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :return: The task_run_id of this ShowMergeReportLogsOutlineRequest.
        :rtype: int
        """
        return self._task_run_id

    @task_run_id.setter
    def task_run_id(self, task_run_id):
        r"""Sets the task_run_id of this ShowMergeReportLogsOutlineRequest.

        运行任务id，即报告id。启动任务（更新任务状态或批量启停任务）接口，会返回运行任务id。

        :param task_run_id: The task_run_id of this ShowMergeReportLogsOutlineRequest.
        :type task_run_id: int
        """
        self._task_run_id = task_run_id

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
        if not isinstance(other, ShowMergeReportLogsOutlineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
