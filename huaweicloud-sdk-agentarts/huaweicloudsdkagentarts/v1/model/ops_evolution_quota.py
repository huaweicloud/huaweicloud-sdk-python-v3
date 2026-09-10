# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsEvolutionQuota:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'quota': 'int',
        'used': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quota': 'quota',
        'used': 'used'
    }

    def __init__(self, type=None, quota=None, used=None):
        r"""OpsEvolutionQuota

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 配额类型。 **取值范围：** - model_tuning_task_count: 单个租户可以创建的模型优化任务个数 - agent_tuning_task_count: 单个租户可以创建的智能体优化任务个数 - parallel_agent_tuning_task_count: 单个租户可以并行运行的的智能体优化任务个数 - analysis_task_count: 单个租户可以创建的分析任务个数 - parallel_analysis_task_count: 单个租户可以并行运行的的分析任务个数 - model_deployment_count: 单个租户可以创建的模型部署个数
        :type type: str
        :param quota: **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。
        :type quota: int
        :param used: **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。
        :type used: int
        """
        
        

        self._type = None
        self._quota = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.quota = quota
        self.used = used

    @property
    def type(self):
        r"""Gets the type of this OpsEvolutionQuota.

        **参数解释：** 配额类型。 **取值范围：** - model_tuning_task_count: 单个租户可以创建的模型优化任务个数 - agent_tuning_task_count: 单个租户可以创建的智能体优化任务个数 - parallel_agent_tuning_task_count: 单个租户可以并行运行的的智能体优化任务个数 - analysis_task_count: 单个租户可以创建的分析任务个数 - parallel_analysis_task_count: 单个租户可以并行运行的的分析任务个数 - model_deployment_count: 单个租户可以创建的模型部署个数

        :return: The type of this OpsEvolutionQuota.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsEvolutionQuota.

        **参数解释：** 配额类型。 **取值范围：** - model_tuning_task_count: 单个租户可以创建的模型优化任务个数 - agent_tuning_task_count: 单个租户可以创建的智能体优化任务个数 - parallel_agent_tuning_task_count: 单个租户可以并行运行的的智能体优化任务个数 - analysis_task_count: 单个租户可以创建的分析任务个数 - parallel_analysis_task_count: 单个租户可以并行运行的的分析任务个数 - model_deployment_count: 单个租户可以创建的模型部署个数

        :param type: The type of this OpsEvolutionQuota.
        :type type: str
        """
        self._type = type

    @property
    def quota(self):
        r"""Gets the quota of this OpsEvolutionQuota.

        **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。

        :return: The quota of this OpsEvolutionQuota.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this OpsEvolutionQuota.

        **参数解释：** 当前配置的配额值。 **取值范围：** 取值为 1-10000个。

        :param quota: The quota of this OpsEvolutionQuota.
        :type quota: int
        """
        self._quota = quota

    @property
    def used(self):
        r"""Gets the used of this OpsEvolutionQuota.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。

        :return: The used of this OpsEvolutionQuota.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this OpsEvolutionQuota.

        **参数解释：** 已使用数量（实时计算）。 **取值范围：** 取值为 0-10000个。

        :param used: The used of this OpsEvolutionQuota.
        :type used: int
        """
        self._used = used

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
        if not isinstance(other, OpsEvolutionQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
