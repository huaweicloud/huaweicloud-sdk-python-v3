# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Match:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic': 'str',
        'criteria': 'list[Criteria]'
    }

    attribute_map = {
        'logic': 'logic',
        'criteria': 'criteria'
    }

    def __init__(self, logic=None, criteria=None):
        r"""Match

        The model defined in huaweicloud sdk

        :param logic: **参数解释：** 逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及
        :type logic: str
        :param criteria: **参数解释：** 匹配条件列表 **约束限制：** 不涉及
        :type criteria: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        
        

        self._logic = None
        self._criteria = None
        self.discriminator = None

        self.logic = logic
        self.criteria = criteria

    @property
    def logic(self):
        r"""Gets the logic of this Match.

        **参数解释：** 逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及

        :return: The logic of this Match.
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        r"""Sets the logic of this Match.

        **参数解释：** 逻辑运算符 **约束限制：** 不涉及 **取值范围：** - and: 与关系 - or: 或关系 **默认取值：** 不涉及

        :param logic: The logic of this Match.
        :type logic: str
        """
        self._logic = logic

    @property
    def criteria(self):
        r"""Gets the criteria of this Match.

        **参数解释：** 匹配条件列表 **约束限制：** 不涉及

        :return: The criteria of this Match.
        :rtype: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        return self._criteria

    @criteria.setter
    def criteria(self, criteria):
        r"""Sets the criteria of this Match.

        **参数解释：** 匹配条件列表 **约束限制：** 不涉及

        :param criteria: The criteria of this Match.
        :type criteria: list[:class:`huaweicloudsdkcdn.v2.Criteria`]
        """
        self._criteria = criteria

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
        if not isinstance(other, Match):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
