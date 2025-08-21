# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiteMergeRequestDto:

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
        'repository_id': 'int',
        'title': 'str',
        'description': 'str',
        'state': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'author': 'UserBasicDto',
        'web_url': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'repository_id': 'repository_id',
        'title': 'title',
        'description': 'description',
        'state': 'state',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'author': 'author',
        'web_url': 'web_url',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, id=None, repository_id=None, title=None, description=None, state=None, source_branch=None, target_branch=None, author=None, web_url=None, create_at=None, update_at=None):
        r"""LiteMergeRequestDto

        The model defined in huaweicloud sdk

        :param id: MR id
        :type id: int
        :param repository_id: 仓库id
        :type repository_id: int
        :param title: 合并请求标题
        :type title: str
        :param description: 合并请求描述
        :type description: str
        :param state: 合并请求状态
        :type state: str
        :param source_branch: 合并请求源分支名
        :type source_branch: str
        :param target_branch: 合并请求目标分支名
        :type target_branch: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param web_url: 合并请求URL链接
        :type web_url: str
        :param create_at: 合并请求创建时间
        :type create_at: str
        :param update_at: 合并请求最后更新时间
        :type update_at: str
        """
        
        

        self._id = None
        self._repository_id = None
        self._title = None
        self._description = None
        self._state = None
        self._source_branch = None
        self._target_branch = None
        self._author = None
        self._web_url = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if repository_id is not None:
            self.repository_id = repository_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if author is not None:
            self.author = author
        if web_url is not None:
            self.web_url = web_url
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at

    @property
    def id(self):
        r"""Gets the id of this LiteMergeRequestDto.

        MR id

        :return: The id of this LiteMergeRequestDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LiteMergeRequestDto.

        MR id

        :param id: The id of this LiteMergeRequestDto.
        :type id: int
        """
        self._id = id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this LiteMergeRequestDto.

        仓库id

        :return: The repository_id of this LiteMergeRequestDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this LiteMergeRequestDto.

        仓库id

        :param repository_id: The repository_id of this LiteMergeRequestDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def title(self):
        r"""Gets the title of this LiteMergeRequestDto.

        合并请求标题

        :return: The title of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LiteMergeRequestDto.

        合并请求标题

        :param title: The title of this LiteMergeRequestDto.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this LiteMergeRequestDto.

        合并请求描述

        :return: The description of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LiteMergeRequestDto.

        合并请求描述

        :param description: The description of this LiteMergeRequestDto.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this LiteMergeRequestDto.

        合并请求状态

        :return: The state of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this LiteMergeRequestDto.

        合并请求状态

        :param state: The state of this LiteMergeRequestDto.
        :type state: str
        """
        self._state = state

    @property
    def source_branch(self):
        r"""Gets the source_branch of this LiteMergeRequestDto.

        合并请求源分支名

        :return: The source_branch of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this LiteMergeRequestDto.

        合并请求源分支名

        :param source_branch: The source_branch of this LiteMergeRequestDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this LiteMergeRequestDto.

        合并请求目标分支名

        :return: The target_branch of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this LiteMergeRequestDto.

        合并请求目标分支名

        :param target_branch: The target_branch of this LiteMergeRequestDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def author(self):
        r"""Gets the author of this LiteMergeRequestDto.

        :return: The author of this LiteMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this LiteMergeRequestDto.

        :param author: The author of this LiteMergeRequestDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def web_url(self):
        r"""Gets the web_url of this LiteMergeRequestDto.

        合并请求URL链接

        :return: The web_url of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this LiteMergeRequestDto.

        合并请求URL链接

        :param web_url: The web_url of this LiteMergeRequestDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def create_at(self):
        r"""Gets the create_at of this LiteMergeRequestDto.

        合并请求创建时间

        :return: The create_at of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this LiteMergeRequestDto.

        合并请求创建时间

        :param create_at: The create_at of this LiteMergeRequestDto.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this LiteMergeRequestDto.

        合并请求最后更新时间

        :return: The update_at of this LiteMergeRequestDto.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this LiteMergeRequestDto.

        合并请求最后更新时间

        :param update_at: The update_at of this LiteMergeRequestDto.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, LiteMergeRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
