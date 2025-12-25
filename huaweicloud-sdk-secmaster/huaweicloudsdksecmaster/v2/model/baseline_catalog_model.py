# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineCatalogModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'serial_number': 'int',
        'level_number': 'int',
        'root': 'str',
        'parent': 'str',
        'is_leaf': 'bool',
        'check_items': 'list[CheckitemCatalogModel]'
    }

    attribute_map = {
        'uuid': 'uuid',
        'serial_number': 'serial_number',
        'level_number': 'level_number',
        'root': 'root',
        'parent': 'parent',
        'is_leaf': 'is_leaf',
        'check_items': 'check_items'
    }

    def __init__(self, uuid=None, serial_number=None, level_number=None, root=None, parent=None, is_leaf=None, check_items=None):
        r"""BaselineCatalogModel

        The model defined in huaweicloud sdk

        :param uuid: 目录ID唯一标识，UUID
        :type uuid: str
        :param serial_number: 目录的位置顺序
        :type serial_number: int
        :param level_number: 目录的层级关系
        :type level_number: int
        :param root: 该目录所在遵从包UUID
        :type root: str
        :param parent: 该目录的父目录UUID，如果等于为第一层目录，则为遵从包UUID
        :type parent: str
        :param is_leaf: 该目录是否是叶子节点 0：不是 1：是
        :type is_leaf: bool
        :param check_items: 目录关联的检查项
        :type check_items: list[:class:`huaweicloudsdksecmaster.v2.CheckitemCatalogModel`]
        """
        
        

        self._uuid = None
        self._serial_number = None
        self._level_number = None
        self._root = None
        self._parent = None
        self._is_leaf = None
        self._check_items = None
        self.discriminator = None

        self.uuid = uuid
        self.serial_number = serial_number
        self.level_number = level_number
        self.root = root
        self.parent = parent
        if is_leaf is not None:
            self.is_leaf = is_leaf
        if check_items is not None:
            self.check_items = check_items

    @property
    def uuid(self):
        r"""Gets the uuid of this BaselineCatalogModel.

        目录ID唯一标识，UUID

        :return: The uuid of this BaselineCatalogModel.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this BaselineCatalogModel.

        目录ID唯一标识，UUID

        :param uuid: The uuid of this BaselineCatalogModel.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def serial_number(self):
        r"""Gets the serial_number of this BaselineCatalogModel.

        目录的位置顺序

        :return: The serial_number of this BaselineCatalogModel.
        :rtype: int
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this BaselineCatalogModel.

        目录的位置顺序

        :param serial_number: The serial_number of this BaselineCatalogModel.
        :type serial_number: int
        """
        self._serial_number = serial_number

    @property
    def level_number(self):
        r"""Gets the level_number of this BaselineCatalogModel.

        目录的层级关系

        :return: The level_number of this BaselineCatalogModel.
        :rtype: int
        """
        return self._level_number

    @level_number.setter
    def level_number(self, level_number):
        r"""Sets the level_number of this BaselineCatalogModel.

        目录的层级关系

        :param level_number: The level_number of this BaselineCatalogModel.
        :type level_number: int
        """
        self._level_number = level_number

    @property
    def root(self):
        r"""Gets the root of this BaselineCatalogModel.

        该目录所在遵从包UUID

        :return: The root of this BaselineCatalogModel.
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        r"""Sets the root of this BaselineCatalogModel.

        该目录所在遵从包UUID

        :param root: The root of this BaselineCatalogModel.
        :type root: str
        """
        self._root = root

    @property
    def parent(self):
        r"""Gets the parent of this BaselineCatalogModel.

        该目录的父目录UUID，如果等于为第一层目录，则为遵从包UUID

        :return: The parent of this BaselineCatalogModel.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        r"""Sets the parent of this BaselineCatalogModel.

        该目录的父目录UUID，如果等于为第一层目录，则为遵从包UUID

        :param parent: The parent of this BaselineCatalogModel.
        :type parent: str
        """
        self._parent = parent

    @property
    def is_leaf(self):
        r"""Gets the is_leaf of this BaselineCatalogModel.

        该目录是否是叶子节点 0：不是 1：是

        :return: The is_leaf of this BaselineCatalogModel.
        :rtype: bool
        """
        return self._is_leaf

    @is_leaf.setter
    def is_leaf(self, is_leaf):
        r"""Sets the is_leaf of this BaselineCatalogModel.

        该目录是否是叶子节点 0：不是 1：是

        :param is_leaf: The is_leaf of this BaselineCatalogModel.
        :type is_leaf: bool
        """
        self._is_leaf = is_leaf

    @property
    def check_items(self):
        r"""Gets the check_items of this BaselineCatalogModel.

        目录关联的检查项

        :return: The check_items of this BaselineCatalogModel.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.CheckitemCatalogModel`]
        """
        return self._check_items

    @check_items.setter
    def check_items(self, check_items):
        r"""Sets the check_items of this BaselineCatalogModel.

        目录关联的检查项

        :param check_items: The check_items of this BaselineCatalogModel.
        :type check_items: list[:class:`huaweicloudsdksecmaster.v2.CheckitemCatalogModel`]
        """
        self._check_items = check_items

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
        if not isinstance(other, BaselineCatalogModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
