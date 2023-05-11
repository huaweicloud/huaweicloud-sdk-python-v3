# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNewTaskStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_status': 'str',
        'task_msg': 'str'
    }

    attribute_map = {
        'task_status': 'task_status',
        'task_msg': 'task_msg'
    }

    def __init__(self, task_status=None, task_msg=None):
        """ShowNewTaskStatusResponse

        The model defined in huaweicloud sdk

        :param task_status: 任务状态，有以下几种： - success - failed - waiting - running - preprocess - ready
        :type task_status: str
        :param task_msg: 任务的附加信息
        :type task_msg: str
        """
        
        super(ShowNewTaskStatusResponse, self).__init__()

        self._task_status = None
        self._task_msg = None
        self.discriminator = None

        if task_status is not None:
            self.task_status = task_status
        if task_msg is not None:
            self.task_msg = task_msg

    @property
    def task_status(self):
        """Gets the task_status of this ShowNewTaskStatusResponse.

        任务状态，有以下几种： - success - failed - waiting - running - preprocess - ready

        :return: The task_status of this ShowNewTaskStatusResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowNewTaskStatusResponse.

        任务状态，有以下几种： - success - failed - waiting - running - preprocess - ready

        :param task_status: The task_status of this ShowNewTaskStatusResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_msg(self):
        """Gets the task_msg of this ShowNewTaskStatusResponse.

        任务的附加信息

        :return: The task_msg of this ShowNewTaskStatusResponse.
        :rtype: str
        """
        return self._task_msg

    @task_msg.setter
    def task_msg(self, task_msg):
        """Sets the task_msg of this ShowNewTaskStatusResponse.

        任务的附加信息

        :param task_msg: The task_msg of this ShowNewTaskStatusResponse.
        :type task_msg: str
        """
        self._task_msg = task_msg

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
        if not isinstance(other, ShowNewTaskStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
