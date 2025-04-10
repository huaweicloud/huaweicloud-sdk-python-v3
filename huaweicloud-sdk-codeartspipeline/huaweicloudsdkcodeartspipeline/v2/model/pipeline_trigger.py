# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTrigger:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'git_url': 'str',
        'git_type': 'str',
        'is_auto_commit': 'bool',
        'events': 'list[CodeEvent]',
        'hook_id': 'str',
        'repo_id': 'str',
        'endpoint_id': 'str',
        'callback_url': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'git_url': 'git_url',
        'git_type': 'git_type',
        'is_auto_commit': 'is_auto_commit',
        'events': 'events',
        'hook_id': 'hook_id',
        'repo_id': 'repo_id',
        'endpoint_id': 'endpoint_id',
        'callback_url': 'callback_url',
        'security_token': 'security_token'
    }

    def __init__(self, pipeline_id=None, git_url=None, git_type=None, is_auto_commit=None, events=None, hook_id=None, repo_id=None, endpoint_id=None, callback_url=None, security_token=None):
        r"""PipelineTrigger

        The model defined in huaweicloud sdk

        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param git_url: git链接
        :type git_url: str
        :param git_type: 代码仓类型
        :type git_type: str
        :param is_auto_commit: 是否自动提交
        :type is_auto_commit: bool
        :param events: 事件
        :type events: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeEvent`]
        :param hook_id: 回调id
        :type hook_id: str
        :param repo_id: 仓库id
        :type repo_id: str
        :param endpoint_id: 扩展点id
        :type endpoint_id: str
        :param callback_url: 回调链接
        :type callback_url: str
        :param security_token: 用户token
        :type security_token: str
        """
        
        

        self._pipeline_id = None
        self._git_url = None
        self._git_type = None
        self._is_auto_commit = None
        self._events = None
        self._hook_id = None
        self._repo_id = None
        self._endpoint_id = None
        self._callback_url = None
        self._security_token = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if git_url is not None:
            self.git_url = git_url
        if git_type is not None:
            self.git_type = git_type
        if is_auto_commit is not None:
            self.is_auto_commit = is_auto_commit
        if events is not None:
            self.events = events
        if hook_id is not None:
            self.hook_id = hook_id
        if repo_id is not None:
            self.repo_id = repo_id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if callback_url is not None:
            self.callback_url = callback_url
        if security_token is not None:
            self.security_token = security_token

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineTrigger.

        流水线ID

        :return: The pipeline_id of this PipelineTrigger.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineTrigger.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineTrigger.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def git_url(self):
        r"""Gets the git_url of this PipelineTrigger.

        git链接

        :return: The git_url of this PipelineTrigger.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this PipelineTrigger.

        git链接

        :param git_url: The git_url of this PipelineTrigger.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_type(self):
        r"""Gets the git_type of this PipelineTrigger.

        代码仓类型

        :return: The git_type of this PipelineTrigger.
        :rtype: str
        """
        return self._git_type

    @git_type.setter
    def git_type(self, git_type):
        r"""Sets the git_type of this PipelineTrigger.

        代码仓类型

        :param git_type: The git_type of this PipelineTrigger.
        :type git_type: str
        """
        self._git_type = git_type

    @property
    def is_auto_commit(self):
        r"""Gets the is_auto_commit of this PipelineTrigger.

        是否自动提交

        :return: The is_auto_commit of this PipelineTrigger.
        :rtype: bool
        """
        return self._is_auto_commit

    @is_auto_commit.setter
    def is_auto_commit(self, is_auto_commit):
        r"""Sets the is_auto_commit of this PipelineTrigger.

        是否自动提交

        :param is_auto_commit: The is_auto_commit of this PipelineTrigger.
        :type is_auto_commit: bool
        """
        self._is_auto_commit = is_auto_commit

    @property
    def events(self):
        r"""Gets the events of this PipelineTrigger.

        事件

        :return: The events of this PipelineTrigger.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this PipelineTrigger.

        事件

        :param events: The events of this PipelineTrigger.
        :type events: list[:class:`huaweicloudsdkcodeartspipeline.v2.CodeEvent`]
        """
        self._events = events

    @property
    def hook_id(self):
        r"""Gets the hook_id of this PipelineTrigger.

        回调id

        :return: The hook_id of this PipelineTrigger.
        :rtype: str
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        r"""Sets the hook_id of this PipelineTrigger.

        回调id

        :param hook_id: The hook_id of this PipelineTrigger.
        :type hook_id: str
        """
        self._hook_id = hook_id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this PipelineTrigger.

        仓库id

        :return: The repo_id of this PipelineTrigger.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this PipelineTrigger.

        仓库id

        :param repo_id: The repo_id of this PipelineTrigger.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this PipelineTrigger.

        扩展点id

        :return: The endpoint_id of this PipelineTrigger.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this PipelineTrigger.

        扩展点id

        :param endpoint_id: The endpoint_id of this PipelineTrigger.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def callback_url(self):
        r"""Gets the callback_url of this PipelineTrigger.

        回调链接

        :return: The callback_url of this PipelineTrigger.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this PipelineTrigger.

        回调链接

        :param callback_url: The callback_url of this PipelineTrigger.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def security_token(self):
        r"""Gets the security_token of this PipelineTrigger.

        用户token

        :return: The security_token of this PipelineTrigger.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this PipelineTrigger.

        用户token

        :param security_token: The security_token of this PipelineTrigger.
        :type security_token: str
        """
        self._security_token = security_token

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
        if not isinstance(other, PipelineTrigger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
