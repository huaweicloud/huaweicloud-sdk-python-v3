# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineSourceParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'git_type': 'str',
        'codehub_id': 'str',
        'endpoint_id': 'str',
        'default_branch': 'str',
        'git_url': 'str',
        'ssh_git_url': 'str',
        'web_url': 'str',
        'repo_name': 'str',
        'artifact_type': 'str',
        'artifact_type_name': 'str',
        'branch_filter': 'str',
        'directory': 'str',
        'directory_id': 'str',
        'organization': 'str',
        'package_name': 'str',
        'version': 'str',
        'version_strategy': 'str',
        'source_system': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'git_type': 'git_type',
        'codehub_id': 'codehub_id',
        'endpoint_id': 'endpoint_id',
        'default_branch': 'default_branch',
        'git_url': 'git_url',
        'ssh_git_url': 'ssh_git_url',
        'web_url': 'web_url',
        'repo_name': 'repo_name',
        'artifact_type': 'artifact_type',
        'artifact_type_name': 'artifact_type_name',
        'branch_filter': 'branch_filter',
        'directory': 'directory',
        'directory_id': 'directory_id',
        'organization': 'organization',
        'package_name': 'package_name',
        'version': 'version',
        'version_strategy': 'version_strategy',
        'source_system': 'source_system'
    }

    def __init__(self, alias=None, git_type=None, codehub_id=None, endpoint_id=None, default_branch=None, git_url=None, ssh_git_url=None, web_url=None, repo_name=None, artifact_type=None, artifact_type_name=None, branch_filter=None, directory=None, directory_id=None, organization=None, package_name=None, version=None, version_strategy=None, source_system=None):
        """PipelineSourceParam

        The model defined in huaweicloud sdk

        :param alias: 代码/制品源参数 - 代码仓/制品源别名。别名仅支持输入大小写英文字母、数字、“_”，至多128个字符
        :type alias: str
        :param git_type: 代码源参数 - git类型
        :type git_type: str
        :param codehub_id: 代码源参数 - Repo代码仓ID
        :type codehub_id: str
        :param endpoint_id: 代码源参数 - 扩展点id
        :type endpoint_id: str
        :param default_branch: 代码源参数 - 默认分支
        :type default_branch: str
        :param git_url: 代码源参数 - git链接
        :type git_url: str
        :param ssh_git_url: 代码源参数 - ssh_git链接
        :type ssh_git_url: str
        :param web_url: 代码源参数 - 网页url
        :type web_url: str
        :param repo_name: 代码源参数 - 流水线源名称
        :type repo_name: str
        :param artifact_type: 制品源参数 - 制品源类型，generic/docker
        :type artifact_type: str
        :param artifact_type_name: 制品源参数 - 制品源类型名
        :type artifact_type_name: str
        :param branch_filter: 制品源参数 - 过滤分支
        :type branch_filter: str
        :param directory: 制品源参数 - 目录
        :type directory: str
        :param directory_id: 制品源参数 - 目录ID
        :type directory_id: str
        :param organization: 制品源参数 - Docker组织
        :type organization: str
        :param package_name: 制品源参数 - 包名称
        :type package_name: str
        :param version: 制品源参数 - 版本
        :type version: str
        :param version_strategy: 制品源参数 - 获取制品源版本的策略，latest/specificVersion
        :type version_strategy: str
        :param source_system: 制品源参数 - 制品源名称,如CloudArtifact
        :type source_system: str
        """
        
        

        self._alias = None
        self._git_type = None
        self._codehub_id = None
        self._endpoint_id = None
        self._default_branch = None
        self._git_url = None
        self._ssh_git_url = None
        self._web_url = None
        self._repo_name = None
        self._artifact_type = None
        self._artifact_type_name = None
        self._branch_filter = None
        self._directory = None
        self._directory_id = None
        self._organization = None
        self._package_name = None
        self._version = None
        self._version_strategy = None
        self._source_system = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if git_type is not None:
            self.git_type = git_type
        if codehub_id is not None:
            self.codehub_id = codehub_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if default_branch is not None:
            self.default_branch = default_branch
        if git_url is not None:
            self.git_url = git_url
        if ssh_git_url is not None:
            self.ssh_git_url = ssh_git_url
        if web_url is not None:
            self.web_url = web_url
        if repo_name is not None:
            self.repo_name = repo_name
        if artifact_type is not None:
            self.artifact_type = artifact_type
        if artifact_type_name is not None:
            self.artifact_type_name = artifact_type_name
        if branch_filter is not None:
            self.branch_filter = branch_filter
        if directory is not None:
            self.directory = directory
        if directory_id is not None:
            self.directory_id = directory_id
        if organization is not None:
            self.organization = organization
        if package_name is not None:
            self.package_name = package_name
        if version is not None:
            self.version = version
        if version_strategy is not None:
            self.version_strategy = version_strategy
        if source_system is not None:
            self.source_system = source_system

    @property
    def alias(self):
        """Gets the alias of this PipelineSourceParam.

        代码/制品源参数 - 代码仓/制品源别名。别名仅支持输入大小写英文字母、数字、“_”，至多128个字符

        :return: The alias of this PipelineSourceParam.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PipelineSourceParam.

        代码/制品源参数 - 代码仓/制品源别名。别名仅支持输入大小写英文字母、数字、“_”，至多128个字符

        :param alias: The alias of this PipelineSourceParam.
        :type alias: str
        """
        self._alias = alias

    @property
    def git_type(self):
        """Gets the git_type of this PipelineSourceParam.

        代码源参数 - git类型

        :return: The git_type of this PipelineSourceParam.
        :rtype: str
        """
        return self._git_type

    @git_type.setter
    def git_type(self, git_type):
        """Sets the git_type of this PipelineSourceParam.

        代码源参数 - git类型

        :param git_type: The git_type of this PipelineSourceParam.
        :type git_type: str
        """
        self._git_type = git_type

    @property
    def codehub_id(self):
        """Gets the codehub_id of this PipelineSourceParam.

        代码源参数 - Repo代码仓ID

        :return: The codehub_id of this PipelineSourceParam.
        :rtype: str
        """
        return self._codehub_id

    @codehub_id.setter
    def codehub_id(self, codehub_id):
        """Sets the codehub_id of this PipelineSourceParam.

        代码源参数 - Repo代码仓ID

        :param codehub_id: The codehub_id of this PipelineSourceParam.
        :type codehub_id: str
        """
        self._codehub_id = codehub_id

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this PipelineSourceParam.

        代码源参数 - 扩展点id

        :return: The endpoint_id of this PipelineSourceParam.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this PipelineSourceParam.

        代码源参数 - 扩展点id

        :param endpoint_id: The endpoint_id of this PipelineSourceParam.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def default_branch(self):
        """Gets the default_branch of this PipelineSourceParam.

        代码源参数 - 默认分支

        :return: The default_branch of this PipelineSourceParam.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this PipelineSourceParam.

        代码源参数 - 默认分支

        :param default_branch: The default_branch of this PipelineSourceParam.
        :type default_branch: str
        """
        self._default_branch = default_branch

    @property
    def git_url(self):
        """Gets the git_url of this PipelineSourceParam.

        代码源参数 - git链接

        :return: The git_url of this PipelineSourceParam.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this PipelineSourceParam.

        代码源参数 - git链接

        :param git_url: The git_url of this PipelineSourceParam.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def ssh_git_url(self):
        """Gets the ssh_git_url of this PipelineSourceParam.

        代码源参数 - ssh_git链接

        :return: The ssh_git_url of this PipelineSourceParam.
        :rtype: str
        """
        return self._ssh_git_url

    @ssh_git_url.setter
    def ssh_git_url(self, ssh_git_url):
        """Sets the ssh_git_url of this PipelineSourceParam.

        代码源参数 - ssh_git链接

        :param ssh_git_url: The ssh_git_url of this PipelineSourceParam.
        :type ssh_git_url: str
        """
        self._ssh_git_url = ssh_git_url

    @property
    def web_url(self):
        """Gets the web_url of this PipelineSourceParam.

        代码源参数 - 网页url

        :return: The web_url of this PipelineSourceParam.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this PipelineSourceParam.

        代码源参数 - 网页url

        :param web_url: The web_url of this PipelineSourceParam.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def repo_name(self):
        """Gets the repo_name of this PipelineSourceParam.

        代码源参数 - 流水线源名称

        :return: The repo_name of this PipelineSourceParam.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this PipelineSourceParam.

        代码源参数 - 流水线源名称

        :param repo_name: The repo_name of this PipelineSourceParam.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def artifact_type(self):
        """Gets the artifact_type of this PipelineSourceParam.

        制品源参数 - 制品源类型，generic/docker

        :return: The artifact_type of this PipelineSourceParam.
        :rtype: str
        """
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, artifact_type):
        """Sets the artifact_type of this PipelineSourceParam.

        制品源参数 - 制品源类型，generic/docker

        :param artifact_type: The artifact_type of this PipelineSourceParam.
        :type artifact_type: str
        """
        self._artifact_type = artifact_type

    @property
    def artifact_type_name(self):
        """Gets the artifact_type_name of this PipelineSourceParam.

        制品源参数 - 制品源类型名

        :return: The artifact_type_name of this PipelineSourceParam.
        :rtype: str
        """
        return self._artifact_type_name

    @artifact_type_name.setter
    def artifact_type_name(self, artifact_type_name):
        """Sets the artifact_type_name of this PipelineSourceParam.

        制品源参数 - 制品源类型名

        :param artifact_type_name: The artifact_type_name of this PipelineSourceParam.
        :type artifact_type_name: str
        """
        self._artifact_type_name = artifact_type_name

    @property
    def branch_filter(self):
        """Gets the branch_filter of this PipelineSourceParam.

        制品源参数 - 过滤分支

        :return: The branch_filter of this PipelineSourceParam.
        :rtype: str
        """
        return self._branch_filter

    @branch_filter.setter
    def branch_filter(self, branch_filter):
        """Sets the branch_filter of this PipelineSourceParam.

        制品源参数 - 过滤分支

        :param branch_filter: The branch_filter of this PipelineSourceParam.
        :type branch_filter: str
        """
        self._branch_filter = branch_filter

    @property
    def directory(self):
        """Gets the directory of this PipelineSourceParam.

        制品源参数 - 目录

        :return: The directory of this PipelineSourceParam.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this PipelineSourceParam.

        制品源参数 - 目录

        :param directory: The directory of this PipelineSourceParam.
        :type directory: str
        """
        self._directory = directory

    @property
    def directory_id(self):
        """Gets the directory_id of this PipelineSourceParam.

        制品源参数 - 目录ID

        :return: The directory_id of this PipelineSourceParam.
        :rtype: str
        """
        return self._directory_id

    @directory_id.setter
    def directory_id(self, directory_id):
        """Sets the directory_id of this PipelineSourceParam.

        制品源参数 - 目录ID

        :param directory_id: The directory_id of this PipelineSourceParam.
        :type directory_id: str
        """
        self._directory_id = directory_id

    @property
    def organization(self):
        """Gets the organization of this PipelineSourceParam.

        制品源参数 - Docker组织

        :return: The organization of this PipelineSourceParam.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PipelineSourceParam.

        制品源参数 - Docker组织

        :param organization: The organization of this PipelineSourceParam.
        :type organization: str
        """
        self._organization = organization

    @property
    def package_name(self):
        """Gets the package_name of this PipelineSourceParam.

        制品源参数 - 包名称

        :return: The package_name of this PipelineSourceParam.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this PipelineSourceParam.

        制品源参数 - 包名称

        :param package_name: The package_name of this PipelineSourceParam.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def version(self):
        """Gets the version of this PipelineSourceParam.

        制品源参数 - 版本

        :return: The version of this PipelineSourceParam.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PipelineSourceParam.

        制品源参数 - 版本

        :param version: The version of this PipelineSourceParam.
        :type version: str
        """
        self._version = version

    @property
    def version_strategy(self):
        """Gets the version_strategy of this PipelineSourceParam.

        制品源参数 - 获取制品源版本的策略，latest/specificVersion

        :return: The version_strategy of this PipelineSourceParam.
        :rtype: str
        """
        return self._version_strategy

    @version_strategy.setter
    def version_strategy(self, version_strategy):
        """Sets the version_strategy of this PipelineSourceParam.

        制品源参数 - 获取制品源版本的策略，latest/specificVersion

        :param version_strategy: The version_strategy of this PipelineSourceParam.
        :type version_strategy: str
        """
        self._version_strategy = version_strategy

    @property
    def source_system(self):
        """Gets the source_system of this PipelineSourceParam.

        制品源参数 - 制品源名称,如CloudArtifact

        :return: The source_system of this PipelineSourceParam.
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        """Sets the source_system of this PipelineSourceParam.

        制品源参数 - 制品源名称,如CloudArtifact

        :param source_system: The source_system of this PipelineSourceParam.
        :type source_system: str
        """
        self._source_system = source_system

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
        if not isinstance(other, PipelineSourceParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
