# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_ch': 'str',
        'name_en': 'str',
        'description': 'str',
        'qualified_name': 'str',
        'guid': 'str',
        'code': 'str',
        'alias': 'str',
        'status': 'BizStatusEnum',
        'new_biz': 'BizVersionManageVO',
        'data_owner': 'str',
        'data_owner_list': 'str',
        'data_department': 'str',
        'path': 'str',
        'level': 'int',
        'ordinal': 'int',
        'owner': 'str',
        'parent_id': 'str',
        'swap_order_id': 'str',
        'id': 'str',
        'qualified_id': 'str',
        'from_public': 'bool',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'children_num': 'int',
        'children': 'list[CatalogVO]',
        'self_defined_fields': 'list[SelfDefinedFieldVO]'
    }

    attribute_map = {
        'name_ch': 'name_ch',
        'name_en': 'name_en',
        'description': 'description',
        'qualified_name': 'qualified_name',
        'guid': 'guid',
        'code': 'code',
        'alias': 'alias',
        'status': 'status',
        'new_biz': 'new_biz',
        'data_owner': 'data_owner',
        'data_owner_list': 'data_owner_list',
        'data_department': 'data_department',
        'path': 'path',
        'level': 'level',
        'ordinal': 'ordinal',
        'owner': 'owner',
        'parent_id': 'parent_id',
        'swap_order_id': 'swap_order_id',
        'id': 'id',
        'qualified_id': 'qualified_id',
        'from_public': 'from_public',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'children_num': 'children_num',
        'children': 'children',
        'self_defined_fields': 'self_defined_fields'
    }

    def __init__(self, name_ch=None, name_en=None, description=None, qualified_name=None, guid=None, code=None, alias=None, status=None, new_biz=None, data_owner=None, data_owner_list=None, data_department=None, path=None, level=None, ordinal=None, owner=None, parent_id=None, swap_order_id=None, id=None, qualified_id=None, from_public=None, create_by=None, update_by=None, create_time=None, update_time=None, children_num=None, children=None, self_defined_fields=None):
        r"""CatalogVO

        The model defined in huaweicloud sdk

        :param name_ch: 中文名称。
        :type name_ch: str
        :param name_en: 英文名称。
        :type name_en: str
        :param description: 描述信息。
        :type description: str
        :param qualified_name: 扩展名。
        :type qualified_name: str
        :param guid: guid，自动生成。
        :type guid: str
        :param code: 编码。
        :type code: str
        :param alias: 别名。
        :type alias: str
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        :param new_biz: 
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        :param data_owner: 数据所有者。
        :type data_owner: str
        :param data_owner_list: 数据所有者集合。
        :type data_owner_list: str
        :param data_department: 数据域。
        :type data_department: str
        :param path: 路径信息。
        :type path: str
        :param level: 层级信息。
        :type level: int
        :param ordinal: 序号。
        :type ordinal: int
        :param owner: 责任人。
        :type owner: str
        :param parent_id: 父目录ID，木有则为根目录，ID字符串。
        :type parent_id: str
        :param swap_order_id: 同层排序，目标节点的ID，ID字符串。
        :type swap_order_id: str
        :param id: 主题ID，ID字符串。
        :type id: str
        :param qualified_id: 认证ID，自动生成。
        :type qualified_id: str
        :param from_public: 是否来自公共层。
        :type from_public: bool
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param children_num: 拥有子流程的数量，不包括子流程的子流程，前端不传。
        :type children_num: int
        :param children: 下层子目录，只读。
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogVO`]
        :param self_defined_fields: 属性自定义项。
        :type self_defined_fields: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        
        

        self._name_ch = None
        self._name_en = None
        self._description = None
        self._qualified_name = None
        self._guid = None
        self._code = None
        self._alias = None
        self._status = None
        self._new_biz = None
        self._data_owner = None
        self._data_owner_list = None
        self._data_department = None
        self._path = None
        self._level = None
        self._ordinal = None
        self._owner = None
        self._parent_id = None
        self._swap_order_id = None
        self._id = None
        self._qualified_id = None
        self._from_public = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self._children_num = None
        self._children = None
        self._self_defined_fields = None
        self.discriminator = None

        if name_ch is not None:
            self.name_ch = name_ch
        if name_en is not None:
            self.name_en = name_en
        if description is not None:
            self.description = description
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if guid is not None:
            self.guid = guid
        if code is not None:
            self.code = code
        if alias is not None:
            self.alias = alias
        if status is not None:
            self.status = status
        if new_biz is not None:
            self.new_biz = new_biz
        if data_owner is not None:
            self.data_owner = data_owner
        if data_owner_list is not None:
            self.data_owner_list = data_owner_list
        if data_department is not None:
            self.data_department = data_department
        if path is not None:
            self.path = path
        if level is not None:
            self.level = level
        if ordinal is not None:
            self.ordinal = ordinal
        if owner is not None:
            self.owner = owner
        if parent_id is not None:
            self.parent_id = parent_id
        if swap_order_id is not None:
            self.swap_order_id = swap_order_id
        if id is not None:
            self.id = id
        if qualified_id is not None:
            self.qualified_id = qualified_id
        if from_public is not None:
            self.from_public = from_public
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if children_num is not None:
            self.children_num = children_num
        if children is not None:
            self.children = children
        if self_defined_fields is not None:
            self.self_defined_fields = self_defined_fields

    @property
    def name_ch(self):
        r"""Gets the name_ch of this CatalogVO.

        中文名称。

        :return: The name_ch of this CatalogVO.
        :rtype: str
        """
        return self._name_ch

    @name_ch.setter
    def name_ch(self, name_ch):
        r"""Sets the name_ch of this CatalogVO.

        中文名称。

        :param name_ch: The name_ch of this CatalogVO.
        :type name_ch: str
        """
        self._name_ch = name_ch

    @property
    def name_en(self):
        r"""Gets the name_en of this CatalogVO.

        英文名称。

        :return: The name_en of this CatalogVO.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this CatalogVO.

        英文名称。

        :param name_en: The name_en of this CatalogVO.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def description(self):
        r"""Gets the description of this CatalogVO.

        描述信息。

        :return: The description of this CatalogVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CatalogVO.

        描述信息。

        :param description: The description of this CatalogVO.
        :type description: str
        """
        self._description = description

    @property
    def qualified_name(self):
        r"""Gets the qualified_name of this CatalogVO.

        扩展名。

        :return: The qualified_name of this CatalogVO.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        r"""Sets the qualified_name of this CatalogVO.

        扩展名。

        :param qualified_name: The qualified_name of this CatalogVO.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def guid(self):
        r"""Gets the guid of this CatalogVO.

        guid，自动生成。

        :return: The guid of this CatalogVO.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this CatalogVO.

        guid，自动生成。

        :param guid: The guid of this CatalogVO.
        :type guid: str
        """
        self._guid = guid

    @property
    def code(self):
        r"""Gets the code of this CatalogVO.

        编码。

        :return: The code of this CatalogVO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CatalogVO.

        编码。

        :param code: The code of this CatalogVO.
        :type code: str
        """
        self._code = code

    @property
    def alias(self):
        r"""Gets the alias of this CatalogVO.

        别名。

        :return: The alias of this CatalogVO.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this CatalogVO.

        别名。

        :param alias: The alias of this CatalogVO.
        :type alias: str
        """
        self._alias = alias

    @property
    def status(self):
        r"""Gets the status of this CatalogVO.

        :return: The status of this CatalogVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CatalogVO.

        :param status: The status of this CatalogVO.
        :type status: :class:`huaweicloudsdkdataartsstudio.v1.BizStatusEnum`
        """
        self._status = status

    @property
    def new_biz(self):
        r"""Gets the new_biz of this CatalogVO.

        :return: The new_biz of this CatalogVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        return self._new_biz

    @new_biz.setter
    def new_biz(self, new_biz):
        r"""Sets the new_biz of this CatalogVO.

        :param new_biz: The new_biz of this CatalogVO.
        :type new_biz: :class:`huaweicloudsdkdataartsstudio.v1.BizVersionManageVO`
        """
        self._new_biz = new_biz

    @property
    def data_owner(self):
        r"""Gets the data_owner of this CatalogVO.

        数据所有者。

        :return: The data_owner of this CatalogVO.
        :rtype: str
        """
        return self._data_owner

    @data_owner.setter
    def data_owner(self, data_owner):
        r"""Sets the data_owner of this CatalogVO.

        数据所有者。

        :param data_owner: The data_owner of this CatalogVO.
        :type data_owner: str
        """
        self._data_owner = data_owner

    @property
    def data_owner_list(self):
        r"""Gets the data_owner_list of this CatalogVO.

        数据所有者集合。

        :return: The data_owner_list of this CatalogVO.
        :rtype: str
        """
        return self._data_owner_list

    @data_owner_list.setter
    def data_owner_list(self, data_owner_list):
        r"""Sets the data_owner_list of this CatalogVO.

        数据所有者集合。

        :param data_owner_list: The data_owner_list of this CatalogVO.
        :type data_owner_list: str
        """
        self._data_owner_list = data_owner_list

    @property
    def data_department(self):
        r"""Gets the data_department of this CatalogVO.

        数据域。

        :return: The data_department of this CatalogVO.
        :rtype: str
        """
        return self._data_department

    @data_department.setter
    def data_department(self, data_department):
        r"""Sets the data_department of this CatalogVO.

        数据域。

        :param data_department: The data_department of this CatalogVO.
        :type data_department: str
        """
        self._data_department = data_department

    @property
    def path(self):
        r"""Gets the path of this CatalogVO.

        路径信息。

        :return: The path of this CatalogVO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this CatalogVO.

        路径信息。

        :param path: The path of this CatalogVO.
        :type path: str
        """
        self._path = path

    @property
    def level(self):
        r"""Gets the level of this CatalogVO.

        层级信息。

        :return: The level of this CatalogVO.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this CatalogVO.

        层级信息。

        :param level: The level of this CatalogVO.
        :type level: int
        """
        self._level = level

    @property
    def ordinal(self):
        r"""Gets the ordinal of this CatalogVO.

        序号。

        :return: The ordinal of this CatalogVO.
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        r"""Sets the ordinal of this CatalogVO.

        序号。

        :param ordinal: The ordinal of this CatalogVO.
        :type ordinal: int
        """
        self._ordinal = ordinal

    @property
    def owner(self):
        r"""Gets the owner of this CatalogVO.

        责任人。

        :return: The owner of this CatalogVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this CatalogVO.

        责任人。

        :param owner: The owner of this CatalogVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CatalogVO.

        父目录ID，木有则为根目录，ID字符串。

        :return: The parent_id of this CatalogVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CatalogVO.

        父目录ID，木有则为根目录，ID字符串。

        :param parent_id: The parent_id of this CatalogVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def swap_order_id(self):
        r"""Gets the swap_order_id of this CatalogVO.

        同层排序，目标节点的ID，ID字符串。

        :return: The swap_order_id of this CatalogVO.
        :rtype: str
        """
        return self._swap_order_id

    @swap_order_id.setter
    def swap_order_id(self, swap_order_id):
        r"""Sets the swap_order_id of this CatalogVO.

        同层排序，目标节点的ID，ID字符串。

        :param swap_order_id: The swap_order_id of this CatalogVO.
        :type swap_order_id: str
        """
        self._swap_order_id = swap_order_id

    @property
    def id(self):
        r"""Gets the id of this CatalogVO.

        主题ID，ID字符串。

        :return: The id of this CatalogVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CatalogVO.

        主题ID，ID字符串。

        :param id: The id of this CatalogVO.
        :type id: str
        """
        self._id = id

    @property
    def qualified_id(self):
        r"""Gets the qualified_id of this CatalogVO.

        认证ID，自动生成。

        :return: The qualified_id of this CatalogVO.
        :rtype: str
        """
        return self._qualified_id

    @qualified_id.setter
    def qualified_id(self, qualified_id):
        r"""Sets the qualified_id of this CatalogVO.

        认证ID，自动生成。

        :param qualified_id: The qualified_id of this CatalogVO.
        :type qualified_id: str
        """
        self._qualified_id = qualified_id

    @property
    def from_public(self):
        r"""Gets the from_public of this CatalogVO.

        是否来自公共层。

        :return: The from_public of this CatalogVO.
        :rtype: bool
        """
        return self._from_public

    @from_public.setter
    def from_public(self, from_public):
        r"""Sets the from_public of this CatalogVO.

        是否来自公共层。

        :param from_public: The from_public of this CatalogVO.
        :type from_public: bool
        """
        self._from_public = from_public

    @property
    def create_by(self):
        r"""Gets the create_by of this CatalogVO.

        创建人。

        :return: The create_by of this CatalogVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CatalogVO.

        创建人。

        :param create_by: The create_by of this CatalogVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this CatalogVO.

        更新人。

        :return: The update_by of this CatalogVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CatalogVO.

        更新人。

        :param update_by: The update_by of this CatalogVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CatalogVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this CatalogVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CatalogVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this CatalogVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this CatalogVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this CatalogVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CatalogVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this CatalogVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def children_num(self):
        r"""Gets the children_num of this CatalogVO.

        拥有子流程的数量，不包括子流程的子流程，前端不传。

        :return: The children_num of this CatalogVO.
        :rtype: int
        """
        return self._children_num

    @children_num.setter
    def children_num(self, children_num):
        r"""Sets the children_num of this CatalogVO.

        拥有子流程的数量，不包括子流程的子流程，前端不传。

        :param children_num: The children_num of this CatalogVO.
        :type children_num: int
        """
        self._children_num = children_num

    @property
    def children(self):
        r"""Gets the children of this CatalogVO.

        下层子目录，只读。

        :return: The children of this CatalogVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogVO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this CatalogVO.

        下层子目录，只读。

        :param children: The children of this CatalogVO.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.CatalogVO`]
        """
        self._children = children

    @property
    def self_defined_fields(self):
        r"""Gets the self_defined_fields of this CatalogVO.

        属性自定义项。

        :return: The self_defined_fields of this CatalogVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SelfDefinedFieldVO`]
        """
        return self._self_defined_fields

    @self_defined_fields.setter
    def self_defined_fields(self, self_defined_fields):
        r"""Sets the self_defined_fields of this CatalogVO.

        属性自定义项。

        :param self_defined_fields: The self_defined_fields of this CatalogVO.
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
        if not isinstance(other, CatalogVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
