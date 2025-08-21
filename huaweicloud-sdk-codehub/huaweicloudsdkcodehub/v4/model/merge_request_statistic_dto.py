# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestStatisticDto:

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
        'iid': 'int',
        'title': 'str',
        'state': 'str',
        'commits_count': 'int',
        'changed_files_count': 'str',
        'notes_count': 'NotesCountDto',
        'changed_lines_count': 'MergeRequestLineChange',
        'merge_error': 'str',
        'json_merge_error': 'object',
        'votes': 'int'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'title': 'title',
        'state': 'state',
        'commits_count': 'commits_count',
        'changed_files_count': 'changed_files_count',
        'notes_count': 'notes_count',
        'changed_lines_count': 'changed_lines_count',
        'merge_error': 'merge_error',
        'json_merge_error': 'json_merge_error',
        'votes': 'votes'
    }

    def __init__(self, id=None, iid=None, title=None, state=None, commits_count=None, changed_files_count=None, notes_count=None, changed_lines_count=None, merge_error=None, json_merge_error=None, votes=None):
        r"""MergeRequestStatisticDto

        The model defined in huaweicloud sdk

        :param id: 合并请求ID
        :type id: int
        :param iid: 合并请求序号
        :type iid: int
        :param title: 合并请求标题
        :type title: str
        :param state: 合并请求状态
        :type state: str
        :param commits_count: 合并请求提交数
        :type commits_count: int
        :param changed_files_count: 合并请求文件变数
        :type changed_files_count: str
        :param notes_count: 
        :type notes_count: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        :param changed_lines_count: 
        :type changed_lines_count: :class:`huaweicloudsdkcodehub.v4.MergeRequestLineChange`
        :param merge_error: 合并请求合入异常信息
        :type merge_error: str
        :param json_merge_error: 合并请求合入异常信息
        :type json_merge_error: object
        :param votes: 合并请求评分数
        :type votes: int
        """
        
        

        self._id = None
        self._iid = None
        self._title = None
        self._state = None
        self._commits_count = None
        self._changed_files_count = None
        self._notes_count = None
        self._changed_lines_count = None
        self._merge_error = None
        self._json_merge_error = None
        self._votes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if title is not None:
            self.title = title
        if state is not None:
            self.state = state
        if commits_count is not None:
            self.commits_count = commits_count
        if changed_files_count is not None:
            self.changed_files_count = changed_files_count
        if notes_count is not None:
            self.notes_count = notes_count
        if changed_lines_count is not None:
            self.changed_lines_count = changed_lines_count
        if merge_error is not None:
            self.merge_error = merge_error
        if json_merge_error is not None:
            self.json_merge_error = json_merge_error
        if votes is not None:
            self.votes = votes

    @property
    def id(self):
        r"""Gets the id of this MergeRequestStatisticDto.

        合并请求ID

        :return: The id of this MergeRequestStatisticDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestStatisticDto.

        合并请求ID

        :param id: The id of this MergeRequestStatisticDto.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this MergeRequestStatisticDto.

        合并请求序号

        :return: The iid of this MergeRequestStatisticDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this MergeRequestStatisticDto.

        合并请求序号

        :param iid: The iid of this MergeRequestStatisticDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def title(self):
        r"""Gets the title of this MergeRequestStatisticDto.

        合并请求标题

        :return: The title of this MergeRequestStatisticDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this MergeRequestStatisticDto.

        合并请求标题

        :param title: The title of this MergeRequestStatisticDto.
        :type title: str
        """
        self._title = title

    @property
    def state(self):
        r"""Gets the state of this MergeRequestStatisticDto.

        合并请求状态

        :return: The state of this MergeRequestStatisticDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MergeRequestStatisticDto.

        合并请求状态

        :param state: The state of this MergeRequestStatisticDto.
        :type state: str
        """
        self._state = state

    @property
    def commits_count(self):
        r"""Gets the commits_count of this MergeRequestStatisticDto.

        合并请求提交数

        :return: The commits_count of this MergeRequestStatisticDto.
        :rtype: int
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        r"""Sets the commits_count of this MergeRequestStatisticDto.

        合并请求提交数

        :param commits_count: The commits_count of this MergeRequestStatisticDto.
        :type commits_count: int
        """
        self._commits_count = commits_count

    @property
    def changed_files_count(self):
        r"""Gets the changed_files_count of this MergeRequestStatisticDto.

        合并请求文件变数

        :return: The changed_files_count of this MergeRequestStatisticDto.
        :rtype: str
        """
        return self._changed_files_count

    @changed_files_count.setter
    def changed_files_count(self, changed_files_count):
        r"""Sets the changed_files_count of this MergeRequestStatisticDto.

        合并请求文件变数

        :param changed_files_count: The changed_files_count of this MergeRequestStatisticDto.
        :type changed_files_count: str
        """
        self._changed_files_count = changed_files_count

    @property
    def notes_count(self):
        r"""Gets the notes_count of this MergeRequestStatisticDto.

        :return: The notes_count of this MergeRequestStatisticDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        """
        return self._notes_count

    @notes_count.setter
    def notes_count(self, notes_count):
        r"""Sets the notes_count of this MergeRequestStatisticDto.

        :param notes_count: The notes_count of this MergeRequestStatisticDto.
        :type notes_count: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        """
        self._notes_count = notes_count

    @property
    def changed_lines_count(self):
        r"""Gets the changed_lines_count of this MergeRequestStatisticDto.

        :return: The changed_lines_count of this MergeRequestStatisticDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MergeRequestLineChange`
        """
        return self._changed_lines_count

    @changed_lines_count.setter
    def changed_lines_count(self, changed_lines_count):
        r"""Sets the changed_lines_count of this MergeRequestStatisticDto.

        :param changed_lines_count: The changed_lines_count of this MergeRequestStatisticDto.
        :type changed_lines_count: :class:`huaweicloudsdkcodehub.v4.MergeRequestLineChange`
        """
        self._changed_lines_count = changed_lines_count

    @property
    def merge_error(self):
        r"""Gets the merge_error of this MergeRequestStatisticDto.

        合并请求合入异常信息

        :return: The merge_error of this MergeRequestStatisticDto.
        :rtype: str
        """
        return self._merge_error

    @merge_error.setter
    def merge_error(self, merge_error):
        r"""Sets the merge_error of this MergeRequestStatisticDto.

        合并请求合入异常信息

        :param merge_error: The merge_error of this MergeRequestStatisticDto.
        :type merge_error: str
        """
        self._merge_error = merge_error

    @property
    def json_merge_error(self):
        r"""Gets the json_merge_error of this MergeRequestStatisticDto.

        合并请求合入异常信息

        :return: The json_merge_error of this MergeRequestStatisticDto.
        :rtype: object
        """
        return self._json_merge_error

    @json_merge_error.setter
    def json_merge_error(self, json_merge_error):
        r"""Sets the json_merge_error of this MergeRequestStatisticDto.

        合并请求合入异常信息

        :param json_merge_error: The json_merge_error of this MergeRequestStatisticDto.
        :type json_merge_error: object
        """
        self._json_merge_error = json_merge_error

    @property
    def votes(self):
        r"""Gets the votes of this MergeRequestStatisticDto.

        合并请求评分数

        :return: The votes of this MergeRequestStatisticDto.
        :rtype: int
        """
        return self._votes

    @votes.setter
    def votes(self, votes):
        r"""Sets the votes of this MergeRequestStatisticDto.

        合并请求评分数

        :param votes: The votes of this MergeRequestStatisticDto.
        :type votes: int
        """
        self._votes = votes

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
        if not isinstance(other, MergeRequestStatisticDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
