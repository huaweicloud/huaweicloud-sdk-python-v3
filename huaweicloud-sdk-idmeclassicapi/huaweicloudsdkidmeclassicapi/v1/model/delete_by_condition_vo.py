# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteByConditionVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'QueryRequestVo',
        'modifier': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'modifier': 'modifier'
    }

    def __init__(self, condition=None, modifier=None):
        r"""DeleteByConditionVo

        The model defined in huaweicloud sdk

        :param condition: 
        :type condition: :class:`huaweicloudsdkidmeclassicapi.v1.QueryRequestVo`
        :param modifier: **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._condition = None
        self._modifier = None
        self.discriminator = None

        self.condition = condition
        if modifier is not None:
            self.modifier = modifier

    @property
    def condition(self):
        r"""Gets the condition of this DeleteByConditionVo.

        :return: The condition of this DeleteByConditionVo.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.QueryRequestVo`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this DeleteByConditionVo.

        :param condition: The condition of this DeleteByConditionVo.
        :type condition: :class:`huaweicloudsdkidmeclassicapi.v1.QueryRequestVo`
        """
        self._condition = condition

    @property
    def modifier(self):
        r"""Gets the modifier of this DeleteByConditionVo.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this DeleteByConditionVo.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this DeleteByConditionVo.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this DeleteByConditionVo.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, DeleteByConditionVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
