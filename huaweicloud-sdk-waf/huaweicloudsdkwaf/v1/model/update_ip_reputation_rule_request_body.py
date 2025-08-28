# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIpReputationRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'policyname': 'str',
        'description': 'str',
        'action': 'UpdateIpReputationRuleRequestBodyAction',
        'type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'policyname': 'policyname',
        'description': 'description',
        'action': 'action',
        'type': 'type',
        'tags': 'tags'
    }

    def __init__(self, name=None, policyname=None, description=None, action=None, type=None, tags=None):
        r"""UpdateIpReputationRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param policyname: **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyname: str
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.UpdateIpReputationRuleRequestBodyAction`
        :param type: **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        :param tags: **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: list[str]
        """
        
        

        self._name = None
        self._policyname = None
        self._description = None
        self._action = None
        self._type = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if policyname is not None:
            self.policyname = policyname
        if description is not None:
            self.description = description
        if action is not None:
            self.action = action
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this UpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this UpdateIpReputationRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def policyname(self):
        r"""Gets the policyname of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyname of this UpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        r"""Sets the policyname of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyname: The policyname of this UpdateIpReputationRuleRequestBody.
        :type policyname: str
        """
        self._policyname = policyname

    @property
    def description(self):
        r"""Gets the description of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this UpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this UpdateIpReputationRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def action(self):
        r"""Gets the action of this UpdateIpReputationRuleRequestBody.

        :return: The action of this UpdateIpReputationRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.UpdateIpReputationRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateIpReputationRuleRequestBody.

        :param action: The action of this UpdateIpReputationRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.UpdateIpReputationRuleRequestBodyAction`
        """
        self._action = action

    @property
    def type(self):
        r"""Gets the type of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this UpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this UpdateIpReputationRuleRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this UpdateIpReputationRuleRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this UpdateIpReputationRuleRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateIpReputationRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
