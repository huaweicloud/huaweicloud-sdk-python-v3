# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'created_at': 'str',
        'update_at': 'str',
        'process': 'str',
        'status': 'str',
        'sub_task_list': 'list[SubTaskInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'created_at': 'created_at',
        'update_at': 'update_at',
        'process': 'process',
        'status': 'status',
        'sub_task_list': 'sub_task_list',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, instance_id=None, instance_name=None, job_id=None, job_name=None, created_at=None, update_at=None, process=None, status=None, sub_task_list=None, x_request_id=None):
        r"""ShowTaskDetailResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名。
        :type instance_name: str
        :param job_id: 工作流ID。
        :type job_id: str
        :param job_name: 工作流名称。
        :type job_name: str
        :param created_at: 工作流创建时间。
        :type created_at: str
        :param update_at: 工作流更新时间。
        :type update_at: str
        :param process: 工作流进度。
        :type process: str
        :param status: 工作流状态。
        :type status: str
        :param sub_task_list: 子任务进度信息
        :type sub_task_list: list[:class:`huaweicloudsdkrds.v3.SubTaskInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowTaskDetailResponse, self).__init__()

        self._instance_id = None
        self._instance_name = None
        self._job_id = None
        self._job_name = None
        self._created_at = None
        self._update_at = None
        self._process = None
        self._status = None
        self._sub_task_list = None
        self._x_request_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        if process is not None:
            self.process = process
        if status is not None:
            self.status = status
        if sub_task_list is not None:
            self.sub_task_list = sub_task_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTaskDetailResponse.

        实例ID。

        :return: The instance_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTaskDetailResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowTaskDetailResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShowTaskDetailResponse.

        实例名。

        :return: The instance_name of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShowTaskDetailResponse.

        实例名。

        :param instance_name: The instance_name of this ShowTaskDetailResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTaskDetailResponse.

        工作流ID。

        :return: The job_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTaskDetailResponse.

        工作流ID。

        :param job_id: The job_id of this ShowTaskDetailResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowTaskDetailResponse.

        工作流名称。

        :return: The job_name of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowTaskDetailResponse.

        工作流名称。

        :param job_name: The job_name of this ShowTaskDetailResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowTaskDetailResponse.

        工作流创建时间。

        :return: The created_at of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowTaskDetailResponse.

        工作流创建时间。

        :param created_at: The created_at of this ShowTaskDetailResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def update_at(self):
        r"""Gets the update_at of this ShowTaskDetailResponse.

        工作流更新时间。

        :return: The update_at of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this ShowTaskDetailResponse.

        工作流更新时间。

        :param update_at: The update_at of this ShowTaskDetailResponse.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def process(self):
        r"""Gets the process of this ShowTaskDetailResponse.

        工作流进度。

        :return: The process of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this ShowTaskDetailResponse.

        工作流进度。

        :param process: The process of this ShowTaskDetailResponse.
        :type process: str
        """
        self._process = process

    @property
    def status(self):
        r"""Gets the status of this ShowTaskDetailResponse.

        工作流状态。

        :return: The status of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTaskDetailResponse.

        工作流状态。

        :param status: The status of this ShowTaskDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def sub_task_list(self):
        r"""Gets the sub_task_list of this ShowTaskDetailResponse.

        子任务进度信息

        :return: The sub_task_list of this ShowTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SubTaskInfo`]
        """
        return self._sub_task_list

    @sub_task_list.setter
    def sub_task_list(self, sub_task_list):
        r"""Sets the sub_task_list of this ShowTaskDetailResponse.

        子任务进度信息

        :param sub_task_list: The sub_task_list of this ShowTaskDetailResponse.
        :type sub_task_list: list[:class:`huaweicloudsdkrds.v3.SubTaskInfo`]
        """
        self._sub_task_list = sub_task_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowTaskDetailResponse.

        :return: The x_request_id of this ShowTaskDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowTaskDetailResponse.

        :param x_request_id: The x_request_id of this ShowTaskDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
