# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitRepoV2:

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
        'created_at': 'str',
        'title': 'str',
        'parent_ids': 'list[str]',
        'message': 'str',
        'author_name': 'str',
        'committer_name': 'str',
        'committed_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'short_id': 'short_id',
        'created_at': 'created_at',
        'title': 'title',
        'parent_ids': 'parent_ids',
        'message': 'message',
        'author_name': 'author_name',
        'committer_name': 'committer_name',
        'committed_date': 'committed_date'
    }

    def __init__(self, id=None, short_id=None, created_at=None, title=None, parent_ids=None, message=None, author_name=None, committer_name=None, committed_date=None):
        """CommitRepoV2

        The model defined in huaweicloud sdk

        :param id: 提交对应的SHA id
        :type id: str
        :param short_id: 提交对应的短SHA id
        :type short_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param title: 提交标题
        :type title: str
        :param parent_ids: 父提交id
        :type parent_ids: list[str]
        :param message: 提交信息
        :type message: str
        :param author_name: 作者
        :type author_name: str
        :param committer_name: 提交作者
        :type committer_name: str
        :param committed_date: 提交时间
        :type committed_date: datetime
        """
        
        

        self._id = None
        self._short_id = None
        self._created_at = None
        self._title = None
        self._parent_ids = None
        self._message = None
        self._author_name = None
        self._committer_name = None
        self._committed_date = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if short_id is not None:
            self.short_id = short_id
        if created_at is not None:
            self.created_at = created_at
        if title is not None:
            self.title = title
        if parent_ids is not None:
            self.parent_ids = parent_ids
        if message is not None:
            self.message = message
        if author_name is not None:
            self.author_name = author_name
        if committer_name is not None:
            self.committer_name = committer_name
        if committed_date is not None:
            self.committed_date = committed_date

    @property
    def id(self):
        """Gets the id of this CommitRepoV2.

        提交对应的SHA id

        :return: The id of this CommitRepoV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CommitRepoV2.

        提交对应的SHA id

        :param id: The id of this CommitRepoV2.
        :type id: str
        """
        self._id = id

    @property
    def short_id(self):
        """Gets the short_id of this CommitRepoV2.

        提交对应的短SHA id

        :return: The short_id of this CommitRepoV2.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        """Sets the short_id of this CommitRepoV2.

        提交对应的短SHA id

        :param short_id: The short_id of this CommitRepoV2.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def created_at(self):
        """Gets the created_at of this CommitRepoV2.

        创建时间

        :return: The created_at of this CommitRepoV2.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CommitRepoV2.

        创建时间

        :param created_at: The created_at of this CommitRepoV2.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def title(self):
        """Gets the title of this CommitRepoV2.

        提交标题

        :return: The title of this CommitRepoV2.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CommitRepoV2.

        提交标题

        :param title: The title of this CommitRepoV2.
        :type title: str
        """
        self._title = title

    @property
    def parent_ids(self):
        """Gets the parent_ids of this CommitRepoV2.

        父提交id

        :return: The parent_ids of this CommitRepoV2.
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        """Sets the parent_ids of this CommitRepoV2.

        父提交id

        :param parent_ids: The parent_ids of this CommitRepoV2.
        :type parent_ids: list[str]
        """
        self._parent_ids = parent_ids

    @property
    def message(self):
        """Gets the message of this CommitRepoV2.

        提交信息

        :return: The message of this CommitRepoV2.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CommitRepoV2.

        提交信息

        :param message: The message of this CommitRepoV2.
        :type message: str
        """
        self._message = message

    @property
    def author_name(self):
        """Gets the author_name of this CommitRepoV2.

        作者

        :return: The author_name of this CommitRepoV2.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this CommitRepoV2.

        作者

        :param author_name: The author_name of this CommitRepoV2.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def committer_name(self):
        """Gets the committer_name of this CommitRepoV2.

        提交作者

        :return: The committer_name of this CommitRepoV2.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """Sets the committer_name of this CommitRepoV2.

        提交作者

        :param committer_name: The committer_name of this CommitRepoV2.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def committed_date(self):
        """Gets the committed_date of this CommitRepoV2.

        提交时间

        :return: The committed_date of this CommitRepoV2.
        :rtype: datetime
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        """Sets the committed_date of this CommitRepoV2.

        提交时间

        :param committed_date: The committed_date of this CommitRepoV2.
        :type committed_date: datetime
        """
        self._committed_date = committed_date

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
        if not isinstance(other, CommitRepoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
