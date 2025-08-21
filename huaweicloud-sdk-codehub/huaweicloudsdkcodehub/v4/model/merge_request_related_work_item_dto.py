# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestRelatedWorkItemDto:

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
        'user_id': 'str',
        'repo_id': 'int',
        'merge_request_id': 'int',
        'target_branch': 'str',
        'source_branch': 'str',
        'merge_request_title': 'str',
        'merge_request_url': 'str',
        'merge_request_state': 'str',
        'related_id': 'str',
        'related_title': 'str',
        'related_url': 'str',
        'result': 'int',
        'message': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'subject': 'str',
        'tracker': 'object',
        'status': 'object'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'repo_id': 'repo_id',
        'merge_request_id': 'merge_request_id',
        'target_branch': 'target_branch',
        'source_branch': 'source_branch',
        'merge_request_title': 'merge_request_title',
        'merge_request_url': 'merge_request_url',
        'merge_request_state': 'merge_request_state',
        'related_id': 'related_id',
        'related_title': 'related_title',
        'related_url': 'related_url',
        'result': 'result',
        'message': 'message',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'subject': 'subject',
        'tracker': 'tracker',
        'status': 'status'
    }

    def __init__(self, id=None, user_id=None, repo_id=None, merge_request_id=None, target_branch=None, source_branch=None, merge_request_title=None, merge_request_url=None, merge_request_state=None, related_id=None, related_title=None, related_url=None, result=None, message=None, create_at=None, update_at=None, subject=None, tracker=None, status=None):
        r"""MergeRequestRelatedWorkItemDto

        The model defined in huaweicloud sdk

        :param id: 关联id
        :type id: int
        :param user_id: 用户id
        :type user_id: str
        :param repo_id: 仓库id
        :type repo_id: int
        :param merge_request_id: 合并请求id
        :type merge_request_id: int
        :param target_branch: 目标分支
        :type target_branch: str
        :param source_branch: 源分支
        :type source_branch: str
        :param merge_request_title: 合并请求标题
        :type merge_request_title: str
        :param merge_request_url: 合并请求url
        :type merge_request_url: str
        :param merge_request_state: 合并请求状态
        :type merge_request_state: str
        :param related_id: 关联单id
        :type related_id: str
        :param related_title: 关联单标题
        :type related_title: str
        :param related_url: 关联单url
        :type related_url: str
        :param result: 关联结果
        :type result: int
        :param message: 关联结果信息
        :type message: str
        :param create_at: 创建时间
        :type create_at: str
        :param update_at: 更新时间
        :type update_at: str
        :param subject: 话题
        :type subject: str
        :param tracker: 跟单人
        :type tracker: object
        :param status: 状态
        :type status: object
        """
        
        

        self._id = None
        self._user_id = None
        self._repo_id = None
        self._merge_request_id = None
        self._target_branch = None
        self._source_branch = None
        self._merge_request_title = None
        self._merge_request_url = None
        self._merge_request_state = None
        self._related_id = None
        self._related_title = None
        self._related_url = None
        self._result = None
        self._message = None
        self._create_at = None
        self._update_at = None
        self._subject = None
        self._tracker = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if repo_id is not None:
            self.repo_id = repo_id
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if target_branch is not None:
            self.target_branch = target_branch
        if source_branch is not None:
            self.source_branch = source_branch
        if merge_request_title is not None:
            self.merge_request_title = merge_request_title
        if merge_request_url is not None:
            self.merge_request_url = merge_request_url
        if merge_request_state is not None:
            self.merge_request_state = merge_request_state
        if related_id is not None:
            self.related_id = related_id
        if related_title is not None:
            self.related_title = related_title
        if related_url is not None:
            self.related_url = related_url
        if result is not None:
            self.result = result
        if message is not None:
            self.message = message
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if subject is not None:
            self.subject = subject
        if tracker is not None:
            self.tracker = tracker
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this MergeRequestRelatedWorkItemDto.

        关联id

        :return: The id of this MergeRequestRelatedWorkItemDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestRelatedWorkItemDto.

        关联id

        :param id: The id of this MergeRequestRelatedWorkItemDto.
        :type id: int
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this MergeRequestRelatedWorkItemDto.

        用户id

        :return: The user_id of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this MergeRequestRelatedWorkItemDto.

        用户id

        :param user_id: The user_id of this MergeRequestRelatedWorkItemDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def repo_id(self):
        r"""Gets the repo_id of this MergeRequestRelatedWorkItemDto.

        仓库id

        :return: The repo_id of this MergeRequestRelatedWorkItemDto.
        :rtype: int
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this MergeRequestRelatedWorkItemDto.

        仓库id

        :param repo_id: The repo_id of this MergeRequestRelatedWorkItemDto.
        :type repo_id: int
        """
        self._repo_id = repo_id

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this MergeRequestRelatedWorkItemDto.

        合并请求id

        :return: The merge_request_id of this MergeRequestRelatedWorkItemDto.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this MergeRequestRelatedWorkItemDto.

        合并请求id

        :param merge_request_id: The merge_request_id of this MergeRequestRelatedWorkItemDto.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def target_branch(self):
        r"""Gets the target_branch of this MergeRequestRelatedWorkItemDto.

        目标分支

        :return: The target_branch of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this MergeRequestRelatedWorkItemDto.

        目标分支

        :param target_branch: The target_branch of this MergeRequestRelatedWorkItemDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def source_branch(self):
        r"""Gets the source_branch of this MergeRequestRelatedWorkItemDto.

        源分支

        :return: The source_branch of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this MergeRequestRelatedWorkItemDto.

        源分支

        :param source_branch: The source_branch of this MergeRequestRelatedWorkItemDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def merge_request_title(self):
        r"""Gets the merge_request_title of this MergeRequestRelatedWorkItemDto.

        合并请求标题

        :return: The merge_request_title of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._merge_request_title

    @merge_request_title.setter
    def merge_request_title(self, merge_request_title):
        r"""Sets the merge_request_title of this MergeRequestRelatedWorkItemDto.

        合并请求标题

        :param merge_request_title: The merge_request_title of this MergeRequestRelatedWorkItemDto.
        :type merge_request_title: str
        """
        self._merge_request_title = merge_request_title

    @property
    def merge_request_url(self):
        r"""Gets the merge_request_url of this MergeRequestRelatedWorkItemDto.

        合并请求url

        :return: The merge_request_url of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._merge_request_url

    @merge_request_url.setter
    def merge_request_url(self, merge_request_url):
        r"""Sets the merge_request_url of this MergeRequestRelatedWorkItemDto.

        合并请求url

        :param merge_request_url: The merge_request_url of this MergeRequestRelatedWorkItemDto.
        :type merge_request_url: str
        """
        self._merge_request_url = merge_request_url

    @property
    def merge_request_state(self):
        r"""Gets the merge_request_state of this MergeRequestRelatedWorkItemDto.

        合并请求状态

        :return: The merge_request_state of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._merge_request_state

    @merge_request_state.setter
    def merge_request_state(self, merge_request_state):
        r"""Sets the merge_request_state of this MergeRequestRelatedWorkItemDto.

        合并请求状态

        :param merge_request_state: The merge_request_state of this MergeRequestRelatedWorkItemDto.
        :type merge_request_state: str
        """
        self._merge_request_state = merge_request_state

    @property
    def related_id(self):
        r"""Gets the related_id of this MergeRequestRelatedWorkItemDto.

        关联单id

        :return: The related_id of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._related_id

    @related_id.setter
    def related_id(self, related_id):
        r"""Sets the related_id of this MergeRequestRelatedWorkItemDto.

        关联单id

        :param related_id: The related_id of this MergeRequestRelatedWorkItemDto.
        :type related_id: str
        """
        self._related_id = related_id

    @property
    def related_title(self):
        r"""Gets the related_title of this MergeRequestRelatedWorkItemDto.

        关联单标题

        :return: The related_title of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._related_title

    @related_title.setter
    def related_title(self, related_title):
        r"""Sets the related_title of this MergeRequestRelatedWorkItemDto.

        关联单标题

        :param related_title: The related_title of this MergeRequestRelatedWorkItemDto.
        :type related_title: str
        """
        self._related_title = related_title

    @property
    def related_url(self):
        r"""Gets the related_url of this MergeRequestRelatedWorkItemDto.

        关联单url

        :return: The related_url of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._related_url

    @related_url.setter
    def related_url(self, related_url):
        r"""Sets the related_url of this MergeRequestRelatedWorkItemDto.

        关联单url

        :param related_url: The related_url of this MergeRequestRelatedWorkItemDto.
        :type related_url: str
        """
        self._related_url = related_url

    @property
    def result(self):
        r"""Gets the result of this MergeRequestRelatedWorkItemDto.

        关联结果

        :return: The result of this MergeRequestRelatedWorkItemDto.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this MergeRequestRelatedWorkItemDto.

        关联结果

        :param result: The result of this MergeRequestRelatedWorkItemDto.
        :type result: int
        """
        self._result = result

    @property
    def message(self):
        r"""Gets the message of this MergeRequestRelatedWorkItemDto.

        关联结果信息

        :return: The message of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this MergeRequestRelatedWorkItemDto.

        关联结果信息

        :param message: The message of this MergeRequestRelatedWorkItemDto.
        :type message: str
        """
        self._message = message

    @property
    def create_at(self):
        r"""Gets the create_at of this MergeRequestRelatedWorkItemDto.

        创建时间

        :return: The create_at of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this MergeRequestRelatedWorkItemDto.

        创建时间

        :param create_at: The create_at of this MergeRequestRelatedWorkItemDto.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this MergeRequestRelatedWorkItemDto.

        更新时间

        :return: The update_at of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this MergeRequestRelatedWorkItemDto.

        更新时间

        :param update_at: The update_at of this MergeRequestRelatedWorkItemDto.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def subject(self):
        r"""Gets the subject of this MergeRequestRelatedWorkItemDto.

        话题

        :return: The subject of this MergeRequestRelatedWorkItemDto.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this MergeRequestRelatedWorkItemDto.

        话题

        :param subject: The subject of this MergeRequestRelatedWorkItemDto.
        :type subject: str
        """
        self._subject = subject

    @property
    def tracker(self):
        r"""Gets the tracker of this MergeRequestRelatedWorkItemDto.

        跟单人

        :return: The tracker of this MergeRequestRelatedWorkItemDto.
        :rtype: object
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        r"""Sets the tracker of this MergeRequestRelatedWorkItemDto.

        跟单人

        :param tracker: The tracker of this MergeRequestRelatedWorkItemDto.
        :type tracker: object
        """
        self._tracker = tracker

    @property
    def status(self):
        r"""Gets the status of this MergeRequestRelatedWorkItemDto.

        状态

        :return: The status of this MergeRequestRelatedWorkItemDto.
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MergeRequestRelatedWorkItemDto.

        状态

        :param status: The status of this MergeRequestRelatedWorkItemDto.
        :type status: object
        """
        self._status = status

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
        if not isinstance(other, MergeRequestRelatedWorkItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
