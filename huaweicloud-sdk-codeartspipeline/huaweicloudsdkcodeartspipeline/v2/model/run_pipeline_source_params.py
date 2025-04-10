# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunPipelineSourceParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'git_type': 'str',
        'git_url': 'str',
        'ssh_git_url': 'str',
        'web_url': 'str',
        'repo_name': 'str',
        'default_branch': 'str',
        'endpoint_id': 'str',
        'codehub_id': 'str',
        'alias': 'str',
        'build_params': 'RunPipelineSourceParamsBuildParams'
    }

    attribute_map = {
        'git_type': 'git_type',
        'git_url': 'git_url',
        'ssh_git_url': 'ssh_git_url',
        'web_url': 'web_url',
        'repo_name': 'repo_name',
        'default_branch': 'default_branch',
        'endpoint_id': 'endpoint_id',
        'codehub_id': 'codehub_id',
        'alias': 'alias',
        'build_params': 'build_params'
    }

    def __init__(self, git_type=None, git_url=None, ssh_git_url=None, web_url=None, repo_name=None, default_branch=None, endpoint_id=None, codehub_id=None, alias=None, build_params=None):
        r"""RunPipelineSourceParams

        The model defined in huaweicloud sdk

        :param git_type: 代码仓类型
        :type git_type: str
        :param git_url: 代码仓https地址
        :type git_url: str
        :param ssh_git_url: 代码仓ssh地址
        :type ssh_git_url: str
        :param web_url: 代码仓页面地址
        :type web_url: str
        :param repo_name: 代码仓名
        :type repo_name: str
        :param default_branch: 默认分支
        :type default_branch: str
        :param endpoint_id: 扩展点ID
        :type endpoint_id: str
        :param codehub_id: codehub代码仓ID
        :type codehub_id: str
        :param alias: 代码仓别名
        :type alias: str
        :param build_params: 
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSourceParamsBuildParams`
        """
        
        

        self._git_type = None
        self._git_url = None
        self._ssh_git_url = None
        self._web_url = None
        self._repo_name = None
        self._default_branch = None
        self._endpoint_id = None
        self._codehub_id = None
        self._alias = None
        self._build_params = None
        self.discriminator = None

        if git_type is not None:
            self.git_type = git_type
        if git_url is not None:
            self.git_url = git_url
        if ssh_git_url is not None:
            self.ssh_git_url = ssh_git_url
        if web_url is not None:
            self.web_url = web_url
        if repo_name is not None:
            self.repo_name = repo_name
        if default_branch is not None:
            self.default_branch = default_branch
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if codehub_id is not None:
            self.codehub_id = codehub_id
        if alias is not None:
            self.alias = alias
        if build_params is not None:
            self.build_params = build_params

    @property
    def git_type(self):
        r"""Gets the git_type of this RunPipelineSourceParams.

        代码仓类型

        :return: The git_type of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._git_type

    @git_type.setter
    def git_type(self, git_type):
        r"""Sets the git_type of this RunPipelineSourceParams.

        代码仓类型

        :param git_type: The git_type of this RunPipelineSourceParams.
        :type git_type: str
        """
        self._git_type = git_type

    @property
    def git_url(self):
        r"""Gets the git_url of this RunPipelineSourceParams.

        代码仓https地址

        :return: The git_url of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this RunPipelineSourceParams.

        代码仓https地址

        :param git_url: The git_url of this RunPipelineSourceParams.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def ssh_git_url(self):
        r"""Gets the ssh_git_url of this RunPipelineSourceParams.

        代码仓ssh地址

        :return: The ssh_git_url of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._ssh_git_url

    @ssh_git_url.setter
    def ssh_git_url(self, ssh_git_url):
        r"""Sets the ssh_git_url of this RunPipelineSourceParams.

        代码仓ssh地址

        :param ssh_git_url: The ssh_git_url of this RunPipelineSourceParams.
        :type ssh_git_url: str
        """
        self._ssh_git_url = ssh_git_url

    @property
    def web_url(self):
        r"""Gets the web_url of this RunPipelineSourceParams.

        代码仓页面地址

        :return: The web_url of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this RunPipelineSourceParams.

        代码仓页面地址

        :param web_url: The web_url of this RunPipelineSourceParams.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def repo_name(self):
        r"""Gets the repo_name of this RunPipelineSourceParams.

        代码仓名

        :return: The repo_name of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        r"""Sets the repo_name of this RunPipelineSourceParams.

        代码仓名

        :param repo_name: The repo_name of this RunPipelineSourceParams.
        :type repo_name: str
        """
        self._repo_name = repo_name

    @property
    def default_branch(self):
        r"""Gets the default_branch of this RunPipelineSourceParams.

        默认分支

        :return: The default_branch of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        r"""Sets the default_branch of this RunPipelineSourceParams.

        默认分支

        :param default_branch: The default_branch of this RunPipelineSourceParams.
        :type default_branch: str
        """
        self._default_branch = default_branch

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this RunPipelineSourceParams.

        扩展点ID

        :return: The endpoint_id of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this RunPipelineSourceParams.

        扩展点ID

        :param endpoint_id: The endpoint_id of this RunPipelineSourceParams.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def codehub_id(self):
        r"""Gets the codehub_id of this RunPipelineSourceParams.

        codehub代码仓ID

        :return: The codehub_id of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._codehub_id

    @codehub_id.setter
    def codehub_id(self, codehub_id):
        r"""Sets the codehub_id of this RunPipelineSourceParams.

        codehub代码仓ID

        :param codehub_id: The codehub_id of this RunPipelineSourceParams.
        :type codehub_id: str
        """
        self._codehub_id = codehub_id

    @property
    def alias(self):
        r"""Gets the alias of this RunPipelineSourceParams.

        代码仓别名

        :return: The alias of this RunPipelineSourceParams.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this RunPipelineSourceParams.

        代码仓别名

        :param alias: The alias of this RunPipelineSourceParams.
        :type alias: str
        """
        self._alias = alias

    @property
    def build_params(self):
        r"""Gets the build_params of this RunPipelineSourceParams.

        :return: The build_params of this RunPipelineSourceParams.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSourceParamsBuildParams`
        """
        return self._build_params

    @build_params.setter
    def build_params(self, build_params):
        r"""Sets the build_params of this RunPipelineSourceParams.

        :param build_params: The build_params of this RunPipelineSourceParams.
        :type build_params: :class:`huaweicloudsdkcodeartspipeline.v2.RunPipelineSourceParamsBuildParams`
        """
        self._build_params = build_params

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
        if not isinstance(other, RunPipelineSourceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
