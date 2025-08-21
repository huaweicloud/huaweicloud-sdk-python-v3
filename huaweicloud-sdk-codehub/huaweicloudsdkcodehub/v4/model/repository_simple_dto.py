# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositorySimpleDto:

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
        'description': 'str',
        'name': 'str',
        'name_with_namespace': 'str',
        'path': 'str',
        'path_with_namespace': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'archived': 'bool',
        'ssh_url_to_repo': 'str',
        'http_url_to_repo': 'str',
        'web_url': 'str',
        'readme_url': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'develop_mode': 'str',
        'moderation_result': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'name_with_namespace': 'name_with_namespace',
        'path': 'path',
        'path_with_namespace': 'path_with_namespace',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'archived': 'archived',
        'ssh_url_to_repo': 'ssh_url_to_repo',
        'http_url_to_repo': 'http_url_to_repo',
        'web_url': 'web_url',
        'readme_url': 'readme_url',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'develop_mode': 'develop_mode',
        'moderation_result': 'moderation_result'
    }

    def __init__(self, id=None, description=None, name=None, name_with_namespace=None, path=None, path_with_namespace=None, created_at=None, updated_at=None, archived=None, ssh_url_to_repo=None, http_url_to_repo=None, web_url=None, readme_url=None, project_id=None, project_name=None, develop_mode=None, moderation_result=None):
        r"""RepositorySimpleDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库ID。
        :type id: int
        :param description: **参数解释：** 仓库描述信息。
        :type description: str
        :param name: **参数解释：** 仓库名称。
        :type name: str
        :param name_with_namespace: **参数解释：** 仓库完整名称。
        :type name_with_namespace: str
        :param path: **参数解释：** 仓库路径。
        :type path: str
        :param path_with_namespace: **参数解释：** 仓库完整路径。
        :type path_with_namespace: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param archived: **参数解释：** 是否归档。
        :type archived: bool
        :param ssh_url_to_repo: **参数解释：** 仓库ssh地址。
        :type ssh_url_to_repo: str
        :param http_url_to_repo: **参数解释：** 仓库http地址。
        :type http_url_to_repo: str
        :param web_url: **参数解释：** 仓库页面链接。
        :type web_url: str
        :param readme_url: **参数解释：** 仓库readme文件链接。
        :type readme_url: str
        :param project_id: **参数解释：** 仓库所属项目ID。
        :type project_id: str
        :param project_name: **参数解释：** 仓库所属项目名称。
        :type project_name: str
        :param develop_mode: **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR
        :type develop_mode: str
        :param moderation_result: **参数解释：** 审核状态。
        :type moderation_result: bool
        """
        
        

        self._id = None
        self._description = None
        self._name = None
        self._name_with_namespace = None
        self._path = None
        self._path_with_namespace = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._ssh_url_to_repo = None
        self._http_url_to_repo = None
        self._web_url = None
        self._readme_url = None
        self._project_id = None
        self._project_name = None
        self._develop_mode = None
        self._moderation_result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if path is not None:
            self.path = path
        if path_with_namespace is not None:
            self.path_with_namespace = path_with_namespace
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if archived is not None:
            self.archived = archived
        if ssh_url_to_repo is not None:
            self.ssh_url_to_repo = ssh_url_to_repo
        if http_url_to_repo is not None:
            self.http_url_to_repo = http_url_to_repo
        if web_url is not None:
            self.web_url = web_url
        if readme_url is not None:
            self.readme_url = readme_url
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if moderation_result is not None:
            self.moderation_result = moderation_result

    @property
    def id(self):
        r"""Gets the id of this RepositorySimpleDto.

        **参数解释：** 仓库ID。

        :return: The id of this RepositorySimpleDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositorySimpleDto.

        **参数解释：** 仓库ID。

        :param id: The id of this RepositorySimpleDto.
        :type id: int
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this RepositorySimpleDto.

        **参数解释：** 仓库描述信息。

        :return: The description of this RepositorySimpleDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositorySimpleDto.

        **参数解释：** 仓库描述信息。

        :param description: The description of this RepositorySimpleDto.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this RepositorySimpleDto.

        **参数解释：** 仓库名称。

        :return: The name of this RepositorySimpleDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositorySimpleDto.

        **参数解释：** 仓库名称。

        :param name: The name of this RepositorySimpleDto.
        :type name: str
        """
        self._name = name

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this RepositorySimpleDto.

        **参数解释：** 仓库完整名称。

        :return: The name_with_namespace of this RepositorySimpleDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this RepositorySimpleDto.

        **参数解释：** 仓库完整名称。

        :param name_with_namespace: The name_with_namespace of this RepositorySimpleDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def path(self):
        r"""Gets the path of this RepositorySimpleDto.

        **参数解释：** 仓库路径。

        :return: The path of this RepositorySimpleDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this RepositorySimpleDto.

        **参数解释：** 仓库路径。

        :param path: The path of this RepositorySimpleDto.
        :type path: str
        """
        self._path = path

    @property
    def path_with_namespace(self):
        r"""Gets the path_with_namespace of this RepositorySimpleDto.

        **参数解释：** 仓库完整路径。

        :return: The path_with_namespace of this RepositorySimpleDto.
        :rtype: str
        """
        return self._path_with_namespace

    @path_with_namespace.setter
    def path_with_namespace(self, path_with_namespace):
        r"""Sets the path_with_namespace of this RepositorySimpleDto.

        **参数解释：** 仓库完整路径。

        :param path_with_namespace: The path_with_namespace of this RepositorySimpleDto.
        :type path_with_namespace: str
        """
        self._path_with_namespace = path_with_namespace

    @property
    def created_at(self):
        r"""Gets the created_at of this RepositorySimpleDto.

        **参数解释：** 创建时间。

        :return: The created_at of this RepositorySimpleDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RepositorySimpleDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this RepositorySimpleDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RepositorySimpleDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this RepositorySimpleDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RepositorySimpleDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this RepositorySimpleDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def archived(self):
        r"""Gets the archived of this RepositorySimpleDto.

        **参数解释：** 是否归档。

        :return: The archived of this RepositorySimpleDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this RepositorySimpleDto.

        **参数解释：** 是否归档。

        :param archived: The archived of this RepositorySimpleDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def ssh_url_to_repo(self):
        r"""Gets the ssh_url_to_repo of this RepositorySimpleDto.

        **参数解释：** 仓库ssh地址。

        :return: The ssh_url_to_repo of this RepositorySimpleDto.
        :rtype: str
        """
        return self._ssh_url_to_repo

    @ssh_url_to_repo.setter
    def ssh_url_to_repo(self, ssh_url_to_repo):
        r"""Sets the ssh_url_to_repo of this RepositorySimpleDto.

        **参数解释：** 仓库ssh地址。

        :param ssh_url_to_repo: The ssh_url_to_repo of this RepositorySimpleDto.
        :type ssh_url_to_repo: str
        """
        self._ssh_url_to_repo = ssh_url_to_repo

    @property
    def http_url_to_repo(self):
        r"""Gets the http_url_to_repo of this RepositorySimpleDto.

        **参数解释：** 仓库http地址。

        :return: The http_url_to_repo of this RepositorySimpleDto.
        :rtype: str
        """
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, http_url_to_repo):
        r"""Sets the http_url_to_repo of this RepositorySimpleDto.

        **参数解释：** 仓库http地址。

        :param http_url_to_repo: The http_url_to_repo of this RepositorySimpleDto.
        :type http_url_to_repo: str
        """
        self._http_url_to_repo = http_url_to_repo

    @property
    def web_url(self):
        r"""Gets the web_url of this RepositorySimpleDto.

        **参数解释：** 仓库页面链接。

        :return: The web_url of this RepositorySimpleDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this RepositorySimpleDto.

        **参数解释：** 仓库页面链接。

        :param web_url: The web_url of this RepositorySimpleDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def readme_url(self):
        r"""Gets the readme_url of this RepositorySimpleDto.

        **参数解释：** 仓库readme文件链接。

        :return: The readme_url of this RepositorySimpleDto.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        r"""Sets the readme_url of this RepositorySimpleDto.

        **参数解释：** 仓库readme文件链接。

        :param readme_url: The readme_url of this RepositorySimpleDto.
        :type readme_url: str
        """
        self._readme_url = readme_url

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositorySimpleDto.

        **参数解释：** 仓库所属项目ID。

        :return: The project_id of this RepositorySimpleDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositorySimpleDto.

        **参数解释：** 仓库所属项目ID。

        :param project_id: The project_id of this RepositorySimpleDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this RepositorySimpleDto.

        **参数解释：** 仓库所属项目名称。

        :return: The project_name of this RepositorySimpleDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this RepositorySimpleDto.

        **参数解释：** 仓库所属项目名称。

        :param project_name: The project_name of this RepositorySimpleDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this RepositorySimpleDto.

        **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR

        :return: The develop_mode of this RepositorySimpleDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this RepositorySimpleDto.

        **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR

        :param develop_mode: The develop_mode of this RepositorySimpleDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this RepositorySimpleDto.

        **参数解释：** 审核状态。

        :return: The moderation_result of this RepositorySimpleDto.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this RepositorySimpleDto.

        **参数解释：** 审核状态。

        :param moderation_result: The moderation_result of this RepositorySimpleDto.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

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
        if not isinstance(other, RepositorySimpleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
