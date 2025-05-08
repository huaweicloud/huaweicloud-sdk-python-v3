# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'ObsInfo',
        'task_result': 'list[ObjectTaskResult]'
    }

    attribute_map = {
        'input': 'input',
        'task_result': 'task_result'
    }

    def __init__(self, input=None, task_result=None):
        r"""WorkflowTask

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param task_result: 工作流任务结果列表
        :type task_result: list[:class:`huaweicloudsdkvod.v1.ObjectTaskResult`]
        """
        
        

        self._input = None
        self._task_result = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if task_result is not None:
            self.task_result = task_result

    @property
    def input(self):
        r"""Gets the input of this WorkflowTask.

        :return: The input of this WorkflowTask.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this WorkflowTask.

        :param input: The input of this WorkflowTask.
        :type input: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._input = input

    @property
    def task_result(self):
        r"""Gets the task_result of this WorkflowTask.

        工作流任务结果列表

        :return: The task_result of this WorkflowTask.
        :rtype: list[:class:`huaweicloudsdkvod.v1.ObjectTaskResult`]
        """
        return self._task_result

    @task_result.setter
    def task_result(self, task_result):
        r"""Sets the task_result of this WorkflowTask.

        工作流任务结果列表

        :param task_result: The task_result of this WorkflowTask.
        :type task_result: list[:class:`huaweicloudsdkvod.v1.ObjectTaskResult`]
        """
        self._task_result = task_result

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
        if not isinstance(other, WorkflowTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
