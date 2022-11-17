# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefectEvents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[DefectEvents]',
        'description': 'str',
        'fix_suggestions': 'list[str]',
        'line': 'int',
        'end_line': 'int',
        'code_context_start_line': 'int',
        'main': 'bool',
        'path': 'str',
        'tag': 'str',
        'main_buggy_code': 'str',
        'code_context': 'str'
    }

    attribute_map = {
        'events': 'events',
        'description': 'description',
        'fix_suggestions': 'fix_suggestions',
        'line': 'line',
        'end_line': 'end_line',
        'code_context_start_line': 'code_context_start_line',
        'main': 'main',
        'path': 'path',
        'tag': 'tag',
        'main_buggy_code': 'main_buggy_code',
        'code_context': 'code_context'
    }

    def __init__(self, events=None, description=None, fix_suggestions=None, line=None, end_line=None, code_context_start_line=None, main=None, path=None, tag=None, main_buggy_code=None, code_context=None):
        """DefectEvents

        The model defined in huaweicloud sdk

        :param events: 调用链信息
        :type events: list[:class:`huaweicloudsdkcodecheck.v2.DefectEvents`]
        :param description: 描述
        :type description: str
        :param fix_suggestions: fix suggestions
        :type fix_suggestions: list[str]
        :param line: 缺陷所在行
        :type line: int
        :param end_line: 缺陷结束行
        :type end_line: int
        :param code_context_start_line: 缺陷开始行
        :type code_context_start_line: int
        :param main: 代码片段
        :type main: bool
        :param path: file path
        :type path: str
        :param tag: 标签
        :type tag: str
        :param main_buggy_code: main buggy code
        :type main_buggy_code: str
        :param code_context: code context
        :type code_context: str
        """
        
        

        self._events = None
        self._description = None
        self._fix_suggestions = None
        self._line = None
        self._end_line = None
        self._code_context_start_line = None
        self._main = None
        self._path = None
        self._tag = None
        self._main_buggy_code = None
        self._code_context = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if description is not None:
            self.description = description
        if fix_suggestions is not None:
            self.fix_suggestions = fix_suggestions
        if line is not None:
            self.line = line
        if end_line is not None:
            self.end_line = end_line
        if code_context_start_line is not None:
            self.code_context_start_line = code_context_start_line
        if main is not None:
            self.main = main
        if path is not None:
            self.path = path
        if tag is not None:
            self.tag = tag
        if main_buggy_code is not None:
            self.main_buggy_code = main_buggy_code
        if code_context is not None:
            self.code_context = code_context

    @property
    def events(self):
        """Gets the events of this DefectEvents.

        调用链信息

        :return: The events of this DefectEvents.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.DefectEvents`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this DefectEvents.

        调用链信息

        :param events: The events of this DefectEvents.
        :type events: list[:class:`huaweicloudsdkcodecheck.v2.DefectEvents`]
        """
        self._events = events

    @property
    def description(self):
        """Gets the description of this DefectEvents.

        描述

        :return: The description of this DefectEvents.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DefectEvents.

        描述

        :param description: The description of this DefectEvents.
        :type description: str
        """
        self._description = description

    @property
    def fix_suggestions(self):
        """Gets the fix_suggestions of this DefectEvents.

        fix suggestions

        :return: The fix_suggestions of this DefectEvents.
        :rtype: list[str]
        """
        return self._fix_suggestions

    @fix_suggestions.setter
    def fix_suggestions(self, fix_suggestions):
        """Sets the fix_suggestions of this DefectEvents.

        fix suggestions

        :param fix_suggestions: The fix_suggestions of this DefectEvents.
        :type fix_suggestions: list[str]
        """
        self._fix_suggestions = fix_suggestions

    @property
    def line(self):
        """Gets the line of this DefectEvents.

        缺陷所在行

        :return: The line of this DefectEvents.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this DefectEvents.

        缺陷所在行

        :param line: The line of this DefectEvents.
        :type line: int
        """
        self._line = line

    @property
    def end_line(self):
        """Gets the end_line of this DefectEvents.

        缺陷结束行

        :return: The end_line of this DefectEvents.
        :rtype: int
        """
        return self._end_line

    @end_line.setter
    def end_line(self, end_line):
        """Sets the end_line of this DefectEvents.

        缺陷结束行

        :param end_line: The end_line of this DefectEvents.
        :type end_line: int
        """
        self._end_line = end_line

    @property
    def code_context_start_line(self):
        """Gets the code_context_start_line of this DefectEvents.

        缺陷开始行

        :return: The code_context_start_line of this DefectEvents.
        :rtype: int
        """
        return self._code_context_start_line

    @code_context_start_line.setter
    def code_context_start_line(self, code_context_start_line):
        """Sets the code_context_start_line of this DefectEvents.

        缺陷开始行

        :param code_context_start_line: The code_context_start_line of this DefectEvents.
        :type code_context_start_line: int
        """
        self._code_context_start_line = code_context_start_line

    @property
    def main(self):
        """Gets the main of this DefectEvents.

        代码片段

        :return: The main of this DefectEvents.
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this DefectEvents.

        代码片段

        :param main: The main of this DefectEvents.
        :type main: bool
        """
        self._main = main

    @property
    def path(self):
        """Gets the path of this DefectEvents.

        file path

        :return: The path of this DefectEvents.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DefectEvents.

        file path

        :param path: The path of this DefectEvents.
        :type path: str
        """
        self._path = path

    @property
    def tag(self):
        """Gets the tag of this DefectEvents.

        标签

        :return: The tag of this DefectEvents.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this DefectEvents.

        标签

        :param tag: The tag of this DefectEvents.
        :type tag: str
        """
        self._tag = tag

    @property
    def main_buggy_code(self):
        """Gets the main_buggy_code of this DefectEvents.

        main buggy code

        :return: The main_buggy_code of this DefectEvents.
        :rtype: str
        """
        return self._main_buggy_code

    @main_buggy_code.setter
    def main_buggy_code(self, main_buggy_code):
        """Sets the main_buggy_code of this DefectEvents.

        main buggy code

        :param main_buggy_code: The main_buggy_code of this DefectEvents.
        :type main_buggy_code: str
        """
        self._main_buggy_code = main_buggy_code

    @property
    def code_context(self):
        """Gets the code_context of this DefectEvents.

        code context

        :return: The code_context of this DefectEvents.
        :rtype: str
        """
        return self._code_context

    @code_context.setter
    def code_context(self, code_context):
        """Sets the code_context of this DefectEvents.

        code context

        :param code_context: The code_context of this DefectEvents.
        :type code_context: str
        """
        self._code_context = code_context

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
        if not isinstance(other, DefectEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
