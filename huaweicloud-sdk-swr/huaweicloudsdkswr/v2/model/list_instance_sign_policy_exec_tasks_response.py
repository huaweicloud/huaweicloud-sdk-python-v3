# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceSignPolicyExecTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[SignatureExecutionTask]',
        'total': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'total': 'total'
    }

    def __init__(self, tasks=None, total=None):
        r"""ListInstanceSignPolicyExecTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: 签名策略执行记录任务列表
        :type tasks: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionTask`]
        :param total: 签名策略执行记录任务总数
        :type total: int
        """
        
        super(ListInstanceSignPolicyExecTasksResponse, self).__init__()

        self._tasks = None
        self._total = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if total is not None:
            self.total = total

    @property
    def tasks(self):
        r"""Gets the tasks of this ListInstanceSignPolicyExecTasksResponse.

        签名策略执行记录任务列表

        :return: The tasks of this ListInstanceSignPolicyExecTasksResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListInstanceSignPolicyExecTasksResponse.

        签名策略执行记录任务列表

        :param tasks: The tasks of this ListInstanceSignPolicyExecTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkswr.v2.SignatureExecutionTask`]
        """
        self._tasks = tasks

    @property
    def total(self):
        r"""Gets the total of this ListInstanceSignPolicyExecTasksResponse.

        签名策略执行记录任务总数

        :return: The total of this ListInstanceSignPolicyExecTasksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceSignPolicyExecTasksResponse.

        签名策略执行记录任务总数

        :param total: The total of this ListInstanceSignPolicyExecTasksResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceSignPolicyExecTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
