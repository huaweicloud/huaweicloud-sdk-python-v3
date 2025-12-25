# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDirectoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'directories': 'list[str]',
        'directory_i18ns': 'list[DirectoryI18N]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'directories': 'directories',
        'directory_i18ns': 'directory_i18ns'
    }

    def __init__(self, project_id=None, workspace_id=None, directories=None, directory_i18ns=None):
        r"""ListDirectoriesResponse

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param directories: 目录列表
        :type directories: list[str]
        :param directory_i18ns: 目录I18N列表
        :type directory_i18ns: list[:class:`huaweicloudsdksecmaster.v2.DirectoryI18N`]
        """
        
        super().__init__()

        self._project_id = None
        self._workspace_id = None
        self._directories = None
        self._directory_i18ns = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if directories is not None:
            self.directories = directories
        if directory_i18ns is not None:
            self.directory_i18ns = directory_i18ns

    @property
    def project_id(self):
        r"""Gets the project_id of this ListDirectoriesResponse.

        项目ID

        :return: The project_id of this ListDirectoriesResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListDirectoriesResponse.

        项目ID

        :param project_id: The project_id of this ListDirectoriesResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListDirectoriesResponse.

        工作空间ID

        :return: The workspace_id of this ListDirectoriesResponse.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListDirectoriesResponse.

        工作空间ID

        :param workspace_id: The workspace_id of this ListDirectoriesResponse.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def directories(self):
        r"""Gets the directories of this ListDirectoriesResponse.

        目录列表

        :return: The directories of this ListDirectoriesResponse.
        :rtype: list[str]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        r"""Sets the directories of this ListDirectoriesResponse.

        目录列表

        :param directories: The directories of this ListDirectoriesResponse.
        :type directories: list[str]
        """
        self._directories = directories

    @property
    def directory_i18ns(self):
        r"""Gets the directory_i18ns of this ListDirectoriesResponse.

        目录I18N列表

        :return: The directory_i18ns of this ListDirectoriesResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.DirectoryI18N`]
        """
        return self._directory_i18ns

    @directory_i18ns.setter
    def directory_i18ns(self, directory_i18ns):
        r"""Sets the directory_i18ns of this ListDirectoriesResponse.

        目录I18N列表

        :param directory_i18ns: The directory_i18ns of this ListDirectoriesResponse.
        :type directory_i18ns: list[:class:`huaweicloudsdksecmaster.v2.DirectoryI18N`]
        """
        self._directory_i18ns = directory_i18ns

    def to_dict(self):
        import warnings
        warnings.warn("ListDirectoriesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListDirectoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
