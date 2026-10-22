# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobUpdateRequestBodySpecSchedulePolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'int',
        'preemptible': 'bool'
    }

    attribute_map = {
        'priority': 'priority',
        'preemptible': 'preemptible'
    }

    def __init__(self, priority=None, preemptible=None):
        r"""JobUpdateRequestBodySpecSchedulePolicy

        The model defined in huaweicloud sdk

        :param priority: **参数解释**：训练作业优先级。 **约束限制**： - 仅使用专属资源池训练时才支持设置训练作业优先级。 - 作业优先级取值为1~3，默认优先级为1，最高优先级为3。 默认用户权限可选择优先级1和2，配置了“设置作业为高优先级权限”的用户可选择优先级1~3。  **取值范围**：1-3 **默认取值**：不涉及。
        :type priority: int
        :param preemptible: **参数解释**：是否可以被抢占。 **约束限制**：不涉及。 **取值范围**： - true：可以被抢占 - false：不可以被抢占  **默认取值**：不涉及。
        :type preemptible: bool
        """
        
        

        self._priority = None
        self._preemptible = None
        self.discriminator = None

        if priority is not None:
            self.priority = priority
        if preemptible is not None:
            self.preemptible = preemptible

    @property
    def priority(self):
        r"""Gets the priority of this JobUpdateRequestBodySpecSchedulePolicy.

        **参数解释**：训练作业优先级。 **约束限制**： - 仅使用专属资源池训练时才支持设置训练作业优先级。 - 作业优先级取值为1~3，默认优先级为1，最高优先级为3。 默认用户权限可选择优先级1和2，配置了“设置作业为高优先级权限”的用户可选择优先级1~3。  **取值范围**：1-3 **默认取值**：不涉及。

        :return: The priority of this JobUpdateRequestBodySpecSchedulePolicy.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this JobUpdateRequestBodySpecSchedulePolicy.

        **参数解释**：训练作业优先级。 **约束限制**： - 仅使用专属资源池训练时才支持设置训练作业优先级。 - 作业优先级取值为1~3，默认优先级为1，最高优先级为3。 默认用户权限可选择优先级1和2，配置了“设置作业为高优先级权限”的用户可选择优先级1~3。  **取值范围**：1-3 **默认取值**：不涉及。

        :param priority: The priority of this JobUpdateRequestBodySpecSchedulePolicy.
        :type priority: int
        """
        self._priority = priority

    @property
    def preemptible(self):
        r"""Gets the preemptible of this JobUpdateRequestBodySpecSchedulePolicy.

        **参数解释**：是否可以被抢占。 **约束限制**：不涉及。 **取值范围**： - true：可以被抢占 - false：不可以被抢占  **默认取值**：不涉及。

        :return: The preemptible of this JobUpdateRequestBodySpecSchedulePolicy.
        :rtype: bool
        """
        return self._preemptible

    @preemptible.setter
    def preemptible(self, preemptible):
        r"""Sets the preemptible of this JobUpdateRequestBodySpecSchedulePolicy.

        **参数解释**：是否可以被抢占。 **约束限制**：不涉及。 **取值范围**： - true：可以被抢占 - false：不可以被抢占  **默认取值**：不涉及。

        :param preemptible: The preemptible of this JobUpdateRequestBodySpecSchedulePolicy.
        :type preemptible: bool
        """
        self._preemptible = preemptible

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
        if not isinstance(other, JobUpdateRequestBodySpecSchedulePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
