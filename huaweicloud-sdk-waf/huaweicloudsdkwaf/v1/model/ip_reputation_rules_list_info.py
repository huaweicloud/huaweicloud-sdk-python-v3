# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IpReputationRulesListInfo:

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
        'id': 'str',
        'policyid': 'str',
        'type': 'str',
        'description': 'str',
        'tags': 'list[str]',
        'status': 'int',
        'action': 'IpReputationRulesListInfoAction'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'policyid': 'policyid',
        'type': 'type',
        'description': 'description',
        'tags': 'tags',
        'status': 'status',
        'action': 'action'
    }

    def __init__(self, name=None, id=None, policyid=None, type=None, description=None, tags=None, status=None, action=None):
        r"""IpReputationRulesListInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param id: **参数解释：** Rule ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param policyid: **参数解释：** Policy ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyid: str
        :param type: **参数解释：** 信誉类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param tags: **参数解释：** 信誉类型的IDC数据中心 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: list[str]
        :param status: **参数解释：** 规则状态，0：关闭，1：开启 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: int
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfoAction`
        """
        
        

        self._name = None
        self._id = None
        self._policyid = None
        self._type = None
        self._description = None
        self._tags = None
        self._status = None
        self._action = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if action is not None:
            self.action = action

    @property
    def name(self):
        r"""Gets the name of this IpReputationRulesListInfo.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this IpReputationRulesListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IpReputationRulesListInfo.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this IpReputationRulesListInfo.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this IpReputationRulesListInfo.

        **参数解释：** Rule ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this IpReputationRulesListInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IpReputationRulesListInfo.

        **参数解释：** Rule ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this IpReputationRulesListInfo.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this IpReputationRulesListInfo.

        **参数解释：** Policy ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyid of this IpReputationRulesListInfo.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this IpReputationRulesListInfo.

        **参数解释：** Policy ID. **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyid: The policyid of this IpReputationRulesListInfo.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def type(self):
        r"""Gets the type of this IpReputationRulesListInfo.

        **参数解释：** 信誉类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this IpReputationRulesListInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IpReputationRulesListInfo.

        **参数解释：** 信誉类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this IpReputationRulesListInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this IpReputationRulesListInfo.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this IpReputationRulesListInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IpReputationRulesListInfo.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this IpReputationRulesListInfo.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this IpReputationRulesListInfo.

        **参数解释：** 信誉类型的IDC数据中心 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this IpReputationRulesListInfo.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this IpReputationRulesListInfo.

        **参数解释：** 信誉类型的IDC数据中心 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this IpReputationRulesListInfo.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this IpReputationRulesListInfo.

        **参数解释：** 规则状态，0：关闭，1：开启 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this IpReputationRulesListInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IpReputationRulesListInfo.

        **参数解释：** 规则状态，0：关闭，1：开启 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this IpReputationRulesListInfo.
        :type status: int
        """
        self._status = status

    @property
    def action(self):
        r"""Gets the action of this IpReputationRulesListInfo.

        :return: The action of this IpReputationRulesListInfo.
        :rtype: :class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfoAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this IpReputationRulesListInfo.

        :param action: The action of this IpReputationRulesListInfo.
        :type action: :class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfoAction`
        """
        self._action = action

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
        if not isinstance(other, IpReputationRulesListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
