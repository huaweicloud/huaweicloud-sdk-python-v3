# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTransferTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'task_name': 'task_name'
    }

    def __init__(self, stream_name=None, task_name=None):
        r"""DeleteTransferTaskRequest

        The model defined in huaweicloud sdk

        :param stream_name: 已创建的通道的名称。
        :type stream_name: str
        :param task_name: 待删除的转储任务名称。
        :type task_name: str
        """
        
        

        self._stream_name = None
        self._task_name = None
        self.discriminator = None

        self.stream_name = stream_name
        self.task_name = task_name

    @property
    def stream_name(self):
        r"""Gets the stream_name of this DeleteTransferTaskRequest.

        已创建的通道的名称。

        :return: The stream_name of this DeleteTransferTaskRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this DeleteTransferTaskRequest.

        已创建的通道的名称。

        :param stream_name: The stream_name of this DeleteTransferTaskRequest.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def task_name(self):
        r"""Gets the task_name of this DeleteTransferTaskRequest.

        待删除的转储任务名称。

        :return: The task_name of this DeleteTransferTaskRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this DeleteTransferTaskRequest.

        待删除的转储任务名称。

        :param task_name: The task_name of this DeleteTransferTaskRequest.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, DeleteTransferTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
