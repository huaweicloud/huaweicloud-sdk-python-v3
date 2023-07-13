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
        'id': 'int',
        'parent_id': 'int',
        'prev_id': 'int',
        'root_id': 'int',
        'qualified_name': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'create_by': 'str',
        'update_by': 'str',
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
        'create_time': 'create_time',
        'update_time': 'update_time',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'children': 'children'
    }

    def __init__(self, name=None, description=None, type=None, id=None, parent_id=None, prev_id=None, root_id=None, qualified_name=None, create_time=None, update_time=None, create_by=None, update_by=None, children=None):
        """DirectoryVO

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param description: 描述
        :type description: str
        :param type: 目录类型
        :type type: str
        :param id: ID
        :type id: int
        :param parent_id: 父目录ID,根节点没有此ID
        :type parent_id: int
        :param prev_id: 上个节点ID,首节点没有
        :type prev_id: int
        :param root_id: 根节点ID,根节点此ID为自身ID
        :type root_id: int
        :param qualified_name: 所属目录
        :type qualified_name: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param create_by: 创建人
        :type create_by: str
        :param update_by: 更新人
        :type update_by: str
        :param children: 子目录
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
        self._create_time = None
        self._update_time = None
        self._create_by = None
        self._update_by = None
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
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if children is not None:
            self.children = children

    @property
    def name(self):
        """Gets the name of this DirectoryVO.

        名称

        :return: The name of this DirectoryVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectoryVO.

        名称

        :param name: The name of this DirectoryVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DirectoryVO.

        描述

        :return: The description of this DirectoryVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DirectoryVO.

        描述

        :param description: The description of this DirectoryVO.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this DirectoryVO.

        目录类型

        :return: The type of this DirectoryVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DirectoryVO.

        目录类型

        :param type: The type of this DirectoryVO.
        :type type: str
        """
        self._type = type

    @property
    def id(self):
        """Gets the id of this DirectoryVO.

        ID

        :return: The id of this DirectoryVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DirectoryVO.

        ID

        :param id: The id of this DirectoryVO.
        :type id: int
        """
        self._id = id

    @property
    def parent_id(self):
        """Gets the parent_id of this DirectoryVO.

        父目录ID,根节点没有此ID

        :return: The parent_id of this DirectoryVO.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DirectoryVO.

        父目录ID,根节点没有此ID

        :param parent_id: The parent_id of this DirectoryVO.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def prev_id(self):
        """Gets the prev_id of this DirectoryVO.

        上个节点ID,首节点没有

        :return: The prev_id of this DirectoryVO.
        :rtype: int
        """
        return self._prev_id

    @prev_id.setter
    def prev_id(self, prev_id):
        """Sets the prev_id of this DirectoryVO.

        上个节点ID,首节点没有

        :param prev_id: The prev_id of this DirectoryVO.
        :type prev_id: int
        """
        self._prev_id = prev_id

    @property
    def root_id(self):
        """Gets the root_id of this DirectoryVO.

        根节点ID,根节点此ID为自身ID

        :return: The root_id of this DirectoryVO.
        :rtype: int
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this DirectoryVO.

        根节点ID,根节点此ID为自身ID

        :param root_id: The root_id of this DirectoryVO.
        :type root_id: int
        """
        self._root_id = root_id

    @property
    def qualified_name(self):
        """Gets the qualified_name of this DirectoryVO.

        所属目录

        :return: The qualified_name of this DirectoryVO.
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this DirectoryVO.

        所属目录

        :param qualified_name: The qualified_name of this DirectoryVO.
        :type qualified_name: str
        """
        self._qualified_name = qualified_name

    @property
    def create_time(self):
        """Gets the create_time of this DirectoryVO.

        创建时间

        :return: The create_time of this DirectoryVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DirectoryVO.

        创建时间

        :param create_time: The create_time of this DirectoryVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this DirectoryVO.

        更新时间

        :return: The update_time of this DirectoryVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DirectoryVO.

        更新时间

        :param update_time: The update_time of this DirectoryVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_by(self):
        """Gets the create_by of this DirectoryVO.

        创建人

        :return: The create_by of this DirectoryVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DirectoryVO.

        创建人

        :param create_by: The create_by of this DirectoryVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        """Gets the update_by of this DirectoryVO.

        更新人

        :return: The update_by of this DirectoryVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        """Sets the update_by of this DirectoryVO.

        更新人

        :param update_by: The update_by of this DirectoryVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def children(self):
        """Gets the children of this DirectoryVO.

        子目录

        :return: The children of this DirectoryVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DirectoryVO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this DirectoryVO.

        子目录

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
