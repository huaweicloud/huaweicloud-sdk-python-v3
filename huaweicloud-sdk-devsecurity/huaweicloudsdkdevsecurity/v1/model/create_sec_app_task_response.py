# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecAppTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'info_code': 'str',
        'info_description': 'str',
        'task_id': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'info_code': 'info_code',
        'info_description': 'info_description',
        'task_id': 'task_id',
        'task_status': 'task_status'
    }

    def __init__(self, info_code=None, info_description=None, task_id=None, task_status=None):
        """CreateSecAppTaskResponse

        The model defined in huaweicloud sdk

        :param info_code: 状态码:   * success - 成功   * failure - 失败 
        :type info_code: str
        :param info_description: 返回的提示信息
        :type info_description: str
        :param task_id: 任务ID
        :type task_id: str
        :param task_status: 任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 
        :type task_status: str
        """
        
        super(CreateSecAppTaskResponse, self).__init__()

        self._info_code = None
        self._info_description = None
        self._task_id = None
        self._task_status = None
        self.discriminator = None

        if info_code is not None:
            self.info_code = info_code
        if info_description is not None:
            self.info_description = info_description
        if task_id is not None:
            self.task_id = task_id
        if task_status is not None:
            self.task_status = task_status

    @property
    def info_code(self):
        """Gets the info_code of this CreateSecAppTaskResponse.

        状态码:   * success - 成功   * failure - 失败 

        :return: The info_code of this CreateSecAppTaskResponse.
        :rtype: str
        """
        return self._info_code

    @info_code.setter
    def info_code(self, info_code):
        """Sets the info_code of this CreateSecAppTaskResponse.

        状态码:   * success - 成功   * failure - 失败 

        :param info_code: The info_code of this CreateSecAppTaskResponse.
        :type info_code: str
        """
        self._info_code = info_code

    @property
    def info_description(self):
        """Gets the info_description of this CreateSecAppTaskResponse.

        返回的提示信息

        :return: The info_description of this CreateSecAppTaskResponse.
        :rtype: str
        """
        return self._info_description

    @info_description.setter
    def info_description(self, info_description):
        """Sets the info_description of this CreateSecAppTaskResponse.

        返回的提示信息

        :param info_description: The info_description of this CreateSecAppTaskResponse.
        :type info_description: str
        """
        self._info_description = info_description

    @property
    def task_id(self):
        """Gets the task_id of this CreateSecAppTaskResponse.

        任务ID

        :return: The task_id of this CreateSecAppTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateSecAppTaskResponse.

        任务ID

        :param task_id: The task_id of this CreateSecAppTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_status(self):
        """Gets the task_status of this CreateSecAppTaskResponse.

        任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 

        :return: The task_status of this CreateSecAppTaskResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this CreateSecAppTaskResponse.

        任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 

        :param task_status: The task_status of this CreateSecAppTaskResponse.
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
        if not isinstance(other, CreateSecAppTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
