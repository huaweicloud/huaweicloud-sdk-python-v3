# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoFileDOV5:

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
        'file_id': 'str',
        'repo_name': 'str',
        'project_name': 'str',
        'parent_id': 'str',
        'name': 'str',
        'file_name': 'str',
        'type': 'str',
        'category': 'str',
        'extension': 'str',
        'path': 'str',
        'full_path': 'str',
        'size': 'int',
        'md5': 'str',
        'sha256': 'str',
        'download_url': 'str',
        'download_url_with_id': 'str',
        'web_url': 'str',
        'version_enable': 'bool',
        'migrated_state': 'int',
        'upload_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_id': 'file_id',
        'repo_name': 'repo_name',
        'project_name': 'project_name',
        'parent_id': 'parent_id',
        'name': 'name',
        'file_name': 'file_name',
        'type': 'type',
        'category': 'category',
        'extension': 'extension',
        'path': 'path',
        'full_path': 'full_path',
        'size': 'size',
        'md5': 'md5',
        'sha256': 'sha256',
        'download_url': 'download_url',
        'download_url_with_id': 'download_url_with_id',
        'web_url': 'web_url',
        'version_enable': 'version_enable',
        'migrated_state': 'migrated_state',
        'upload_id': 'upload_id'
    }

    def __init__(self, id=None, file_id=None, repo_name=None, project_name=None, parent_id=None, name=None, file_name=None, type=None, category=None, extension=None, path=None, full_path=None, size=None, md5=None, sha256=None, download_url=None, download_url_with_id=None, web_url=None, version_enable=None, migrated_state=None, upload_id=None):
        r"""RepoFileDOV5

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id。 **取值范围**: 不涉及。 
        :type id: str
        :param file_id: **参数解释**: 文件id。 **取值范围**: 不涉及。 
        :type file_id: str
        :param repo_name: **参数解释**: 仓库id。 **取值范围**: 不涉及。 
        :type repo_name: str
        :param project_name: **参数解释**: 项目名称。 **取值范围**: 不涉及。 
        :type project_name: str
        :param parent_id: **参数解释**: 父级目录ID。 **取值范围**: 不涉及。 
        :type parent_id: str
        :param name: **参数解释**: 文件名。 **取值范围**: 不涉及。 
        :type name: str
        :param file_name: **参数解释**: 文件名。 **取值范围**: 不涉及。 
        :type file_name: str
        :param type: **参数解释**: 文件类型, folder代表是目录,file代表文件。 **取值范围**: 不涉及。 
        :type type: str
        :param category: **参数解释**: 发布包状态 test为测试包 prod为发布包。 **取值范围**: 不涉及。 
        :type category: str
        :param extension: **参数解释**: 文件扩展名。 **取值范围**: 不涉及。 
        :type extension: str
        :param path: **参数解释**: 文件路径。 **取值范围**: 不涉及。 
        :type path: str
        :param full_path: **参数解释**: 文件路径(含项目)。 **取值范围**: 不涉及。 
        :type full_path: str
        :param size: **参数解释**: 文件大小,单位为byte。 **取值范围**: 不涉及。 
        :type size: int
        :param md5: **参数解释**: md5校验和。 **取值范围**: 不涉及。 
        :type md5: str
        :param sha256: **参数解释**: sha256校验和。 **取值范围**: 不涉及。 
        :type sha256: str
        :param download_url: **参数解释**: 下载地址。 **取值范围**: 不涉及。 
        :type download_url: str
        :param download_url_with_id: **参数解释**: 带有id的下载地址。 **取值范围**: 不涉及。 
        :type download_url_with_id: str
        :param web_url: **参数解释**: 历史版本遗留字段，请忽略。 **取值范围**: 不涉及。 
        :type web_url: str
        :param version_enable: **参数解释**: 判断当前文件或文件夹父目录是否为版本路径，即仓库下第一层子目录。 **取值范围**: - true：父目录是版本路径。 - false：父目录不是版本路径。 
        :type version_enable: bool
        :param migrated_state: **参数解释**: migrated_state。 **取值范围**: 该参数为内部数据改造参数，无业务含义，请忽略。 
        :type migrated_state: int
        :param upload_id: **参数解释**: 该参数无返回值，请忽略。 **取值范围**: 不涉及。 
        :type upload_id: str
        """
        
        

        self._id = None
        self._file_id = None
        self._repo_name = None
        self._project_name = None
        self._parent_id = None
        self._name = None
        self._file_name = None
        self._type = None
        self._category = None
        self._extension = None
        self._path = None
        self._full_path = None
        self._size = None
        self._md5 = None
        self._sha256 = None
        self._download_url = None
        self._download_url_with_id = None
        self._web_url = None
        self._version_enable = None
        self._migrated_state = None
        self._upload_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if file_id is not None:
            self.file_id = file_id
        if repo_name is not None:
            self.repo_name = repo_name
        if project_name is not None:
            self.project_name = project_name
        if parent_id is not None:
            self.parent_id = parent_id
        if name is not None:
            self.name = name
        if file_name is not None:
            self.file_name = file_name
        if type is not None:
            self.type = type
        if category is not None:
            self.category = category
        if extension is not None:
            self.extension = extension
        if path is not None:
            self.path = path
        if full_path is not None:
            self.full_path = full_path
        if size is not None:
            self.size = size
        if md5 is not None:
            self.md5 = md5
        if sha256 is not None:
            self.sha256 = sha256
        if download_url is not None:
            self.download_url = download_url
        if download_url_with_id is not None:
            self.download_url_with_id = download_url_with_id
        if web_url is not None:
            self.web_url = web_url
        if version_enable is not None:
            self.version_enable = version_enable
        if migrated_state is not None:
            self.migrated_state = migrated_state
        if upload_id is not None:
            self.upload_id = upload_id

    @property
    def id(self):
        r"""Gets the id of this RepoFileDOV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :return: The id of this RepoFileDOV5.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepoFileDOV5.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :param id: The id of this RepoFileDOV5.
        :type id: str
        """
        self._id = id

    @property
    def file_id(self):
        r"""Gets the file_id of this RepoFileDOV5.

        **参数解释**: 文件id。 **取值范围**: 不涉及。 

        :return: The file_id of this RepoFileDOV5.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this RepoFileDOV5.

        **参数解释**: 文件id。 **取值范围**: 不涉及。 

        :param file_id: The file_id of this RepoFileDOV5.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def repo_name(self):
        r"""Gets the repo_name of this RepoFileDOV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。 

        :return: The repo_name of this RepoFileDOV5.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this RepoFileDOV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。 

        :param repo_name: The repo_name of this RepoFileDOV5.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def project_name(self):
        r"""Gets the project_name of this RepoFileDOV5.

        **参数解释**: 项目名称。 **取值范围**: 不涉及。 

        :return: The project_name of this RepoFileDOV5.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this RepoFileDOV5.

        **参数解释**: 项目名称。 **取值范围**: 不涉及。 

        :param project_name: The project_name of this RepoFileDOV5.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this RepoFileDOV5.

        **参数解释**: 父级目录ID。 **取值范围**: 不涉及。 

        :return: The parent_id of this RepoFileDOV5.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this RepoFileDOV5.

        **参数解释**: 父级目录ID。 **取值范围**: 不涉及。 

        :param parent_id: The parent_id of this RepoFileDOV5.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def name(self):
        r"""Gets the name of this RepoFileDOV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :return: The name of this RepoFileDOV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepoFileDOV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :param name: The name of this RepoFileDOV5.
        :type name: str
        """
        self._name = name

    @property
    def file_name(self):
        r"""Gets the file_name of this RepoFileDOV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :return: The file_name of this RepoFileDOV5.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this RepoFileDOV5.

        **参数解释**: 文件名。 **取值范围**: 不涉及。 

        :param file_name: The file_name of this RepoFileDOV5.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def type(self):
        r"""Gets the type of this RepoFileDOV5.

        **参数解释**: 文件类型, folder代表是目录,file代表文件。 **取值范围**: 不涉及。 

        :return: The type of this RepoFileDOV5.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RepoFileDOV5.

        **参数解释**: 文件类型, folder代表是目录,file代表文件。 **取值范围**: 不涉及。 

        :param type: The type of this RepoFileDOV5.
        :type type: str
        """
        self._type = type

    @property
    def category(self):
        r"""Gets the category of this RepoFileDOV5.

        **参数解释**: 发布包状态 test为测试包 prod为发布包。 **取值范围**: 不涉及。 

        :return: The category of this RepoFileDOV5.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RepoFileDOV5.

        **参数解释**: 发布包状态 test为测试包 prod为发布包。 **取值范围**: 不涉及。 

        :param category: The category of this RepoFileDOV5.
        :type category: str
        """
        self._category = category

    @property
    def extension(self):
        r"""Gets the extension of this RepoFileDOV5.

        **参数解释**: 文件扩展名。 **取值范围**: 不涉及。 

        :return: The extension of this RepoFileDOV5.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this RepoFileDOV5.

        **参数解释**: 文件扩展名。 **取值范围**: 不涉及。 

        :param extension: The extension of this RepoFileDOV5.
        :type extension: str
        """
        self._extension = extension

    @property
    def path(self):
        r"""Gets the path of this RepoFileDOV5.

        **参数解释**: 文件路径。 **取值范围**: 不涉及。 

        :return: The path of this RepoFileDOV5.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this RepoFileDOV5.

        **参数解释**: 文件路径。 **取值范围**: 不涉及。 

        :param path: The path of this RepoFileDOV5.
        :type path: str
        """
        self._path = path

    @property
    def full_path(self):
        r"""Gets the full_path of this RepoFileDOV5.

        **参数解释**: 文件路径(含项目)。 **取值范围**: 不涉及。 

        :return: The full_path of this RepoFileDOV5.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this RepoFileDOV5.

        **参数解释**: 文件路径(含项目)。 **取值范围**: 不涉及。 

        :param full_path: The full_path of this RepoFileDOV5.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def size(self):
        r"""Gets the size of this RepoFileDOV5.

        **参数解释**: 文件大小,单位为byte。 **取值范围**: 不涉及。 

        :return: The size of this RepoFileDOV5.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RepoFileDOV5.

        **参数解释**: 文件大小,单位为byte。 **取值范围**: 不涉及。 

        :param size: The size of this RepoFileDOV5.
        :type size: int
        """
        self._size = size

    @property
    def md5(self):
        r"""Gets the md5 of this RepoFileDOV5.

        **参数解释**: md5校验和。 **取值范围**: 不涉及。 

        :return: The md5 of this RepoFileDOV5.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        r"""Sets the md5 of this RepoFileDOV5.

        **参数解释**: md5校验和。 **取值范围**: 不涉及。 

        :param md5: The md5 of this RepoFileDOV5.
        :type md5: str
        """
        self._md5 = md5

    @property
    def sha256(self):
        r"""Gets the sha256 of this RepoFileDOV5.

        **参数解释**: sha256校验和。 **取值范围**: 不涉及。 

        :return: The sha256 of this RepoFileDOV5.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this RepoFileDOV5.

        **参数解释**: sha256校验和。 **取值范围**: 不涉及。 

        :param sha256: The sha256 of this RepoFileDOV5.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def download_url(self):
        r"""Gets the download_url of this RepoFileDOV5.

        **参数解释**: 下载地址。 **取值范围**: 不涉及。 

        :return: The download_url of this RepoFileDOV5.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this RepoFileDOV5.

        **参数解释**: 下载地址。 **取值范围**: 不涉及。 

        :param download_url: The download_url of this RepoFileDOV5.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def download_url_with_id(self):
        r"""Gets the download_url_with_id of this RepoFileDOV5.

        **参数解释**: 带有id的下载地址。 **取值范围**: 不涉及。 

        :return: The download_url_with_id of this RepoFileDOV5.
        :rtype: str
        """
        return self._download_url_with_id

    @download_url_with_id.setter
    def download_url_with_id(self, download_url_with_id):
        r"""Sets the download_url_with_id of this RepoFileDOV5.

        **参数解释**: 带有id的下载地址。 **取值范围**: 不涉及。 

        :param download_url_with_id: The download_url_with_id of this RepoFileDOV5.
        :type download_url_with_id: str
        """
        self._download_url_with_id = download_url_with_id

    @property
    def web_url(self):
        r"""Gets the web_url of this RepoFileDOV5.

        **参数解释**: 历史版本遗留字段，请忽略。 **取值范围**: 不涉及。 

        :return: The web_url of this RepoFileDOV5.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this RepoFileDOV5.

        **参数解释**: 历史版本遗留字段，请忽略。 **取值范围**: 不涉及。 

        :param web_url: The web_url of this RepoFileDOV5.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def version_enable(self):
        r"""Gets the version_enable of this RepoFileDOV5.

        **参数解释**: 判断当前文件或文件夹父目录是否为版本路径，即仓库下第一层子目录。 **取值范围**: - true：父目录是版本路径。 - false：父目录不是版本路径。 

        :return: The version_enable of this RepoFileDOV5.
        :rtype: bool
        """
        return self._version_enable

    @version_enable.setter
    def version_enable(self, version_enable):
        r"""Sets the version_enable of this RepoFileDOV5.

        **参数解释**: 判断当前文件或文件夹父目录是否为版本路径，即仓库下第一层子目录。 **取值范围**: - true：父目录是版本路径。 - false：父目录不是版本路径。 

        :param version_enable: The version_enable of this RepoFileDOV5.
        :type version_enable: bool
        """
        self._version_enable = version_enable

    @property
    def migrated_state(self):
        r"""Gets the migrated_state of this RepoFileDOV5.

        **参数解释**: migrated_state。 **取值范围**: 该参数为内部数据改造参数，无业务含义，请忽略。 

        :return: The migrated_state of this RepoFileDOV5.
        :rtype: int
        """
        return self._migrated_state

    @migrated_state.setter
    def migrated_state(self, migrated_state):
        r"""Sets the migrated_state of this RepoFileDOV5.

        **参数解释**: migrated_state。 **取值范围**: 该参数为内部数据改造参数，无业务含义，请忽略。 

        :param migrated_state: The migrated_state of this RepoFileDOV5.
        :type migrated_state: int
        """
        self._migrated_state = migrated_state

    @property
    def upload_id(self):
        r"""Gets the upload_id of this RepoFileDOV5.

        **参数解释**: 该参数无返回值，请忽略。 **取值范围**: 不涉及。 

        :return: The upload_id of this RepoFileDOV5.
        :rtype: str
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        r"""Sets the upload_id of this RepoFileDOV5.

        **参数解释**: 该参数无返回值，请忽略。 **取值范围**: 不涉及。 

        :param upload_id: The upload_id of this RepoFileDOV5.
        :type upload_id: str
        """
        self._upload_id = upload_id

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
        if not isinstance(other, RepoFileDOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
