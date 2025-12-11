# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationNodeResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'str',
        'id': 'str',
        'urn': 'str',
        'name': 'str',
        'org_type': 'str',
        'delegated': 'bool'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'id': 'id',
        'urn': 'urn',
        'name': 'name',
        'org_type': 'org_type',
        'delegated': 'delegated'
    }

    def __init__(self, parent_id=None, id=None, urn=None, name=None, org_type=None, delegated=None):
        r"""OrganizationNodeResponseInfo

        The model defined in huaweicloud sdk

        :param parent_id: **参数解释** 当前组织节点的父节点唯一标识ID，用于标识组织树层级关系（根节点父ID通常为“0”或空）； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范 
        :type parent_id: str
        :param id: **参数解释** 组织树节点的唯一标识ID，用于唯一确定某个组织节点； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范（如UUID或数字组合） 
        :type id: str
        :param urn: **参数解释** 组织节点的统一资源名称（URN），用于跨服务唯一标识组织资源； **取值范围** 字符长度1-256位，格式为organizations::{management_account_id}:xxxxx:{org_id}/xxxxxxxx，符合平台URN命名规范 
        :type urn: str
        :param name: **参数解释** 组织节点的名称（可能是组织单元名称或账号名称，与org_type对应）； **取值范围** 字符长度1-64位，支持字母、数字、连字符、下划线及中文，不能以特殊字符开头或结尾 
        :type name: str
        :param org_type: **参数解释**: 节点（组织单元或账号）的类型； **取值范围**: unit（组织单元）、account（账号） 
        :type org_type: str
        :param delegated: **参数解释**: 标识组织节点（组织单元或账号）是否已完成授权； **取值范围**: true（已授权，无需重复授权）、false（未授权，需完成授权后使用） 
        :type delegated: bool
        """
        
        

        self._parent_id = None
        self._id = None
        self._urn = None
        self._name = None
        self._org_type = None
        self._delegated = None
        self.discriminator = None

        if parent_id is not None:
            self.parent_id = parent_id
        if id is not None:
            self.id = id
        if urn is not None:
            self.urn = urn
        if name is not None:
            self.name = name
        if org_type is not None:
            self.org_type = org_type
        if delegated is not None:
            self.delegated = delegated

    @property
    def parent_id(self):
        r"""Gets the parent_id of this OrganizationNodeResponseInfo.

        **参数解释** 当前组织节点的父节点唯一标识ID，用于标识组织树层级关系（根节点父ID通常为“0”或空）； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范 

        :return: The parent_id of this OrganizationNodeResponseInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this OrganizationNodeResponseInfo.

        **参数解释** 当前组织节点的父节点唯一标识ID，用于标识组织树层级关系（根节点父ID通常为“0”或空）； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范 

        :param parent_id: The parent_id of this OrganizationNodeResponseInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def id(self):
        r"""Gets the id of this OrganizationNodeResponseInfo.

        **参数解释** 组织树节点的唯一标识ID，用于唯一确定某个组织节点； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范（如UUID或数字组合） 

        :return: The id of this OrganizationNodeResponseInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OrganizationNodeResponseInfo.

        **参数解释** 组织树节点的唯一标识ID，用于唯一确定某个组织节点； **取值范围** 字符长度1-64位，符合平台组织节点ID命名规范（如UUID或数字组合） 

        :param id: The id of this OrganizationNodeResponseInfo.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this OrganizationNodeResponseInfo.

        **参数解释** 组织节点的统一资源名称（URN），用于跨服务唯一标识组织资源； **取值范围** 字符长度1-256位，格式为organizations::{management_account_id}:xxxxx:{org_id}/xxxxxxxx，符合平台URN命名规范 

        :return: The urn of this OrganizationNodeResponseInfo.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this OrganizationNodeResponseInfo.

        **参数解释** 组织节点的统一资源名称（URN），用于跨服务唯一标识组织资源； **取值范围** 字符长度1-256位，格式为organizations::{management_account_id}:xxxxx:{org_id}/xxxxxxxx，符合平台URN命名规范 

        :param urn: The urn of this OrganizationNodeResponseInfo.
        :type urn: str
        """
        self._urn = urn

    @property
    def name(self):
        r"""Gets the name of this OrganizationNodeResponseInfo.

        **参数解释** 组织节点的名称（可能是组织单元名称或账号名称，与org_type对应）； **取值范围** 字符长度1-64位，支持字母、数字、连字符、下划线及中文，不能以特殊字符开头或结尾 

        :return: The name of this OrganizationNodeResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OrganizationNodeResponseInfo.

        **参数解释** 组织节点的名称（可能是组织单元名称或账号名称，与org_type对应）； **取值范围** 字符长度1-64位，支持字母、数字、连字符、下划线及中文，不能以特殊字符开头或结尾 

        :param name: The name of this OrganizationNodeResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def org_type(self):
        r"""Gets the org_type of this OrganizationNodeResponseInfo.

        **参数解释**: 节点（组织单元或账号）的类型； **取值范围**: unit（组织单元）、account（账号） 

        :return: The org_type of this OrganizationNodeResponseInfo.
        :rtype: str
        """
        return self._org_type

    @org_type.setter
    def org_type(self, org_type):
        r"""Sets the org_type of this OrganizationNodeResponseInfo.

        **参数解释**: 节点（组织单元或账号）的类型； **取值范围**: unit（组织单元）、account（账号） 

        :param org_type: The org_type of this OrganizationNodeResponseInfo.
        :type org_type: str
        """
        self._org_type = org_type

    @property
    def delegated(self):
        r"""Gets the delegated of this OrganizationNodeResponseInfo.

        **参数解释**: 标识组织节点（组织单元或账号）是否已完成授权； **取值范围**: true（已授权，无需重复授权）、false（未授权，需完成授权后使用） 

        :return: The delegated of this OrganizationNodeResponseInfo.
        :rtype: bool
        """
        return self._delegated

    @delegated.setter
    def delegated(self, delegated):
        r"""Sets the delegated of this OrganizationNodeResponseInfo.

        **参数解释**: 标识组织节点（组织单元或账号）是否已完成授权； **取值范围**: true（已授权，无需重复授权）、false（未授权，需完成授权后使用） 

        :param delegated: The delegated of this OrganizationNodeResponseInfo.
        :type delegated: bool
        """
        self._delegated = delegated

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
        if not isinstance(other, OrganizationNodeResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
