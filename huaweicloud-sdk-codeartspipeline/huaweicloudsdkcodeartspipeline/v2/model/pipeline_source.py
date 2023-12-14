# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scm_type': 'str',
        'hook_flag': 'str',
        'default_branch': 'str',
        'trigger': 'str',
        'alias': 'str',
        'display_name': 'str',
        'repo_name': 'str',
        'repo_id': 'str',
        'repo_owner': 'str',
        'git_url': 'str',
        'web_url': 'str'
    }

    attribute_map = {
        'scm_type': 'scmType',
        'hook_flag': 'hookFlag',
        'default_branch': 'defaultBranch',
        'trigger': 'trigger',
        'alias': 'alias',
        'display_name': 'displayName',
        'repo_name': 'repoName',
        'repo_id': 'repoId',
        'repo_owner': 'repoOwner',
        'git_url': 'gitUrl',
        'web_url': 'webUrl'
    }

    def __init__(self, scm_type=None, hook_flag=None, default_branch=None, trigger=None, alias=None, display_name=None, repo_name=None, repo_id=None, repo_owner=None, git_url=None, web_url=None):
        """PipelineSource

        The model defined in huaweicloud sdk

        :param scm_type: 源码仓类型
        :type scm_type: str
        :param hook_flag: 是否配置Webhook
        :type hook_flag: str
        :param default_branch: 默认分支
        :type default_branch: str
        :param trigger: webhook配置数据
        :type trigger: str
        :param alias: 代码仓别名
        :type alias: str
        :param display_name: 代码仓显示名
        :type display_name: str
        :param repo_name: 源码仓名称
        :type repo_name: str
        :param repo_id: 代码仓ID
        :type repo_id: str
        :param repo_owner: 代码仓所有者
        :type repo_owner: str
        :param git_url: 代码仓访问地址
        :type git_url: str
        :param web_url: 代码仓Web页面地址
        :type web_url: str
        """
        
        

        self._scm_type = None
        self._hook_flag = None
        self._default_branch = None
        self._trigger = None
        self._alias = None
        self._display_name = None
        self._repo_name = None
        self._repo_id = None
        self._repo_owner = None
        self._git_url = None
        self._web_url = None
        self.discriminator = None

        self.scm_type = scm_type
        self.hook_flag = hook_flag
        self.default_branch = default_branch
        self.trigger = trigger
        self.alias = alias
        self.display_name = display_name
        self.repo_name = repo_name
        self.repo_id = repo_id
        self.repo_owner = repo_owner
        self.git_url = git_url
        self.web_url = web_url

    @property
    def scm_type(self):
        """Gets the scm_type of this PipelineSource.

        源码仓类型

        :return: The scm_type of this PipelineSource.
        :rtype: str
        """
        return self._scm_type

    @scm_type.setter
    def scm_type(self, scm_type):
        """Sets the scm_type of this PipelineSource.

        源码仓类型

        :param scm_type: The scm_type of this PipelineSource.
        :type scm_type: str
        """
        self._scm_type = scm_type

    @property
    def hook_flag(self):
        """Gets the hook_flag of this PipelineSource.

        是否配置Webhook

        :return: The hook_flag of this PipelineSource.
        :rtype: str
        """
        return self._hook_flag

    @hook_flag.setter
    def hook_flag(self, hook_flag):
        """Sets the hook_flag of this PipelineSource.

        是否配置Webhook

        :param hook_flag: The hook_flag of this PipelineSource.
        :type hook_flag: str
        """
        self._hook_flag = hook_flag

    @property
    def default_branch(self):
        """Gets the default_branch of this PipelineSource.

        默认分支

        :return: The default_branch of this PipelineSource.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """Sets the default_branch of this PipelineSource.

        默认分支

        :param default_branch: The default_branch of this PipelineSource.
        :type default_branch: str
        """
        self._default_branch = default_branch

    @property
    def trigger(self):
        """Gets the trigger of this PipelineSource.

        webhook配置数据

        :return: The trigger of this PipelineSource.
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this PipelineSource.

        webhook配置数据

        :param trigger: The trigger of this PipelineSource.
        :type trigger: str
        """
        self._trigger = trigger

    @property
    def alias(self):
        """Gets the alias of this PipelineSource.

        代码仓别名

        :return: The alias of this PipelineSource.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this PipelineSource.

        代码仓别名

        :param alias: The alias of this PipelineSource.
        :type alias: str
        """
        self._alias = alias

    @property
    def display_name(self):
        """Gets the display_name of this PipelineSource.

        代码仓显示名

        :return: The display_name of this PipelineSource.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PipelineSource.

        代码仓显示名

        :param display_name: The display_name of this PipelineSource.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def repo_name(self):
        """Gets the repo_name of this PipelineSource.

        源码仓名称

        :return: The repo_name of this PipelineSource.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this PipelineSource.

        源码仓名称

        :param repo_name: The repo_name of this PipelineSource.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def repo_id(self):
        """Gets the repo_id of this PipelineSource.

        代码仓ID

        :return: The repo_id of this PipelineSource.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        """Sets the repo_id of this PipelineSource.

        代码仓ID

        :param repo_id: The repo_id of this PipelineSource.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def repo_owner(self):
        """Gets the repo_owner of this PipelineSource.

        代码仓所有者

        :return: The repo_owner of this PipelineSource.
        :rtype: str
        """
        return self._repo_owner

    @repo_owner.setter
    def repo_owner(self, repo_owner):
        """Sets the repo_owner of this PipelineSource.

        代码仓所有者

        :param repo_owner: The repo_owner of this PipelineSource.
        :type repo_owner: str
        """
        self._repo_owner = repo_owner

    @property
    def git_url(self):
        """Gets the git_url of this PipelineSource.

        代码仓访问地址

        :return: The git_url of this PipelineSource.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this PipelineSource.

        代码仓访问地址

        :param git_url: The git_url of this PipelineSource.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def web_url(self):
        """Gets the web_url of this PipelineSource.

        代码仓Web页面地址

        :return: The web_url of this PipelineSource.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        """Sets the web_url of this PipelineSource.

        代码仓Web页面地址

        :param web_url: The web_url of this PipelineSource.
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
        if not isinstance(other, PipelineSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
