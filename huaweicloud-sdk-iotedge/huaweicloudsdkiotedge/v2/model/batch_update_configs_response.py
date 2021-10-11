# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateConfigsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'status': 'str',
        'status_desc': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'status': 'status',
        'status_desc': 'status_desc'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, status=None, status_desc=None):
        """BatchUpdateConfigsResponse - a model defined in huaweicloud sdk"""
        
        super(BatchUpdateConfigsResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._status = None
        self._status_desc = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc

    @property
    def task_id(self):
        """Gets the task_id of this BatchUpdateConfigsResponse.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :return: The task_id of this BatchUpdateConfigsResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this BatchUpdateConfigsResponse.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :param task_id: The task_id of this BatchUpdateConfigsResponse.
        :type: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this BatchUpdateConfigsResponse.

        批量任务名称。

        :return: The task_name of this BatchUpdateConfigsResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this BatchUpdateConfigsResponse.

        批量任务名称。

        :param task_name: The task_name of this BatchUpdateConfigsResponse.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this BatchUpdateConfigsResponse.

        任务类型。

        :return: The task_type of this BatchUpdateConfigsResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this BatchUpdateConfigsResponse.

        任务类型。

        :param task_type: The task_type of this BatchUpdateConfigsResponse.
        :type: str
        """
        self._task_type = task_type

    @property
    def status(self):
        """Gets the status of this BatchUpdateConfigsResponse.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。

        :return: The status of this BatchUpdateConfigsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpdateConfigsResponse.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。

        :param status: The status of this BatchUpdateConfigsResponse.
        :type: str
        """
        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this BatchUpdateConfigsResponse.

        批量任务状态描述(包含主任务失败错误信息)

        :return: The status_desc of this BatchUpdateConfigsResponse.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this BatchUpdateConfigsResponse.

        批量任务状态描述(包含主任务失败错误信息)

        :param status_desc: The status_desc of this BatchUpdateConfigsResponse.
        :type: str
        """
        self._status_desc = status_desc

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
        if not isinstance(other, BatchUpdateConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
