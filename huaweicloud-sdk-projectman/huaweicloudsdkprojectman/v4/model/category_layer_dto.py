# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CategoryLayerDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'BaseCategory',
        'link_parent_field': 'str',
        'id': 'str',
        'children': 'list[CategoryLayerDTO]',
        'code': 'str',
        'category_code': 'str',
        'category_id': 'str',
        'layer_type': 'str',
        'parent_id': 'str',
        'root_id': 'str',
        'position_x': 'int',
        'position_y': 'int'
    }

    attribute_map = {
        'category': 'category',
        'link_parent_field': 'link_parent_field',
        'id': 'id',
        'children': 'children',
        'code': 'code',
        'category_code': 'category_code',
        'category_id': 'category_id',
        'layer_type': 'layer_type',
        'parent_id': 'parent_id',
        'root_id': 'root_id',
        'position_x': 'position_x',
        'position_y': 'position_y'
    }

    def __init__(self, category=None, link_parent_field=None, id=None, children=None, code=None, category_code=None, category_id=None, layer_type=None, parent_id=None, root_id=None, position_x=None, position_y=None):
        r"""CategoryLayerDTO

        The model defined in huaweicloud sdk

        :param category: 
        :type category: :class:`huaweicloudsdkprojectman.v4.BaseCategory`
        :param link_parent_field: **参数解释**： 父类字段。 **取值范围**： 不涉及。
        :type link_parent_field: str
        :param id: **参数解释**： 工作项层级ID。 **取值范围**： 不涉及。
        :type id: str
        :param children: **参数解释**： 子工作项层级数据类型。 **取值范围**： 不涉及。
        :type children: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        :param code: **参数解释**： 层级对象类型编码。 **取值范围**： 不涉及。
        :type code: str
        :param category_code: **参数解释**： 对象类型编码。 **取值范围**： 不涉及。
        :type category_code: str
        :param category_id: **参数解释**： 对象类型ID。 **取值范围**： 不涉及。
        :type category_id: str
        :param layer_type: **参数解释**： 层级类型。 **取值范围**： 不涉及。
        :type layer_type: str
        :param parent_id: **参数解释**： 父ID。 **取值范围**： 不涉及。
        :type parent_id: str
        :param root_id: **参数解释**： 根工作项ID。 **取值范围**： 不涉及。
        :type root_id: str
        :param position_x: **参数解释**： 画布X轴坐标。 **取值范围**： 不涉及。
        :type position_x: int
        :param position_y: **参数解释**： 画布Y轴坐标。 **取值范围**： 不涉及。
        :type position_y: int
        """
        
        

        self._category = None
        self._link_parent_field = None
        self._id = None
        self._children = None
        self._code = None
        self._category_code = None
        self._category_id = None
        self._layer_type = None
        self._parent_id = None
        self._root_id = None
        self._position_x = None
        self._position_y = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if link_parent_field is not None:
            self.link_parent_field = link_parent_field
        if id is not None:
            self.id = id
        if children is not None:
            self.children = children
        if code is not None:
            self.code = code
        if category_code is not None:
            self.category_code = category_code
        if category_id is not None:
            self.category_id = category_id
        if layer_type is not None:
            self.layer_type = layer_type
        if parent_id is not None:
            self.parent_id = parent_id
        if root_id is not None:
            self.root_id = root_id
        if position_x is not None:
            self.position_x = position_x
        if position_y is not None:
            self.position_y = position_y

    @property
    def category(self):
        r"""Gets the category of this CategoryLayerDTO.

        :return: The category of this CategoryLayerDTO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.BaseCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CategoryLayerDTO.

        :param category: The category of this CategoryLayerDTO.
        :type category: :class:`huaweicloudsdkprojectman.v4.BaseCategory`
        """
        self._category = category

    @property
    def link_parent_field(self):
        r"""Gets the link_parent_field of this CategoryLayerDTO.

        **参数解释**： 父类字段。 **取值范围**： 不涉及。

        :return: The link_parent_field of this CategoryLayerDTO.
        :rtype: str
        """
        return self._link_parent_field

    @link_parent_field.setter
    def link_parent_field(self, link_parent_field):
        r"""Sets the link_parent_field of this CategoryLayerDTO.

        **参数解释**： 父类字段。 **取值范围**： 不涉及。

        :param link_parent_field: The link_parent_field of this CategoryLayerDTO.
        :type link_parent_field: str
        """
        self._link_parent_field = link_parent_field

    @property
    def id(self):
        r"""Gets the id of this CategoryLayerDTO.

        **参数解释**： 工作项层级ID。 **取值范围**： 不涉及。

        :return: The id of this CategoryLayerDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CategoryLayerDTO.

        **参数解释**： 工作项层级ID。 **取值范围**： 不涉及。

        :param id: The id of this CategoryLayerDTO.
        :type id: str
        """
        self._id = id

    @property
    def children(self):
        r"""Gets the children of this CategoryLayerDTO.

        **参数解释**： 子工作项层级数据类型。 **取值范围**： 不涉及。

        :return: The children of this CategoryLayerDTO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this CategoryLayerDTO.

        **参数解释**： 子工作项层级数据类型。 **取值范围**： 不涉及。

        :param children: The children of this CategoryLayerDTO.
        :type children: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        """
        self._children = children

    @property
    def code(self):
        r"""Gets the code of this CategoryLayerDTO.

        **参数解释**： 层级对象类型编码。 **取值范围**： 不涉及。

        :return: The code of this CategoryLayerDTO.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CategoryLayerDTO.

        **参数解释**： 层级对象类型编码。 **取值范围**： 不涉及。

        :param code: The code of this CategoryLayerDTO.
        :type code: str
        """
        self._code = code

    @property
    def category_code(self):
        r"""Gets the category_code of this CategoryLayerDTO.

        **参数解释**： 对象类型编码。 **取值范围**： 不涉及。

        :return: The category_code of this CategoryLayerDTO.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        r"""Sets the category_code of this CategoryLayerDTO.

        **参数解释**： 对象类型编码。 **取值范围**： 不涉及。

        :param category_code: The category_code of this CategoryLayerDTO.
        :type category_code: str
        """
        self._category_code = category_code

    @property
    def category_id(self):
        r"""Gets the category_id of this CategoryLayerDTO.

        **参数解释**： 对象类型ID。 **取值范围**： 不涉及。

        :return: The category_id of this CategoryLayerDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this CategoryLayerDTO.

        **参数解释**： 对象类型ID。 **取值范围**： 不涉及。

        :param category_id: The category_id of this CategoryLayerDTO.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def layer_type(self):
        r"""Gets the layer_type of this CategoryLayerDTO.

        **参数解释**： 层级类型。 **取值范围**： 不涉及。

        :return: The layer_type of this CategoryLayerDTO.
        :rtype: str
        """
        return self._layer_type

    @layer_type.setter
    def layer_type(self, layer_type):
        r"""Sets the layer_type of this CategoryLayerDTO.

        **参数解释**： 层级类型。 **取值范围**： 不涉及。

        :param layer_type: The layer_type of this CategoryLayerDTO.
        :type layer_type: str
        """
        self._layer_type = layer_type

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CategoryLayerDTO.

        **参数解释**： 父ID。 **取值范围**： 不涉及。

        :return: The parent_id of this CategoryLayerDTO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CategoryLayerDTO.

        **参数解释**： 父ID。 **取值范围**： 不涉及。

        :param parent_id: The parent_id of this CategoryLayerDTO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def root_id(self):
        r"""Gets the root_id of this CategoryLayerDTO.

        **参数解释**： 根工作项ID。 **取值范围**： 不涉及。

        :return: The root_id of this CategoryLayerDTO.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this CategoryLayerDTO.

        **参数解释**： 根工作项ID。 **取值范围**： 不涉及。

        :param root_id: The root_id of this CategoryLayerDTO.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def position_x(self):
        r"""Gets the position_x of this CategoryLayerDTO.

        **参数解释**： 画布X轴坐标。 **取值范围**： 不涉及。

        :return: The position_x of this CategoryLayerDTO.
        :rtype: int
        """
        return self._position_x

    @position_x.setter
    def position_x(self, position_x):
        r"""Sets the position_x of this CategoryLayerDTO.

        **参数解释**： 画布X轴坐标。 **取值范围**： 不涉及。

        :param position_x: The position_x of this CategoryLayerDTO.
        :type position_x: int
        """
        self._position_x = position_x

    @property
    def position_y(self):
        r"""Gets the position_y of this CategoryLayerDTO.

        **参数解释**： 画布Y轴坐标。 **取值范围**： 不涉及。

        :return: The position_y of this CategoryLayerDTO.
        :rtype: int
        """
        return self._position_y

    @position_y.setter
    def position_y(self, position_y):
        r"""Sets the position_y of this CategoryLayerDTO.

        **参数解释**： 画布Y轴坐标。 **取值范围**： 不涉及。

        :param position_y: The position_y of this CategoryLayerDTO.
        :type position_y: int
        """
        self._position_y = position_y

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
        if not isinstance(other, CategoryLayerDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
