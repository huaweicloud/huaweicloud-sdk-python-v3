# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamespaceBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'path': 'str',
        'develop_mode': 'str',
        'kind': 'str',
        'full_path': 'str',
        'full_name': 'str',
        'parent_id': 'int',
        'visibility_level': 'int',
        'enable_file_control': 'bool',
        'owner_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'develop_mode': 'develop_mode',
        'kind': 'kind',
        'full_path': 'full_path',
        'full_name': 'full_name',
        'parent_id': 'parent_id',
        'visibility_level': 'visibility_level',
        'enable_file_control': 'enable_file_control',
        'owner_id': 'owner_id'
    }

    def __init__(self, id=None, name=None, path=None, develop_mode=None, kind=None, full_path=None, full_name=None, parent_id=None, visibility_level=None, enable_file_control=None, owner_id=None):
        r"""NamespaceBasicDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 命名空间ID。 **约束限制：** 不涉及。
        :type id: int
        :param name: **参数解释：** 命名空间名称。 **约束限制：** 不涉及。
        :type name: str
        :param path: **参数解释：** 路径。 **约束限制：** 不涉及。
        :type path: str
        :param develop_mode: **参数解释：** 开发模式。 **约束限制：** 不涉及。
        :type develop_mode: str
        :param kind: **参数解释：** 类型。 **约束限制：** 不涉及。
        :type kind: str
        :param full_path: **参数解释：** 完整路径。 **约束限制：** 不涉及。
        :type full_path: str
        :param full_name: **参数解释：** 完整名称。 **约束限制：** 不涉及。
        :type full_name: str
        :param parent_id: **参数解释：** 父级ID。 **约束限制：** 不涉及。
        :type parent_id: int
        :param visibility_level: **参数解释：** 可见级别。 **约束限制：** 不涉及。
        :type visibility_level: int
        :param enable_file_control: **参数解释：** 开启文件权限控制。 **约束限制：** 不涉及。
        :type enable_file_control: bool
        :param owner_id: **参数解释：** 所有人ID。 **约束限制：** 不涉及。
        :type owner_id: int
        """
        
        

        self._id = None
        self._name = None
        self._path = None
        self._develop_mode = None
        self._kind = None
        self._full_path = None
        self._full_name = None
        self._parent_id = None
        self._visibility_level = None
        self._enable_file_control = None
        self._owner_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if kind is not None:
            self.kind = kind
        if full_path is not None:
            self.full_path = full_path
        if full_name is not None:
            self.full_name = full_name
        if parent_id is not None:
            self.parent_id = parent_id
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if enable_file_control is not None:
            self.enable_file_control = enable_file_control
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def id(self):
        r"""Gets the id of this NamespaceBasicDto.

        **参数解释：** 命名空间ID。 **约束限制：** 不涉及。

        :return: The id of this NamespaceBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NamespaceBasicDto.

        **参数解释：** 命名空间ID。 **约束限制：** 不涉及。

        :param id: The id of this NamespaceBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NamespaceBasicDto.

        **参数解释：** 命名空间名称。 **约束限制：** 不涉及。

        :return: The name of this NamespaceBasicDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NamespaceBasicDto.

        **参数解释：** 命名空间名称。 **约束限制：** 不涉及。

        :param name: The name of this NamespaceBasicDto.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this NamespaceBasicDto.

        **参数解释：** 路径。 **约束限制：** 不涉及。

        :return: The path of this NamespaceBasicDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this NamespaceBasicDto.

        **参数解释：** 路径。 **约束限制：** 不涉及。

        :param path: The path of this NamespaceBasicDto.
        :type path: str
        """
        self._path = path

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this NamespaceBasicDto.

        **参数解释：** 开发模式。 **约束限制：** 不涉及。

        :return: The develop_mode of this NamespaceBasicDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this NamespaceBasicDto.

        **参数解释：** 开发模式。 **约束限制：** 不涉及。

        :param develop_mode: The develop_mode of this NamespaceBasicDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def kind(self):
        r"""Gets the kind of this NamespaceBasicDto.

        **参数解释：** 类型。 **约束限制：** 不涉及。

        :return: The kind of this NamespaceBasicDto.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this NamespaceBasicDto.

        **参数解释：** 类型。 **约束限制：** 不涉及。

        :param kind: The kind of this NamespaceBasicDto.
        :type kind: str
        """
        self._kind = kind

    @property
    def full_path(self):
        r"""Gets the full_path of this NamespaceBasicDto.

        **参数解释：** 完整路径。 **约束限制：** 不涉及。

        :return: The full_path of this NamespaceBasicDto.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this NamespaceBasicDto.

        **参数解释：** 完整路径。 **约束限制：** 不涉及。

        :param full_path: The full_path of this NamespaceBasicDto.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def full_name(self):
        r"""Gets the full_name of this NamespaceBasicDto.

        **参数解释：** 完整名称。 **约束限制：** 不涉及。

        :return: The full_name of this NamespaceBasicDto.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this NamespaceBasicDto.

        **参数解释：** 完整名称。 **约束限制：** 不涉及。

        :param full_name: The full_name of this NamespaceBasicDto.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this NamespaceBasicDto.

        **参数解释：** 父级ID。 **约束限制：** 不涉及。

        :return: The parent_id of this NamespaceBasicDto.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this NamespaceBasicDto.

        **参数解释：** 父级ID。 **约束限制：** 不涉及。

        :param parent_id: The parent_id of this NamespaceBasicDto.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def visibility_level(self):
        r"""Gets the visibility_level of this NamespaceBasicDto.

        **参数解释：** 可见级别。 **约束限制：** 不涉及。

        :return: The visibility_level of this NamespaceBasicDto.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        r"""Sets the visibility_level of this NamespaceBasicDto.

        **参数解释：** 可见级别。 **约束限制：** 不涉及。

        :param visibility_level: The visibility_level of this NamespaceBasicDto.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def enable_file_control(self):
        r"""Gets the enable_file_control of this NamespaceBasicDto.

        **参数解释：** 开启文件权限控制。 **约束限制：** 不涉及。

        :return: The enable_file_control of this NamespaceBasicDto.
        :rtype: bool
        """
        return self._enable_file_control

    @enable_file_control.setter
    def enable_file_control(self, enable_file_control):
        r"""Sets the enable_file_control of this NamespaceBasicDto.

        **参数解释：** 开启文件权限控制。 **约束限制：** 不涉及。

        :param enable_file_control: The enable_file_control of this NamespaceBasicDto.
        :type enable_file_control: bool
        """
        self._enable_file_control = enable_file_control

    @property
    def owner_id(self):
        r"""Gets the owner_id of this NamespaceBasicDto.

        **参数解释：** 所有人ID。 **约束限制：** 不涉及。

        :return: The owner_id of this NamespaceBasicDto.
        :rtype: int
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this NamespaceBasicDto.

        **参数解释：** 所有人ID。 **约束限制：** 不涉及。

        :param owner_id: The owner_id of this NamespaceBasicDto.
        :type owner_id: int
        """
        self._owner_id = owner_id

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
        if not isinstance(other, NamespaceBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
