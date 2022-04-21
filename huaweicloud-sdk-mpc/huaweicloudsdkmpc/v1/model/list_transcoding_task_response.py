# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodingTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_array': 'list[QueryTranscodingsTaskResponse]',
        'is_truncated': 'int',
        'total': 'int'
    }

    attribute_map = {
        'task_array': 'task_array',
        'is_truncated': 'is_truncated',
        'total': 'total'
    }

    def __init__(self, task_array=None, is_truncated=None, total=None):
        """ListTranscodingTaskResponse

        The model defined in huaweicloud sdk

        :param task_array: 返回任务组
        :type task_array: list[:class:`huaweicloudsdkmpc.v1.QueryTranscodingsTaskResponse`]
        :param is_truncated: 查询结果是否被截取。 - 1：表示被截取，即还有结果未被返回，可以通过设置page和size参数继续查询。 - 0：表示未被截取，即所有结果已被返回。 
        :type is_truncated: int
        :param total: 查询结果的数量。 
        :type total: int
        """
        
        super(ListTranscodingTaskResponse, self).__init__()

        self._task_array = None
        self._is_truncated = None
        self._total = None
        self.discriminator = None

        if task_array is not None:
            self.task_array = task_array
        if is_truncated is not None:
            self.is_truncated = is_truncated
        if total is not None:
            self.total = total

    @property
    def task_array(self):
        """Gets the task_array of this ListTranscodingTaskResponse.

        返回任务组

        :return: The task_array of this ListTranscodingTaskResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.QueryTranscodingsTaskResponse`]
        """
        return self._task_array

    @task_array.setter
    def task_array(self, task_array):
        """Sets the task_array of this ListTranscodingTaskResponse.

        返回任务组

        :param task_array: The task_array of this ListTranscodingTaskResponse.
        :type task_array: list[:class:`huaweicloudsdkmpc.v1.QueryTranscodingsTaskResponse`]
        """
        self._task_array = task_array

    @property
    def is_truncated(self):
        """Gets the is_truncated of this ListTranscodingTaskResponse.

        查询结果是否被截取。 - 1：表示被截取，即还有结果未被返回，可以通过设置page和size参数继续查询。 - 0：表示未被截取，即所有结果已被返回。 

        :return: The is_truncated of this ListTranscodingTaskResponse.
        :rtype: int
        """
        return self._is_truncated

    @is_truncated.setter
    def is_truncated(self, is_truncated):
        """Sets the is_truncated of this ListTranscodingTaskResponse.

        查询结果是否被截取。 - 1：表示被截取，即还有结果未被返回，可以通过设置page和size参数继续查询。 - 0：表示未被截取，即所有结果已被返回。 

        :param is_truncated: The is_truncated of this ListTranscodingTaskResponse.
        :type is_truncated: int
        """
        self._is_truncated = is_truncated

    @property
    def total(self):
        """Gets the total of this ListTranscodingTaskResponse.

        查询结果的数量。 

        :return: The total of this ListTranscodingTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListTranscodingTaskResponse.

        查询结果的数量。 

        :param total: The total of this ListTranscodingTaskResponse.
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
        if not isinstance(other, ListTranscodingTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
