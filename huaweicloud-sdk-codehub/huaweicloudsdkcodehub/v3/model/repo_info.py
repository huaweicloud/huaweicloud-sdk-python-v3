# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_at': 'str',
        'group_name': 'str',
        'http_url': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'project_is_delete': 'str',
        'repo_id': 'str',
        'ssh_url': 'str',
        'visibility_level': 'int',
        'web_url': 'str'
    }

    attribute_map = {
        'create_at': 'createAt',
        'group_name': 'groupName',
        'http_url': 'httpUrl',
        'id': 'id',
        'name': 'name',
        'project_id': 'projectId',
        'project_is_delete': 'projectIsDelete',
        'repo_id': 'repoId',
        'ssh_url': 'sshUrl',
        'visibility_level': 'visibilityLevel',
        'web_url': 'webUrl'
    }

    def __init__(self, create_at=None, group_name=None, http_url=None, id=None, name=None, project_id=None, project_is_delete=None, repo_id=None, ssh_url=None, visibility_level=None, web_url=None):
        """RepoInfo

        The model defined in huaweicloud sdk

        :param create_at: 创建时间
        :type create_at: str
        :param group_name: 仓库组名(克隆地址中域名后面项目名前的一段 示例：git@codehub.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228)
        :type group_name: str
        :param http_url: https url
        :type http_url: str
        :param id: 仓库uuid(由CreateRepository接口返回)
        :type id: str
        :param name: 仓库名
        :type name: str
        :param project_id: 项目的uuid
        :type project_id: str
        :param project_is_delete: 项目是否被删除
        :type project_is_delete: str
        :param repo_id: 仓库主键id
        :type repo_id: str
        :param ssh_url: ssh url
        :type ssh_url: str
        :param visibility_level: 是否可见：0私有仓库，20公有仓库
        :type visibility_level: int
        :param web_url: web url 访问路径
        :type web_url: str
        """
        
        

        self._create_at = None
        self._group_name = None
        self._http_url = None
        self._id = None
        self._name = None
        self._project_id = None
        self._project_is_delete = None
        self._repo_id = None
        self._ssh_url = None
        self._visibility_level = None
        self._web_url = None
        self.discriminator = None

        if create_at is not None:
            self.create_at = create_at
        if group_name is not None:
            self.group_name = group_name
        if http_url is not None:
            self.http_url = http_url
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if project_is_delete is not None:
            self.project_is_delete = project_is_delete
        if repo_id is not None:
            self.repo_id = repo_id
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if web_url is not None:
            self.web_url = web_url

    @property
    def create_at(self):
        """Gets the create_at of this RepoInfo.

        创建时间

        :return: The create_at of this RepoInfo.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this RepoInfo.

        创建时间

        :param create_at: The create_at of this RepoInfo.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def group_name(self):
        """Gets the group_name of this RepoInfo.

        仓库组名(克隆地址中域名后面项目名前的一段 示例：git@codehub.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228)

        :return: The group_name of this RepoInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this RepoInfo.

        仓库组名(克隆地址中域名后面项目名前的一段 示例：git@codehub.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228)

        :param group_name: The group_name of this RepoInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def http_url(self):
        """Gets the http_url of this RepoInfo.

        https url

        :return: The http_url of this RepoInfo.
        :rtype: str
        """
        return self._http_url

    @http_url.setter
    def http_url(self, http_url):
        """Sets the http_url of this RepoInfo.

        https url

        :param http_url: The http_url of this RepoInfo.
        :type http_url: str
        """
        self._http_url = http_url

    @property
    def id(self):
        """Gets the id of this RepoInfo.

        仓库uuid(由CreateRepository接口返回)

        :return: The id of this RepoInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepoInfo.

        仓库uuid(由CreateRepository接口返回)

        :param id: The id of this RepoInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RepoInfo.

        仓库名

        :return: The name of this RepoInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepoInfo.

        仓库名

        :param name: The name of this RepoInfo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this RepoInfo.

        项目的uuid

        :return: The project_id of this RepoInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RepoInfo.

        项目的uuid

        :param project_id: The project_id of this RepoInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_is_delete(self):
        """Gets the project_is_delete of this RepoInfo.

        项目是否被删除

        :return: The project_is_delete of this RepoInfo.
        :rtype: str
        """
        return self._project_is_delete

    @project_is_delete.setter
    def project_is_delete(self, project_is_delete):
        """Sets the project_is_delete of this RepoInfo.

        项目是否被删除

        :param project_is_delete: The project_is_delete of this RepoInfo.
        :type project_is_delete: str
        """
        self._project_is_delete = project_is_delete

    @property
    def repo_id(self):
        """Gets the repo_id of this RepoInfo.

        仓库主键id

        :return: The repo_id of this RepoInfo.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this RepoInfo.

        仓库主键id

        :param repo_id: The repo_id of this RepoInfo.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def ssh_url(self):
        """Gets the ssh_url of this RepoInfo.

        ssh url

        :return: The ssh_url of this RepoInfo.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """Sets the ssh_url of this RepoInfo.

        ssh url

        :param ssh_url: The ssh_url of this RepoInfo.
        :type ssh_url: str
        """
        self._ssh_url = ssh_url

    @property
    def visibility_level(self):
        """Gets the visibility_level of this RepoInfo.

        是否可见：0私有仓库，20公有仓库

        :return: The visibility_level of this RepoInfo.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        """Sets the visibility_level of this RepoInfo.

        是否可见：0私有仓库，20公有仓库

        :param visibility_level: The visibility_level of this RepoInfo.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def web_url(self):
        """Gets the web_url of this RepoInfo.

        web url 访问路径

        :return: The web_url of this RepoInfo.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this RepoInfo.

        web url 访问路径

        :param web_url: The web_url of this RepoInfo.
        :type web_url: str
        """
        self._web_url = web_url

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
        if not isinstance(other, RepoInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
