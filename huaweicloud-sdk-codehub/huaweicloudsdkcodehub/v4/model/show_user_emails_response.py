# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserEmailsResponse(SdkResponse):

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
        'name': 'str',
        'username': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'last_activity_on': 'str',
        'commit_email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'username': 'username',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'last_activity_on': 'last_activity_on',
        'commit_email': 'commit_email'
    }

    def __init__(self, id=None, name=None, username=None, state=None, created_at=None, updated_at=None, last_activity_on=None, commit_email=None):
        r"""ShowUserEmailsResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 用户id。
        :type id: int
        :param name: **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param username: **参数解释：** 用户长id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type username: str
        :param state: **参数解释：** 用户状态。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type state: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        :param last_activity_on: **参数解释：** 最后活跃时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type last_activity_on: str
        :param commit_email: **参数解释：** 提交邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type commit_email: str
        """
        
        super(ShowUserEmailsResponse, self).__init__()

        self._id = None
        self._name = None
        self._username = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._last_activity_on = None
        self._commit_email = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if last_activity_on is not None:
            self.last_activity_on = last_activity_on
        if commit_email is not None:
            self.commit_email = commit_email

    @property
    def id(self):
        r"""Gets the id of this ShowUserEmailsResponse.

        **参数解释：** 用户id。

        :return: The id of this ShowUserEmailsResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowUserEmailsResponse.

        **参数解释：** 用户id。

        :param id: The id of this ShowUserEmailsResponse.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowUserEmailsResponse.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowUserEmailsResponse.

        **参数解释：** 用户名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this ShowUserEmailsResponse.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this ShowUserEmailsResponse.

        **参数解释：** 用户长id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The username of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ShowUserEmailsResponse.

        **参数解释：** 用户长id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param username: The username of this ShowUserEmailsResponse.
        :type username: str
        """
        self._username = username

    @property
    def state(self):
        r"""Gets the state of this ShowUserEmailsResponse.

        **参数解释：** 用户状态。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The state of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowUserEmailsResponse.

        **参数解释：** 用户状态。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param state: The state of this ShowUserEmailsResponse.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowUserEmailsResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowUserEmailsResponse.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this ShowUserEmailsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowUserEmailsResponse.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowUserEmailsResponse.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this ShowUserEmailsResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def last_activity_on(self):
        r"""Gets the last_activity_on of this ShowUserEmailsResponse.

        **参数解释：** 最后活跃时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The last_activity_on of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._last_activity_on

    @last_activity_on.setter
    def last_activity_on(self, last_activity_on):
        r"""Sets the last_activity_on of this ShowUserEmailsResponse.

        **参数解释：** 最后活跃时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param last_activity_on: The last_activity_on of this ShowUserEmailsResponse.
        :type last_activity_on: str
        """
        self._last_activity_on = last_activity_on

    @property
    def commit_email(self):
        r"""Gets the commit_email of this ShowUserEmailsResponse.

        **参数解释：** 提交邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The commit_email of this ShowUserEmailsResponse.
        :rtype: str
        """
        return self._commit_email

    @commit_email.setter
    def commit_email(self, commit_email):
        r"""Sets the commit_email of this ShowUserEmailsResponse.

        **参数解释：** 提交邮箱。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param commit_email: The commit_email of this ShowUserEmailsResponse.
        :type commit_email: str
        """
        self._commit_email = commit_email

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
        if not isinstance(other, ShowUserEmailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
