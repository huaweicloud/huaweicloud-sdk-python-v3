# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestVotesDto:

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
        'score': 'int',
        'author_name': 'str',
        'author_username': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'last_committed_id': 'str',
        'author_id': 'int',
        'avatar_url': 'str',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'score': 'score',
        'author_name': 'author_name',
        'author_username': 'author_username',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'last_committed_id': 'last_committed_id',
        'author_id': 'author_id',
        'avatar_url': 'avatar_url',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, id=None, score=None, author_name=None, author_username=None, created_at=None, updated_at=None, last_committed_id=None, author_id=None, avatar_url=None, nick_name=None, tenant_name=None):
        r"""MergeRequestVotesDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 打分记录的id。
        :type id: int
        :param score: **参数解释：** 分数。
        :type score: int
        :param author_name: **参数解释：** 作者名。
        :type author_name: str
        :param author_username: **参数解释：** 作者用户名。
        :type author_username: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param last_committed_id: **参数解释：** 最后一次提交记录的id。
        :type last_committed_id: str
        :param author_id: **参数解释：** 作者id。
        :type author_id: int
        :param avatar_url: **参数解释：** 作者头像url。
        :type avatar_url: str
        :param nick_name: **参数解释：** 作者昵称。
        :type nick_name: str
        :param tenant_name: **参数解释：** 作者租户名称。
        :type tenant_name: str
        """
        
        

        self._id = None
        self._score = None
        self._author_name = None
        self._author_username = None
        self._created_at = None
        self._updated_at = None
        self._last_committed_id = None
        self._author_id = None
        self._avatar_url = None
        self._nick_name = None
        self._tenant_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if score is not None:
            self.score = score
        if author_name is not None:
            self.author_name = author_name
        if author_username is not None:
            self.author_username = author_username
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if last_committed_id is not None:
            self.last_committed_id = last_committed_id
        if author_id is not None:
            self.author_id = author_id
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def id(self):
        r"""Gets the id of this MergeRequestVotesDto.

        **参数解释：** 打分记录的id。

        :return: The id of this MergeRequestVotesDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestVotesDto.

        **参数解释：** 打分记录的id。

        :param id: The id of this MergeRequestVotesDto.
        :type id: int
        """
        self._id = id

    @property
    def score(self):
        r"""Gets the score of this MergeRequestVotesDto.

        **参数解释：** 分数。

        :return: The score of this MergeRequestVotesDto.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this MergeRequestVotesDto.

        **参数解释：** 分数。

        :param score: The score of this MergeRequestVotesDto.
        :type score: int
        """
        self._score = score

    @property
    def author_name(self):
        r"""Gets the author_name of this MergeRequestVotesDto.

        **参数解释：** 作者名。

        :return: The author_name of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this MergeRequestVotesDto.

        **参数解释：** 作者名。

        :param author_name: The author_name of this MergeRequestVotesDto.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def author_username(self):
        r"""Gets the author_username of this MergeRequestVotesDto.

        **参数解释：** 作者用户名。

        :return: The author_username of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._author_username

    @author_username.setter
    def author_username(self, author_username):
        r"""Sets the author_username of this MergeRequestVotesDto.

        **参数解释：** 作者用户名。

        :param author_username: The author_username of this MergeRequestVotesDto.
        :type author_username: str
        """
        self._author_username = author_username

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestVotesDto.

        **参数解释：** 创建时间。

        :return: The created_at of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestVotesDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this MergeRequestVotesDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MergeRequestVotesDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MergeRequestVotesDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this MergeRequestVotesDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def last_committed_id(self):
        r"""Gets the last_committed_id of this MergeRequestVotesDto.

        **参数解释：** 最后一次提交记录的id。

        :return: The last_committed_id of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._last_committed_id

    @last_committed_id.setter
    def last_committed_id(self, last_committed_id):
        r"""Sets the last_committed_id of this MergeRequestVotesDto.

        **参数解释：** 最后一次提交记录的id。

        :param last_committed_id: The last_committed_id of this MergeRequestVotesDto.
        :type last_committed_id: str
        """
        self._last_committed_id = last_committed_id

    @property
    def author_id(self):
        r"""Gets the author_id of this MergeRequestVotesDto.

        **参数解释：** 作者id。

        :return: The author_id of this MergeRequestVotesDto.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this MergeRequestVotesDto.

        **参数解释：** 作者id。

        :param author_id: The author_id of this MergeRequestVotesDto.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this MergeRequestVotesDto.

        **参数解释：** 作者头像url。

        :return: The avatar_url of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this MergeRequestVotesDto.

        **参数解释：** 作者头像url。

        :param avatar_url: The avatar_url of this MergeRequestVotesDto.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def nick_name(self):
        r"""Gets the nick_name of this MergeRequestVotesDto.

        **参数解释：** 作者昵称。

        :return: The nick_name of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this MergeRequestVotesDto.

        **参数解释：** 作者昵称。

        :param nick_name: The nick_name of this MergeRequestVotesDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this MergeRequestVotesDto.

        **参数解释：** 作者租户名称。

        :return: The tenant_name of this MergeRequestVotesDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this MergeRequestVotesDto.

        **参数解释：** 作者租户名称。

        :param tenant_name: The tenant_name of this MergeRequestVotesDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, MergeRequestVotesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
