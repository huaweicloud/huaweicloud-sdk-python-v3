# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterPlanActionsParam:

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
        'strategy': 'str'
    }

    attribute_map = {
        'type': 'type',
        'strategy': 'strategy'
    }

    def __init__(self, type=None, strategy=None):
        r"""LogicalClusterPlanActionsParam

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 定时增删计划行为类型，取值范围为（create|delete）。 **约束限制**： 不涉及。 **取值范围**： create：创建 delete：删除 **默认取值**： 不涉及。
        :type type: str
        :param strategy: **参数解释**： 周期性定时增删计划，Cron策略表达式：如\&quot;0 0 0 ? * 3\&quot;。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type strategy: str
        """
        
        

        self._type = None
        self._strategy = None
        self.discriminator = None

        self.type = type
        if strategy is not None:
            self.strategy = strategy

    @property
    def type(self):
        r"""Gets the type of this LogicalClusterPlanActionsParam.

        **参数解释**： 定时增删计划行为类型，取值范围为（create|delete）。 **约束限制**： 不涉及。 **取值范围**： create：创建 delete：删除 **默认取值**： 不涉及。

        :return: The type of this LogicalClusterPlanActionsParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LogicalClusterPlanActionsParam.

        **参数解释**： 定时增删计划行为类型，取值范围为（create|delete）。 **约束限制**： 不涉及。 **取值范围**： create：创建 delete：删除 **默认取值**： 不涉及。

        :param type: The type of this LogicalClusterPlanActionsParam.
        :type type: str
        """
        self._type = type

    @property
    def strategy(self):
        r"""Gets the strategy of this LogicalClusterPlanActionsParam.

        **参数解释**： 周期性定时增删计划，Cron策略表达式：如\"0 0 0 ? * 3\"。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The strategy of this LogicalClusterPlanActionsParam.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this LogicalClusterPlanActionsParam.

        **参数解释**： 周期性定时增删计划，Cron策略表达式：如\"0 0 0 ? * 3\"。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param strategy: The strategy of this LogicalClusterPlanActionsParam.
        :type strategy: str
        """
        self._strategy = strategy

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
        if not isinstance(other, LogicalClusterPlanActionsParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
