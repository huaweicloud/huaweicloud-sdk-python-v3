# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Jobs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'config_info': 'str',
        'description': 'str',
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'next_schedule_time': 'int',
        'platform': 'str',
        'resource_id': 'str',
        'schedule': 'str',
        'status': 'str',
        'workspace_id': 'str',
        'job_config': 'JobConfig'
    }

    attribute_map = {
        'category': 'category',
        'config_info': 'config_info',
        'description': 'description',
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'next_schedule_time': 'next_schedule_time',
        'platform': 'platform',
        'resource_id': 'resource_id',
        'schedule': 'schedule',
        'status': 'status',
        'workspace_id': 'workspace_id',
        'job_config': 'job_config'
    }

    def __init__(self, category=None, config_info=None, description=None, job_id=None, job_name=None, job_type=None, next_schedule_time=None, platform=None, resource_id=None, schedule=None, status=None, workspace_id=None, job_config=None):
        r"""Jobs

        The model defined in huaweicloud sdk

        :param category: 类别。
        :type category: str
        :param config_info: 配置信息。
        :type config_info: str
        :param description: 描述。
        :type description: str
        :param job_id: 作业id。
        :type job_id: str
        :param job_name: 作业名称。
        :type job_name: str
        :param job_type: 作业类型。
        :type job_type: str
        :param next_schedule_time: 下次调度时间。
        :type next_schedule_time: int
        :param platform: 平台。
        :type platform: str
        :param resource_id: 资源id。
        :type resource_id: str
        :param schedule: 调度参数。
        :type schedule: str
        :param status: 状态。
        :type status: str
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        
        

        self._category = None
        self._config_info = None
        self._description = None
        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._next_schedule_time = None
        self._platform = None
        self._resource_id = None
        self._schedule = None
        self._status = None
        self._workspace_id = None
        self._job_config = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if config_info is not None:
            self.config_info = config_info
        if description is not None:
            self.description = description
        self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if next_schedule_time is not None:
            self.next_schedule_time = next_schedule_time
        if platform is not None:
            self.platform = platform
        if resource_id is not None:
            self.resource_id = resource_id
        if schedule is not None:
            self.schedule = schedule
        if status is not None:
            self.status = status
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if job_config is not None:
            self.job_config = job_config

    @property
    def category(self):
        r"""Gets the category of this Jobs.

        类别。

        :return: The category of this Jobs.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this Jobs.

        类别。

        :param category: The category of this Jobs.
        :type category: str
        """
        self._category = category

    @property
    def config_info(self):
        r"""Gets the config_info of this Jobs.

        配置信息。

        :return: The config_info of this Jobs.
        :rtype: str
        """
        return self._config_info

    @config_info.setter
    def config_info(self, config_info):
        r"""Sets the config_info of this Jobs.

        配置信息。

        :param config_info: The config_info of this Jobs.
        :type config_info: str
        """
        self._config_info = config_info

    @property
    def description(self):
        r"""Gets the description of this Jobs.

        描述。

        :return: The description of this Jobs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Jobs.

        描述。

        :param description: The description of this Jobs.
        :type description: str
        """
        self._description = description

    @property
    def job_id(self):
        r"""Gets the job_id of this Jobs.

        作业id。

        :return: The job_id of this Jobs.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Jobs.

        作业id。

        :param job_id: The job_id of this Jobs.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this Jobs.

        作业名称。

        :return: The job_name of this Jobs.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this Jobs.

        作业名称。

        :param job_name: The job_name of this Jobs.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        r"""Gets the job_type of this Jobs.

        作业类型。

        :return: The job_type of this Jobs.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this Jobs.

        作业类型。

        :param job_type: The job_type of this Jobs.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def next_schedule_time(self):
        r"""Gets the next_schedule_time of this Jobs.

        下次调度时间。

        :return: The next_schedule_time of this Jobs.
        :rtype: int
        """
        return self._next_schedule_time

    @next_schedule_time.setter
    def next_schedule_time(self, next_schedule_time):
        r"""Sets the next_schedule_time of this Jobs.

        下次调度时间。

        :param next_schedule_time: The next_schedule_time of this Jobs.
        :type next_schedule_time: int
        """
        self._next_schedule_time = next_schedule_time

    @property
    def platform(self):
        r"""Gets the platform of this Jobs.

        平台。

        :return: The platform of this Jobs.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        r"""Sets the platform of this Jobs.

        平台。

        :param platform: The platform of this Jobs.
        :type platform: str
        """
        self._platform = platform

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Jobs.

        资源id。

        :return: The resource_id of this Jobs.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Jobs.

        资源id。

        :param resource_id: The resource_id of this Jobs.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def schedule(self):
        r"""Gets the schedule of this Jobs.

        调度参数。

        :return: The schedule of this Jobs.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        r"""Sets the schedule of this Jobs.

        调度参数。

        :param schedule: The schedule of this Jobs.
        :type schedule: str
        """
        self._schedule = schedule

    @property
    def status(self):
        r"""Gets the status of this Jobs.

        状态。

        :return: The status of this Jobs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Jobs.

        状态。

        :param status: The status of this Jobs.
        :type status: str
        """
        self._status = status

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this Jobs.

        工作空间id。

        :return: The workspace_id of this Jobs.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this Jobs.

        工作空间id。

        :param workspace_id: The workspace_id of this Jobs.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_config(self):
        r"""Gets the job_config of this Jobs.

        :return: The job_config of this Jobs.
        :rtype: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this Jobs.

        :param job_config: The job_config of this Jobs.
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        self._job_config = job_config

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
        if not isinstance(other, Jobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
