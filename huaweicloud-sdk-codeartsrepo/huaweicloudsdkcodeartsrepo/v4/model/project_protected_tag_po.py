# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectProtectedTagPo:

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
        'source': 'str',
        'project_id': 'str',
        'updated_at': 'str',
        'name': 'str',
        'actions': 'list[ProjectProtectedActionResultDto]'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'project_id': 'project_id',
        'updated_at': 'updated_at',
        'name': 'name',
        'actions': 'actions'
    }

    def __init__(self, id=None, source=None, project_id=None, updated_at=None, name=None, actions=None):
        r"""ProjectProtectedTagPo

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 保护分支唯一标识。
        :type id: int
        :param source: **参数解释：** 来源。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type source: str
        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        :param name: **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param actions: **参数解释：** 事件列表。
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultDto`]
        """
        
        

        self._id = None
        self._source = None
        self._project_id = None
        self._updated_at = None
        self._name = None
        self._actions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source is not None:
            self.source = source
        if project_id is not None:
            self.project_id = project_id
        if updated_at is not None:
            self.updated_at = updated_at
        if name is not None:
            self.name = name
        if actions is not None:
            self.actions = actions

    @property
    def id(self):
        r"""Gets the id of this ProjectProtectedTagPo.

        **参数解释：** 保护分支唯一标识。

        :return: The id of this ProjectProtectedTagPo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectProtectedTagPo.

        **参数解释：** 保护分支唯一标识。

        :param id: The id of this ProjectProtectedTagPo.
        :type id: int
        """
        self._id = id

    @property
    def source(self):
        r"""Gets the source of this ProjectProtectedTagPo.

        **参数解释：** 来源。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The source of this ProjectProtectedTagPo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ProjectProtectedTagPo.

        **参数解释：** 来源。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param source: The source of this ProjectProtectedTagPo.
        :type source: str
        """
        self._source = source

    @property
    def project_id(self):
        r"""Gets the project_id of this ProjectProtectedTagPo.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this ProjectProtectedTagPo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProjectProtectedTagPo.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this ProjectProtectedTagPo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ProjectProtectedTagPo.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this ProjectProtectedTagPo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ProjectProtectedTagPo.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this ProjectProtectedTagPo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def name(self):
        r"""Gets the name of this ProjectProtectedTagPo.

        **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this ProjectProtectedTagPo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectProtectedTagPo.

        **参数解释：** 保护分支名称 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this ProjectProtectedTagPo.
        :type name: str
        """
        self._name = name

    @property
    def actions(self):
        r"""Gets the actions of this ProjectProtectedTagPo.

        **参数解释：** 事件列表。

        :return: The actions of this ProjectProtectedTagPo.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultDto`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ProjectProtectedTagPo.

        **参数解释：** 事件列表。

        :param actions: The actions of this ProjectProtectedTagPo.
        :type actions: list[:class:`huaweicloudsdkcodeartsrepo.v4.ProjectProtectedActionResultDto`]
        """
        self._actions = actions

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
        if not isinstance(other, ProjectProtectedTagPo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
