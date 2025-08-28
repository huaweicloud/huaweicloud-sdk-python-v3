# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpReputationRuleRequestBody:

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
        'status': 'int',
        'action': 'CreateIpReputationRuleRequestBodyAction',
        'type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'policyname': 'policyname',
        'description': 'description',
        'status': 'status',
        'action': 'action',
        'type': 'type',
        'tags': 'tags'
    }

    def __init__(self, name=None, policyname=None, description=None, status=None, action=None, type=None, tags=None):
        r"""CreateIpReputationRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param policyname: **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyname: str
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param status: **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: int
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
        :param type: **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        :param tags: **参数解释：** 标签列表，用于指定关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: list[str]
        """
        
        

        self._name = None
        self._policyname = None
        self._description = None
        self._status = None
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
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this CreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this CreateIpReputationRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def policyname(self):
        r"""Gets the policyname of this CreateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyname of this CreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        r"""Sets the policyname of this CreateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyname: The policyname of this CreateIpReputationRuleRequestBody.
        :type policyname: str
        """
        self._policyname = policyname

    @property
    def description(self):
        r"""Gets the description of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateIpReputationRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this CreateIpReputationRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this CreateIpReputationRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def action(self):
        r"""Gets the action of this CreateIpReputationRuleRequestBody.

        :return: The action of this CreateIpReputationRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateIpReputationRuleRequestBody.

        :param action: The action of this CreateIpReputationRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
        """
        self._action = action

    @property
    def type(self):
        r"""Gets the type of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this CreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this CreateIpReputationRuleRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this CreateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，用于指定关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this CreateIpReputationRuleRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，用于指定关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this CreateIpReputationRuleRequestBody.
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
        if not isinstance(other, CreateIpReputationRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
