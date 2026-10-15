# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobLinkResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'engine_type': 'str',
        'source_endpoint_type': 'str',
        'target_endpoint_type': 'str',
        'job_direction': 'str',
        'net_type': 'str',
        'task_types': 'list[str]',
        'cluster_modes': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'engine_type': 'engine_type',
        'source_endpoint_type': 'source_endpoint_type',
        'target_endpoint_type': 'target_endpoint_type',
        'job_direction': 'job_direction',
        'net_type': 'net_type',
        'task_types': 'task_types',
        'cluster_modes': 'cluster_modes',
        'description': 'description'
    }

    def __init__(self, job_type=None, engine_type=None, source_endpoint_type=None, target_endpoint_type=None, job_direction=None, net_type=None, task_types=None, cluster_modes=None, description=None):
        r"""JobLinkResp

        The model defined in huaweicloud sdk

        :param job_type: **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及
        :type job_type: str
        :param engine_type: **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎组合。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及
        :type engine_type: str
        :param source_endpoint_type: **参数解释**：  源数据库实例类型，标识源数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及
        :type source_endpoint_type: str
        :param target_endpoint_type: **参数解释**：  目标数据库实例类型，标识目标数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及
        :type target_endpoint_type: str
        :param job_direction: **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及
        :type job_direction: str
        :param net_type: **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及
        :type net_type: str
        :param task_types: **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type task_types: list[str]
        :param cluster_modes: **参数解释**：  可用链路支持的引擎实例模式列表，表示该链路支持的数据库部署架构类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type cluster_modes: list[str]
        :param description: **参数解释**：  链路的描述信息，用于说明该链路的适用场景或功能特点。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type description: str
        """
        
        

        self._job_type = None
        self._engine_type = None
        self._source_endpoint_type = None
        self._target_endpoint_type = None
        self._job_direction = None
        self._net_type = None
        self._task_types = None
        self._cluster_modes = None
        self._description = None
        self.discriminator = None

        self.job_type = job_type
        self.engine_type = engine_type
        self.source_endpoint_type = source_endpoint_type
        self.target_endpoint_type = target_endpoint_type
        self.job_direction = job_direction
        self.net_type = net_type
        self.task_types = task_types
        self.cluster_modes = cluster_modes
        self.description = description

    @property
    def job_type(self):
        r"""Gets the job_type of this JobLinkResp.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :return: The job_type of this JobLinkResp.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this JobLinkResp.

        **参数解释**：  DRS任务场景类型，用于区分不同的数据复制场景。  **约束限制**：  不涉及。  **取值范围**：  - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备  **默认取值**：  不涉及

        :param job_type: The job_type of this JobLinkResp.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this JobLinkResp.

        **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎组合。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :return: The engine_type of this JobLinkResp.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this JobLinkResp.

        **参数解释**：  DRS任务引擎类型，标识数据复制任务所使用的数据库引擎组合。  **约束限制**：  不涉及。  **取值范围**：  - oracle-to-gaussdbv5：Oracle同步到GaussDB分布式版，实时同步场景使用 - redis-to-gaussredis：Redis迁移到GeminiDB Redis，实时迁移场景使用 - rediscluster-to-gaussredis：Redis集群迁移到GeminiDB Redis，实时迁移场景使用  **默认取值**：  不涉及

        :param engine_type: The engine_type of this JobLinkResp.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def source_endpoint_type(self):
        r"""Gets the source_endpoint_type of this JobLinkResp.

        **参数解释**：  源数据库实例类型，标识源数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及

        :return: The source_endpoint_type of this JobLinkResp.
        :rtype: str
        """
        return self._source_endpoint_type

    @source_endpoint_type.setter
    def source_endpoint_type(self, source_endpoint_type):
        r"""Sets the source_endpoint_type of this JobLinkResp.

        **参数解释**：  源数据库实例类型，标识源数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及

        :param source_endpoint_type: The source_endpoint_type of this JobLinkResp.
        :type source_endpoint_type: str
        """
        self._source_endpoint_type = source_endpoint_type

    @property
    def target_endpoint_type(self):
        r"""Gets the target_endpoint_type of this JobLinkResp.

        **参数解释**：  目标数据库实例类型，标识目标数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及

        :return: The target_endpoint_type of this JobLinkResp.
        :rtype: str
        """
        return self._target_endpoint_type

    @target_endpoint_type.setter
    def target_endpoint_type(self, target_endpoint_type):
        r"""Sets the target_endpoint_type of this JobLinkResp.

        **参数解释**：  目标数据库实例类型，标识目标数据库的部署方式。  **约束限制**：  不涉及。  **取值范围**：  - offline：自建数据库 - ecs：华为云ECS自建数据库 - cloud：华为云数据库  **默认取值**：  不涉及

        :param target_endpoint_type: The target_endpoint_type of this JobLinkResp.
        :type target_endpoint_type: str
        """
        self._target_endpoint_type = target_endpoint_type

    @property
    def job_direction(self):
        r"""Gets the job_direction of this JobLinkResp.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :return: The job_direction of this JobLinkResp.
        :rtype: str
        """
        return self._job_direction

    @job_direction.setter
    def job_direction(self, job_direction):
        r"""Sets the job_direction of this JobLinkResp.

        **参数解释**：  任务的迁移方向。  **约束限制**：  不涉及。  **取值范围**：  - up：入云，灾备场景时对应本云为备 - down：出云，灾备场景时对应本云为主 - non-dbs：自建  **默认取值**：  不涉及

        :param job_direction: The job_direction of this JobLinkResp.
        :type job_direction: str
        """
        self._job_direction = job_direction

    @property
    def net_type(self):
        r"""Gets the net_type of this JobLinkResp.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :return: The net_type of this JobLinkResp.
        :rtype: str
        """
        return self._net_type

    @net_type.setter
    def net_type(self, net_type):
        r"""Sets the net_type of this JobLinkResp.

        **参数解释**：  任务使用的网络类型。  **约束限制**：  不涉及。  **取值范围**：  - eip：公网网络 - vpc：VPC网络，灾备场景不支持选择VPC网络 - vpn：VPN、专线网络  **默认取值**：  不涉及

        :param net_type: The net_type of this JobLinkResp.
        :type net_type: str
        """
        self._net_type = net_type

    @property
    def task_types(self):
        r"""Gets the task_types of this JobLinkResp.

        **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The task_types of this JobLinkResp.
        :rtype: list[str]
        """
        return self._task_types

    @task_types.setter
    def task_types(self, task_types):
        r"""Sets the task_types of this JobLinkResp.

        **参数解释**：  可用链路支持的迁移模式列表，表示该链路支持的数据迁移执行方式。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param task_types: The task_types of this JobLinkResp.
        :type task_types: list[str]
        """
        self._task_types = task_types

    @property
    def cluster_modes(self):
        r"""Gets the cluster_modes of this JobLinkResp.

        **参数解释**：  可用链路支持的引擎实例模式列表，表示该链路支持的数据库部署架构类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The cluster_modes of this JobLinkResp.
        :rtype: list[str]
        """
        return self._cluster_modes

    @cluster_modes.setter
    def cluster_modes(self, cluster_modes):
        r"""Sets the cluster_modes of this JobLinkResp.

        **参数解释**：  可用链路支持的引擎实例模式列表，表示该链路支持的数据库部署架构类型。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param cluster_modes: The cluster_modes of this JobLinkResp.
        :type cluster_modes: list[str]
        """
        self._cluster_modes = cluster_modes

    @property
    def description(self):
        r"""Gets the description of this JobLinkResp.

        **参数解释**：  链路的描述信息，用于说明该链路的适用场景或功能特点。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The description of this JobLinkResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this JobLinkResp.

        **参数解释**：  链路的描述信息，用于说明该链路的适用场景或功能特点。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param description: The description of this JobLinkResp.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, JobLinkResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
