# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationAccountInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delegated': 'bool',
        'id': 'str',
        'name': 'str',
        'org_type': 'str',
        'parent_id': 'str',
        'urn': 'str'
    }

    attribute_map = {
        'delegated': 'delegated',
        'id': 'id',
        'name': 'name',
        'org_type': 'org_type',
        'parent_id': 'parent_id',
        'urn': 'urn'
    }

    def __init__(self, delegated=None, id=None, name=None, org_type=None, parent_id=None, urn=None):
        r"""OrganizationAccountInfo

        The model defined in huaweicloud sdk

        :param delegated: **参数解释**： 是否已添加 **取值范围**： 不涉及
        :type delegated: bool
        :param id: **参数解释**： 账号的唯一标识符 **取值范围**： 不涉及
        :type id: str
        :param name: **参数解释**： 账号名称 **取值范围**： 不涉及
        :type name: str
        :param org_type: **参数解释**： 组织节点类型 **取值范围**： account
        :type org_type: str
        :param parent_id: **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **取值范围**： 不涉及
        :type parent_id: str
        :param urn: **参数解释**： 账号的统一资源名称 **取值范围**： 不涉及
        :type urn: str
        """
        
        

        self._delegated = None
        self._id = None
        self._name = None
        self._org_type = None
        self._parent_id = None
        self._urn = None
        self.discriminator = None

        if delegated is not None:
            self.delegated = delegated
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if org_type is not None:
            self.org_type = org_type
        if parent_id is not None:
            self.parent_id = parent_id
        if urn is not None:
            self.urn = urn

    @property
    def delegated(self):
        r"""Gets the delegated of this OrganizationAccountInfo.

        **参数解释**： 是否已添加 **取值范围**： 不涉及

        :return: The delegated of this OrganizationAccountInfo.
        :rtype: bool
        """
        return self._delegated

    @delegated.setter
    def delegated(self, delegated):
        r"""Sets the delegated of this OrganizationAccountInfo.

        **参数解释**： 是否已添加 **取值范围**： 不涉及

        :param delegated: The delegated of this OrganizationAccountInfo.
        :type delegated: bool
        """
        self._delegated = delegated

    @property
    def id(self):
        r"""Gets the id of this OrganizationAccountInfo.

        **参数解释**： 账号的唯一标识符 **取值范围**： 不涉及

        :return: The id of this OrganizationAccountInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OrganizationAccountInfo.

        **参数解释**： 账号的唯一标识符 **取值范围**： 不涉及

        :param id: The id of this OrganizationAccountInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OrganizationAccountInfo.

        **参数解释**： 账号名称 **取值范围**： 不涉及

        :return: The name of this OrganizationAccountInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OrganizationAccountInfo.

        **参数解释**： 账号名称 **取值范围**： 不涉及

        :param name: The name of this OrganizationAccountInfo.
        :type name: str
        """
        self._name = name

    @property
    def org_type(self):
        r"""Gets the org_type of this OrganizationAccountInfo.

        **参数解释**： 组织节点类型 **取值范围**： account

        :return: The org_type of this OrganizationAccountInfo.
        :rtype: str
        """
        return self._org_type

    @org_type.setter
    def org_type(self, org_type):
        r"""Sets the org_type of this OrganizationAccountInfo.

        **参数解释**： 组织节点类型 **取值范围**： account

        :param org_type: The org_type of this OrganizationAccountInfo.
        :type org_type: str
        """
        self._org_type = org_type

    @property
    def parent_id(self):
        r"""Gets the parent_id of this OrganizationAccountInfo.

        **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **取值范围**： 不涉及

        :return: The parent_id of this OrganizationAccountInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this OrganizationAccountInfo.

        **参数解释**： 父节点（根或组织单元）的唯一标识符（ID） **取值范围**： 不涉及

        :param parent_id: The parent_id of this OrganizationAccountInfo.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def urn(self):
        r"""Gets the urn of this OrganizationAccountInfo.

        **参数解释**： 账号的统一资源名称 **取值范围**： 不涉及

        :return: The urn of this OrganizationAccountInfo.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this OrganizationAccountInfo.

        **参数解释**： 账号的统一资源名称 **取值范围**： 不涉及

        :param urn: The urn of this OrganizationAccountInfo.
        :type urn: str
        """
        self._urn = urn

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
        if not isinstance(other, OrganizationAccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
