# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BotMDefenseLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'threshold': 'int',
        'defense_action': 'int'
    }

    attribute_map = {
        'threshold': 'threshold',
        'defense_action': 'defense_action'
    }

    def __init__(self, threshold=None, defense_action=None):
        r"""BotMDefenseLevel

        The model defined in huaweicloud sdk

        :param threshold: **参数解释：** 该防护等级对应的分数门限，触发当前防护等级的风险分数阈值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type threshold: int
        :param defense_action: **参数解释：** 该防护等级对应的防护动作ID，如101表示拦截、102表示放行等 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type defense_action: int
        """
        
        

        self._threshold = None
        self._defense_action = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if defense_action is not None:
            self.defense_action = defense_action

    @property
    def threshold(self):
        r"""Gets the threshold of this BotMDefenseLevel.

        **参数解释：** 该防护等级对应的分数门限，触发当前防护等级的风险分数阈值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The threshold of this BotMDefenseLevel.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this BotMDefenseLevel.

        **参数解释：** 该防护等级对应的分数门限，触发当前防护等级的风险分数阈值 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param threshold: The threshold of this BotMDefenseLevel.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def defense_action(self):
        r"""Gets the defense_action of this BotMDefenseLevel.

        **参数解释：** 该防护等级对应的防护动作ID，如101表示拦截、102表示放行等 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The defense_action of this BotMDefenseLevel.
        :rtype: int
        """
        return self._defense_action

    @defense_action.setter
    def defense_action(self, defense_action):
        r"""Sets the defense_action of this BotMDefenseLevel.

        **参数解释：** 该防护等级对应的防护动作ID，如101表示拦截、102表示放行等 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param defense_action: The defense_action of this BotMDefenseLevel.
        :type defense_action: int
        """
        self._defense_action = defense_action

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
        if not isinstance(other, BotMDefenseLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
