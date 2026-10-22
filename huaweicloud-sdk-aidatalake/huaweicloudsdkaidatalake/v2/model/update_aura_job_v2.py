# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuraJobV2:

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
        'worker_group_config': 'list[WorkerGroupConfig]',
        'expand_cpu_resource': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'worker_group_config': 'worker_group_config',
        'expand_cpu_resource': 'expand_cpu_resource'
    }

    def __init__(self, type=None, worker_group_config=None, expand_cpu_resource=None):
        r"""UpdateAuraJobV2

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJobV2。 **默认取值**：不涉及。 
        :type type: str
        :param worker_group_config: **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。
        :type worker_group_config: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        :param expand_cpu_resource: **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。
        :type expand_cpu_resource: bool
        """
        
        

        self._type = None
        self._worker_group_config = None
        self._expand_cpu_resource = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if worker_group_config is not None:
            self.worker_group_config = worker_group_config
        if expand_cpu_resource is not None:
            self.expand_cpu_resource = expand_cpu_resource

    @property
    def type(self):
        r"""Gets the type of this UpdateAuraJobV2.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJobV2。 **默认取值**：不涉及。 

        :return: The type of this UpdateAuraJobV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateAuraJobV2.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：AuraJobV2。 **默认取值**：不涉及。 

        :param type: The type of this UpdateAuraJobV2.
        :type type: str
        """
        self._type = type

    @property
    def worker_group_config(self):
        r"""Gets the worker_group_config of this UpdateAuraJobV2.

        **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。

        :return: The worker_group_config of this UpdateAuraJobV2.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        """
        return self._worker_group_config

    @worker_group_config.setter
    def worker_group_config(self, worker_group_config):
        r"""Sets the worker_group_config of this UpdateAuraJobV2.

        **参数解释**：工作组补充配置，和外部capacity对应。 **约束限制**：最多10个。

        :param worker_group_config: The worker_group_config of this UpdateAuraJobV2.
        :type worker_group_config: list[:class:`huaweicloudsdkaidatalake.v2.WorkerGroupConfig`]
        """
        self._worker_group_config = worker_group_config

    @property
    def expand_cpu_resource(self):
        r"""Gets the expand_cpu_resource of this UpdateAuraJobV2.

        **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。

        :return: The expand_cpu_resource of this UpdateAuraJobV2.
        :rtype: bool
        """
        return self._expand_cpu_resource

    @expand_cpu_resource.setter
    def expand_cpu_resource(self, expand_cpu_resource):
        r"""Sets the expand_cpu_resource of this UpdateAuraJobV2.

        **参数解释**：开启后，通算工作组作业能够使用智算工作组空闲CPU及内存资源，该操作可能会导致智算任务因资源不足而排队。 **约束限制**：不涉及。 **取值范围**：   - true：开启通算工作组作业使用智算工作组空闲CPU及内存资源。   - false：关闭通算工作组作业使用智算工作组空闲CPU及内存资源。 **默认取值**：false。

        :param expand_cpu_resource: The expand_cpu_resource of this UpdateAuraJobV2.
        :type expand_cpu_resource: bool
        """
        self._expand_cpu_resource = expand_cpu_resource

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
        if not isinstance(other, UpdateAuraJobV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
