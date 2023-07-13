# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_array': 'list[TaskDetailInfo]'
    }

    attribute_map = {
        'task_array': 'task_array'
    }

    def __init__(self, task_array=None):
        """ListTranscodeDetailResponse

        The model defined in huaweicloud sdk

        :param task_array: 转码详情任务组
        :type task_array: list[:class:`huaweicloudsdkmpc.v1.TaskDetailInfo`]
        """
        
        super(ListTranscodeDetailResponse, self).__init__()

        self._task_array = None
        self.discriminator = None

        if task_array is not None:
            self.task_array = task_array

    @property
    def task_array(self):
        """Gets the task_array of this ListTranscodeDetailResponse.

        转码详情任务组

        :return: The task_array of this ListTranscodeDetailResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.TaskDetailInfo`]
        """
        return self._task_array

    @task_array.setter
    def task_array(self, task_array):
        """Sets the task_array of this ListTranscodeDetailResponse.

        转码详情任务组

        :param task_array: The task_array of this ListTranscodeDetailResponse.
        :type task_array: list[:class:`huaweicloudsdkmpc.v1.TaskDetailInfo`]
        """
        self._task_array = task_array

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
        if not isinstance(other, ListTranscodeDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
