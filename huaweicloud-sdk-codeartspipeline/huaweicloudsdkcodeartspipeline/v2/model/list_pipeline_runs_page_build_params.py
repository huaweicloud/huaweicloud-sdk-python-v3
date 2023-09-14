# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineRunsPageBuildParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'build_type': 'str',
        'commit_id': 'str',
        'event_type': 'str',
        'merge_id': 'str',
        'message': 'str',
        'source_branch': 'str',
        'tag': 'str',
        'target_branch': 'str',
        'codehub_id': 'str',
        'git_url': 'str',
        'source_codehub_id': 'str',
        'source_codehub_url': 'str',
        'source_codehub_http_url': 'str'
    }

    attribute_map = {
        'action': 'action',
        'build_type': 'build_type',
        'commit_id': 'commit_id',
        'event_type': 'event_type',
        'merge_id': 'merge_id',
        'message': 'message',
        'source_branch': 'source_branch',
        'tag': 'tag',
        'target_branch': 'target_branch',
        'codehub_id': 'codehub_id',
        'git_url': 'git_url',
        'source_codehub_id': 'source_codehub_id',
        'source_codehub_url': 'source_codehub_url',
        'source_codehub_http_url': 'source_codehub_http_url'
    }

    def __init__(self, action=None, build_type=None, commit_id=None, event_type=None, merge_id=None, message=None, source_branch=None, tag=None, target_branch=None, codehub_id=None, git_url=None, source_codehub_id=None, source_codehub_url=None, source_codehub_http_url=None):
        """ListPipelineRunsPageBuildParams

        The model defined in huaweicloud sdk

        :param action: 合并请求事件类型
        :type action: str
        :param build_type: 基于分支还是tag触发
        :type build_type: str
        :param commit_id: 代码仓提交ID
        :type commit_id: str
        :param event_type: 运行事件类型
        :type event_type: str
        :param merge_id: 合并请求ID
        :type merge_id: str
        :param message: 代码仓提交信息
        :type message: str
        :param source_branch: 源分支
        :type source_branch: str
        :param tag: 标签
        :type tag: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param codehub_id: codehub代码仓ID
        :type codehub_id: str
        :param git_url: 代码仓https地址
        :type git_url: str
        :param source_codehub_id: 源codehub代码仓ID
        :type source_codehub_id: str
        :param source_codehub_url: 源codehub代码仓地址
        :type source_codehub_url: str
        :param source_codehub_http_url: 源codehub代码仓http地址
        :type source_codehub_http_url: str
        """
        
        

        self._action = None
        self._build_type = None
        self._commit_id = None
        self._event_type = None
        self._merge_id = None
        self._message = None
        self._source_branch = None
        self._tag = None
        self._target_branch = None
        self._codehub_id = None
        self._git_url = None
        self._source_codehub_id = None
        self._source_codehub_url = None
        self._source_codehub_http_url = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if build_type is not None:
            self.build_type = build_type
        if commit_id is not None:
            self.commit_id = commit_id
        if event_type is not None:
            self.event_type = event_type
        if merge_id is not None:
            self.merge_id = merge_id
        if message is not None:
            self.message = message
        if source_branch is not None:
            self.source_branch = source_branch
        if tag is not None:
            self.tag = tag
        if target_branch is not None:
            self.target_branch = target_branch
        if codehub_id is not None:
            self.codehub_id = codehub_id
        if git_url is not None:
            self.git_url = git_url
        if source_codehub_id is not None:
            self.source_codehub_id = source_codehub_id
        if source_codehub_url is not None:
            self.source_codehub_url = source_codehub_url
        if source_codehub_http_url is not None:
            self.source_codehub_http_url = source_codehub_http_url

    @property
    def action(self):
        """Gets the action of this ListPipelineRunsPageBuildParams.

        合并请求事件类型

        :return: The action of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ListPipelineRunsPageBuildParams.

        合并请求事件类型

        :param action: The action of this ListPipelineRunsPageBuildParams.
        :type action: str
        """
        self._action = action

    @property
    def build_type(self):
        """Gets the build_type of this ListPipelineRunsPageBuildParams.

        基于分支还是tag触发

        :return: The build_type of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this ListPipelineRunsPageBuildParams.

        基于分支还是tag触发

        :param build_type: The build_type of this ListPipelineRunsPageBuildParams.
        :type build_type: str
        """
        self._build_type = build_type

    @property
    def commit_id(self):
        """Gets the commit_id of this ListPipelineRunsPageBuildParams.

        代码仓提交ID

        :return: The commit_id of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ListPipelineRunsPageBuildParams.

        代码仓提交ID

        :param commit_id: The commit_id of this ListPipelineRunsPageBuildParams.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def event_type(self):
        """Gets the event_type of this ListPipelineRunsPageBuildParams.

        运行事件类型

        :return: The event_type of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ListPipelineRunsPageBuildParams.

        运行事件类型

        :param event_type: The event_type of this ListPipelineRunsPageBuildParams.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def merge_id(self):
        """Gets the merge_id of this ListPipelineRunsPageBuildParams.

        合并请求ID

        :return: The merge_id of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._merge_id

    @merge_id.setter
    def merge_id(self, merge_id):
        """Sets the merge_id of this ListPipelineRunsPageBuildParams.

        合并请求ID

        :param merge_id: The merge_id of this ListPipelineRunsPageBuildParams.
        :type merge_id: str
        """
        self._merge_id = merge_id

    @property
    def message(self):
        """Gets the message of this ListPipelineRunsPageBuildParams.

        代码仓提交信息

        :return: The message of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListPipelineRunsPageBuildParams.

        代码仓提交信息

        :param message: The message of this ListPipelineRunsPageBuildParams.
        :type message: str
        """
        self._message = message

    @property
    def source_branch(self):
        """Gets the source_branch of this ListPipelineRunsPageBuildParams.

        源分支

        :return: The source_branch of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        """Sets the source_branch of this ListPipelineRunsPageBuildParams.

        源分支

        :param source_branch: The source_branch of this ListPipelineRunsPageBuildParams.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def tag(self):
        """Gets the tag of this ListPipelineRunsPageBuildParams.

        标签

        :return: The tag of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListPipelineRunsPageBuildParams.

        标签

        :param tag: The tag of this ListPipelineRunsPageBuildParams.
        :type tag: str
        """
        self._tag = tag

    @property
    def target_branch(self):
        """Gets the target_branch of this ListPipelineRunsPageBuildParams.

        目标分支

        :return: The target_branch of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        """Sets the target_branch of this ListPipelineRunsPageBuildParams.

        目标分支

        :param target_branch: The target_branch of this ListPipelineRunsPageBuildParams.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def codehub_id(self):
        """Gets the codehub_id of this ListPipelineRunsPageBuildParams.

        codehub代码仓ID

        :return: The codehub_id of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._codehub_id

    @codehub_id.setter
    def codehub_id(self, codehub_id):
        """Sets the codehub_id of this ListPipelineRunsPageBuildParams.

        codehub代码仓ID

        :param codehub_id: The codehub_id of this ListPipelineRunsPageBuildParams.
        :type codehub_id: str
        """
        self._codehub_id = codehub_id

    @property
    def git_url(self):
        """Gets the git_url of this ListPipelineRunsPageBuildParams.

        代码仓https地址

        :return: The git_url of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this ListPipelineRunsPageBuildParams.

        代码仓https地址

        :param git_url: The git_url of this ListPipelineRunsPageBuildParams.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def source_codehub_id(self):
        """Gets the source_codehub_id of this ListPipelineRunsPageBuildParams.

        源codehub代码仓ID

        :return: The source_codehub_id of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._source_codehub_id

    @source_codehub_id.setter
    def source_codehub_id(self, source_codehub_id):
        """Sets the source_codehub_id of this ListPipelineRunsPageBuildParams.

        源codehub代码仓ID

        :param source_codehub_id: The source_codehub_id of this ListPipelineRunsPageBuildParams.
        :type source_codehub_id: str
        """
        self._source_codehub_id = source_codehub_id

    @property
    def source_codehub_url(self):
        """Gets the source_codehub_url of this ListPipelineRunsPageBuildParams.

        源codehub代码仓地址

        :return: The source_codehub_url of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._source_codehub_url

    @source_codehub_url.setter
    def source_codehub_url(self, source_codehub_url):
        """Sets the source_codehub_url of this ListPipelineRunsPageBuildParams.

        源codehub代码仓地址

        :param source_codehub_url: The source_codehub_url of this ListPipelineRunsPageBuildParams.
        :type source_codehub_url: str
        """
        self._source_codehub_url = source_codehub_url

    @property
    def source_codehub_http_url(self):
        """Gets the source_codehub_http_url of this ListPipelineRunsPageBuildParams.

        源codehub代码仓http地址

        :return: The source_codehub_http_url of this ListPipelineRunsPageBuildParams.
        :rtype: str
        """
        return self._source_codehub_http_url

    @source_codehub_http_url.setter
    def source_codehub_http_url(self, source_codehub_http_url):
        """Sets the source_codehub_http_url of this ListPipelineRunsPageBuildParams.

        源codehub代码仓http地址

        :param source_codehub_http_url: The source_codehub_http_url of this ListPipelineRunsPageBuildParams.
        :type source_codehub_http_url: str
        """
        self._source_codehub_http_url = source_codehub_http_url

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
        if not isinstance(other, ListPipelineRunsPageBuildParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
