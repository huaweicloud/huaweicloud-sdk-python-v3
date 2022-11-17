# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task': 'TaskBasicRsp',
        'task_detail': 'str'
    }

    attribute_map = {
        'task': 'task',
        'task_detail': 'task_detail'
    }

    def __init__(self, task=None, task_detail=None):
        """ShowTaskResponse

        The model defined in huaweicloud sdk

        :param task: 
        :type task: :class:`huaweicloudsdkroma.v2.TaskBasicRsp`
        :param task_detail: 参数类型为string，参数结构参照附录中“数据集成参数说明&gt;RawFormDataResponse”章节
        :type task_detail: str
        """
        
        super(ShowTaskResponse, self).__init__()

        self._task = None
        self._task_detail = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if task_detail is not None:
            self.task_detail = task_detail

    @property
    def task(self):
        """Gets the task of this ShowTaskResponse.

        :return: The task of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.TaskBasicRsp`
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ShowTaskResponse.

        :param task: The task of this ShowTaskResponse.
        :type task: :class:`huaweicloudsdkroma.v2.TaskBasicRsp`
        """
        self._task = task

    @property
    def task_detail(self):
        """Gets the task_detail of this ShowTaskResponse.

        参数类型为string，参数结构参照附录中“数据集成参数说明>RawFormDataResponse”章节

        :return: The task_detail of this ShowTaskResponse.
        :rtype: str
        """
        return self._task_detail

    @task_detail.setter
    def task_detail(self, task_detail):
        """Sets the task_detail of this ShowTaskResponse.

        参数类型为string，参数结构参照附录中“数据集成参数说明>RawFormDataResponse”章节

        :param task_detail: The task_detail of this ShowTaskResponse.
        :type task_detail: str
        """
        self._task_detail = task_detail

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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
