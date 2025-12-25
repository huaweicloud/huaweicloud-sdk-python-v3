# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileTreeResultChildren:

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
        'uri': 'str',
        'path': 'str',
        'modified': 'str',
        'folder': 'bool',
        'modified_by': 'str',
        'has_child': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'uri': 'uri',
        'path': 'path',
        'modified': 'modified',
        'folder': 'folder',
        'modified_by': 'modified_by',
        'has_child': 'has_child'
    }

    def __init__(self, name=None, uri=None, path=None, modified=None, folder=None, modified_by=None, has_child=None):
        r"""ShowFileTreeResultChildren

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 文件或文件夹名称。 **取值范围**: 不涉及。 
        :type name: str
        :param uri: **参数解释**: 访问地址。 **取值范围**: 不涉及。 
        :type uri: str
        :param path: **参数解释**: 路径。 **取值范围**: 不涉及。 
        :type path: str
        :param modified: **参数解释**: 更新时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。 
        :type modified: str
        :param folder: **参数解释**: 是否为文件夹。 **取值范围**: true：文件夹。 false：文件。 
        :type folder: bool
        :param modified_by: **参数解释**: 修改人。 **取值范围**: 不涉及。 
        :type modified_by: str
        :param has_child: **参数解释**: 是否存在下一层。 **取值范围**: true：是。 false：否。 
        :type has_child: bool
        """
        
        

        self._name = None
        self._uri = None
        self._path = None
        self._modified = None
        self._folder = None
        self._modified_by = None
        self._has_child = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if uri is not None:
            self.uri = uri
        if path is not None:
            self.path = path
        if modified is not None:
            self.modified = modified
        if folder is not None:
            self.folder = folder
        if modified_by is not None:
            self.modified_by = modified_by
        if has_child is not None:
            self.has_child = has_child

    @property
    def name(self):
        r"""Gets the name of this ShowFileTreeResultChildren.

        **参数解释**: 文件或文件夹名称。 **取值范围**: 不涉及。 

        :return: The name of this ShowFileTreeResultChildren.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowFileTreeResultChildren.

        **参数解释**: 文件或文件夹名称。 **取值范围**: 不涉及。 

        :param name: The name of this ShowFileTreeResultChildren.
        :type name: str
        """
        self._name = name

    @property
    def uri(self):
        r"""Gets the uri of this ShowFileTreeResultChildren.

        **参数解释**: 访问地址。 **取值范围**: 不涉及。 

        :return: The uri of this ShowFileTreeResultChildren.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ShowFileTreeResultChildren.

        **参数解释**: 访问地址。 **取值范围**: 不涉及。 

        :param uri: The uri of this ShowFileTreeResultChildren.
        :type uri: str
        """
        self._uri = uri

    @property
    def path(self):
        r"""Gets the path of this ShowFileTreeResultChildren.

        **参数解释**: 路径。 **取值范围**: 不涉及。 

        :return: The path of this ShowFileTreeResultChildren.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowFileTreeResultChildren.

        **参数解释**: 路径。 **取值范围**: 不涉及。 

        :param path: The path of this ShowFileTreeResultChildren.
        :type path: str
        """
        self._path = path

    @property
    def modified(self):
        r"""Gets the modified of this ShowFileTreeResultChildren.

        **参数解释**: 更新时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。 

        :return: The modified of this ShowFileTreeResultChildren.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        r"""Sets the modified of this ShowFileTreeResultChildren.

        **参数解释**: 更新时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。 

        :param modified: The modified of this ShowFileTreeResultChildren.
        :type modified: str
        """
        self._modified = modified

    @property
    def folder(self):
        r"""Gets the folder of this ShowFileTreeResultChildren.

        **参数解释**: 是否为文件夹。 **取值范围**: true：文件夹。 false：文件。 

        :return: The folder of this ShowFileTreeResultChildren.
        :rtype: bool
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        r"""Sets the folder of this ShowFileTreeResultChildren.

        **参数解释**: 是否为文件夹。 **取值范围**: true：文件夹。 false：文件。 

        :param folder: The folder of this ShowFileTreeResultChildren.
        :type folder: bool
        """
        self._folder = folder

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ShowFileTreeResultChildren.

        **参数解释**: 修改人。 **取值范围**: 不涉及。 

        :return: The modified_by of this ShowFileTreeResultChildren.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ShowFileTreeResultChildren.

        **参数解释**: 修改人。 **取值范围**: 不涉及。 

        :param modified_by: The modified_by of this ShowFileTreeResultChildren.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def has_child(self):
        r"""Gets the has_child of this ShowFileTreeResultChildren.

        **参数解释**: 是否存在下一层。 **取值范围**: true：是。 false：否。 

        :return: The has_child of this ShowFileTreeResultChildren.
        :rtype: bool
        """
        return self._has_child

    @has_child.setter
    def has_child(self, has_child):
        r"""Sets the has_child of this ShowFileTreeResultChildren.

        **参数解释**: 是否存在下一层。 **取值范围**: true：是。 false：否。 

        :param has_child: The has_child of this ShowFileTreeResultChildren.
        :type has_child: bool
        """
        self._has_child = has_child

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
        if not isinstance(other, ShowFileTreeResultChildren):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
