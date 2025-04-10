# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inner_ip': 'str',
        'import_ip': 'str',
        'agent_id': 'str',
        'host_name': 'str',
        'os_type': 'str',
        'agent_state': 'str',
        'project_id': 'str',
        'version': 'str',
        'is_hw_cloud_host': 'str',
        'vpc_id': 'str',
        'cmdb_id': 'str',
        'ecs_id': 'str',
        'domain_id': 'str'
    }

    attribute_map = {
        'inner_ip': 'inner_ip',
        'import_ip': 'import_ip',
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'os_type': 'os_type',
        'agent_state': 'agent_state',
        'project_id': 'project_id',
        'version': 'version',
        'is_hw_cloud_host': 'is_hw_cloud_host',
        'vpc_id': 'vpc_id',
        'cmdb_id': 'cmdb_id',
        'ecs_id': 'ecs_id',
        'domain_id': 'domain_id'
    }

    def __init__(self, inner_ip=None, import_ip=None, agent_id=None, host_name=None, os_type=None, agent_state=None, project_id=None, version=None, is_hw_cloud_host=None, vpc_id=None, cmdb_id=None, ecs_id=None, domain_id=None):
        r"""AgentInfoResult

        The model defined in huaweicloud sdk

        :param inner_ip: 机器 IP。
        :type inner_ip: str
        :param import_ip: 机器导入IP。
        :type import_ip: str
        :param agent_id: agent id。
        :type agent_id: str
        :param host_name: 主机名。
        :type host_name: str
        :param os_type: 操作系统。
        :type os_type: str
        :param agent_state: UniAgent状态。
        :type agent_state: str
        :param project_id: 所属project ID。
        :type project_id: str
        :param version: UniAgent版本。
        :type version: str
        :param is_hw_cloud_host: 是否华为云机器。
        :type is_hw_cloud_host: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param cmdb_id: CMDB ID.
        :type cmdb_id: str
        :param ecs_id: ECS ID。唯一值.
        :type ecs_id: str
        :param domain_id: 机器所属domain ID。
        :type domain_id: str
        """
        
        

        self._inner_ip = None
        self._import_ip = None
        self._agent_id = None
        self._host_name = None
        self._os_type = None
        self._agent_state = None
        self._project_id = None
        self._version = None
        self._is_hw_cloud_host = None
        self._vpc_id = None
        self._cmdb_id = None
        self._ecs_id = None
        self._domain_id = None
        self.discriminator = None

        if inner_ip is not None:
            self.inner_ip = inner_ip
        if import_ip is not None:
            self.import_ip = import_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if host_name is not None:
            self.host_name = host_name
        if os_type is not None:
            self.os_type = os_type
        if agent_state is not None:
            self.agent_state = agent_state
        if project_id is not None:
            self.project_id = project_id
        if version is not None:
            self.version = version
        if is_hw_cloud_host is not None:
            self.is_hw_cloud_host = is_hw_cloud_host
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if cmdb_id is not None:
            self.cmdb_id = cmdb_id
        if ecs_id is not None:
            self.ecs_id = ecs_id
        if domain_id is not None:
            self.domain_id = domain_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this AgentInfoResult.

        机器 IP。

        :return: The inner_ip of this AgentInfoResult.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this AgentInfoResult.

        机器 IP。

        :param inner_ip: The inner_ip of this AgentInfoResult.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def import_ip(self):
        r"""Gets the import_ip of this AgentInfoResult.

        机器导入IP。

        :return: The import_ip of this AgentInfoResult.
        :rtype: str
        """
        return self._import_ip

    @import_ip.setter
    def import_ip(self, import_ip):
        r"""Sets the import_ip of this AgentInfoResult.

        机器导入IP。

        :param import_ip: The import_ip of this AgentInfoResult.
        :type import_ip: str
        """
        self._import_ip = import_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AgentInfoResult.

        agent id。

        :return: The agent_id of this AgentInfoResult.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AgentInfoResult.

        agent id。

        :param agent_id: The agent_id of this AgentInfoResult.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AgentInfoResult.

        主机名。

        :return: The host_name of this AgentInfoResult.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AgentInfoResult.

        主机名。

        :param host_name: The host_name of this AgentInfoResult.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def os_type(self):
        r"""Gets the os_type of this AgentInfoResult.

        操作系统。

        :return: The os_type of this AgentInfoResult.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AgentInfoResult.

        操作系统。

        :param os_type: The os_type of this AgentInfoResult.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def agent_state(self):
        r"""Gets the agent_state of this AgentInfoResult.

        UniAgent状态。

        :return: The agent_state of this AgentInfoResult.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this AgentInfoResult.

        UniAgent状态。

        :param agent_state: The agent_state of this AgentInfoResult.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def project_id(self):
        r"""Gets the project_id of this AgentInfoResult.

        所属project ID。

        :return: The project_id of this AgentInfoResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AgentInfoResult.

        所属project ID。

        :param project_id: The project_id of this AgentInfoResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def version(self):
        r"""Gets the version of this AgentInfoResult.

        UniAgent版本。

        :return: The version of this AgentInfoResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this AgentInfoResult.

        UniAgent版本。

        :param version: The version of this AgentInfoResult.
        :type version: str
        """
        self._version = version

    @property
    def is_hw_cloud_host(self):
        r"""Gets the is_hw_cloud_host of this AgentInfoResult.

        是否华为云机器。

        :return: The is_hw_cloud_host of this AgentInfoResult.
        :rtype: str
        """
        return self._is_hw_cloud_host

    @is_hw_cloud_host.setter
    def is_hw_cloud_host(self, is_hw_cloud_host):
        r"""Sets the is_hw_cloud_host of this AgentInfoResult.

        是否华为云机器。

        :param is_hw_cloud_host: The is_hw_cloud_host of this AgentInfoResult.
        :type is_hw_cloud_host: str
        """
        self._is_hw_cloud_host = is_hw_cloud_host

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this AgentInfoResult.

        VPC ID。

        :return: The vpc_id of this AgentInfoResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this AgentInfoResult.

        VPC ID。

        :param vpc_id: The vpc_id of this AgentInfoResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def cmdb_id(self):
        r"""Gets the cmdb_id of this AgentInfoResult.

        CMDB ID.

        :return: The cmdb_id of this AgentInfoResult.
        :rtype: str
        """
        return self._cmdb_id

    @cmdb_id.setter
    def cmdb_id(self, cmdb_id):
        r"""Sets the cmdb_id of this AgentInfoResult.

        CMDB ID.

        :param cmdb_id: The cmdb_id of this AgentInfoResult.
        :type cmdb_id: str
        """
        self._cmdb_id = cmdb_id

    @property
    def ecs_id(self):
        r"""Gets the ecs_id of this AgentInfoResult.

        ECS ID。唯一值.

        :return: The ecs_id of this AgentInfoResult.
        :rtype: str
        """
        return self._ecs_id

    @ecs_id.setter
    def ecs_id(self, ecs_id):
        r"""Sets the ecs_id of this AgentInfoResult.

        ECS ID。唯一值.

        :param ecs_id: The ecs_id of this AgentInfoResult.
        :type ecs_id: str
        """
        self._ecs_id = ecs_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this AgentInfoResult.

        机器所属domain ID。

        :return: The domain_id of this AgentInfoResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this AgentInfoResult.

        机器所属domain ID。

        :param domain_id: The domain_id of this AgentInfoResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

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
        if not isinstance(other, AgentInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
