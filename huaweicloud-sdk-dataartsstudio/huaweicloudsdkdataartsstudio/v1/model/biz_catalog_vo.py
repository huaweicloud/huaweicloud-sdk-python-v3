# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizCatalogVO:

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
        'guid': 'str',
        'owner': 'str',
        'parent_id': 'str',
        'prev_id': 'str',
        'next_id': 'str',
        'id': 'str',
        'qualified_id': 'str',
        'create_by': 'str',
        'update_by': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'bizmetric_num': 'int',
        'children_num': 'int',
        'children': 'list[BizCatalogVO]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'guid': 'guid',
        'owner': 'owner',
        'parent_id': 'parent_id',
        'prev_id': 'prev_id',
        'next_id': 'next_id',
        'id': 'id',
        'qualified_id': 'qualified_id',
        'create_by': 'create_by',
        'update_by': 'update_by',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'bizmetric_num': 'bizmetric_num',
        'children_num': 'children_num',
        'children': 'children'
    }

    def __init__(self, name=None, description=None, guid=None, owner=None, parent_id=None, prev_id=None, next_id=None, id=None, qualified_id=None, create_by=None, update_by=None, create_time=None, update_time=None, bizmetric_num=None, children_num=None, children=None):
        r"""BizCatalogVO

        The model defined in huaweicloud sdk

        :param name: 流程名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param guid: 对应资产中ID。
        :type guid: str
        :param owner: 责任人。
        :type owner: str
        :param parent_id: 父目录ID，没有则为根目录。填写String类型替代Long类型。
        :type parent_id: str
        :param prev_id: 上个节点ID，没有则为首节点。填写String类型替代Long类型。
        :type prev_id: str
        :param next_id: 下个节点ID，没有则为尾节点。填写String类型替代Long类型。
        :type next_id: str
        :param id: 创建时传空，更新时必填。填写String类型替代Long类型。
        :type id: str
        :param qualified_id: 认证ID，自动生成。
        :type qualified_id: str
        :param create_by: 创建人。
        :type create_by: str
        :param update_by: 更新人。
        :type update_by: str
        :param create_time: 创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type create_time: datetime
        :param update_time: 更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。
        :type update_time: datetime
        :param bizmetric_num: 拥有业务指标数量，前端不传。
        :type bizmetric_num: int
        :param children_num: 拥有子流程的数量，不包括子流程的子流程。
        :type children_num: int
        :param children: 下层子目录，只读。
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.BizCatalogVO`]
        """
        
        

        self._name = None
        self._description = None
        self._guid = None
        self._owner = None
        self._parent_id = None
        self._prev_id = None
        self._next_id = None
        self._id = None
        self._qualified_id = None
        self._create_by = None
        self._update_by = None
        self._create_time = None
        self._update_time = None
        self._bizmetric_num = None
        self._children_num = None
        self._children = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        self.owner = owner
        if parent_id is not None:
            self.parent_id = parent_id
        if prev_id is not None:
            self.prev_id = prev_id
        if next_id is not None:
            self.next_id = next_id
        self.id = id
        if qualified_id is not None:
            self.qualified_id = qualified_id
        if create_by is not None:
            self.create_by = create_by
        if update_by is not None:
            self.update_by = update_by
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if bizmetric_num is not None:
            self.bizmetric_num = bizmetric_num
        if children_num is not None:
            self.children_num = children_num
        if children is not None:
            self.children = children

    @property
    def name(self):
        r"""Gets the name of this BizCatalogVO.

        流程名称。

        :return: The name of this BizCatalogVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BizCatalogVO.

        流程名称。

        :param name: The name of this BizCatalogVO.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this BizCatalogVO.

        描述。

        :return: The description of this BizCatalogVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BizCatalogVO.

        描述。

        :param description: The description of this BizCatalogVO.
        :type description: str
        """
        self._description = description

    @property
    def guid(self):
        r"""Gets the guid of this BizCatalogVO.

        对应资产中ID。

        :return: The guid of this BizCatalogVO.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this BizCatalogVO.

        对应资产中ID。

        :param guid: The guid of this BizCatalogVO.
        :type guid: str
        """
        self._guid = guid

    @property
    def owner(self):
        r"""Gets the owner of this BizCatalogVO.

        责任人。

        :return: The owner of this BizCatalogVO.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this BizCatalogVO.

        责任人。

        :param owner: The owner of this BizCatalogVO.
        :type owner: str
        """
        self._owner = owner

    @property
    def parent_id(self):
        r"""Gets the parent_id of this BizCatalogVO.

        父目录ID，没有则为根目录。填写String类型替代Long类型。

        :return: The parent_id of this BizCatalogVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this BizCatalogVO.

        父目录ID，没有则为根目录。填写String类型替代Long类型。

        :param parent_id: The parent_id of this BizCatalogVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def prev_id(self):
        r"""Gets the prev_id of this BizCatalogVO.

        上个节点ID，没有则为首节点。填写String类型替代Long类型。

        :return: The prev_id of this BizCatalogVO.
        :rtype: str
        """
        return self._prev_id

    @prev_id.setter
    def prev_id(self, prev_id):
        r"""Sets the prev_id of this BizCatalogVO.

        上个节点ID，没有则为首节点。填写String类型替代Long类型。

        :param prev_id: The prev_id of this BizCatalogVO.
        :type prev_id: str
        """
        self._prev_id = prev_id

    @property
    def next_id(self):
        r"""Gets the next_id of this BizCatalogVO.

        下个节点ID，没有则为尾节点。填写String类型替代Long类型。

        :return: The next_id of this BizCatalogVO.
        :rtype: str
        """
        return self._next_id

    @next_id.setter
    def next_id(self, next_id):
        r"""Sets the next_id of this BizCatalogVO.

        下个节点ID，没有则为尾节点。填写String类型替代Long类型。

        :param next_id: The next_id of this BizCatalogVO.
        :type next_id: str
        """
        self._next_id = next_id

    @property
    def id(self):
        r"""Gets the id of this BizCatalogVO.

        创建时传空，更新时必填。填写String类型替代Long类型。

        :return: The id of this BizCatalogVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BizCatalogVO.

        创建时传空，更新时必填。填写String类型替代Long类型。

        :param id: The id of this BizCatalogVO.
        :type id: str
        """
        self._id = id

    @property
    def qualified_id(self):
        r"""Gets the qualified_id of this BizCatalogVO.

        认证ID，自动生成。

        :return: The qualified_id of this BizCatalogVO.
        :rtype: str
        """
        return self._qualified_id

    @qualified_id.setter
    def qualified_id(self, qualified_id):
        r"""Sets the qualified_id of this BizCatalogVO.

        认证ID，自动生成。

        :param qualified_id: The qualified_id of this BizCatalogVO.
        :type qualified_id: str
        """
        self._qualified_id = qualified_id

    @property
    def create_by(self):
        r"""Gets the create_by of this BizCatalogVO.

        创建人。

        :return: The create_by of this BizCatalogVO.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this BizCatalogVO.

        创建人。

        :param create_by: The create_by of this BizCatalogVO.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def update_by(self):
        r"""Gets the update_by of this BizCatalogVO.

        更新人。

        :return: The update_by of this BizCatalogVO.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this BizCatalogVO.

        更新人。

        :param update_by: The update_by of this BizCatalogVO.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def create_time(self):
        r"""Gets the create_time of this BizCatalogVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The create_time of this BizCatalogVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this BizCatalogVO.

        创建时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param create_time: The create_time of this BizCatalogVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this BizCatalogVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :return: The update_time of this BizCatalogVO.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this BizCatalogVO.

        更新时间，只读，格式遵循RFC3339，精确到秒，UTC时区，即yyyy-mm-ddTHH:MM:SSZ，如1970-01-01T00:00:00Z。

        :param update_time: The update_time of this BizCatalogVO.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def bizmetric_num(self):
        r"""Gets the bizmetric_num of this BizCatalogVO.

        拥有业务指标数量，前端不传。

        :return: The bizmetric_num of this BizCatalogVO.
        :rtype: int
        """
        return self._bizmetric_num

    @bizmetric_num.setter
    def bizmetric_num(self, bizmetric_num):
        r"""Sets the bizmetric_num of this BizCatalogVO.

        拥有业务指标数量，前端不传。

        :param bizmetric_num: The bizmetric_num of this BizCatalogVO.
        :type bizmetric_num: int
        """
        self._bizmetric_num = bizmetric_num

    @property
    def children_num(self):
        r"""Gets the children_num of this BizCatalogVO.

        拥有子流程的数量，不包括子流程的子流程。

        :return: The children_num of this BizCatalogVO.
        :rtype: int
        """
        return self._children_num

    @children_num.setter
    def children_num(self, children_num):
        r"""Sets the children_num of this BizCatalogVO.

        拥有子流程的数量，不包括子流程的子流程。

        :param children_num: The children_num of this BizCatalogVO.
        :type children_num: int
        """
        self._children_num = children_num

    @property
    def children(self):
        r"""Gets the children of this BizCatalogVO.

        下层子目录，只读。

        :return: The children of this BizCatalogVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BizCatalogVO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this BizCatalogVO.

        下层子目录，只读。

        :param children: The children of this BizCatalogVO.
        :type children: list[:class:`huaweicloudsdkdataartsstudio.v1.BizCatalogVO`]
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
        if not isinstance(other, BizCatalogVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
