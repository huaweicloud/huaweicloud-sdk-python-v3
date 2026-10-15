# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportLinkInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'net_type': 'str',
        'task_modes': 'list[str]',
        'job_direction': 'str',
        'cluster_mode': 'str',
        'job_instance_type': 'str',
        'is_support_bind_eip': 'bool'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'net_type': 'net_type',
        'task_modes': 'task_modes',
        'job_direction': 'job_direction',
        'cluster_mode': 'cluster_mode',
        'job_instance_type': 'job_instance_type',
        'is_support_bind_eip': 'is_support_bind_eip'
    }

    def __init__(self, engine_type=None, net_type=None, task_modes=None, job_direction=None, cluster_mode=None, job_instance_type=None, is_support_bind_eip=None):
        r"""SupportLinkInfo

        The model defined in huaweicloud sdk

        :param engine_type: **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type engine_type: str
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及
        :type net_type: str
        :param task_modes: **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移 - FULL_INCR_TRANS：全量+增量迁移 - INCR_TRANS：增量迁移  **默认取值**：  不涉及
        :type task_modes: list[str]
        :param job_direction: **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及
        :type job_direction: str
        :param cluster_mode: **参数解释**：  云上数据库实例的部署模式，标识目标或源数据库实例在云上的集群架构类型。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机模式 - Ha：主备模式 - Cluster：集群模式 - Sharding：分片模式 - Independent：GaussDB独立部署模式  **默认取值**：  不涉及
        :type cluster_mode: str
        :param job_instance_type: **参数解释**：  DRS迁移实例的部署类型，决定迁移任务所使用的实例架构。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机 - Ha：主备  **默认取值**：  不涉及
        :type job_instance_type: str
        :param is_support_bind_eip: **参数解释**：  是否支持绑定弹性公网IP（EIP），标识当前链路是否允许为迁移实例绑定弹性公网IP以实现公网通信。  **约束限制**：  不涉及。  **取值范围**：  - true：支持绑定EIP - false：不支持绑定EIP  **默认取值**：  不涉及
        :type is_support_bind_eip: bool
        """
        
        

        self._engine_type = None
        self._net_type = None
        self._task_modes = None
        self._job_direction = None
        self._cluster_mode = None
        self._job_instance_type = None
        self._is_support_bind_eip = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if net_type is not None:
            self.net_type = net_type
        if task_modes is not None:
            self.task_modes = task_modes
        if job_direction is not None:
            self.job_direction = job_direction
        if cluster_mode is not None:
            self.cluster_mode = cluster_mode
        if job_instance_type is not None:
            self.job_instance_type = job_instance_type
        if is_support_bind_eip is not None:
            self.is_support_bind_eip = is_support_bind_eip

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SupportLinkInfo.

        **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The engine_type of this SupportLinkInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SupportLinkInfo.

        **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param engine_type: The engine_type of this SupportLinkInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def net_type(self):
        r"""Gets the net_type of this SupportLinkInfo.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :return: The net_type of this SupportLinkInfo.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this SupportLinkInfo.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  灾备场景不支持选择VPC网络。  **取值范围**：  - eip：公网网络 - vpc：VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :param net_type: The net_type of this SupportLinkInfo.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def task_modes(self):
        r"""Gets the task_modes of this SupportLinkInfo.

        **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移 - FULL_INCR_TRANS：全量+增量迁移 - INCR_TRANS：增量迁移  **默认取值**：  不涉及

        :return: The task_modes of this SupportLinkInfo.
        :rtype: list[str]
        """
        return self._task_modes

    @task_modes.setter
    def task_modes(self, task_modes):
        r"""Sets the task_modes of this SupportLinkInfo.

        **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  - FULL_TRANS：全量迁移 - FULL_INCR_TRANS：全量+增量迁移 - INCR_TRANS：增量迁移  **默认取值**：  不涉及

        :param task_modes: The task_modes of this SupportLinkInfo.
        :type task_modes: list[str]
        """
        self._task_modes = task_modes

    @property
    def job_direction(self):
        r"""Gets the job_direction of this SupportLinkInfo.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :return: The job_direction of this SupportLinkInfo.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this SupportLinkInfo.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :param job_direction: The job_direction of this SupportLinkInfo.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def cluster_mode(self):
        r"""Gets the cluster_mode of this SupportLinkInfo.

        **参数解释**：  云上数据库实例的部署模式，标识目标或源数据库实例在云上的集群架构类型。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机模式 - Ha：主备模式 - Cluster：集群模式 - Sharding：分片模式 - Independent：GaussDB独立部署模式  **默认取值**：  不涉及

        :return: The cluster_mode of this SupportLinkInfo.
        :rtype: str
        """
        return self._cluster_mode

    @cluster_mode.setter
    def cluster_mode(self, cluster_mode):
        r"""Sets the cluster_mode of this SupportLinkInfo.

        **参数解释**：  云上数据库实例的部署模式，标识目标或源数据库实例在云上的集群架构类型。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机模式 - Ha：主备模式 - Cluster：集群模式 - Sharding：分片模式 - Independent：GaussDB独立部署模式  **默认取值**：  不涉及

        :param cluster_mode: The cluster_mode of this SupportLinkInfo.
        :type cluster_mode: str
        """
        self._cluster_mode = cluster_mode

    @property
    def job_instance_type(self):
        r"""Gets the job_instance_type of this SupportLinkInfo.

        **参数解释**：  DRS迁移实例的部署类型，决定迁移任务所使用的实例架构。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机 - Ha：主备  **默认取值**：  不涉及

        :return: The job_instance_type of this SupportLinkInfo.
        :rtype: str
        """
        return self._job_instance_type

    @job_instance_type.setter
    def job_instance_type(self, job_instance_type):
        r"""Sets the job_instance_type of this SupportLinkInfo.

        **参数解释**：  DRS迁移实例的部署类型，决定迁移任务所使用的实例架构。  **约束限制**：  不涉及。  **取值范围**：  - Single：单机 - Ha：主备  **默认取值**：  不涉及

        :param job_instance_type: The job_instance_type of this SupportLinkInfo.
        :type job_instance_type: str
        """
        self._job_instance_type = job_instance_type

    @property
    def is_support_bind_eip(self):
        r"""Gets the is_support_bind_eip of this SupportLinkInfo.

        **参数解释**：  是否支持绑定弹性公网IP（EIP），标识当前链路是否允许为迁移实例绑定弹性公网IP以实现公网通信。  **约束限制**：  不涉及。  **取值范围**：  - true：支持绑定EIP - false：不支持绑定EIP  **默认取值**：  不涉及

        :return: The is_support_bind_eip of this SupportLinkInfo.
        :rtype: bool
        """
        return self._is_support_bind_eip

    @is_support_bind_eip.setter
    def is_support_bind_eip(self, is_support_bind_eip):
        r"""Sets the is_support_bind_eip of this SupportLinkInfo.

        **参数解释**：  是否支持绑定弹性公网IP（EIP），标识当前链路是否允许为迁移实例绑定弹性公网IP以实现公网通信。  **约束限制**：  不涉及。  **取值范围**：  - true：支持绑定EIP - false：不支持绑定EIP  **默认取值**：  不涉及

        :param is_support_bind_eip: The is_support_bind_eip of this SupportLinkInfo.
        :type is_support_bind_eip: bool
        """
        self._is_support_bind_eip = is_support_bind_eip

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
        if not isinstance(other, SupportLinkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
