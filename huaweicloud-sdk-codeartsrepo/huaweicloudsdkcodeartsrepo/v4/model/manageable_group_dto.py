# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManageableGroupDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_name': 'str',
        'id': 'int',
        'name': 'str',
        'full_path': 'str',
        'path': 'str',
        'visibility': 'str'
    }

    attribute_map = {
        'full_name': 'full_name',
        'id': 'id',
        'name': 'name',
        'full_path': 'full_path',
        'path': 'path',
        'visibility': 'visibility'
    }

    def __init__(self, full_name=None, id=None, name=None, full_path=None, path=None, visibility=None):
        r"""ManageableGroupDto

        The model defined in huaweicloud sdk

        :param full_name: **参数解释：** 代码组全名。
        :type full_name: str
        :param id: **参数解释：** 代码组id。
        :type id: int
        :param name: **参数解释：** 代码组名。 **取值范围：** 字符串长度不少于0，不超过256。
        :type name: str
        :param full_path: **参数解释：** 全路径。 **取值范围：** 字符串长度不少于0，不超过1000。
        :type full_path: str
        :param path: **参数解释：** 路径。 **取值范围：** 字符串长度不少于0，不超过1000。
        :type path: str
        :param visibility: **参数解释：** 可见性。 **取值范围：** private public。
        :type visibility: str
        """
        
        

        self._full_name = None
        self._id = None
        self._name = None
        self._full_path = None
        self._path = None
        self._visibility = None
        self.discriminator = None

        if full_name is not None:
            self.full_name = full_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if full_path is not None:
            self.full_path = full_path
        if path is not None:
            self.path = path
        if visibility is not None:
            self.visibility = visibility

    @property
    def full_name(self):
        r"""Gets the full_name of this ManageableGroupDto.

        **参数解释：** 代码组全名。

        :return: The full_name of this ManageableGroupDto.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this ManageableGroupDto.

        **参数解释：** 代码组全名。

        :param full_name: The full_name of this ManageableGroupDto.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def id(self):
        r"""Gets the id of this ManageableGroupDto.

        **参数解释：** 代码组id。

        :return: The id of this ManageableGroupDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ManageableGroupDto.

        **参数解释：** 代码组id。

        :param id: The id of this ManageableGroupDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ManageableGroupDto.

        **参数解释：** 代码组名。 **取值范围：** 字符串长度不少于0，不超过256。

        :return: The name of this ManageableGroupDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ManageableGroupDto.

        **参数解释：** 代码组名。 **取值范围：** 字符串长度不少于0，不超过256。

        :param name: The name of this ManageableGroupDto.
        :type name: str
        """
        self._name = name

    @property
    def full_path(self):
        r"""Gets the full_path of this ManageableGroupDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于0，不超过1000。

        :return: The full_path of this ManageableGroupDto.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this ManageableGroupDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于0，不超过1000。

        :param full_path: The full_path of this ManageableGroupDto.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def path(self):
        r"""Gets the path of this ManageableGroupDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于0，不超过1000。

        :return: The path of this ManageableGroupDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ManageableGroupDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于0，不超过1000。

        :param path: The path of this ManageableGroupDto.
        :type path: str
        """
        self._path = path

    @property
    def visibility(self):
        r"""Gets the visibility of this ManageableGroupDto.

        **参数解释：** 可见性。 **取值范围：** private public。

        :return: The visibility of this ManageableGroupDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ManageableGroupDto.

        **参数解释：** 可见性。 **取值范围：** private public。

        :param visibility: The visibility of this ManageableGroupDto.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ManageableGroupDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
