# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectoryVO:

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
        'description': 'str',
        'type': 'str',
        'id': 'str',
        'parent_id': 'str',
        'prev_id': 'str',
        'root_id': 'str',
        'qualified_name': 'str',
        'from_public': 'bool',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str',
        'ref_id': 'str',
        'children': 'list[DirectoryVO]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'id': 'id',
        'parent_id': 'parent_id',
        'prev_id': 'prev_id',
        'root_id': 'root_id',
        'qualified_name': 'qualified_name',
        'from_public': 'from_public',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'ref_id': 'ref_id',
        'children': 'children'
    }

    def __init__(self, name=None, description=None, type=None, id=None, parent_id=None, prev_id=None, root_id=None, qualified_name=None, from_public=None, create_time=None, update_time=None, create_by=None, update_by=None, ref_id=None, children=None):
        r"""DirectoryVO

        The model defined in huaweicloud sdk

        :param name: 目录名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param type: 目录类型。 枚举值：   - STANDARD_ELEMENT: 数据标准   - CODE: 码表 
        :type type: str
        :param id: ID，创建时可不传，更新时必填。填写String类型替代Long类型。
        :type id: str
        :param parent_id: 父目录ID，首层传null。填写String类型替代Long类型。
        :type parent_id: str
        :param prev_id: 上个节点ID，首节点传null。填写String类型替代Long类型。
        :type prev_id: str
        :param root_id: 根节点ID，根节点此ID为自身ID，只读。填写String类型替代Long类型。
        :type root_id: str
        :param qualified_name: 目录的资产名称，只读。
        :type qualified_name: str
        :param from_public: 是否来自公共层，只读。
        :type from_public: bool
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param create_by: 创建人，只读。
        :type create_by: str
        :param update_by: 更新人，只读。
        :type update_by: str
        :param ref_id: 关联的主题ID，ID字符串。
        :type ref_id: str
        :param children: 子目录。
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryVO`]
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._id = None
        self._parent_id = None
        self._prev_id = None
        self._root_id = None
        self._qualified_name = None
        self._from_public = None
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
        self._ref_id = None
        self._children = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if id is not None:
            self.id = id
        self.parent_id = parent_id
        self.prev_id = prev_id
        if root_id is not None:
            self.root_id = root_id
        if qualified_name is not None:
            self.qualified_name = qualified_name
        if from_public is not None:
            self.from_public = from_public
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if ref_id is not None:
            self.ref_id = ref_id
        if children is not None:
            self.children = children

    @property
    def name(self):
        r"""Gets the name of this DirectoryVO.

        目录名称。

        :return: The name of this DirectoryVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DirectoryVO.

        目录名称。

        :param name: The name of this DirectoryVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this DirectoryVO.

        描述。

        :return: The description of this DirectoryVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DirectoryVO.

        描述。

        :param description: The description of this DirectoryVO.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this DirectoryVO.

        目录类型。 枚举值：   - STANDARD_ELEMENT: 数据标准   - CODE: 码表 

        :return: The type of this DirectoryVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DirectoryVO.

        目录类型。 枚举值：   - STANDARD_ELEMENT: 数据标准   - CODE: 码表 

        :param type: The type of this DirectoryVO.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        r"""Gets the id of this DirectoryVO.

        ID，创建时可不传，更新时必填。填写String类型替代Long类型。

        :return: The id of this DirectoryVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DirectoryVO.

        ID，创建时可不传，更新时必填。填写String类型替代Long类型。

        :param id: The id of this DirectoryVO.
        :type id: str
        """
        self._id = id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this DirectoryVO.

        父目录ID，首层传null。填写String类型替代Long类型。

        :return: The parent_id of this DirectoryVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this DirectoryVO.

        父目录ID，首层传null。填写String类型替代Long类型。

        :param parent_id: The parent_id of this DirectoryVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def prev_id(self):
        r"""Gets the prev_id of this DirectoryVO.

        上个节点ID，首节点传null。填写String类型替代Long类型。

        :return: The prev_id of this DirectoryVO.
        :rtype: str
        """
        return self._prev_id

    @prev_id.setter
    def prev_id(self, prev_id):
        r"""Sets the prev_id of this DirectoryVO.

        上个节点ID，首节点传null。填写String类型替代Long类型。

        :param prev_id: The prev_id of this DirectoryVO.
        :type prev_id: str
        """
        self._prev_id = prev_id

    @property
    def root_id(self):
        r"""Gets the root_id of this DirectoryVO.

        根节点ID，根节点此ID为自身ID，只读。填写String类型替代Long类型。

        :return: The root_id of this DirectoryVO.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this DirectoryVO.

        根节点ID，根节点此ID为自身ID，只读。填写String类型替代Long类型。

        :param root_id: The root_id of this DirectoryVO.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def qualified_name(self):
        r"""Gets the qualified_name of this DirectoryVO.

        目录的资产名称，只读。

        :return: The qualified_name of this DirectoryVO.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        r"""Sets the qualified_name of this DirectoryVO.

        目录的资产名称，只读。

        :param qualified_name: The qualified_name of this DirectoryVO.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def from_public(self):
        r"""Gets the from_public of this DirectoryVO.

        是否来自公共层，只读。

        :return: The from_public of this DirectoryVO.
        :rtype: bool
        """
        return self._from_public

    @from_public.setter
    def from_public(self, from_public):
        r"""Sets the from_public of this DirectoryVO.

        是否来自公共层，只读。

        :param from_public: The from_public of this DirectoryVO.
        :type from_public: bool
        """
        self._from_public = from_public

    @property
    def create_time(self):
        r"""Gets the create_time of this DirectoryVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this DirectoryVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DirectoryVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this DirectoryVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this DirectoryVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this DirectoryVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this DirectoryVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this DirectoryVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        r"""Gets the create_by of this DirectoryVO.

        创建人，只读。

        :return: The create_by of this DirectoryVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this DirectoryVO.

        创建人，只读。

        :param create_by: The create_by of this DirectoryVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this DirectoryVO.

        更新人，只读。

        :return: The update_by of this DirectoryVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this DirectoryVO.

        更新人，只读。

        :param update_by: The update_by of this DirectoryVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def ref_id(self):
        r"""Gets the ref_id of this DirectoryVO.

        关联的主题ID，ID字符串。

        :return: The ref_id of this DirectoryVO.
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        r"""Sets the ref_id of this DirectoryVO.

        关联的主题ID，ID字符串。

        :param ref_id: The ref_id of this DirectoryVO.
        :type ref_id: str
        """
        self._ref_id = ref_id

    @property
    def children(self):
        r"""Gets the children of this DirectoryVO.

        子目录。

        :return: The children of this DirectoryVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryVO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this DirectoryVO.

        子目录。

        :param children: The children of this DirectoryVO.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryVO`]
        """
        self._children = children

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
        if not isinstance(other, DirectoryVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
