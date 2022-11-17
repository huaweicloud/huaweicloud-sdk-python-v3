# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Commit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author_email': 'str',
        'author_name': 'str',
        'authored_date': 'datetime',
        'committed_date': 'datetime',
        'committer_email': 'str',
        'committer_name': 'str',
        'format': 'object',
        'id': 'str',
        'message': 'str',
        'parent_ids': 'list[str]'
    }

    attribute_map = {
        'author_email': 'author_email',
        'author_name': 'author_name',
        'authored_date': 'authored_date',
        'committed_date': 'committed_date',
        'committer_email': 'committer_email',
        'committer_name': 'committer_name',
        'format': 'format',
        'id': 'id',
        'message': 'message',
        'parent_ids': 'parent_ids'
    }

    def __init__(self, author_email=None, author_name=None, authored_date=None, committed_date=None, committer_email=None, committer_name=None, format=None, id=None, message=None, parent_ids=None):
        """Commit

        The model defined in huaweicloud sdk

        :param author_email: 作者邮箱
        :type author_email: str
        :param author_name: 作者
        :type author_name: str
        :param authored_date: 作者提交时间
        :type authored_date: datetime
        :param committed_date: 提交时间
        :type committed_date: datetime
        :param committer_email: 提交作者邮箱
        :type committer_email: str
        :param committer_name: 提交作者
        :type committer_name: str
        :param format: 文件变更的详情信息，其格式由请求查询参数 stat_format 决定
        :type format: object
        :param id: 提交对应的SHA id
        :type id: str
        :param message: 提交的信息
        :type message: str
        :param parent_ids: 父提交id
        :type parent_ids: list[str]
        """
        
        

        self._author_email = None
        self._author_name = None
        self._authored_date = None
        self._committed_date = None
        self._committer_email = None
        self._committer_name = None
        self._format = None
        self._id = None
        self._message = None
        self._parent_ids = None
        self.discriminator = None

        if author_email is not None:
            self.author_email = author_email
        if author_name is not None:
            self.author_name = author_name
        if authored_date is not None:
            self.authored_date = authored_date
        if committed_date is not None:
            self.committed_date = committed_date
        if committer_email is not None:
            self.committer_email = committer_email
        if committer_name is not None:
            self.committer_name = committer_name
        if format is not None:
            self.format = format
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if parent_ids is not None:
            self.parent_ids = parent_ids

    @property
    def author_email(self):
        """Gets the author_email of this Commit.

        作者邮箱

        :return: The author_email of this Commit.
        :rtype: str
        """
        return self._author_email

    @author_email.setter
    def author_email(self, author_email):
        """Sets the author_email of this Commit.

        作者邮箱

        :param author_email: The author_email of this Commit.
        :type author_email: str
        """
        self._author_email = author_email

    @property
    def author_name(self):
        """Gets the author_name of this Commit.

        作者

        :return: The author_name of this Commit.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this Commit.

        作者

        :param author_name: The author_name of this Commit.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def authored_date(self):
        """Gets the authored_date of this Commit.

        作者提交时间

        :return: The authored_date of this Commit.
        :rtype: datetime
        """
        return self._authored_date

    @authored_date.setter
    def authored_date(self, authored_date):
        """Sets the authored_date of this Commit.

        作者提交时间

        :param authored_date: The authored_date of this Commit.
        :type authored_date: datetime
        """
        self._authored_date = authored_date

    @property
    def committed_date(self):
        """Gets the committed_date of this Commit.

        提交时间

        :return: The committed_date of this Commit.
        :rtype: datetime
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        """Sets the committed_date of this Commit.

        提交时间

        :param committed_date: The committed_date of this Commit.
        :type committed_date: datetime
        """
        self._committed_date = committed_date

    @property
    def committer_email(self):
        """Gets the committer_email of this Commit.

        提交作者邮箱

        :return: The committer_email of this Commit.
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """Sets the committer_email of this Commit.

        提交作者邮箱

        :param committer_email: The committer_email of this Commit.
        :type committer_email: str
        """
        self._committer_email = committer_email

    @property
    def committer_name(self):
        """Gets the committer_name of this Commit.

        提交作者

        :return: The committer_name of this Commit.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """Sets the committer_name of this Commit.

        提交作者

        :param committer_name: The committer_name of this Commit.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def format(self):
        """Gets the format of this Commit.

        文件变更的详情信息，其格式由请求查询参数 stat_format 决定

        :return: The format of this Commit.
        :rtype: object
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Commit.

        文件变更的详情信息，其格式由请求查询参数 stat_format 决定

        :param format: The format of this Commit.
        :type format: object
        """
        self._format = format

    @property
    def id(self):
        """Gets the id of this Commit.

        提交对应的SHA id

        :return: The id of this Commit.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Commit.

        提交对应的SHA id

        :param id: The id of this Commit.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        """Gets the message of this Commit.

        提交的信息

        :return: The message of this Commit.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Commit.

        提交的信息

        :param message: The message of this Commit.
        :type message: str
        """
        self._message = message

    @property
    def parent_ids(self):
        """Gets the parent_ids of this Commit.

        父提交id

        :return: The parent_ids of this Commit.
        :rtype: list[str]
        """
        return self._parent_ids

    @parent_ids.setter
    def parent_ids(self, parent_ids):
        """Sets the parent_ids of this Commit.

        父提交id

        :param parent_ids: The parent_ids of this Commit.
        :type parent_ids: list[str]
        """
        self._parent_ids = parent_ids

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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
