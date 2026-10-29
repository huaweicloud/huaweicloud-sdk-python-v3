# coding: utf-8

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
        'main': 'bool',
        'path': 'str',
        'tag': 'str',
        'main_buggy_code': 'str',
        'code_context': 'str',
        'code_context_start_line': 'int'
    }

    attribute_map = {
        'events': 'events',
        'description': 'description',
        'fix_suggestions': 'fix_suggestions',
        'line': 'line',
        'end_line': 'end_line',
        'main': 'main',
        'path': 'path',
        'tag': 'tag',
        'main_buggy_code': 'main_buggy_code',
        'code_context': 'code_context',
        'code_context_start_line': 'code_context_start_line'
    }

    def __init__(self, events=None, description=None, fix_suggestions=None, line=None, end_line=None, main=None, path=None, tag=None, main_buggy_code=None, code_context=None, code_context_start_line=None):
        r"""DefectEvents

        The model defined in huaweicloud sdk

        :param events: **参数解释：** 调用链信息。
        :type events: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        :param description: **参数解释：** 问题详细描述。 **取值范围：** 不涉及。
        :type description: str
        :param fix_suggestions: **参数解释：** 修复建议。
        :type fix_suggestions: list[str]
        :param line: **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。
        :type line: int
        :param end_line: **参数解释：** 废弃字段。 **取值范围：** 不涉及。
        :type end_line: int
        :param main: **参数解释：** 废弃字段。 **取值范围：** 不涉及。
        :type main: bool
        :param path: **参数解释：** 文件路径。 **取值范围：** 不涉及。
        :type path: str
        :param tag: **参数解释：** 废弃字段。 **取值范围：** 不涉及。
        :type tag: str
        :param main_buggy_code: **参数解释：** 问题主事件对应的代码片段内容。 **取值范围：** 不涉及。
        :type main_buggy_code: str
        :param code_context: **参数解释：** 代码上下文。 **取值范围：** 不涉及。
        :type code_context: str
        :param code_context_start_line: **参数解释：** 代码上下文起始行号。 **取值范围：** 不涉及。
        :type code_context_start_line: int
        """
        
        

        self._events = None
        self._description = None
        self._fix_suggestions = None
        self._line = None
        self._end_line = None
        self._main = None
        self._path = None
        self._tag = None
        self._main_buggy_code = None
        self._code_context = None
        self._code_context_start_line = None
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
        if code_context_start_line is not None:
            self.code_context_start_line = code_context_start_line

    @property
    def events(self):
        r"""Gets the events of this DefectEvents.

        **参数解释：** 调用链信息。

        :return: The events of this DefectEvents.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this DefectEvents.

        **参数解释：** 调用链信息。

        :param events: The events of this DefectEvents.
        :type events: list[:class:`huaweicloudsdkcodeartscheck.v2.DefectEvents`]
        """
        self._events = events

    @property
    def description(self):
        r"""Gets the description of this DefectEvents.

        **参数解释：** 问题详细描述。 **取值范围：** 不涉及。

        :return: The description of this DefectEvents.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DefectEvents.

        **参数解释：** 问题详细描述。 **取值范围：** 不涉及。

        :param description: The description of this DefectEvents.
        :type description: str
        """
        self._description = description

    @property
    def fix_suggestions(self):
        r"""Gets the fix_suggestions of this DefectEvents.

        **参数解释：** 修复建议。

        :return: The fix_suggestions of this DefectEvents.
        :rtype: list[str]
        """
        return self._fix_suggestions

    @fix_suggestions.setter
    def fix_suggestions(self, fix_suggestions):
        r"""Sets the fix_suggestions of this DefectEvents.

        **参数解释：** 修复建议。

        :param fix_suggestions: The fix_suggestions of this DefectEvents.
        :type fix_suggestions: list[str]
        """
        self._fix_suggestions = fix_suggestions

    @property
    def line(self):
        r"""Gets the line of this DefectEvents.

        **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。

        :return: The line of this DefectEvents.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this DefectEvents.

        **参数解释：** 问题所在文件行号。 **取值范围：** 不涉及。

        :param line: The line of this DefectEvents.
        :type line: int
        """
        self._line = line

    @property
    def end_line(self):
        r"""Gets the end_line of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :return: The end_line of this DefectEvents.
        :rtype: int
        """
        return self._end_line

    @end_line.setter
    def end_line(self, end_line):
        r"""Sets the end_line of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :param end_line: The end_line of this DefectEvents.
        :type end_line: int
        """
        self._end_line = end_line

    @property
    def main(self):
        r"""Gets the main of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :return: The main of this DefectEvents.
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        r"""Sets the main of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :param main: The main of this DefectEvents.
        :type main: bool
        """
        self._main = main

    @property
    def path(self):
        r"""Gets the path of this DefectEvents.

        **参数解释：** 文件路径。 **取值范围：** 不涉及。

        :return: The path of this DefectEvents.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this DefectEvents.

        **参数解释：** 文件路径。 **取值范围：** 不涉及。

        :param path: The path of this DefectEvents.
        :type path: str
        """
        self._path = path

    @property
    def tag(self):
        r"""Gets the tag of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :return: The tag of this DefectEvents.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this DefectEvents.

        **参数解释：** 废弃字段。 **取值范围：** 不涉及。

        :param tag: The tag of this DefectEvents.
        :type tag: str
        """
        self._tag = tag

    @property
    def main_buggy_code(self):
        r"""Gets the main_buggy_code of this DefectEvents.

        **参数解释：** 问题主事件对应的代码片段内容。 **取值范围：** 不涉及。

        :return: The main_buggy_code of this DefectEvents.
        :rtype: str
        """
        return self._main_buggy_code

    @main_buggy_code.setter
    def main_buggy_code(self, main_buggy_code):
        r"""Sets the main_buggy_code of this DefectEvents.

        **参数解释：** 问题主事件对应的代码片段内容。 **取值范围：** 不涉及。

        :param main_buggy_code: The main_buggy_code of this DefectEvents.
        :type main_buggy_code: str
        """
        self._main_buggy_code = main_buggy_code

    @property
    def code_context(self):
        r"""Gets the code_context of this DefectEvents.

        **参数解释：** 代码上下文。 **取值范围：** 不涉及。

        :return: The code_context of this DefectEvents.
        :rtype: str
        """
        return self._code_context

    @code_context.setter
    def code_context(self, code_context):
        r"""Sets the code_context of this DefectEvents.

        **参数解释：** 代码上下文。 **取值范围：** 不涉及。

        :param code_context: The code_context of this DefectEvents.
        :type code_context: str
        """
        self._code_context = code_context

    @property
    def code_context_start_line(self):
        r"""Gets the code_context_start_line of this DefectEvents.

        **参数解释：** 代码上下文起始行号。 **取值范围：** 不涉及。

        :return: The code_context_start_line of this DefectEvents.
        :rtype: int
        """
        return self._code_context_start_line

    @code_context_start_line.setter
    def code_context_start_line(self, code_context_start_line):
        r"""Sets the code_context_start_line of this DefectEvents.

        **参数解释：** 代码上下文起始行号。 **取值范围：** 不涉及。

        :param code_context_start_line: The code_context_start_line of this DefectEvents.
        :type code_context_start_line: int
        """
        self._code_context_start_line = code_context_start_line

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
