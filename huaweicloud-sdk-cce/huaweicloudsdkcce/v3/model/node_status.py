# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'last_probe_time': 'str',
        'job_id': 'str',
        'server_id': 'str',
        'private_ip': 'str',
        'private_i_pv6_ip': 'str',
        'public_ip': 'str',
        'delete_status': 'DeleteStatus',
        'configuration_up_to_date': 'bool'
    }

    attribute_map = {
        'phase': 'phase',
        'last_probe_time': 'lastProbeTime',
        'job_id': 'jobID',
        'server_id': 'serverId',
        'private_ip': 'privateIP',
        'private_i_pv6_ip': 'privateIPv6IP',
        'public_ip': 'publicIP',
        'delete_status': 'deleteStatus',
        'configuration_up_to_date': 'configurationUpToDate'
    }

    def __init__(self, phase=None, last_probe_time=None, job_id=None, server_id=None, private_ip=None, private_i_pv6_ip=None, public_ip=None, delete_status=None, configuration_up_to_date=None):
        r"""NodeStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释**： 节点状态：节点资源生命周期管理（如安装卸载等）状态和集群内k8s node状态的综合体现 **约束限制**： 不涉及 **取值范围**： - Build：创建中，表示节点正处于创建过程中。 - Installing：安装中，表示节点正处于纳管过程中。 - Upgrading：升级中，表示节点正处于升级过程中。 - Active：运行中，表示节点处于正常状态。 - Abnormal：不可用，表示节点处于异常状态。 - Deleting： 删除中，表示节点正处于删除过程中。 - Error：错误，表示节点处于故障状态。  **默认取值**： 不涉及
        :type phase: str
        :param last_probe_time: **参数解释**： 节点最近一次状态检查时间。集群处于异常、冻结或者中间态（例如创建中）时，节点的状态检查动作可能受影响。检查时间超过5分的节点状态不具有参考意义。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type last_probe_time: str
        :param job_id: **参数解释**： 创建或删除时的任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type job_id: str
        :param server_id: **参数解释**： 底层云服务器或裸金属节点ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type server_id: str
        :param private_ip: **参数解释**： 节点主网卡私有网段IP地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type private_ip: str
        :param private_i_pv6_ip: **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type private_i_pv6_ip: str
        :param public_ip: **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type public_ip: str
        :param delete_status: 
        :type delete_status: :class:`huaweicloudsdkcce.v3.DeleteStatus`
        :param configuration_up_to_date: **参数解释**： 节点配置是否与所属节点池的节点模板最新配置一致。 当更新节点池os或runtime后，该节点池中存量节点的os或runtime便与节点池存在差异，configurationUpToDate参数值即为false。 重置节点后，存量节点的os和runtime与节点池配置保持一致，configurationUpToDate参数值即为true。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type configuration_up_to_date: bool
        """
        
        

        self._phase = None
        self._last_probe_time = None
        self._job_id = None
        self._server_id = None
        self._private_ip = None
        self._private_i_pv6_ip = None
        self._public_ip = None
        self._delete_status = None
        self._configuration_up_to_date = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if last_probe_time is not None:
            self.last_probe_time = last_probe_time
        if job_id is not None:
            self.job_id = job_id
        if server_id is not None:
            self.server_id = server_id
        if private_ip is not None:
            self.private_ip = private_ip
        if private_i_pv6_ip is not None:
            self.private_i_pv6_ip = private_i_pv6_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if delete_status is not None:
            self.delete_status = delete_status
        if configuration_up_to_date is not None:
            self.configuration_up_to_date = configuration_up_to_date

    @property
    def phase(self):
        r"""Gets the phase of this NodeStatus.

        **参数解释**： 节点状态：节点资源生命周期管理（如安装卸载等）状态和集群内k8s node状态的综合体现 **约束限制**： 不涉及 **取值范围**： - Build：创建中，表示节点正处于创建过程中。 - Installing：安装中，表示节点正处于纳管过程中。 - Upgrading：升级中，表示节点正处于升级过程中。 - Active：运行中，表示节点处于正常状态。 - Abnormal：不可用，表示节点处于异常状态。 - Deleting： 删除中，表示节点正处于删除过程中。 - Error：错误，表示节点处于故障状态。  **默认取值**： 不涉及

        :return: The phase of this NodeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this NodeStatus.

        **参数解释**： 节点状态：节点资源生命周期管理（如安装卸载等）状态和集群内k8s node状态的综合体现 **约束限制**： 不涉及 **取值范围**： - Build：创建中，表示节点正处于创建过程中。 - Installing：安装中，表示节点正处于纳管过程中。 - Upgrading：升级中，表示节点正处于升级过程中。 - Active：运行中，表示节点处于正常状态。 - Abnormal：不可用，表示节点处于异常状态。 - Deleting： 删除中，表示节点正处于删除过程中。 - Error：错误，表示节点处于故障状态。  **默认取值**： 不涉及

        :param phase: The phase of this NodeStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def last_probe_time(self):
        r"""Gets the last_probe_time of this NodeStatus.

        **参数解释**： 节点最近一次状态检查时间。集群处于异常、冻结或者中间态（例如创建中）时，节点的状态检查动作可能受影响。检查时间超过5分的节点状态不具有参考意义。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The last_probe_time of this NodeStatus.
        :rtype: str
        """
        return self._last_probe_time

    @last_probe_time.setter
    def last_probe_time(self, last_probe_time):
        r"""Sets the last_probe_time of this NodeStatus.

        **参数解释**： 节点最近一次状态检查时间。集群处于异常、冻结或者中间态（例如创建中）时，节点的状态检查动作可能受影响。检查时间超过5分的节点状态不具有参考意义。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param last_probe_time: The last_probe_time of this NodeStatus.
        :type last_probe_time: str
        """
        self._last_probe_time = last_probe_time

    @property
    def job_id(self):
        r"""Gets the job_id of this NodeStatus.

        **参数解释**： 创建或删除时的任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The job_id of this NodeStatus.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this NodeStatus.

        **参数解释**： 创建或删除时的任务ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param job_id: The job_id of this NodeStatus.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def server_id(self):
        r"""Gets the server_id of this NodeStatus.

        **参数解释**： 底层云服务器或裸金属节点ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The server_id of this NodeStatus.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this NodeStatus.

        **参数解释**： 底层云服务器或裸金属节点ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param server_id: The server_id of this NodeStatus.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def private_ip(self):
        r"""Gets the private_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IP地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The private_ip of this NodeStatus.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IP地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param private_ip: The private_ip of this NodeStatus.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def private_i_pv6_ip(self):
        r"""Gets the private_i_pv6_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The private_i_pv6_ip of this NodeStatus.
        :rtype: str
        """
        return self._private_i_pv6_ip

    @private_i_pv6_ip.setter
    def private_i_pv6_ip(self, private_i_pv6_ip):
        r"""Sets the private_i_pv6_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param private_i_pv6_ip: The private_i_pv6_ip of this NodeStatus.
        :type private_i_pv6_ip: str
        """
        self._private_i_pv6_ip = private_i_pv6_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The public_ip of this NodeStatus.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this NodeStatus.

        **参数解释**： 节点主网卡私有网段IPv6地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param public_ip: The public_ip of this NodeStatus.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def delete_status(self):
        r"""Gets the delete_status of this NodeStatus.

        :return: The delete_status of this NodeStatus.
        :rtype: :class:`huaweicloudsdkcce.v3.DeleteStatus`
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        r"""Sets the delete_status of this NodeStatus.

        :param delete_status: The delete_status of this NodeStatus.
        :type delete_status: :class:`huaweicloudsdkcce.v3.DeleteStatus`
        """
        self._delete_status = delete_status

    @property
    def configuration_up_to_date(self):
        r"""Gets the configuration_up_to_date of this NodeStatus.

        **参数解释**： 节点配置是否与所属节点池的节点模板最新配置一致。 当更新节点池os或runtime后，该节点池中存量节点的os或runtime便与节点池存在差异，configurationUpToDate参数值即为false。 重置节点后，存量节点的os和runtime与节点池配置保持一致，configurationUpToDate参数值即为true。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The configuration_up_to_date of this NodeStatus.
        :rtype: bool
        """
        return self._configuration_up_to_date

    @configuration_up_to_date.setter
    def configuration_up_to_date(self, configuration_up_to_date):
        r"""Sets the configuration_up_to_date of this NodeStatus.

        **参数解释**： 节点配置是否与所属节点池的节点模板最新配置一致。 当更新节点池os或runtime后，该节点池中存量节点的os或runtime便与节点池存在差异，configurationUpToDate参数值即为false。 重置节点后，存量节点的os和runtime与节点池配置保持一致，configurationUpToDate参数值即为true。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param configuration_up_to_date: The configuration_up_to_date of this NodeStatus.
        :type configuration_up_to_date: bool
        """
        self._configuration_up_to_date = configuration_up_to_date

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
