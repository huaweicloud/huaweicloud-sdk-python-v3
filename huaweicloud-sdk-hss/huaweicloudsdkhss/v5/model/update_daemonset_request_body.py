# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDaemonsetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_version': 'str',
        'cluster_name': 'str',
        'auto_upgrade': 'bool',
        'runtime_info': 'list[RuntimeRequestBody]',
        'schedule_info': 'CreateDaemonsetRequestBodyScheduleInfo',
        'invoked_service': 'str',
        'charging_mode': 'str',
        'cce_protection_type': 'str',
        'prefer_packet_cycle': 'bool'
    }

    attribute_map = {
        'agent_version': 'agent_version',
        'cluster_name': 'cluster_name',
        'auto_upgrade': 'auto_upgrade',
        'runtime_info': 'runtime_info',
        'schedule_info': 'schedule_info',
        'invoked_service': 'invoked_service',
        'charging_mode': 'charging_mode',
        'cce_protection_type': 'cce_protection_type',
        'prefer_packet_cycle': 'prefer_packet_cycle'
    }

    def __init__(self, agent_version=None, cluster_name=None, auto_upgrade=None, runtime_info=None, schedule_info=None, invoked_service=None, charging_mode=None, cce_protection_type=None, prefer_packet_cycle=None):
        r"""UpdateDaemonsetRequestBody

        The model defined in huaweicloud sdk

        :param agent_version: agent版本
        :type agent_version: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param auto_upgrade: 开启agent自动升级
        :type auto_upgrade: bool
        :param runtime_info: 容器运行时配置
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        :param schedule_info: 
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        :param invoked_service: 调用服务，默认hss，cce集成防护调用场景使用:   - hss：hss服务    - cce：cce服务
        :type invoked_service: str
        :param charging_mode: 付费模式，cce集成防护调用场景使用:   - on_demand:按需    - free_security_check:免费安全体检
        :type charging_mode: str
        :param cce_protection_type: cce防护类型，cce集成防护调用场景使用:   - cluster_level:集群级别防护    - node_level:节点级别防护
        :type cce_protection_type: str
        :param prefer_packet_cycle: 优先使用包周期配额，cce集成防护调用场景使用，默认false
        :type prefer_packet_cycle: bool
        """
        
        

        self._agent_version = None
        self._cluster_name = None
        self._auto_upgrade = None
        self._runtime_info = None
        self._schedule_info = None
        self._invoked_service = None
        self._charging_mode = None
        self._cce_protection_type = None
        self._prefer_packet_cycle = None
        self.discriminator = None

        if agent_version is not None:
            self.agent_version = agent_version
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if auto_upgrade is not None:
            self.auto_upgrade = auto_upgrade
        if runtime_info is not None:
            self.runtime_info = runtime_info
        if schedule_info is not None:
            self.schedule_info = schedule_info
        if invoked_service is not None:
            self.invoked_service = invoked_service
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cce_protection_type is not None:
            self.cce_protection_type = cce_protection_type
        if prefer_packet_cycle is not None:
            self.prefer_packet_cycle = prefer_packet_cycle

    @property
    def agent_version(self):
        r"""Gets the agent_version of this UpdateDaemonsetRequestBody.

        agent版本

        :return: The agent_version of this UpdateDaemonsetRequestBody.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this UpdateDaemonsetRequestBody.

        agent版本

        :param agent_version: The agent_version of this UpdateDaemonsetRequestBody.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this UpdateDaemonsetRequestBody.

        集群名称

        :return: The cluster_name of this UpdateDaemonsetRequestBody.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this UpdateDaemonsetRequestBody.

        集群名称

        :param cluster_name: The cluster_name of this UpdateDaemonsetRequestBody.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def auto_upgrade(self):
        r"""Gets the auto_upgrade of this UpdateDaemonsetRequestBody.

        开启agent自动升级

        :return: The auto_upgrade of this UpdateDaemonsetRequestBody.
        :rtype: bool
        """
        return self._auto_upgrade

    @auto_upgrade.setter
    def auto_upgrade(self, auto_upgrade):
        r"""Sets the auto_upgrade of this UpdateDaemonsetRequestBody.

        开启agent自动升级

        :param auto_upgrade: The auto_upgrade of this UpdateDaemonsetRequestBody.
        :type auto_upgrade: bool
        """
        self._auto_upgrade = auto_upgrade

    @property
    def runtime_info(self):
        r"""Gets the runtime_info of this UpdateDaemonsetRequestBody.

        容器运行时配置

        :return: The runtime_info of this UpdateDaemonsetRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        return self._runtime_info

    @runtime_info.setter
    def runtime_info(self, runtime_info):
        r"""Sets the runtime_info of this UpdateDaemonsetRequestBody.

        容器运行时配置

        :param runtime_info: The runtime_info of this UpdateDaemonsetRequestBody.
        :type runtime_info: list[:class:`huaweicloudsdkhss.v5.RuntimeRequestBody`]
        """
        self._runtime_info = runtime_info

    @property
    def schedule_info(self):
        r"""Gets the schedule_info of this UpdateDaemonsetRequestBody.

        :return: The schedule_info of this UpdateDaemonsetRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        return self._schedule_info

    @schedule_info.setter
    def schedule_info(self, schedule_info):
        r"""Sets the schedule_info of this UpdateDaemonsetRequestBody.

        :param schedule_info: The schedule_info of this UpdateDaemonsetRequestBody.
        :type schedule_info: :class:`huaweicloudsdkhss.v5.CreateDaemonsetRequestBodyScheduleInfo`
        """
        self._schedule_info = schedule_info

    @property
    def invoked_service(self):
        r"""Gets the invoked_service of this UpdateDaemonsetRequestBody.

        调用服务，默认hss，cce集成防护调用场景使用:   - hss：hss服务    - cce：cce服务

        :return: The invoked_service of this UpdateDaemonsetRequestBody.
        :rtype: str
        """
        return self._invoked_service

    @invoked_service.setter
    def invoked_service(self, invoked_service):
        r"""Sets the invoked_service of this UpdateDaemonsetRequestBody.

        调用服务，默认hss，cce集成防护调用场景使用:   - hss：hss服务    - cce：cce服务

        :param invoked_service: The invoked_service of this UpdateDaemonsetRequestBody.
        :type invoked_service: str
        """
        self._invoked_service = invoked_service

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this UpdateDaemonsetRequestBody.

        付费模式，cce集成防护调用场景使用:   - on_demand:按需    - free_security_check:免费安全体检

        :return: The charging_mode of this UpdateDaemonsetRequestBody.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this UpdateDaemonsetRequestBody.

        付费模式，cce集成防护调用场景使用:   - on_demand:按需    - free_security_check:免费安全体检

        :param charging_mode: The charging_mode of this UpdateDaemonsetRequestBody.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def cce_protection_type(self):
        r"""Gets the cce_protection_type of this UpdateDaemonsetRequestBody.

        cce防护类型，cce集成防护调用场景使用:   - cluster_level:集群级别防护    - node_level:节点级别防护

        :return: The cce_protection_type of this UpdateDaemonsetRequestBody.
        :rtype: str
        """
        return self._cce_protection_type

    @cce_protection_type.setter
    def cce_protection_type(self, cce_protection_type):
        r"""Sets the cce_protection_type of this UpdateDaemonsetRequestBody.

        cce防护类型，cce集成防护调用场景使用:   - cluster_level:集群级别防护    - node_level:节点级别防护

        :param cce_protection_type: The cce_protection_type of this UpdateDaemonsetRequestBody.
        :type cce_protection_type: str
        """
        self._cce_protection_type = cce_protection_type

    @property
    def prefer_packet_cycle(self):
        r"""Gets the prefer_packet_cycle of this UpdateDaemonsetRequestBody.

        优先使用包周期配额，cce集成防护调用场景使用，默认false

        :return: The prefer_packet_cycle of this UpdateDaemonsetRequestBody.
        :rtype: bool
        """
        return self._prefer_packet_cycle

    @prefer_packet_cycle.setter
    def prefer_packet_cycle(self, prefer_packet_cycle):
        r"""Sets the prefer_packet_cycle of this UpdateDaemonsetRequestBody.

        优先使用包周期配额，cce集成防护调用场景使用，默认false

        :param prefer_packet_cycle: The prefer_packet_cycle of this UpdateDaemonsetRequestBody.
        :type prefer_packet_cycle: bool
        """
        self._prefer_packet_cycle = prefer_packet_cycle

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
        if not isinstance(other, UpdateDaemonsetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
