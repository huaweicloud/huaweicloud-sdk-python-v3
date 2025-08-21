# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryPushEventDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action_name': 'str',
        'author': 'RepositoryEventAuthorDto',
        'author_id': 'int',
        'author_username': 'str',
        'created_at': 'str',
        'repository_id': 'int',
        'repository_name': 'str',
        'push_data': 'PushEventPayloadDto'
    }

    attribute_map = {
        'action_name': 'action_name',
        'author': 'author',
        'author_id': 'author_id',
        'author_username': 'author_username',
        'created_at': 'created_at',
        'repository_id': 'repository_id',
        'repository_name': 'repository_name',
        'push_data': 'push_data'
    }

    def __init__(self, action_name=None, author=None, author_id=None, author_username=None, created_at=None, repository_id=None, repository_name=None, push_data=None):
        r"""RepositoryPushEventDto

        The model defined in huaweicloud sdk

        :param action_name: **参数解释：** 操作名称。 - pushed to，表示推送。 - pushed new，表示推送并新建。 - deleted，表示删除。
        :type action_name: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.RepositoryEventAuthorDto`
        :param author_id: **参数解释：** 触发者ID。
        :type author_id: int
        :param author_username: **参数解释：** 触发者名称。
        :type author_username: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param repository_id: **参数解释：** 仓库ID。
        :type repository_id: int
        :param repository_name: **参数解释：** 仓库名。
        :type repository_name: str
        :param push_data: 
        :type push_data: :class:`huaweicloudsdkcodehub.v4.PushEventPayloadDto`
        """
        
        

        self._action_name = None
        self._author = None
        self._author_id = None
        self._author_username = None
        self._created_at = None
        self._repository_id = None
        self._repository_name = None
        self._push_data = None
        self.discriminator = None

        if action_name is not None:
            self.action_name = action_name
        if author is not None:
            self.author = author
        if author_id is not None:
            self.author_id = author_id
        if author_username is not None:
            self.author_username = author_username
        if created_at is not None:
            self.created_at = created_at
        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if push_data is not None:
            self.push_data = push_data

    @property
    def action_name(self):
        r"""Gets the action_name of this RepositoryPushEventDto.

        **参数解释：** 操作名称。 - pushed to，表示推送。 - pushed new，表示推送并新建。 - deleted，表示删除。

        :return: The action_name of this RepositoryPushEventDto.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this RepositoryPushEventDto.

        **参数解释：** 操作名称。 - pushed to，表示推送。 - pushed new，表示推送并新建。 - deleted，表示删除。

        :param action_name: The action_name of this RepositoryPushEventDto.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def author(self):
        r"""Gets the author of this RepositoryPushEventDto.

        :return: The author of this RepositoryPushEventDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryEventAuthorDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this RepositoryPushEventDto.

        :param author: The author of this RepositoryPushEventDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.RepositoryEventAuthorDto`
        """
        self._author = author

    @property
    def author_id(self):
        r"""Gets the author_id of this RepositoryPushEventDto.

        **参数解释：** 触发者ID。

        :return: The author_id of this RepositoryPushEventDto.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this RepositoryPushEventDto.

        **参数解释：** 触发者ID。

        :param author_id: The author_id of this RepositoryPushEventDto.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def author_username(self):
        r"""Gets the author_username of this RepositoryPushEventDto.

        **参数解释：** 触发者名称。

        :return: The author_username of this RepositoryPushEventDto.
        :rtype: str
        """
        return self._author_username

    @author_username.setter
    def author_username(self, author_username):
        r"""Sets the author_username of this RepositoryPushEventDto.

        **参数解释：** 触发者名称。

        :param author_username: The author_username of this RepositoryPushEventDto.
        :type author_username: str
        """
        self._author_username = author_username

    @property
    def created_at(self):
        r"""Gets the created_at of this RepositoryPushEventDto.

        **参数解释：** 创建时间。

        :return: The created_at of this RepositoryPushEventDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RepositoryPushEventDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this RepositoryPushEventDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def repository_id(self):
        r"""Gets the repository_id of this RepositoryPushEventDto.

        **参数解释：** 仓库ID。

        :return: The repository_id of this RepositoryPushEventDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this RepositoryPushEventDto.

        **参数解释：** 仓库ID。

        :param repository_id: The repository_id of this RepositoryPushEventDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this RepositoryPushEventDto.

        **参数解释：** 仓库名。

        :return: The repository_name of this RepositoryPushEventDto.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this RepositoryPushEventDto.

        **参数解释：** 仓库名。

        :param repository_name: The repository_name of this RepositoryPushEventDto.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def push_data(self):
        r"""Gets the push_data of this RepositoryPushEventDto.

        :return: The push_data of this RepositoryPushEventDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.PushEventPayloadDto`
        """
        return self._push_data

    @push_data.setter
    def push_data(self, push_data):
        r"""Sets the push_data of this RepositoryPushEventDto.

        :param push_data: The push_data of this RepositoryPushEventDto.
        :type push_data: :class:`huaweicloudsdkcodehub.v4.PushEventPayloadDto`
        """
        self._push_data = push_data

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
        if not isinstance(other, RepositoryPushEventDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
