# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InteractionRuleGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'interaction_rules': 'list[InteractionRuleInfo]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'interaction_rules': 'interaction_rules'
    }

    def __init__(self, group_name=None, interaction_rules=None):
        r"""InteractionRuleGroup

        The model defined in huaweicloud sdk

        :param group_name: 互动规则库名称
        :type group_name: str
        :param interaction_rules: 互动规则列表
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        
        

        self._group_name = None
        self._interaction_rules = None
        self.discriminator = None

        self.group_name = group_name
        if interaction_rules is not None:
            self.interaction_rules = interaction_rules

    @property
    def group_name(self):
        r"""Gets the group_name of this InteractionRuleGroup.

        互动规则库名称

        :return: The group_name of this InteractionRuleGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this InteractionRuleGroup.

        互动规则库名称

        :param group_name: The group_name of this InteractionRuleGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def interaction_rules(self):
        r"""Gets the interaction_rules of this InteractionRuleGroup.

        互动规则列表

        :return: The interaction_rules of this InteractionRuleGroup.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        r"""Sets the interaction_rules of this InteractionRuleGroup.

        互动规则列表

        :param interaction_rules: The interaction_rules of this InteractionRuleGroup.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        self._interaction_rules = interaction_rules

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
        if not isinstance(other, InteractionRuleGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
