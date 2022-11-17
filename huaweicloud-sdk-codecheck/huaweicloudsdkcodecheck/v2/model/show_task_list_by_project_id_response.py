# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskListByProjectIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[SimpleTaskInfoV2]',
        'total': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'total': 'total'
    }

    def __init__(self, tasks=None, total=None):
        """ShowTaskListByProjectIdResponse

        The model defined in huaweicloud sdk

        :param tasks: 任务信息
        :type tasks: list[:class:`huaweicloudsdkcodecheck.v2.SimpleTaskInfoV2`]
        :param total: 总数
        :type total: int
        """
        
        super(ShowTaskListByProjectIdResponse, self).__init__()

        self._tasks = None
        self._total = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if total is not None:
            self.total = total

    @property
    def tasks(self):
        """Gets the tasks of this ShowTaskListByProjectIdResponse.

        任务信息

        :return: The tasks of this ShowTaskListByProjectIdResponse.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.SimpleTaskInfoV2`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ShowTaskListByProjectIdResponse.

        任务信息

        :param tasks: The tasks of this ShowTaskListByProjectIdResponse.
        :type tasks: list[:class:`huaweicloudsdkcodecheck.v2.SimpleTaskInfoV2`]
        """
        self._tasks = tasks

    @property
    def total(self):
        """Gets the total of this ShowTaskListByProjectIdResponse.

        总数

        :return: The total of this ShowTaskListByProjectIdResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowTaskListByProjectIdResponse.

        总数

        :param total: The total of this ShowTaskListByProjectIdResponse.
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
        if not isinstance(other, ShowTaskListByProjectIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
