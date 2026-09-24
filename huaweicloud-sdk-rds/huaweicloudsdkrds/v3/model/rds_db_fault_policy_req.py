# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsDBFaultPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_policy': 'str'
    }

    attribute_map = {
        'db_policy': 'db_policy'
    }

    def __init__(self, db_policy=None):
        r"""RdsDBFaultPolicyReq

        The model defined in huaweicloud sdk

        :param db_policy: **参数解释**：  内核故障的处理策略。  **约束限制**：  不涉及。  **取值范围**：  - repairFirst：优先修复 - failoverFirst：优先切换  **默认取值**：  不涉及。
        :type db_policy: str
        """
        
        

        self._db_policy = None
        self.discriminator = None

        self.db_policy = db_policy

    @property
    def db_policy(self):
        r"""Gets the db_policy of this RdsDBFaultPolicyReq.

        **参数解释**：  内核故障的处理策略。  **约束限制**：  不涉及。  **取值范围**：  - repairFirst：优先修复 - failoverFirst：优先切换  **默认取值**：  不涉及。

        :return: The db_policy of this RdsDBFaultPolicyReq.
        :rtype: str
        """
        return self._db_policy

    @db_policy.setter
    def db_policy(self, db_policy):
        r"""Sets the db_policy of this RdsDBFaultPolicyReq.

        **参数解释**：  内核故障的处理策略。  **约束限制**：  不涉及。  **取值范围**：  - repairFirst：优先修复 - failoverFirst：优先切换  **默认取值**：  不涉及。

        :param db_policy: The db_policy of this RdsDBFaultPolicyReq.
        :type db_policy: str
        """
        self._db_policy = db_policy

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
        if not isinstance(other, RdsDBFaultPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
