# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseCategory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'created_by': 'str',
        'created_date': 'str',
        'code': 'str',
        'prefix': 'str',
        'domain_id': 'str',
        'icon': 'str',
        'color': 'str',
        'description': 'str',
        'definition_type': 'int',
        'type_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'code': 'code',
        'prefix': 'prefix',
        'domain_id': 'domain_id',
        'icon': 'icon',
        'color': 'color',
        'description': 'description',
        'definition_type': 'definition_type',
        'type_id': 'type_id'
    }

    def __init__(self, tenant_id=None, modified_by=None, modified_date=None, created_by=None, created_date=None, code=None, prefix=None, domain_id=None, icon=None, color=None, description=None, definition_type=None, type_id=None):
        r"""BaseCategory

        The model defined in huaweicloud sdk

        :param tenant_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param modified_by: **参数解释**： 修改人。 **取值范围**： 不涉及。
        :type modified_by: str
        :param modified_date: **参数解释**： 修改时间。 **取值范围**： 不涉及。
        :type modified_date: str
        :param created_by: **参数解释**： 创建人。 **取值范围**： 不涉及。
        :type created_by: str
        :param created_date: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created_date: str
        :param code: **参数解释**： 对象类型编码。 **取值范围**： 不涉及。
        :type code: str
        :param prefix: **参数解释**： 编号前缀。 **取值范围**： 不涉及。
        :type prefix: str
        :param domain_id: **参数解释**： 租户下项目空间唯一标识ID。 **取值范围**： - -1：自定义工作项类型 - 0：预设工作项模型
        :type domain_id: str
        :param icon: **参数解释**： 图标。 **取值范围**： 不涉及。
        :type icon: str
        :param color: **参数解释**： 颜色。 **取值范围**： 不涉及。
        :type color: str
        :param description: **参数解释**： 描述信息。 **取值范围**： 不涉及。
        :type description: str
        :param definition_type: **参数解释**： 定义类型。 **取值范围**： - 1~3 系统级别 - 4 租户级别
        :type definition_type: int
        :param type_id: **参数解释**： 类别ID。 **取值范围**： 不涉及。
        :type type_id: str
        """
        
        

        self._tenant_id = None
        self._modified_by = None
        self._modified_date = None
        self._created_by = None
        self._created_date = None
        self._code = None
        self._prefix = None
        self._domain_id = None
        self._icon = None
        self._color = None
        self._description = None
        self._definition_type = None
        self._type_id = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if code is not None:
            self.code = code
        if prefix is not None:
            self.prefix = prefix
        if domain_id is not None:
            self.domain_id = domain_id
        if icon is not None:
            self.icon = icon
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if definition_type is not None:
            self.definition_type = definition_type
        if type_id is not None:
            self.type_id = type_id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this BaseCategory.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The tenant_id of this BaseCategory.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this BaseCategory.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this BaseCategory.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this BaseCategory.

        **参数解释**： 修改人。 **取值范围**： 不涉及。

        :return: The modified_by of this BaseCategory.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this BaseCategory.

        **参数解释**： 修改人。 **取值范围**： 不涉及。

        :param modified_by: The modified_by of this BaseCategory.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this BaseCategory.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。

        :return: The modified_date of this BaseCategory.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this BaseCategory.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。

        :param modified_date: The modified_date of this BaseCategory.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this BaseCategory.

        **参数解释**： 创建人。 **取值范围**： 不涉及。

        :return: The created_by of this BaseCategory.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this BaseCategory.

        **参数解释**： 创建人。 **取值范围**： 不涉及。

        :param created_by: The created_by of this BaseCategory.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this BaseCategory.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created_date of this BaseCategory.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this BaseCategory.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created_date: The created_date of this BaseCategory.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def code(self):
        r"""Gets the code of this BaseCategory.

        **参数解释**： 对象类型编码。 **取值范围**： 不涉及。

        :return: The code of this BaseCategory.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this BaseCategory.

        **参数解释**： 对象类型编码。 **取值范围**： 不涉及。

        :param code: The code of this BaseCategory.
        :type code: str
        """
        self._code = code

    @property
    def prefix(self):
        r"""Gets the prefix of this BaseCategory.

        **参数解释**： 编号前缀。 **取值范围**： 不涉及。

        :return: The prefix of this BaseCategory.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this BaseCategory.

        **参数解释**： 编号前缀。 **取值范围**： 不涉及。

        :param prefix: The prefix of this BaseCategory.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BaseCategory.

        **参数解释**： 租户下项目空间唯一标识ID。 **取值范围**： - -1：自定义工作项类型 - 0：预设工作项模型

        :return: The domain_id of this BaseCategory.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BaseCategory.

        **参数解释**： 租户下项目空间唯一标识ID。 **取值范围**： - -1：自定义工作项类型 - 0：预设工作项模型

        :param domain_id: The domain_id of this BaseCategory.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def icon(self):
        r"""Gets the icon of this BaseCategory.

        **参数解释**： 图标。 **取值范围**： 不涉及。

        :return: The icon of this BaseCategory.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this BaseCategory.

        **参数解释**： 图标。 **取值范围**： 不涉及。

        :param icon: The icon of this BaseCategory.
        :type icon: str
        """
        self._icon = icon

    @property
    def color(self):
        r"""Gets the color of this BaseCategory.

        **参数解释**： 颜色。 **取值范围**： 不涉及。

        :return: The color of this BaseCategory.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this BaseCategory.

        **参数解释**： 颜色。 **取值范围**： 不涉及。

        :param color: The color of this BaseCategory.
        :type color: str
        """
        self._color = color

    @property
    def description(self):
        r"""Gets the description of this BaseCategory.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :return: The description of this BaseCategory.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BaseCategory.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :param description: The description of this BaseCategory.
        :type description: str
        """
        self._description = description

    @property
    def definition_type(self):
        r"""Gets the definition_type of this BaseCategory.

        **参数解释**： 定义类型。 **取值范围**： - 1~3 系统级别 - 4 租户级别

        :return: The definition_type of this BaseCategory.
        :rtype: int
        """
        return self._definition_type

    @definition_type.setter
    def definition_type(self, definition_type):
        r"""Sets the definition_type of this BaseCategory.

        **参数解释**： 定义类型。 **取值范围**： - 1~3 系统级别 - 4 租户级别

        :param definition_type: The definition_type of this BaseCategory.
        :type definition_type: int
        """
        self._definition_type = definition_type

    @property
    def type_id(self):
        r"""Gets the type_id of this BaseCategory.

        **参数解释**： 类别ID。 **取值范围**： 不涉及。

        :return: The type_id of this BaseCategory.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        r"""Sets the type_id of this BaseCategory.

        **参数解释**： 类别ID。 **取值范围**： 不涉及。

        :param type_id: The type_id of this BaseCategory.
        :type type_id: str
        """
        self._type_id = type_id

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
        if not isinstance(other, BaseCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
