# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyRecyclePolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_days': 'int',
        'default_use_recycle': 'bool'
    }

    attribute_map = {
        'retention_days': 'retention_days',
        'default_use_recycle': 'default_use_recycle'
    }

    def __init__(self, retention_days=None, default_use_recycle=None):
        r"""ModifyRecyclePolicyReq

        The model defined in huaweicloud sdk

        :param retention_days: **参数解释**： 保留天数。 **约束限制**： 不涉及。 **取值范围**： 1~7天。 **默认取值**： 不涉及
        :type retention_days: int
        :param default_use_recycle: **参数解释**： 是否使用回收站。  **约束限制**： 不涉及。 **取值范围**： - true：使用回收站。 - false：不使用回收站。 **默认取值**： 不涉及
        :type default_use_recycle: bool
        """
        
        

        self._retention_days = None
        self._default_use_recycle = None
        self.discriminator = None

        if retention_days is not None:
            self.retention_days = retention_days
        if default_use_recycle is not None:
            self.default_use_recycle = default_use_recycle

    @property
    def retention_days(self):
        r"""Gets the retention_days of this ModifyRecyclePolicyReq.

        **参数解释**： 保留天数。 **约束限制**： 不涉及。 **取值范围**： 1~7天。 **默认取值**： 不涉及

        :return: The retention_days of this ModifyRecyclePolicyReq.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this ModifyRecyclePolicyReq.

        **参数解释**： 保留天数。 **约束限制**： 不涉及。 **取值范围**： 1~7天。 **默认取值**： 不涉及

        :param retention_days: The retention_days of this ModifyRecyclePolicyReq.
        :type retention_days: int
        """
        self._retention_days = retention_days

    @property
    def default_use_recycle(self):
        r"""Gets the default_use_recycle of this ModifyRecyclePolicyReq.

        **参数解释**： 是否使用回收站。  **约束限制**： 不涉及。 **取值范围**： - true：使用回收站。 - false：不使用回收站。 **默认取值**： 不涉及

        :return: The default_use_recycle of this ModifyRecyclePolicyReq.
        :rtype: bool
        """
        return self._default_use_recycle

    @default_use_recycle.setter
    def default_use_recycle(self, default_use_recycle):
        r"""Sets the default_use_recycle of this ModifyRecyclePolicyReq.

        **参数解释**： 是否使用回收站。  **约束限制**： 不涉及。 **取值范围**： - true：使用回收站。 - false：不使用回收站。 **默认取值**： 不涉及

        :param default_use_recycle: The default_use_recycle of this ModifyRecyclePolicyReq.
        :type default_use_recycle: bool
        """
        self._default_use_recycle = default_use_recycle

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
        if not isinstance(other, ModifyRecyclePolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
