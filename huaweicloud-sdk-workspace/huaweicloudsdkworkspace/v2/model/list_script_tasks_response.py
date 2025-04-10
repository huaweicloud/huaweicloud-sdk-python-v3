# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'script_tasks': 'list[ScriptTaskInfo]'
    }

    attribute_map = {
        'count': 'count',
        'script_tasks': 'script_tasks'
    }

    def __init__(self, count=None, script_tasks=None):
        r"""ListScriptTasksResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param script_tasks: 脚本任务列表。
        :type script_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfo`]
        """
        
        super(ListScriptTasksResponse, self).__init__()

        self._count = None
        self._script_tasks = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if script_tasks is not None:
            self.script_tasks = script_tasks

    @property
    def count(self):
        r"""Gets the count of this ListScriptTasksResponse.

        总数。

        :return: The count of this ListScriptTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScriptTasksResponse.

        总数。

        :param count: The count of this ListScriptTasksResponse.
        :type count: int
        """
        self._count = count

    @property
    def script_tasks(self):
        r"""Gets the script_tasks of this ListScriptTasksResponse.

        脚本任务列表。

        :return: The script_tasks of this ListScriptTasksResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfo`]
        """
        return self._script_tasks

    @script_tasks.setter
    def script_tasks(self, script_tasks):
        r"""Sets the script_tasks of this ListScriptTasksResponse.

        脚本任务列表。

        :param script_tasks: The script_tasks of this ListScriptTasksResponse.
        :type script_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfo`]
        """
        self._script_tasks = script_tasks

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
        if not isinstance(other, ListScriptTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
