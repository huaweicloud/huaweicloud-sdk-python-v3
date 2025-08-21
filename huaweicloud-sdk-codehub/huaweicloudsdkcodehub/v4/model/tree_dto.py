# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TreeDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'path': 'str',
        'level': 'int',
        'is_shown_drop_down': 'bool',
        'folder': 'bool',
        'children': 'list[TreeDto]',
        'submodule_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'path': 'path',
        'level': 'level',
        'is_shown_drop_down': 'isShownDropDown',
        'folder': 'folder',
        'children': 'children',
        'submodule_link': 'submodule_link'
    }

    def __init__(self, id=None, name=None, type=None, path=None, level=None, is_shown_drop_down=None, folder=None, children=None, submodule_link=None):
        r"""TreeDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 提交ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 文件名称。 **取值范围：** 不涉及。
        :type name: str
        :param type: **参数解释：** 文件结构。 **取值范围：** - commit, 子模块。 - tree, 目录。 - blob, 文件
        :type type: str
        :param path: **参数解释：** 文件路径。 **取值范围：** 不涉及
        :type path: str
        :param level: **参数解释：** 当前所在目录层级。 **取值范围：** 不涉及
        :type level: int
        :param is_shown_drop_down: **参数解释：** 是否下拉。 **取值范围：** - false, 不下拉。 - true, 下拉
        :type is_shown_drop_down: bool
        :param folder: **参数解释：** 是否折叠。 **取值范围：** - false, 不折叠。 - true, 折叠。
        :type folder: bool
        :param children: 子节点
        :type children: list[:class:`huaweicloudsdkcodehub.v4.TreeDto`]
        :param submodule_link: **参数解释：** 子模块连接。 **取值范围：** 不涉及。
        :type submodule_link: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._path = None
        self._level = None
        self._is_shown_drop_down = None
        self._folder = None
        self._children = None
        self._submodule_link = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if level is not None:
            self.level = level
        if is_shown_drop_down is not None:
            self.is_shown_drop_down = is_shown_drop_down
        if folder is not None:
            self.folder = folder
        if children is not None:
            self.children = children
        if submodule_link is not None:
            self.submodule_link = submodule_link

    @property
    def id(self):
        r"""Gets the id of this TreeDto.

        **参数解释：** 提交ID。 **取值范围：** 不涉及。

        :return: The id of this TreeDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TreeDto.

        **参数解释：** 提交ID。 **取值范围：** 不涉及。

        :param id: The id of this TreeDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TreeDto.

        **参数解释：** 文件名称。 **取值范围：** 不涉及。

        :return: The name of this TreeDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TreeDto.

        **参数解释：** 文件名称。 **取值范围：** 不涉及。

        :param name: The name of this TreeDto.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this TreeDto.

        **参数解释：** 文件结构。 **取值范围：** - commit, 子模块。 - tree, 目录。 - blob, 文件

        :return: The type of this TreeDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TreeDto.

        **参数解释：** 文件结构。 **取值范围：** - commit, 子模块。 - tree, 目录。 - blob, 文件

        :param type: The type of this TreeDto.
        :type type: str
        """
        self._type = type

    @property
    def path(self):
        r"""Gets the path of this TreeDto.

        **参数解释：** 文件路径。 **取值范围：** 不涉及

        :return: The path of this TreeDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this TreeDto.

        **参数解释：** 文件路径。 **取值范围：** 不涉及

        :param path: The path of this TreeDto.
        :type path: str
        """
        self._path = path

    @property
    def level(self):
        r"""Gets the level of this TreeDto.

        **参数解释：** 当前所在目录层级。 **取值范围：** 不涉及

        :return: The level of this TreeDto.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this TreeDto.

        **参数解释：** 当前所在目录层级。 **取值范围：** 不涉及

        :param level: The level of this TreeDto.
        :type level: int
        """
        self._level = level

    @property
    def is_shown_drop_down(self):
        r"""Gets the is_shown_drop_down of this TreeDto.

        **参数解释：** 是否下拉。 **取值范围：** - false, 不下拉。 - true, 下拉

        :return: The is_shown_drop_down of this TreeDto.
        :rtype: bool
        """
        return self._is_shown_drop_down

    @is_shown_drop_down.setter
    def is_shown_drop_down(self, is_shown_drop_down):
        r"""Sets the is_shown_drop_down of this TreeDto.

        **参数解释：** 是否下拉。 **取值范围：** - false, 不下拉。 - true, 下拉

        :param is_shown_drop_down: The is_shown_drop_down of this TreeDto.
        :type is_shown_drop_down: bool
        """
        self._is_shown_drop_down = is_shown_drop_down

    @property
    def folder(self):
        r"""Gets the folder of this TreeDto.

        **参数解释：** 是否折叠。 **取值范围：** - false, 不折叠。 - true, 折叠。

        :return: The folder of this TreeDto.
        :rtype: bool
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        r"""Sets the folder of this TreeDto.

        **参数解释：** 是否折叠。 **取值范围：** - false, 不折叠。 - true, 折叠。

        :param folder: The folder of this TreeDto.
        :type folder: bool
        """
        self._folder = folder

    @property
    def children(self):
        r"""Gets the children of this TreeDto.

        子节点

        :return: The children of this TreeDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.TreeDto`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this TreeDto.

        子节点

        :param children: The children of this TreeDto.
        :type children: list[:class:`huaweicloudsdkcodehub.v4.TreeDto`]
        """
        self._children = children

    @property
    def submodule_link(self):
        r"""Gets the submodule_link of this TreeDto.

        **参数解释：** 子模块连接。 **取值范围：** 不涉及。

        :return: The submodule_link of this TreeDto.
        :rtype: str
        """
        return self._submodule_link

    @submodule_link.setter
    def submodule_link(self, submodule_link):
        r"""Sets the submodule_link of this TreeDto.

        **参数解释：** 子模块连接。 **取值范围：** 不涉及。

        :param submodule_link: The submodule_link of this TreeDto.
        :type submodule_link: str
        """
        self._submodule_link = submodule_link

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
        if not isinstance(other, TreeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
