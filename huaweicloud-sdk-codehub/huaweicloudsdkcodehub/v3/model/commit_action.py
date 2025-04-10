# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitAction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'file_path': 'str',
        'previous_path': 'str',
        'content': 'str',
        'encoding': 'str',
        'last_commit_id': 'str',
        'execute_filemode': 'bool'
    }

    attribute_map = {
        'action': 'action',
        'file_path': 'file_path',
        'previous_path': 'previous_path',
        'content': 'content',
        'encoding': 'encoding',
        'last_commit_id': 'last_commit_id',
        'execute_filemode': 'execute_filemode'
    }

    def __init__(self, action=None, file_path=None, previous_path=None, content=None, encoding=None, last_commit_id=None, execute_filemode=None):
        r"""CommitAction

        The model defined in huaweicloud sdk

        :param action: 要执行的操作：create、delete、move、update、chmod
        :type action: str
        :param file_path: 文件的完整路径。例如lib/class.rb
        :type file_path: str
        :param previous_path: 要移动的文件的原始完整路径。例如lib/class1.rb。仅在move操作时生效
        :type previous_path: str
        :param content: 文件内容，create和update操作时必须。未指定内容的移动操作将保留现有文件内容，内容的任何其他值将覆盖文件内容。
        :type content: str
        :param encoding: 文件编码：text、base64。默认为text
        :type encoding: str
        :param last_commit_id: 最后一个已知的提交ID。仅在update、move、delete操作时生效
        :type last_commit_id: str
        :param execute_filemode: 启用或者禁用文件的执行模式。仅在chmod操作时生效
        :type execute_filemode: bool
        """
        
        

        self._action = None
        self._file_path = None
        self._previous_path = None
        self._content = None
        self._encoding = None
        self._last_commit_id = None
        self._execute_filemode = None
        self.discriminator = None

        self.action = action
        self.file_path = file_path
        if previous_path is not None:
            self.previous_path = previous_path
        if content is not None:
            self.content = content
        if encoding is not None:
            self.encoding = encoding
        if last_commit_id is not None:
            self.last_commit_id = last_commit_id
        if execute_filemode is not None:
            self.execute_filemode = execute_filemode

    @property
    def action(self):
        r"""Gets the action of this CommitAction.

        要执行的操作：create、delete、move、update、chmod

        :return: The action of this CommitAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CommitAction.

        要执行的操作：create、delete、move、update、chmod

        :param action: The action of this CommitAction.
        :type action: str
        """
        self._action = action

    @property
    def file_path(self):
        r"""Gets the file_path of this CommitAction.

        文件的完整路径。例如lib/class.rb

        :return: The file_path of this CommitAction.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CommitAction.

        文件的完整路径。例如lib/class.rb

        :param file_path: The file_path of this CommitAction.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def previous_path(self):
        r"""Gets the previous_path of this CommitAction.

        要移动的文件的原始完整路径。例如lib/class1.rb。仅在move操作时生效

        :return: The previous_path of this CommitAction.
        :rtype: str
        """
        return self._previous_path

    @previous_path.setter
    def previous_path(self, previous_path):
        r"""Sets the previous_path of this CommitAction.

        要移动的文件的原始完整路径。例如lib/class1.rb。仅在move操作时生效

        :param previous_path: The previous_path of this CommitAction.
        :type previous_path: str
        """
        self._previous_path = previous_path

    @property
    def content(self):
        r"""Gets the content of this CommitAction.

        文件内容，create和update操作时必须。未指定内容的移动操作将保留现有文件内容，内容的任何其他值将覆盖文件内容。

        :return: The content of this CommitAction.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CommitAction.

        文件内容，create和update操作时必须。未指定内容的移动操作将保留现有文件内容，内容的任何其他值将覆盖文件内容。

        :param content: The content of this CommitAction.
        :type content: str
        """
        self._content = content

    @property
    def encoding(self):
        r"""Gets the encoding of this CommitAction.

        文件编码：text、base64。默认为text

        :return: The encoding of this CommitAction.
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        r"""Sets the encoding of this CommitAction.

        文件编码：text、base64。默认为text

        :param encoding: The encoding of this CommitAction.
        :type encoding: str
        """
        self._encoding = encoding

    @property
    def last_commit_id(self):
        r"""Gets the last_commit_id of this CommitAction.

        最后一个已知的提交ID。仅在update、move、delete操作时生效

        :return: The last_commit_id of this CommitAction.
        :rtype: str
        """
        return self._last_commit_id

    @last_commit_id.setter
    def last_commit_id(self, last_commit_id):
        r"""Sets the last_commit_id of this CommitAction.

        最后一个已知的提交ID。仅在update、move、delete操作时生效

        :param last_commit_id: The last_commit_id of this CommitAction.
        :type last_commit_id: str
        """
        self._last_commit_id = last_commit_id

    @property
    def execute_filemode(self):
        r"""Gets the execute_filemode of this CommitAction.

        启用或者禁用文件的执行模式。仅在chmod操作时生效

        :return: The execute_filemode of this CommitAction.
        :rtype: bool
        """
        return self._execute_filemode

    @execute_filemode.setter
    def execute_filemode(self, execute_filemode):
        r"""Sets the execute_filemode of this CommitAction.

        启用或者禁用文件的执行模式。仅在chmod操作时生效

        :param execute_filemode: The execute_filemode of this CommitAction.
        :type execute_filemode: bool
        """
        self._execute_filemode = execute_filemode

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
        if not isinstance(other, CommitAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
