# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogAttributeVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'qualified_name': 'str',
        'level': 'str',
        'name': 'str',
        'name_eng': 'str',
        'alias': 'str',
        'description': 'str',
        'data_owner': 'str',
        'owner': 'str',
        'data_owner_list': 'list[str]',
        'create_time': 'str',
        'create_by': 'str',
        'update_time': 'str',
        'update_by': 'str',
        'parent': 'CatalogAttributeVOParent',
        'parent_id': 'str',
        'l1': 'bool',
        'l2': 'bool',
        'l3': 'bool',
        'ordinal': 'int',
        'tenant_id': 'str',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'path': 'path',
        'qualified_name': 'qualifiedName',
        'level': 'level',
        'name': 'name',
        'name_eng': 'nameEng',
        'alias': 'alias',
        'description': 'description',
        'data_owner': 'dataOwner',
        'owner': 'owner',
        'data_owner_list': 'dataOwnerList',
        'create_time': 'createTime',
        'create_by': 'createBy',
        'update_time': 'updateTime',
        'update_by': 'updateBy',
        'parent': 'parent',
        'parent_id': 'parentId',
        'l1': 'l1',
        'l2': 'l2',
        'l3': 'l3',
        'ordinal': 'ordinal',
        'tenant_id': 'tenantId',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, path=None, qualified_name=None, level=None, name=None, name_eng=None, alias=None, description=None, data_owner=None, owner=None, data_owner_list=None, create_time=None, create_by=None, update_time=None, update_by=None, parent=None, parent_id=None, l1=None, l2=None, l3=None, ordinal=None, tenant_id=None, self_defined_fields=None):
        """CatalogAttributeVO

        The model defined in huaweicloud sdk

        :param path: 路径
        :type path: str
        :param qualified_name: 名称
        :type qualified_name: str
        :param level: 主题所属层级
        :type level: str
        :param name: 名称
        :type name: str
        :param name_eng: 英文名称
        :type name_eng: str
        :param alias: 别名
        :type alias: str
        :param description: 描述
        :type description: str
        :param data_owner: 数据主体
        :type data_owner: str
        :param owner: 责任人
        :type owner: str
        :param data_owner_list: 数据主体列表
        :type data_owner_list: list[str]
        :param create_time: 创建时间，时间戳
        :type create_time: str
        :param create_by: 创建人
        :type create_by: str
        :param update_time: 更新时间，时间戳
        :type update_time: str
        :param update_by: 更新人
        :type update_by: str
        :param parent: 
        :type parent: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVOParent`
        :param parent_id: 父节点ID
        :type parent_id: str
        :param l1: 是否为L1层
        :type l1: bool
        :param l2: 是否为L2层
        :type l2: bool
        :param l3: 是否为L3层
        :type l3: bool
        :param ordinal: 顺序编号
        :type ordinal: int
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param self_defined_fields: 自定义项
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._path = None
        self._qualified_name = None
        self._level = None
        self._name = None
        self._name_eng = None
        self._alias = None
        self._description = None
        self._data_owner = None
        self._owner = None
        self._data_owner_list = None
        self._create_time = None
        self._create_by = None
        self._update_time = None
        self._update_by = None
        self._parent = None
        self._parent_id = None
        self._l1 = None
        self._l2 = None
        self._l3 = None
        self._ordinal = None
        self._tenant_id = None
        self._self_defined_fields = None
        self.discriminator = None

        self.path = path
        self.qualified_name = qualified_name
        self.level = level
        self.name = name
        self.name_eng = name_eng
        if alias is not None:
            self.alias = alias
        self.description = description
        self.data_owner = data_owner
        if owner is not None:
            self.owner = owner
        self.data_owner_list = data_owner_list
        if create_time is not None:
            self.create_time = create_time
        if create_by is not None:
            self.create_by = create_by
        if update_time is not None:
            self.update_time = update_time
        if update_by is not None:
            self.update_by = update_by
        if parent is not None:
            self.parent = parent
        if parent_id is not None:
            self.parent_id = parent_id
        if l1 is not None:
            self.l1 = l1
        if l2 is not None:
            self.l2 = l2
        if l3 is not None:
            self.l3 = l3
        if ordinal is not None:
            self.ordinal = ordinal
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields

    @property
    def path(self):
        """Gets the path of this CatalogAttributeVO.

        路径

        :return: The path of this CatalogAttributeVO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this CatalogAttributeVO.

        路径

        :param path: The path of this CatalogAttributeVO.
        :type path: str
        """
        self._path = path

    @property
    def qualified_name(self):
        """Gets the qualified_name of this CatalogAttributeVO.

        名称

        :return: The qualified_name of this CatalogAttributeVO.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this CatalogAttributeVO.

        名称

        :param qualified_name: The qualified_name of this CatalogAttributeVO.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def level(self):
        """Gets the level of this CatalogAttributeVO.

        主题所属层级

        :return: The level of this CatalogAttributeVO.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CatalogAttributeVO.

        主题所属层级

        :param level: The level of this CatalogAttributeVO.
        :type level: str
        """
        self._level = level

    @property
    def name(self):
        """Gets the name of this CatalogAttributeVO.

        名称

        :return: The name of this CatalogAttributeVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CatalogAttributeVO.

        名称

        :param name: The name of this CatalogAttributeVO.
        :type name: str
        """
        self._name = name

    @property
    def name_eng(self):
        """Gets the name_eng of this CatalogAttributeVO.

        英文名称

        :return: The name_eng of this CatalogAttributeVO.
        :rtype: str
        """
        return self._name_eng

    @name_eng.setter
    def name_eng(self, name_eng):
        """Sets the name_eng of this CatalogAttributeVO.

        英文名称

        :param name_eng: The name_eng of this CatalogAttributeVO.
        :type name_eng: str
        """
        self._name_eng = name_eng

    @property
    def alias(self):
        """Gets the alias of this CatalogAttributeVO.

        别名

        :return: The alias of this CatalogAttributeVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CatalogAttributeVO.

        别名

        :param alias: The alias of this CatalogAttributeVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def description(self):
        """Gets the description of this CatalogAttributeVO.

        描述

        :return: The description of this CatalogAttributeVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CatalogAttributeVO.

        描述

        :param description: The description of this CatalogAttributeVO.
        :type description: str
        """
        self._description = description

    @property
    def data_owner(self):
        """Gets the data_owner of this CatalogAttributeVO.

        数据主体

        :return: The data_owner of this CatalogAttributeVO.
        :rtype: str
        """
        return self._data_owner

    @data_owner.setter
    def data_owner(self, data_owner):
        """Sets the data_owner of this CatalogAttributeVO.

        数据主体

        :param data_owner: The data_owner of this CatalogAttributeVO.
        :type data_owner: str
        """
        self._data_owner = data_owner

    @property
    def owner(self):
        """Gets the owner of this CatalogAttributeVO.

        责任人

        :return: The owner of this CatalogAttributeVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CatalogAttributeVO.

        责任人

        :param owner: The owner of this CatalogAttributeVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def data_owner_list(self):
        """Gets the data_owner_list of this CatalogAttributeVO.

        数据主体列表

        :return: The data_owner_list of this CatalogAttributeVO.
        :rtype: list[str]
        """
        return self._data_owner_list

    @data_owner_list.setter
    def data_owner_list(self, data_owner_list):
        """Sets the data_owner_list of this CatalogAttributeVO.

        数据主体列表

        :param data_owner_list: The data_owner_list of this CatalogAttributeVO.
        :type data_owner_list: list[str]
        """
        self._data_owner_list = data_owner_list

    @property
    def create_time(self):
        """Gets the create_time of this CatalogAttributeVO.

        创建时间，时间戳

        :return: The create_time of this CatalogAttributeVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CatalogAttributeVO.

        创建时间，时间戳

        :param create_time: The create_time of this CatalogAttributeVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_by(self):
        """Gets the create_by of this CatalogAttributeVO.

        创建人

        :return: The create_by of this CatalogAttributeVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this CatalogAttributeVO.

        创建人

        :param create_by: The create_by of this CatalogAttributeVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_time(self):
        """Gets the update_time of this CatalogAttributeVO.

        更新时间，时间戳

        :return: The update_time of this CatalogAttributeVO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CatalogAttributeVO.

        更新时间，时间戳

        :param update_time: The update_time of this CatalogAttributeVO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_by(self):
        """Gets the update_by of this CatalogAttributeVO.

        更新人

        :return: The update_by of this CatalogAttributeVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this CatalogAttributeVO.

        更新人

        :param update_by: The update_by of this CatalogAttributeVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def parent(self):
        """Gets the parent of this CatalogAttributeVO.

        :return: The parent of this CatalogAttributeVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVOParent`
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this CatalogAttributeVO.

        :param parent: The parent of this CatalogAttributeVO.
        :type parent: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVOParent`
        """
        self._parent = parent

    @property
    def parent_id(self):
        """Gets the parent_id of this CatalogAttributeVO.

        父节点ID

        :return: The parent_id of this CatalogAttributeVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CatalogAttributeVO.

        父节点ID

        :param parent_id: The parent_id of this CatalogAttributeVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def l1(self):
        """Gets the l1 of this CatalogAttributeVO.

        是否为L1层

        :return: The l1 of this CatalogAttributeVO.
        :rtype: bool
        """
        return self._l1

    @l1.setter
    def l1(self, l1):
        """Sets the l1 of this CatalogAttributeVO.

        是否为L1层

        :param l1: The l1 of this CatalogAttributeVO.
        :type l1: bool
        """
        self._l1 = l1

    @property
    def l2(self):
        """Gets the l2 of this CatalogAttributeVO.

        是否为L2层

        :return: The l2 of this CatalogAttributeVO.
        :rtype: bool
        """
        return self._l2

    @l2.setter
    def l2(self, l2):
        """Sets the l2 of this CatalogAttributeVO.

        是否为L2层

        :param l2: The l2 of this CatalogAttributeVO.
        :type l2: bool
        """
        self._l2 = l2

    @property
    def l3(self):
        """Gets the l3 of this CatalogAttributeVO.

        是否为L3层

        :return: The l3 of this CatalogAttributeVO.
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this CatalogAttributeVO.

        是否为L3层

        :param l3: The l3 of this CatalogAttributeVO.
        :type l3: bool
        """
        self._l3 = l3

    @property
    def ordinal(self):
        """Gets the ordinal of this CatalogAttributeVO.

        顺序编号

        :return: The ordinal of this CatalogAttributeVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this CatalogAttributeVO.

        顺序编号

        :param ordinal: The ordinal of this CatalogAttributeVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CatalogAttributeVO.

        租户ID

        :return: The tenant_id of this CatalogAttributeVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CatalogAttributeVO.

        租户ID

        :param tenant_id: The tenant_id of this CatalogAttributeVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def self_defined_fields(self):
        """Gets the self_defined_fields of this CatalogAttributeVO.

        自定义项

        :return: The self_defined_fields of this CatalogAttributeVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        """Sets the self_defined_fields of this CatalogAttributeVO.

        自定义项

        :param self_defined_fields: The self_defined_fields of this CatalogAttributeVO.
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        self._self_defined_fields = self_defined_fields

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
        if not isinstance(other, CatalogAttributeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
