# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpReputationRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'name': 'str',
        'policyname': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'type': 'str',
        'tags': 'list[str]',
        'action': 'CreateIpReputationRuleRequestBodyAction'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'name': 'name',
        'policyname': 'policyname',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'type': 'type',
        'tags': 'tags',
        'action': 'action'
    }

    def __init__(self, id=None, policyid=None, name=None, policyname=None, timestamp=None, description=None, status=None, type=None, tags=None, action=None):
        r"""CreateIpReputationRuleResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则ID，唯一标识该规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param policyid: **参数解释：** 所属防护策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyid: str
        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param policyname: **参数解释：** 所属策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyname: str
        :param timestamp: **参数解释：** 规则创建时间戳（毫秒级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type timestamp: int
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param status: **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: int
        :param type: **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        :param tags: **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: list[str]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
        """
        
        super(CreateIpReputationRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._name = None
        self._policyname = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._type = None
        self._tags = None
        self._action = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if name is not None:
            self.name = name
        if policyname is not None:
            self.policyname = policyname
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags
        if action is not None:
            self.action = action

    @property
    def id(self):
        r"""Gets the id of this CreateIpReputationRuleResponse.

        **参数解释：** 规则ID，唯一标识该规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateIpReputationRuleResponse.

        **参数解释：** 规则ID，唯一标识该规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this CreateIpReputationRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        r"""Gets the policyid of this CreateIpReputationRuleResponse.

        **参数解释：** 所属防护策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyid of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        r"""Sets the policyid of this CreateIpReputationRuleResponse.

        **参数解释：** 所属防护策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyid: The policyid of this CreateIpReputationRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def name(self):
        r"""Gets the name of this CreateIpReputationRuleResponse.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIpReputationRuleResponse.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this CreateIpReputationRuleResponse.
        :type name: str
        """
        self._name = name

    @property
    def policyname(self):
        r"""Gets the policyname of this CreateIpReputationRuleResponse.

        **参数解释：** 所属策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyname of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        r"""Sets the policyname of this CreateIpReputationRuleResponse.

        **参数解释：** 所属策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyname: The policyname of this CreateIpReputationRuleResponse.
        :type policyname: str
        """
        self._policyname = policyname

    @property
    def timestamp(self):
        r"""Gets the timestamp of this CreateIpReputationRuleResponse.

        **参数解释：** 规则创建时间戳（毫秒级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The timestamp of this CreateIpReputationRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this CreateIpReputationRuleResponse.

        **参数解释：** 规则创建时间戳（毫秒级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param timestamp: The timestamp of this CreateIpReputationRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        r"""Gets the description of this CreateIpReputationRuleResponse.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIpReputationRuleResponse.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateIpReputationRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateIpReputationRuleResponse.

        **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this CreateIpReputationRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateIpReputationRuleResponse.

        **参数解释：** 规则状态（1表示开启，0表示关闭） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this CreateIpReputationRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this CreateIpReputationRuleResponse.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this CreateIpReputationRuleResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateIpReputationRuleResponse.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this CreateIpReputationRuleResponse.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this CreateIpReputationRuleResponse.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this CreateIpReputationRuleResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateIpReputationRuleResponse.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this CreateIpReputationRuleResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def action(self):
        r"""Gets the action of this CreateIpReputationRuleResponse.

        :return: The action of this CreateIpReputationRuleResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateIpReputationRuleResponse.

        :param action: The action of this CreateIpReputationRuleResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.CreateIpReputationRuleRequestBodyAction`
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
        if not isinstance(other, CreateIpReputationRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
