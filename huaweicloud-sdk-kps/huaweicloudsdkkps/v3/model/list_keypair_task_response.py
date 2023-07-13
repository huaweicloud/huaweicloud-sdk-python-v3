# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeypairTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'task_id': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'task_id': 'task_id',
        'task_status': 'task_status'
    }

    def __init__(self, server_id=None, task_id=None, task_status=None):
        """ListKeypairTaskResponse

        The model defined in huaweicloud sdk

        :param server_id: 租户虚拟机ID
        :type server_id: str
        :param task_id: 任务下发成功返回的ID
        :type task_id: str
        :param task_status: 密钥对正在处理的状态。 - READY_RESET 准备重置 - RUNNING_RESET 正在重置 - FAILED_RESET 重置失败 - SUCCESS_RESET 重置成功 - READY_REPLACE 准备替换 - RUNNING_REPLACE 正在替换 - FAILED_RESET 替换失败 - SUCCESS_RESET 替换成功 - READY_UNBIND 准备解绑 - RUNNING_UNBIND 正在解绑 - FAILED_UNBIND 解绑失败 - SUCCESS_UNBIND 解绑成功
        :type task_status: str
        """
        
        super(ListKeypairTaskResponse, self).__init__()

        self._server_id = None
        self._task_id = None
        self._task_status = None
        self.discriminator = None

        if server_id is not None:
            self.server_id = server_id
        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status

    @property
    def server_id(self):
        """Gets the server_id of this ListKeypairTaskResponse.

        租户虚拟机ID

        :return: The server_id of this ListKeypairTaskResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListKeypairTaskResponse.

        租户虚拟机ID

        :param server_id: The server_id of this ListKeypairTaskResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def task_id(self):
        """Gets the task_id of this ListKeypairTaskResponse.

        任务下发成功返回的ID

        :return: The task_id of this ListKeypairTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListKeypairTaskResponse.

        任务下发成功返回的ID

        :param task_id: The task_id of this ListKeypairTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this ListKeypairTaskResponse.

        密钥对正在处理的状态。 - READY_RESET 准备重置 - RUNNING_RESET 正在重置 - FAILED_RESET 重置失败 - SUCCESS_RESET 重置成功 - READY_REPLACE 准备替换 - RUNNING_REPLACE 正在替换 - FAILED_RESET 替换失败 - SUCCESS_RESET 替换成功 - READY_UNBIND 准备解绑 - RUNNING_UNBIND 正在解绑 - FAILED_UNBIND 解绑失败 - SUCCESS_UNBIND 解绑成功

        :return: The task_status of this ListKeypairTaskResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ListKeypairTaskResponse.

        密钥对正在处理的状态。 - READY_RESET 准备重置 - RUNNING_RESET 正在重置 - FAILED_RESET 重置失败 - SUCCESS_RESET 重置成功 - READY_REPLACE 准备替换 - RUNNING_REPLACE 正在替换 - FAILED_RESET 替换失败 - SUCCESS_RESET 替换成功 - READY_UNBIND 准备解绑 - RUNNING_UNBIND 正在解绑 - FAILED_UNBIND 解绑失败 - SUCCESS_UNBIND 解绑成功

        :param task_status: The task_status of this ListKeypairTaskResponse.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, ListKeypairTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
