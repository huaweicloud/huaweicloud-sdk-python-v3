# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupProtectedBranchApiDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'actions': 'list[ProjectProtectedActionResultApiDto]',
        'namespace_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'actions': 'actions',
        'namespace_id': 'namespace_id'
    }

    def __init__(self, id=None, name=None, actions=None, namespace_id=None):
        r"""GroupProtectedBranchApiDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 保护分支唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: int
        :param name: **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。 **约束限制：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param actions: **参数解释：** 事件列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultApiDto`]
        :param namespace_id: **参数解释：** 代码组id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type namespace_id: int
        """
        
        

        self._id = None
        self._name = None
        self._actions = None
        self._namespace_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if actions is not None:
            self.actions = actions
        if namespace_id is not None:
            self.namespace_id = namespace_id

    @property
    def id(self):
        r"""Gets the id of this GroupProtectedBranchApiDto.

        **参数解释：** 保护分支唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this GroupProtectedBranchApiDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupProtectedBranchApiDto.

        **参数解释：** 保护分支唯一标识。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this GroupProtectedBranchApiDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupProtectedBranchApiDto.

        **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。 **约束限制：** 不涉及 **默认取值：** 不涉及

        :return: The name of this GroupProtectedBranchApiDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupProtectedBranchApiDto.

        **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。 **约束限制：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this GroupProtectedBranchApiDto.
        :type name: str
        """
        self._name = name

    @property
    def actions(self):
        r"""Gets the actions of this GroupProtectedBranchApiDto.

        **参数解释：** 事件列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The actions of this GroupProtectedBranchApiDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultApiDto`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this GroupProtectedBranchApiDto.

        **参数解释：** 事件列表。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param actions: The actions of this GroupProtectedBranchApiDto.
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultApiDto`]
        """
        self._actions = actions

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this GroupProtectedBranchApiDto.

        **参数解释：** 代码组id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The namespace_id of this GroupProtectedBranchApiDto.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this GroupProtectedBranchApiDto.

        **参数解释：** 代码组id。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param namespace_id: The namespace_id of this GroupProtectedBranchApiDto.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

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
        if not isinstance(other, GroupProtectedBranchApiDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
