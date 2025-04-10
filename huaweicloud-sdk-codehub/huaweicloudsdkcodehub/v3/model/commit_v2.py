# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'committed_date': 'str',
        'committer_name': 'str',
        'id': 'str',
        'message': 'str',
        'short_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'committed_date': 'committed_date',
        'committer_name': 'committer_name',
        'id': 'id',
        'message': 'message',
        'short_id': 'short_id',
        'title': 'title'
    }

    def __init__(self, committed_date=None, committer_name=None, id=None, message=None, short_id=None, title=None):
        r"""CommitV2

        The model defined in huaweicloud sdk

        :param committed_date: 提交时间
        :type committed_date: str
        :param committer_name: 提交者
        :type committer_name: str
        :param id: 提交id
        :type id: str
        :param message: 提交信息
        :type message: str
        :param short_id: 提交短id
        :type short_id: str
        :param title: 提交标题
        :type title: str
        """
        
        

        self._committed_date = None
        self._committer_name = None
        self._id = None
        self._message = None
        self._short_id = None
        self._title = None
        self.discriminator = None

        if committed_date is not None:
            self.committed_date = committed_date
        if committer_name is not None:
            self.committer_name = committer_name
        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if short_id is not None:
            self.short_id = short_id
        if title is not None:
            self.title = title

    @property
    def committed_date(self):
        r"""Gets the committed_date of this CommitV2.

        提交时间

        :return: The committed_date of this CommitV2.
        :rtype: str
        """
        return self._committed_date

    @committed_date.setter
    def committed_date(self, committed_date):
        r"""Sets the committed_date of this CommitV2.

        提交时间

        :param committed_date: The committed_date of this CommitV2.
        :type committed_date: str
        """
        self._committed_date = committed_date

    @property
    def committer_name(self):
        r"""Gets the committer_name of this CommitV2.

        提交者

        :return: The committer_name of this CommitV2.
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        r"""Sets the committer_name of this CommitV2.

        提交者

        :param committer_name: The committer_name of this CommitV2.
        :type committer_name: str
        """
        self._committer_name = committer_name

    @property
    def id(self):
        r"""Gets the id of this CommitV2.

        提交id

        :return: The id of this CommitV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommitV2.

        提交id

        :param id: The id of this CommitV2.
        :type id: str
        """
        self._id = id

    @property
    def message(self):
        r"""Gets the message of this CommitV2.

        提交信息

        :return: The message of this CommitV2.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CommitV2.

        提交信息

        :param message: The message of this CommitV2.
        :type message: str
        """
        self._message = message

    @property
    def short_id(self):
        r"""Gets the short_id of this CommitV2.

        提交短id

        :return: The short_id of this CommitV2.
        :rtype: str
        """
        return self._short_id

    @short_id.setter
    def short_id(self, short_id):
        r"""Sets the short_id of this CommitV2.

        提交短id

        :param short_id: The short_id of this CommitV2.
        :type short_id: str
        """
        self._short_id = short_id

    @property
    def title(self):
        r"""Gets the title of this CommitV2.

        提交标题

        :return: The title of this CommitV2.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CommitV2.

        提交标题

        :param title: The title of this CommitV2.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, CommitV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
