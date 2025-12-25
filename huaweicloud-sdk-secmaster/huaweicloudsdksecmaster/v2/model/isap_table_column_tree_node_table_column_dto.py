# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsapTableColumnTreeNodeTableColumnDto:

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
        'parent_name': 'str',
        'own_name': 'str',
        'depth': 'int',
        'source': 'IsapTableColumnDto',
        'children': 'list[IsapTableColumnTreeNodeTableColumnDto]',
        'previous_name': 'str',
        'column_sequence_number': 'int'
    }

    attribute_map = {
        'name': 'name',
        'parent_name': 'parent_name',
        'own_name': 'own_name',
        'depth': 'depth',
        'source': 'source',
        'children': 'children',
        'previous_name': 'previous_name',
        'column_sequence_number': 'column_sequence_number'
    }

    def __init__(self, name=None, parent_name=None, own_name=None, depth=None, source=None, children=None, previous_name=None, column_sequence_number=None):
        r"""IsapTableColumnTreeNodeTableColumnDto

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param parent_name: 父级名称
        :type parent_name: str
        :param own_name: 所属名称
        :type own_name: str
        :param depth: 深度
        :type depth: int
        :param source: 
        :type source: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`
        :param children: 子节点数组
        :type children: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`]
        :param previous_name: 父级名称
        :type previous_name: str
        :param column_sequence_number: 列序号
        :type column_sequence_number: int
        """
        
        

        self._name = None
        self._parent_name = None
        self._own_name = None
        self._depth = None
        self._source = None
        self._children = None
        self._previous_name = None
        self._column_sequence_number = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_name is not None:
            self.parent_name = parent_name
        if own_name is not None:
            self.own_name = own_name
        if depth is not None:
            self.depth = depth
        if source is not None:
            self.source = source
        if children is not None:
            self.children = children
        if previous_name is not None:
            self.previous_name = previous_name
        if column_sequence_number is not None:
            self.column_sequence_number = column_sequence_number

    @property
    def name(self):
        r"""Gets the name of this IsapTableColumnTreeNodeTableColumnDto.

        名称

        :return: The name of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this IsapTableColumnTreeNodeTableColumnDto.

        名称

        :param name: The name of this IsapTableColumnTreeNodeTableColumnDto.
        :type name: str
        """
        self._name = name

    @property
    def parent_name(self):
        r"""Gets the parent_name of this IsapTableColumnTreeNodeTableColumnDto.

        父级名称

        :return: The parent_name of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this IsapTableColumnTreeNodeTableColumnDto.

        父级名称

        :param parent_name: The parent_name of this IsapTableColumnTreeNodeTableColumnDto.
        :type parent_name: str
        """
        self._parent_name = parent_name

    @property
    def own_name(self):
        r"""Gets the own_name of this IsapTableColumnTreeNodeTableColumnDto.

        所属名称

        :return: The own_name of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: str
        """
        return self._own_name

    @own_name.setter
    def own_name(self, own_name):
        r"""Sets the own_name of this IsapTableColumnTreeNodeTableColumnDto.

        所属名称

        :param own_name: The own_name of this IsapTableColumnTreeNodeTableColumnDto.
        :type own_name: str
        """
        self._own_name = own_name

    @property
    def depth(self):
        r"""Gets the depth of this IsapTableColumnTreeNodeTableColumnDto.

        深度

        :return: The depth of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        r"""Sets the depth of this IsapTableColumnTreeNodeTableColumnDto.

        深度

        :param depth: The depth of this IsapTableColumnTreeNodeTableColumnDto.
        :type depth: int
        """
        self._depth = depth

    @property
    def source(self):
        r"""Gets the source of this IsapTableColumnTreeNodeTableColumnDto.

        :return: The source of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this IsapTableColumnTreeNodeTableColumnDto.

        :param source: The source of this IsapTableColumnTreeNodeTableColumnDto.
        :type source: :class:`huaweicloudsdksecmaster.v2.IsapTableColumnDto`
        """
        self._source = source

    @property
    def children(self):
        r"""Gets the children of this IsapTableColumnTreeNodeTableColumnDto.

        子节点数组

        :return: The children of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this IsapTableColumnTreeNodeTableColumnDto.

        子节点数组

        :param children: The children of this IsapTableColumnTreeNodeTableColumnDto.
        :type children: list[:class:`huaweicloudsdksecmaster.v2.IsapTableColumnTreeNodeTableColumnDto`]
        """
        self._children = children

    @property
    def previous_name(self):
        r"""Gets the previous_name of this IsapTableColumnTreeNodeTableColumnDto.

        父级名称

        :return: The previous_name of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: str
        """
        return self._previous_name

    @previous_name.setter
    def previous_name(self, previous_name):
        r"""Sets the previous_name of this IsapTableColumnTreeNodeTableColumnDto.

        父级名称

        :param previous_name: The previous_name of this IsapTableColumnTreeNodeTableColumnDto.
        :type previous_name: str
        """
        self._previous_name = previous_name

    @property
    def column_sequence_number(self):
        r"""Gets the column_sequence_number of this IsapTableColumnTreeNodeTableColumnDto.

        列序号

        :return: The column_sequence_number of this IsapTableColumnTreeNodeTableColumnDto.
        :rtype: int
        """
        return self._column_sequence_number

    @column_sequence_number.setter
    def column_sequence_number(self, column_sequence_number):
        r"""Sets the column_sequence_number of this IsapTableColumnTreeNodeTableColumnDto.

        列序号

        :param column_sequence_number: The column_sequence_number of this IsapTableColumnTreeNodeTableColumnDto.
        :type column_sequence_number: int
        """
        self._column_sequence_number = column_sequence_number

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
        if not isinstance(other, IsapTableColumnTreeNodeTableColumnDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
