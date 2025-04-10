# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectSimpleDto:

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
        'develop_mode': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'archived': 'bool',
        'is_kia': 'bool',
        'ssh_url_to_repo': 'str',
        'http_url_to_repo': 'str',
        'web_url': 'str',
        'readme_url': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'member_mgnt_mode': 'int',
        'visibility': 'str',
        'namespace': 'NamespaceBasicDto',
        'repo_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'name_with_namespace': 'name_with_namespace',
        'path': 'path',
        'path_with_namespace': 'path_with_namespace',
        'develop_mode': 'develop_mode',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'archived': 'archived',
        'is_kia': 'is_kia',
        'ssh_url_to_repo': 'ssh_url_to_repo',
        'http_url_to_repo': 'http_url_to_repo',
        'web_url': 'web_url',
        'readme_url': 'readme_url',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'member_mgnt_mode': 'member_mgnt_mode',
        'visibility': 'visibility',
        'namespace': 'namespace',
        'repo_type': 'repo_type'
    }

    def __init__(self, id=None, description=None, name=None, name_with_namespace=None, path=None, path_with_namespace=None, develop_mode=None, created_at=None, updated_at=None, archived=None, is_kia=None, ssh_url_to_repo=None, http_url_to_repo=None, web_url=None, readme_url=None, product_id=None, product_name=None, member_mgnt_mode=None, visibility=None, namespace=None, repo_type=None):
        r"""ProjectSimpleDto

        The model defined in huaweicloud sdk

        :param id: 项目id
        :type id: int
        :param description: 项目描述
        :type description: str
        :param name: 项目名称
        :type name: str
        :param name_with_namespace: 项目名称
        :type name_with_namespace: str
        :param path: 项目路径
        :type path: str
        :param path_with_namespace: 项目路径
        :type path_with_namespace: str
        :param develop_mode: 开发模式
        :type develop_mode: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param archived: 是否归档
        :type archived: bool
        :param is_kia: 是否为kia仓
        :type is_kia: bool
        :param ssh_url_to_repo: 项目url
        :type ssh_url_to_repo: str
        :param http_url_to_repo: 项目url
        :type http_url_to_repo: str
        :param web_url: 项目url
        :type web_url: str
        :param readme_url: 项目readme url
        :type readme_url: str
        :param product_id: product id
        :type product_id: str
        :param product_name: product name
        :type product_name: str
        :param member_mgnt_mode: member mgnt mode
        :type member_mgnt_mode: int
        :param visibility: visibility
        :type visibility: str
        :param namespace: 
        :type namespace: :class:`huaweicloudsdkcodehub.v3.NamespaceBasicDto`
        :param repo_type: 项目类型
        :type repo_type: str
        """
        
        

        self._id = None
        self._description = None
        self._name = None
        self._name_with_namespace = None
        self._path = None
        self._path_with_namespace = None
        self._develop_mode = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._is_kia = None
        self._ssh_url_to_repo = None
        self._http_url_to_repo = None
        self._web_url = None
        self._readme_url = None
        self._product_id = None
        self._product_name = None
        self._member_mgnt_mode = None
        self._visibility = None
        self._namespace = None
        self._repo_type = None
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
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if archived is not None:
            self.archived = archived
        if is_kia is not None:
            self.is_kia = is_kia
        if ssh_url_to_repo is not None:
            self.ssh_url_to_repo = ssh_url_to_repo
        if http_url_to_repo is not None:
            self.http_url_to_repo = http_url_to_repo
        if web_url is not None:
            self.web_url = web_url
        if readme_url is not None:
            self.readme_url = readme_url
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if member_mgnt_mode is not None:
            self.member_mgnt_mode = member_mgnt_mode
        if visibility is not None:
            self.visibility = visibility
        if namespace is not None:
            self.namespace = namespace
        if repo_type is not None:
            self.repo_type = repo_type

    @property
    def id(self):
        r"""Gets the id of this ProjectSimpleDto.

        项目id

        :return: The id of this ProjectSimpleDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectSimpleDto.

        项目id

        :param id: The id of this ProjectSimpleDto.
        :type id: int
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ProjectSimpleDto.

        项目描述

        :return: The description of this ProjectSimpleDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProjectSimpleDto.

        项目描述

        :param description: The description of this ProjectSimpleDto.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this ProjectSimpleDto.

        项目名称

        :return: The name of this ProjectSimpleDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ProjectSimpleDto.

        项目名称

        :param name: The name of this ProjectSimpleDto.
        :type name: str
        """
        self._name = name

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this ProjectSimpleDto.

        项目名称

        :return: The name_with_namespace of this ProjectSimpleDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this ProjectSimpleDto.

        项目名称

        :param name_with_namespace: The name_with_namespace of this ProjectSimpleDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def path(self):
        r"""Gets the path of this ProjectSimpleDto.

        项目路径

        :return: The path of this ProjectSimpleDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ProjectSimpleDto.

        项目路径

        :param path: The path of this ProjectSimpleDto.
        :type path: str
        """
        self._path = path

    @property
    def path_with_namespace(self):
        r"""Gets the path_with_namespace of this ProjectSimpleDto.

        项目路径

        :return: The path_with_namespace of this ProjectSimpleDto.
        :rtype: str
        """
        return self._path_with_namespace

    @path_with_namespace.setter
    def path_with_namespace(self, path_with_namespace):
        r"""Sets the path_with_namespace of this ProjectSimpleDto.

        项目路径

        :param path_with_namespace: The path_with_namespace of this ProjectSimpleDto.
        :type path_with_namespace: str
        """
        self._path_with_namespace = path_with_namespace

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this ProjectSimpleDto.

        开发模式

        :return: The develop_mode of this ProjectSimpleDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this ProjectSimpleDto.

        开发模式

        :param develop_mode: The develop_mode of this ProjectSimpleDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def created_at(self):
        r"""Gets the created_at of this ProjectSimpleDto.

        创建时间

        :return: The created_at of this ProjectSimpleDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ProjectSimpleDto.

        创建时间

        :param created_at: The created_at of this ProjectSimpleDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ProjectSimpleDto.

        更新时间

        :return: The updated_at of this ProjectSimpleDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ProjectSimpleDto.

        更新时间

        :param updated_at: The updated_at of this ProjectSimpleDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def archived(self):
        r"""Gets the archived of this ProjectSimpleDto.

        是否归档

        :return: The archived of this ProjectSimpleDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this ProjectSimpleDto.

        是否归档

        :param archived: The archived of this ProjectSimpleDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def is_kia(self):
        r"""Gets the is_kia of this ProjectSimpleDto.

        是否为kia仓

        :return: The is_kia of this ProjectSimpleDto.
        :rtype: bool
        """
        return self._is_kia

    @is_kia.setter
    def is_kia(self, is_kia):
        r"""Sets the is_kia of this ProjectSimpleDto.

        是否为kia仓

        :param is_kia: The is_kia of this ProjectSimpleDto.
        :type is_kia: bool
        """
        self._is_kia = is_kia

    @property
    def ssh_url_to_repo(self):
        r"""Gets the ssh_url_to_repo of this ProjectSimpleDto.

        项目url

        :return: The ssh_url_to_repo of this ProjectSimpleDto.
        :rtype: str
        """
        return self._ssh_url_to_repo

    @ssh_url_to_repo.setter
    def ssh_url_to_repo(self, ssh_url_to_repo):
        r"""Sets the ssh_url_to_repo of this ProjectSimpleDto.

        项目url

        :param ssh_url_to_repo: The ssh_url_to_repo of this ProjectSimpleDto.
        :type ssh_url_to_repo: str
        """
        self._ssh_url_to_repo = ssh_url_to_repo

    @property
    def http_url_to_repo(self):
        r"""Gets the http_url_to_repo of this ProjectSimpleDto.

        项目url

        :return: The http_url_to_repo of this ProjectSimpleDto.
        :rtype: str
        """
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, http_url_to_repo):
        r"""Sets the http_url_to_repo of this ProjectSimpleDto.

        项目url

        :param http_url_to_repo: The http_url_to_repo of this ProjectSimpleDto.
        :type http_url_to_repo: str
        """
        self._http_url_to_repo = http_url_to_repo

    @property
    def web_url(self):
        r"""Gets the web_url of this ProjectSimpleDto.

        项目url

        :return: The web_url of this ProjectSimpleDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this ProjectSimpleDto.

        项目url

        :param web_url: The web_url of this ProjectSimpleDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def readme_url(self):
        r"""Gets the readme_url of this ProjectSimpleDto.

        项目readme url

        :return: The readme_url of this ProjectSimpleDto.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        r"""Sets the readme_url of this ProjectSimpleDto.

        项目readme url

        :param readme_url: The readme_url of this ProjectSimpleDto.
        :type readme_url: str
        """
        self._readme_url = readme_url

    @property
    def product_id(self):
        r"""Gets the product_id of this ProjectSimpleDto.

        product id

        :return: The product_id of this ProjectSimpleDto.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProjectSimpleDto.

        product id

        :param product_id: The product_id of this ProjectSimpleDto.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this ProjectSimpleDto.

        product name

        :return: The product_name of this ProjectSimpleDto.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ProjectSimpleDto.

        product name

        :param product_name: The product_name of this ProjectSimpleDto.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def member_mgnt_mode(self):
        r"""Gets the member_mgnt_mode of this ProjectSimpleDto.

        member mgnt mode

        :return: The member_mgnt_mode of this ProjectSimpleDto.
        :rtype: int
        """
        return self._member_mgnt_mode

    @member_mgnt_mode.setter
    def member_mgnt_mode(self, member_mgnt_mode):
        r"""Sets the member_mgnt_mode of this ProjectSimpleDto.

        member mgnt mode

        :param member_mgnt_mode: The member_mgnt_mode of this ProjectSimpleDto.
        :type member_mgnt_mode: int
        """
        self._member_mgnt_mode = member_mgnt_mode

    @property
    def visibility(self):
        r"""Gets the visibility of this ProjectSimpleDto.

        visibility

        :return: The visibility of this ProjectSimpleDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ProjectSimpleDto.

        visibility

        :param visibility: The visibility of this ProjectSimpleDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def namespace(self):
        r"""Gets the namespace of this ProjectSimpleDto.

        :return: The namespace of this ProjectSimpleDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.NamespaceBasicDto`
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ProjectSimpleDto.

        :param namespace: The namespace of this ProjectSimpleDto.
        :type namespace: :class:`huaweicloudsdkcodehub.v3.NamespaceBasicDto`
        """
        self._namespace = namespace

    @property
    def repo_type(self):
        r"""Gets the repo_type of this ProjectSimpleDto.

        项目类型

        :return: The repo_type of this ProjectSimpleDto.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this ProjectSimpleDto.

        项目类型

        :param repo_type: The repo_type of this ProjectSimpleDto.
        :type repo_type: str
        """
        self._repo_type = repo_type

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
        if not isinstance(other, ProjectSimpleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
