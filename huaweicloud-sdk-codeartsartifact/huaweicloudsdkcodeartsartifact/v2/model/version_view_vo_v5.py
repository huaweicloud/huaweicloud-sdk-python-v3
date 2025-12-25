# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionViewVoV5:

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
        'project_id': 'str',
        'file_id': 'str',
        'name': 'str',
        'path': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'file_id': 'file_id',
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, id=None, project_id=None, file_id=None, name=None, path=None):
        r"""VersionViewVoV5

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id。 **取值范围**: 不涉及。 
        :type id: str
        :param project_id: **参数解释**: 项目id。 **取值范围**: 不涉及。 
        :type project_id: str
        :param file_id: **参数解释**: 文件id。 **取值范围**: 不涉及。 
        :type file_id: str
        :param name: **参数解释**: 文件名。 **取值范围**: 不涉及。 
        :type name: str
        :param path: **参数解释**: 文件路径。 **取值范围**: 不涉及。 
        :type path: str
        """
        
        

        self._id = None
        self._project_id = None
        self._file_id = None
        self._name = None
        self._path = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if file_id is not None:
            self.file_id = file_id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path

    @property
    def id(self):
        r"""Gets the id of this VersionViewVoV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :return: The id of this VersionViewVoV5.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VersionViewVoV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :param id: The id of this VersionViewVoV5.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this VersionViewVoV5.

        **参数解释**: 项目id。 **取值范围**: 不涉及。 

        :return: The project_id of this VersionViewVoV5.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VersionViewVoV5.

        **参数解释**: 项目id。 **取值范围**: 不涉及。 

        :param project_id: The project_id of this VersionViewVoV5.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def file_id(self):
        r"""Gets the file_id of this VersionViewVoV5.

        **参数解释**: 文件id。 **取值范围**: 不涉及。 

        :return: The file_id of this VersionViewVoV5.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this VersionViewVoV5.

        **参数解释**: 文件id。 **取值范围**: 不涉及。 

        :param file_id: The file_id of this VersionViewVoV5.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def name(self):
        r"""Gets the name of this VersionViewVoV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :return: The name of this VersionViewVoV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VersionViewVoV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :param name: The name of this VersionViewVoV5.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this VersionViewVoV5.

        **参数解释**: 文件路径。 **取值范围**: 不涉及。 

        :return: The path of this VersionViewVoV5.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this VersionViewVoV5.

        **参数解释**: 文件路径。 **取值范围**: 不涉及。 

        :param path: The path of this VersionViewVoV5.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, VersionViewVoV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
