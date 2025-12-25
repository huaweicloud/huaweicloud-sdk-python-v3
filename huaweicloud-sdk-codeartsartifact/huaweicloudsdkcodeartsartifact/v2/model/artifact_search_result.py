# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArtifactSearchResult:

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
        'relative_path': 'str',
        'repo': 'str',
        'repo_name': 'str',
        'display_name': 'str',
        'repo_type': 'str',
        'created_by': 'str',
        'created_user_name': 'str',
        'created': 'str',
        'modified': 'str',
        'old_repo_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'relative_path': 'relativePath',
        'repo': 'repo',
        'repo_name': 'repoName',
        'display_name': 'displayName',
        'repo_type': 'repoType',
        'created_by': 'createdBy',
        'created_user_name': 'createdUserName',
        'created': 'created',
        'modified': 'modified',
        'old_repo_id': 'oldRepoId'
    }

    def __init__(self, name=None, relative_path=None, repo=None, repo_name=None, display_name=None, repo_type=None, created_by=None, created_user_name=None, created=None, modified=None, old_repo_id=None):
        r"""ArtifactSearchResult

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 文件名。 **取值范围**： 不涉及。 
        :type name: str
        :param relative_path: **参数解释**： 文件相对路径。 **取值范围**： 不涉及。 
        :type relative_path: str
        :param repo: **参数解释**： 仓库ID。 **取值范围**： 不涉及。 
        :type repo: str
        :param repo_name: **参数解释**： 仓库名。 **取值范围**： 不涉及。 
        :type repo_name: str
        :param display_name: **参数解释**： 展示名称。 **取值范围**： 不涉及。 
        :type display_name: str
        :param repo_type: **参数解释**： 制品类型。 **取值范围**： 不涉及。 
        :type repo_type: str
        :param created_by: **参数解释**： 创建人ID。 **取值范围**： 不涉及。 
        :type created_by: str
        :param created_user_name: **参数解释**： 创建人名称。 **取值范围**： 不涉及。 
        :type created_user_name: str
        :param created: **参数解释**： 创建时间。 **取值范围**： 不涉及。 
        :type created: str
        :param modified: **参数解释**： 修改时间。 **取值范围**： 不涉及。 
        :type modified: str
        :param old_repo_id: **参数解释**： 旧仓库ID。 **取值范围**： 不涉及。 
        :type old_repo_id: str
        """
        
        

        self._name = None
        self._relative_path = None
        self._repo = None
        self._repo_name = None
        self._display_name = None
        self._repo_type = None
        self._created_by = None
        self._created_user_name = None
        self._created = None
        self._modified = None
        self._old_repo_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if relative_path is not None:
            self.relative_path = relative_path
        if repo is not None:
            self.repo = repo
        if repo_name is not None:
            self.repo_name = repo_name
        if display_name is not None:
            self.display_name = display_name
        if repo_type is not None:
            self.repo_type = repo_type
        if created_by is not None:
            self.created_by = created_by
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified
        if old_repo_id is not None:
            self.old_repo_id = old_repo_id

    @property
    def name(self):
        r"""Gets the name of this ArtifactSearchResult.

        **参数解释**： 文件名。 **取值范围**： 不涉及。 

        :return: The name of this ArtifactSearchResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArtifactSearchResult.

        **参数解释**： 文件名。 **取值范围**： 不涉及。 

        :param name: The name of this ArtifactSearchResult.
        :type name: str
        """
        self._name = name

    @property
    def relative_path(self):
        r"""Gets the relative_path of this ArtifactSearchResult.

        **参数解释**： 文件相对路径。 **取值范围**： 不涉及。 

        :return: The relative_path of this ArtifactSearchResult.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        r"""Sets the relative_path of this ArtifactSearchResult.

        **参数解释**： 文件相对路径。 **取值范围**： 不涉及。 

        :param relative_path: The relative_path of this ArtifactSearchResult.
        :type relative_path: str
        """
        self._relative_path = relative_path

    @property
    def repo(self):
        r"""Gets the repo of this ArtifactSearchResult.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。 

        :return: The repo of this ArtifactSearchResult.
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        r"""Sets the repo of this ArtifactSearchResult.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。 

        :param repo: The repo of this ArtifactSearchResult.
        :type repo: str
        """
        self._repo = repo

    @property
    def repo_name(self):
        r"""Gets the repo_name of this ArtifactSearchResult.

        **参数解释**： 仓库名。 **取值范围**： 不涉及。 

        :return: The repo_name of this ArtifactSearchResult.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this ArtifactSearchResult.

        **参数解释**： 仓库名。 **取值范围**： 不涉及。 

        :param repo_name: The repo_name of this ArtifactSearchResult.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def display_name(self):
        r"""Gets the display_name of this ArtifactSearchResult.

        **参数解释**： 展示名称。 **取值范围**： 不涉及。 

        :return: The display_name of this ArtifactSearchResult.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ArtifactSearchResult.

        **参数解释**： 展示名称。 **取值范围**： 不涉及。 

        :param display_name: The display_name of this ArtifactSearchResult.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def repo_type(self):
        r"""Gets the repo_type of this ArtifactSearchResult.

        **参数解释**： 制品类型。 **取值范围**： 不涉及。 

        :return: The repo_type of this ArtifactSearchResult.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this ArtifactSearchResult.

        **参数解释**： 制品类型。 **取值范围**： 不涉及。 

        :param repo_type: The repo_type of this ArtifactSearchResult.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def created_by(self):
        r"""Gets the created_by of this ArtifactSearchResult.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。 

        :return: The created_by of this ArtifactSearchResult.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ArtifactSearchResult.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。 

        :param created_by: The created_by of this ArtifactSearchResult.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this ArtifactSearchResult.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。 

        :return: The created_user_name of this ArtifactSearchResult.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this ArtifactSearchResult.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。 

        :param created_user_name: The created_user_name of this ArtifactSearchResult.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def created(self):
        r"""Gets the created of this ArtifactSearchResult.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :return: The created of this ArtifactSearchResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ArtifactSearchResult.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。 

        :param created: The created of this ArtifactSearchResult.
        :type created: str
        """
        self._created = created

    @property
    def modified(self):
        r"""Gets the modified of this ArtifactSearchResult.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。 

        :return: The modified of this ArtifactSearchResult.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        r"""Sets the modified of this ArtifactSearchResult.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。 

        :param modified: The modified of this ArtifactSearchResult.
        :type modified: str
        """
        self._modified = modified

    @property
    def old_repo_id(self):
        r"""Gets the old_repo_id of this ArtifactSearchResult.

        **参数解释**： 旧仓库ID。 **取值范围**： 不涉及。 

        :return: The old_repo_id of this ArtifactSearchResult.
        :rtype: str
        """
        return self._old_repo_id

    @old_repo_id.setter
    def old_repo_id(self, old_repo_id):
        r"""Sets the old_repo_id of this ArtifactSearchResult.

        **参数解释**： 旧仓库ID。 **取值范围**： 不涉及。 

        :param old_repo_id: The old_repo_id of this ArtifactSearchResult.
        :type old_repo_id: str
        """
        self._old_repo_id = old_repo_id

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
        if not isinstance(other, ArtifactSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
