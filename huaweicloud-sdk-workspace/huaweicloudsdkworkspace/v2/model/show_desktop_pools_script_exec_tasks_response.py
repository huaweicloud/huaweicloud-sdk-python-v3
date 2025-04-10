# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopPoolsScriptExecTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_execution_tasks': 'list[ScriptExecutionTask]',
        'total_count': 'int'
    }

    attribute_map = {
        'script_execution_tasks': 'script_execution_tasks',
        'total_count': 'total_count'
    }

    def __init__(self, script_execution_tasks=None, total_count=None):
        r"""ShowDesktopPoolsScriptExecTasksResponse

        The model defined in huaweicloud sdk

        :param script_execution_tasks: 脚本执行任务列表。
        :type script_execution_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScriptExecutionTask`]
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ShowDesktopPoolsScriptExecTasksResponse, self).__init__()

        self._script_execution_tasks = None
        self._total_count = None
        self.discriminator = None

        if script_execution_tasks is not None:
            self.script_execution_tasks = script_execution_tasks
        if total_count is not None:
            self.total_count = total_count

    @property
    def script_execution_tasks(self):
        r"""Gets the script_execution_tasks of this ShowDesktopPoolsScriptExecTasksResponse.

        脚本执行任务列表。

        :return: The script_execution_tasks of this ShowDesktopPoolsScriptExecTasksResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptExecutionTask`]
        """
        return self._script_execution_tasks

    @script_execution_tasks.setter
    def script_execution_tasks(self, script_execution_tasks):
        r"""Sets the script_execution_tasks of this ShowDesktopPoolsScriptExecTasksResponse.

        脚本执行任务列表。

        :param script_execution_tasks: The script_execution_tasks of this ShowDesktopPoolsScriptExecTasksResponse.
        :type script_execution_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScriptExecutionTask`]
        """
        self._script_execution_tasks = script_execution_tasks

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowDesktopPoolsScriptExecTasksResponse.

        总数。

        :return: The total_count of this ShowDesktopPoolsScriptExecTasksResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowDesktopPoolsScriptExecTasksResponse.

        总数。

        :param total_count: The total_count of this ShowDesktopPoolsScriptExecTasksResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowDesktopPoolsScriptExecTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
