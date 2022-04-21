# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskRequestV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'check_type': 'list[str]',
        'git_url': 'str',
        'git_branch': 'str',
        'language': 'list[str]',
        'rule_sets': 'list[RuleSetV2]',
        'task_type': 'str',
        'username': 'str',
        'access_token': 'str',
        'endpoint_id': 'str',
        'inc_config': 'IncConfigV2',
        'enable_fossbot': 'bool',
        'resource_pool_id': 'str'
    }

    attribute_map = {
        'check_type': 'check_type',
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'language': 'language',
        'rule_sets': 'rule_sets',
        'task_type': 'task_type',
        'username': 'username',
        'access_token': 'access_token',
        'endpoint_id': 'endpoint_id',
        'inc_config': 'inc_config',
        'enable_fossbot': 'enable_fossbot',
        'resource_pool_id': 'resource_pool_id'
    }

    def __init__(self, check_type=None, git_url=None, git_branch=None, language=None, rule_sets=None, task_type=None, username=None, access_token=None, endpoint_id=None, inc_config=None, enable_fossbot=None, resource_pool_id=None):
        """CreateTaskRequestV2

        The model defined in huaweicloud sdk

        :param check_type: 检查类型，数组格式，默认为source
        :type check_type: list[str]
        :param git_url: 仓库地址
        :type git_url: str
        :param git_branch: 仓库分支
        :type git_branch: str
        :param language: 检查语言，数组格式，支持cpp,java,js,python,php,css,html,go,typescript,csharp
        :type language: list[str]
        :param rule_sets: 指定规则集
        :type rule_sets: list[:class:`huaweicloudsdkcodecheck.v2.RuleSetV2`]
        :param task_type: 检查类型，支持full/inc两种类型，full表示全量检查，inc表示mr检查
        :type task_type: str
        :param username: 仓库有权限的用户名
        :type username: str
        :param access_token: 仓库有权限的用户token
        :type access_token: str
        :param endpoint_id: 仓库有权限的用户endpointId
        :type endpoint_id: str
        :param inc_config: 
        :type inc_config: :class:`huaweicloudsdkcodecheck.v2.IncConfigV2`
        :param enable_fossbot: 是否打开fossbot检查,默认不开
        :type enable_fossbot: bool
        :param resource_pool_id: 资源池id，可以从资源池管理页面获取
        :type resource_pool_id: str
        """
        
        

        self._check_type = None
        self._git_url = None
        self._git_branch = None
        self._language = None
        self._rule_sets = None
        self._task_type = None
        self._username = None
        self._access_token = None
        self._endpoint_id = None
        self._inc_config = None
        self._enable_fossbot = None
        self._resource_pool_id = None
        self.discriminator = None

        if check_type is not None:
            self.check_type = check_type
        self.git_url = git_url
        self.git_branch = git_branch
        self.language = language
        if rule_sets is not None:
            self.rule_sets = rule_sets
        if task_type is not None:
            self.task_type = task_type
        if username is not None:
            self.username = username
        if access_token is not None:
            self.access_token = access_token
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if inc_config is not None:
            self.inc_config = inc_config
        if enable_fossbot is not None:
            self.enable_fossbot = enable_fossbot
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id

    @property
    def check_type(self):
        """Gets the check_type of this CreateTaskRequestV2.

        检查类型，数组格式，默认为source

        :return: The check_type of this CreateTaskRequestV2.
        :rtype: list[str]
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this CreateTaskRequestV2.

        检查类型，数组格式，默认为source

        :param check_type: The check_type of this CreateTaskRequestV2.
        :type check_type: list[str]
        """
        self._check_type = check_type

    @property
    def git_url(self):
        """Gets the git_url of this CreateTaskRequestV2.

        仓库地址

        :return: The git_url of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this CreateTaskRequestV2.

        仓库地址

        :param git_url: The git_url of this CreateTaskRequestV2.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        """Gets the git_branch of this CreateTaskRequestV2.

        仓库分支

        :return: The git_branch of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """Sets the git_branch of this CreateTaskRequestV2.

        仓库分支

        :param git_branch: The git_branch of this CreateTaskRequestV2.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def language(self):
        """Gets the language of this CreateTaskRequestV2.

        检查语言，数组格式，支持cpp,java,js,python,php,css,html,go,typescript,csharp

        :return: The language of this CreateTaskRequestV2.
        :rtype: list[str]
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateTaskRequestV2.

        检查语言，数组格式，支持cpp,java,js,python,php,css,html,go,typescript,csharp

        :param language: The language of this CreateTaskRequestV2.
        :type language: list[str]
        """
        self._language = language

    @property
    def rule_sets(self):
        """Gets the rule_sets of this CreateTaskRequestV2.

        指定规则集

        :return: The rule_sets of this CreateTaskRequestV2.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.RuleSetV2`]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        """Sets the rule_sets of this CreateTaskRequestV2.

        指定规则集

        :param rule_sets: The rule_sets of this CreateTaskRequestV2.
        :type rule_sets: list[:class:`huaweicloudsdkcodecheck.v2.RuleSetV2`]
        """
        self._rule_sets = rule_sets

    @property
    def task_type(self):
        """Gets the task_type of this CreateTaskRequestV2.

        检查类型，支持full/inc两种类型，full表示全量检查，inc表示mr检查

        :return: The task_type of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateTaskRequestV2.

        检查类型，支持full/inc两种类型，full表示全量检查，inc表示mr检查

        :param task_type: The task_type of this CreateTaskRequestV2.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def username(self):
        """Gets the username of this CreateTaskRequestV2.

        仓库有权限的用户名

        :return: The username of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreateTaskRequestV2.

        仓库有权限的用户名

        :param username: The username of this CreateTaskRequestV2.
        :type username: str
        """
        self._username = username

    @property
    def access_token(self):
        """Gets the access_token of this CreateTaskRequestV2.

        仓库有权限的用户token

        :return: The access_token of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this CreateTaskRequestV2.

        仓库有权限的用户token

        :param access_token: The access_token of this CreateTaskRequestV2.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this CreateTaskRequestV2.

        仓库有权限的用户endpointId

        :return: The endpoint_id of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this CreateTaskRequestV2.

        仓库有权限的用户endpointId

        :param endpoint_id: The endpoint_id of this CreateTaskRequestV2.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def inc_config(self):
        """Gets the inc_config of this CreateTaskRequestV2.


        :return: The inc_config of this CreateTaskRequestV2.
        :rtype: :class:`huaweicloudsdkcodecheck.v2.IncConfigV2`
        """
        return self._inc_config

    @inc_config.setter
    def inc_config(self, inc_config):
        """Sets the inc_config of this CreateTaskRequestV2.


        :param inc_config: The inc_config of this CreateTaskRequestV2.
        :type inc_config: :class:`huaweicloudsdkcodecheck.v2.IncConfigV2`
        """
        self._inc_config = inc_config

    @property
    def enable_fossbot(self):
        """Gets the enable_fossbot of this CreateTaskRequestV2.

        是否打开fossbot检查,默认不开

        :return: The enable_fossbot of this CreateTaskRequestV2.
        :rtype: bool
        """
        return self._enable_fossbot

    @enable_fossbot.setter
    def enable_fossbot(self, enable_fossbot):
        """Sets the enable_fossbot of this CreateTaskRequestV2.

        是否打开fossbot检查,默认不开

        :param enable_fossbot: The enable_fossbot of this CreateTaskRequestV2.
        :type enable_fossbot: bool
        """
        self._enable_fossbot = enable_fossbot

    @property
    def resource_pool_id(self):
        """Gets the resource_pool_id of this CreateTaskRequestV2.

        资源池id，可以从资源池管理页面获取

        :return: The resource_pool_id of this CreateTaskRequestV2.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """Sets the resource_pool_id of this CreateTaskRequestV2.

        资源池id，可以从资源池管理页面获取

        :param resource_pool_id: The resource_pool_id of this CreateTaskRequestV2.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

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
        if not isinstance(other, CreateTaskRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
