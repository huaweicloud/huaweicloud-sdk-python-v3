# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNextflowTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[NextflowTaskListDto]',
        'count': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'count': 'count'
    }

    def __init__(self, tasks=None, count=None):
        r"""ListNextflowTaskResponse

        The model defined in huaweicloud sdk

        :param tasks: 子任务实例
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.NextflowTaskListDto`]
        :param count: 子任务的总数
        :type count: int
        """
        
        super(ListNextflowTaskResponse, self).__init__()

        self._tasks = None
        self._count = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if count is not None:
            self.count = count

    @property
    def tasks(self):
        r"""Gets the tasks of this ListNextflowTaskResponse.

        子任务实例

        :return: The tasks of this ListNextflowTaskResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NextflowTaskListDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListNextflowTaskResponse.

        子任务实例

        :param tasks: The tasks of this ListNextflowTaskResponse.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.NextflowTaskListDto`]
        """
        self._tasks = tasks

    @property
    def count(self):
        r"""Gets the count of this ListNextflowTaskResponse.

        子任务的总数

        :return: The count of this ListNextflowTaskResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListNextflowTaskResponse.

        子任务的总数

        :param count: The count of this ListNextflowTaskResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListNextflowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
