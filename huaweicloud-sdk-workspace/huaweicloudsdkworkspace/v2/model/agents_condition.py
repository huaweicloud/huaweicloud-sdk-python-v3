# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentsCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'desktop_pool_id': 'str',
        'status': 'str',
        'task_status': 'str',
        'ip_address': 'str',
        'enterprise_project_id': 'str',
        'process': 'int',
        'agent_info': 'list[AgentInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'desktop_pool_id': 'desktop_pool_id',
        'status': 'status',
        'task_status': 'task_status',
        'ip_address': 'ip_address',
        'enterprise_project_id': 'enterprise_project_id',
        'process': 'process',
        'agent_info': 'agent_info'
    }

    def __init__(self, desktop_id=None, desktop_name=None, desktop_pool_id=None, status=None, task_status=None, ip_address=None, enterprise_project_id=None, process=None, agent_info=None):
        r"""AgentsCondition

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面的desktopId。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param desktop_pool_id: 桌面池id。
        :type desktop_pool_id: str
        :param status: 桌面运行状态。
        :type status: str
        :param task_status: 桌面的任务状态。
        :type task_status: str
        :param ip_address: ip地址。
        :type ip_address: str
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param process: 桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。
        :type process: int
        :param agent_info: 单个桌面内的agent安装情况。
        :type agent_info: list[:class:`huaweicloudsdkworkspace.v2.AgentInfo`]
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._desktop_pool_id = None
        self._status = None
        self._task_status = None
        self._ip_address = None
        self._enterprise_project_id = None
        self._process = None
        self._agent_info = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if status is not None:
            self.status = status
        if task_status is not None:
            self.task_status = task_status
        if ip_address is not None:
            self.ip_address = ip_address
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if process is not None:
            self.process = process
        if agent_info is not None:
            self.agent_info = agent_info

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this AgentsCondition.

        桌面的desktopId。

        :return: The desktop_id of this AgentsCondition.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this AgentsCondition.

        桌面的desktopId。

        :param desktop_id: The desktop_id of this AgentsCondition.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this AgentsCondition.

        桌面名称。

        :return: The desktop_name of this AgentsCondition.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this AgentsCondition.

        桌面名称。

        :param desktop_name: The desktop_name of this AgentsCondition.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this AgentsCondition.

        桌面池id。

        :return: The desktop_pool_id of this AgentsCondition.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this AgentsCondition.

        桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this AgentsCondition.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def status(self):
        r"""Gets the status of this AgentsCondition.

        桌面运行状态。

        :return: The status of this AgentsCondition.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AgentsCondition.

        桌面运行状态。

        :param status: The status of this AgentsCondition.
        :type status: str
        """
        self._status = status

    @property
    def task_status(self):
        r"""Gets the task_status of this AgentsCondition.

        桌面的任务状态。

        :return: The task_status of this AgentsCondition.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this AgentsCondition.

        桌面的任务状态。

        :param task_status: The task_status of this AgentsCondition.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def ip_address(self):
        r"""Gets the ip_address of this AgentsCondition.

        ip地址。

        :return: The ip_address of this AgentsCondition.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this AgentsCondition.

        ip地址。

        :param ip_address: The ip_address of this AgentsCondition.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AgentsCondition.

        企业项目ID。

        :return: The enterprise_project_id of this AgentsCondition.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AgentsCondition.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this AgentsCondition.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def process(self):
        r"""Gets the process of this AgentsCondition.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :return: The process of this AgentsCondition.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this AgentsCondition.

        桌面任务进度， 取值范围0-100以及null，null表示该桌面无任务，0-100表明该任务进度的百分比。

        :param process: The process of this AgentsCondition.
        :type process: int
        """
        self._process = process

    @property
    def agent_info(self):
        r"""Gets the agent_info of this AgentsCondition.

        单个桌面内的agent安装情况。

        :return: The agent_info of this AgentsCondition.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AgentInfo`]
        """
        return self._agent_info

    @agent_info.setter
    def agent_info(self, agent_info):
        r"""Sets the agent_info of this AgentsCondition.

        单个桌面内的agent安装情况。

        :param agent_info: The agent_info of this AgentsCondition.
        :type agent_info: list[:class:`huaweicloudsdkworkspace.v2.AgentInfo`]
        """
        self._agent_info = agent_info

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
        if not isinstance(other, AgentsCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
