# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceBindingStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduler_observed_generation': 'int',
        'conditions': 'list[ConditionStatus]'
    }

    attribute_map = {
        'scheduler_observed_generation': 'schedulerObservedGeneration',
        'conditions': 'conditions'
    }

    def __init__(self, scheduler_observed_generation=None, conditions=None):
        r"""ResourceBindingStatus

        The model defined in huaweicloud sdk

        :param scheduler_observed_generation: 记录调度器当前观察到的资源生成版本代数
        :type scheduler_observed_generation: int
        :param conditions: 资源的各种状态条件
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        """
        
        

        self._scheduler_observed_generation = None
        self._conditions = None
        self.discriminator = None

        if scheduler_observed_generation is not None:
            self.scheduler_observed_generation = scheduler_observed_generation
        if conditions is not None:
            self.conditions = conditions

    @property
    def scheduler_observed_generation(self):
        r"""Gets the scheduler_observed_generation of this ResourceBindingStatus.

        记录调度器当前观察到的资源生成版本代数

        :return: The scheduler_observed_generation of this ResourceBindingStatus.
        :rtype: int
        """
        return self._scheduler_observed_generation

    @scheduler_observed_generation.setter
    def scheduler_observed_generation(self, scheduler_observed_generation):
        r"""Sets the scheduler_observed_generation of this ResourceBindingStatus.

        记录调度器当前观察到的资源生成版本代数

        :param scheduler_observed_generation: The scheduler_observed_generation of this ResourceBindingStatus.
        :type scheduler_observed_generation: int
        """
        self._scheduler_observed_generation = scheduler_observed_generation

    @property
    def conditions(self):
        r"""Gets the conditions of this ResourceBindingStatus.

        资源的各种状态条件

        :return: The conditions of this ResourceBindingStatus.
        :rtype: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this ResourceBindingStatus.

        资源的各种状态条件

        :param conditions: The conditions of this ResourceBindingStatus.
        :type conditions: list[:class:`huaweicloudsdkucs.v1.ConditionStatus`]
        """
        self._conditions = conditions

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
        if not isinstance(other, ResourceBindingStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
