# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartDeployTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'task_id': 'str',
        'job_name': 'str',
        'app_component_list': 'list[AppComponentDao]'
    }

    attribute_map = {
        'id': 'id',
        'task_id': 'task_id',
        'job_name': 'job_name',
        'app_component_list': 'app_component_list'
    }

    def __init__(self, id=None, task_id=None, job_name=None, app_component_list=None):
        """StartDeployTaskResponse

        The model defined in huaweicloud sdk

        :param id: 执行记录id
        :type id: str
        :param task_id: 部署任务id
        :type task_id: str
        :param job_name: 执行任务名称
        :type job_name: str
        :param app_component_list: 部署任务和应用组件对应关系
        :type app_component_list: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        """
        
        super(StartDeployTaskResponse, self).__init__()

        self._id = None
        self._task_id = None
        self._job_name = None
        self._app_component_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_id is not None:
            self.task_id = task_id
        if job_name is not None:
            self.job_name = job_name
        if app_component_list is not None:
            self.app_component_list = app_component_list

    @property
    def id(self):
        """Gets the id of this StartDeployTaskResponse.

        执行记录id

        :return: The id of this StartDeployTaskResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StartDeployTaskResponse.

        执行记录id

        :param id: The id of this StartDeployTaskResponse.
        :type id: str
        """
        self._id = id

    @property
    def task_id(self):
        """Gets the task_id of this StartDeployTaskResponse.

        部署任务id

        :return: The task_id of this StartDeployTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this StartDeployTaskResponse.

        部署任务id

        :param task_id: The task_id of this StartDeployTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def job_name(self):
        """Gets the job_name of this StartDeployTaskResponse.

        执行任务名称

        :return: The job_name of this StartDeployTaskResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this StartDeployTaskResponse.

        执行任务名称

        :param job_name: The job_name of this StartDeployTaskResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def app_component_list(self):
        """Gets the app_component_list of this StartDeployTaskResponse.

        部署任务和应用组件对应关系

        :return: The app_component_list of this StartDeployTaskResponse.
        :rtype: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        """
        return self._app_component_list

    @app_component_list.setter
    def app_component_list(self, app_component_list):
        """Sets the app_component_list of this StartDeployTaskResponse.

        部署任务和应用组件对应关系

        :param app_component_list: The app_component_list of this StartDeployTaskResponse.
        :type app_component_list: list[:class:`huaweicloudsdkclouddeploy.v2.AppComponentDao`]
        """
        self._app_component_list = app_component_list

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
        if not isinstance(other, StartDeployTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
