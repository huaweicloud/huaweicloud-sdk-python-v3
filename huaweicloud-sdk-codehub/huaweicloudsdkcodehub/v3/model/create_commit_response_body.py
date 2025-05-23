# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommitResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'short_id': 'str',
        'title': 'str',
        'author_name': 'str',
        'author_email': 'str',
        'committer_name': 'str',
        'committer_email': 'str',
        'created_at': 'str',
        'message': 'str',
        'parent_ids': 'list[str]',
        'committed_date': 'datetime',
        'authored_date': 'datetime',
        'stats': 'CreateCommitResponseBodyStats'
    }

    attribute_map = {
        'id': 'id',
        'short_id': 'short_id',
        'title': 'title',
        'author_name': 'author_name',
        'author_email': 'author_email',
        'committer_name': 'committer_name',
        'committer_email': 'committer_email',
        'created_at': 'created_at',
        'message': 'message',
        'parent_ids': 'parent_ids',
        'committed_date': 'committed_date',
        'authored_date': 'authored_date',
        'stats': 'stats'
    }

    def __init__(self, id=None, short_id=None, title=None, author_name=None, author_email=None, committer_name=None, committer_email=None, created_at=None, message=None, parent_ids=None, committed_date=None, authored_date=None, stats=None):
        r"""CreateCommitResponseBody

        The model defined in huaweicloud sdk

        :param id: 提交对应的SHA id
        :type id: str
        :param short_id: 提交对应的短SHA id
        :type short_id: str
        :param title: 提交标题
        :type title: str
        :param author_name: 作者
        :type author_name: str
        :param author_email: 作者邮箱
        :type author_email: str
        :param committer_name: 提交作者
        :type committer_name: str
        :param committer_email: 提交作者邮箱
        :type committer_email: str
        :param created_at: 创建时间
        :type created_at: str
        :param message: 提交信息
        :type message: str
        :param parent_ids: 父提交id
        :type parent_ids: list[str]
        :param committed_date: 提交时间
        :type committed_date: datetime
        :param authored_date: 作者提交时间
        :type authored_date: datetime
        :param stats: 
        :type stats: :class:`huaweicloudsdkcodehub.v3.CreateCommitResponseBodyStats`
        """
        
        

        self._id = None
        self._short_id = None
        self._title = None
        self._author_name = None
        self._author_email = None
        self._committer_name = None
        self._committer_email = None
        self._created_at = None
        self._message = None
        self._parent_ids = None
        self._committed_date = None
        self._authored_date = None
        self._stats = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if short_id is not None:
            self.short_id = short_id
        if title is not None:
            self.title = title
        if author_name is not None:
            self.author_name = author_name
        if author_email is not None:
            self.author_email = author_email
        if committer_name is not None:
            self.committer_name = committer_name
        if committer_email is not None:
            self.committer_email = committer_email
        if created_at is not None:
            self.created_at = created_at
        if message is not None:
            self.message = message
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if committed_date is not None:
            self.committed_date = committed_date
        if authored_date is not None:
            self.authored_date = authored_date
        if stats is not None:
            self.stats = stats

    @property
    def id(self):
        r"""Gets the id of this CreateCommitResponseBody.

        提交对应的SHA id

        :return: The id of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateCommitResponseBody.

        提交对应的SHA id

        :param id: The id of this CreateCommitResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def short_id(self):
        r"""Gets the short_id of this CreateCommitResponseBody.

        提交对应的短SHA id

        :return: The short_id of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        r"""Sets the short_id of this CreateCommitResponseBody.

        提交对应的短SHA id

        :param short_id: The short_id of this CreateCommitResponseBody.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def title(self):
        r"""Gets the title of this CreateCommitResponseBody.

        提交标题

        :return: The title of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateCommitResponseBody.

        提交标题

        :param title: The title of this CreateCommitResponseBody.
        :type title: str
        """
        self._title = title

    @property
    def author_name(self):
        r"""Gets the author_name of this CreateCommitResponseBody.

        作者

        :return: The author_name of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        r"""Sets the author_name of this CreateCommitResponseBody.

        作者

        :param author_name: The author_name of this CreateCommitResponseBody.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def author_email(self):
        r"""Gets the author_email of this CreateCommitResponseBody.

        作者邮箱

        :return: The author_email of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        r"""Sets the author_email of this CreateCommitResponseBody.

        作者邮箱

        :param author_email: The author_email of this CreateCommitResponseBody.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def committer_name(self):
        r"""Gets the committer_name of this CreateCommitResponseBody.

        提交作者

        :return: The committer_name of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        r"""Sets the committer_name of this CreateCommitResponseBody.

        提交作者

        :param committer_name: The committer_name of this CreateCommitResponseBody.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def committer_email(self):
        r"""Gets the committer_email of this CreateCommitResponseBody.

        提交作者邮箱

        :return: The committer_email of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        r"""Sets the committer_email of this CreateCommitResponseBody.

        提交作者邮箱

        :param committer_email: The committer_email of this CreateCommitResponseBody.
        :type committer_email: str
        """
        self._committer_email = committer_email

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateCommitResponseBody.

        创建时间

        :return: The created_at of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateCommitResponseBody.

        创建时间

        :param created_at: The created_at of this CreateCommitResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def message(self):
        r"""Gets the message of this CreateCommitResponseBody.

        提交信息

        :return: The message of this CreateCommitResponseBody.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateCommitResponseBody.

        提交信息

        :param message: The message of this CreateCommitResponseBody.
        :type message: str
        """
        self._message = message

    @property
    def parent_ids(self):
        r"""Gets the parent_ids of this CreateCommitResponseBody.

        父提交id

        :return: The parent_ids of this CreateCommitResponseBody.
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        r"""Sets the parent_ids of this CreateCommitResponseBody.

        父提交id

        :param parent_ids: The parent_ids of this CreateCommitResponseBody.
        :type parent_ids: list[str]
        """
        self._parent_ids = parent_ids

    @property
    def committed_date(self):
        r"""Gets the committed_date of this CreateCommitResponseBody.

        提交时间

        :return: The committed_date of this CreateCommitResponseBody.
        :rtype: datetime
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        r"""Sets the committed_date of this CreateCommitResponseBody.

        提交时间

        :param committed_date: The committed_date of this CreateCommitResponseBody.
        :type committed_date: datetime
        """
        self._committed_date = committed_date

    @property
    def authored_date(self):
        r"""Gets the authored_date of this CreateCommitResponseBody.

        作者提交时间

        :return: The authored_date of this CreateCommitResponseBody.
        :rtype: datetime
        """
        return self._authored_date

    @authored_date.setter
    def authored_date(self, authored_date):
        r"""Sets the authored_date of this CreateCommitResponseBody.

        作者提交时间

        :param authored_date: The authored_date of this CreateCommitResponseBody.
        :type authored_date: datetime
        """
        self._authored_date = authored_date

    @property
    def stats(self):
        r"""Gets the stats of this CreateCommitResponseBody.

        :return: The stats of this CreateCommitResponseBody.
        :rtype: :class:`huaweicloudsdkcodehub.v3.CreateCommitResponseBodyStats`
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        r"""Sets the stats of this CreateCommitResponseBody.

        :param stats: The stats of this CreateCommitResponseBody.
        :type stats: :class:`huaweicloudsdkcodehub.v3.CreateCommitResponseBodyStats`
        """
        self._stats = stats

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
        if not isinstance(other, CreateCommitResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
