# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrainingJobLogsFromAomResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_line': 'str',
        'end_line': 'str',
        'lines': 'int',
        'content': 'str'
    }

    attribute_map = {
        'start_line': 'start_line',
        'end_line': 'end_line',
        'lines': 'lines',
        'content': 'content'
    }

    def __init__(self, start_line=None, end_line=None, lines=None, content=None):
        r"""ShowTrainingJobLogsFromAomResponse

        The model defined in huaweicloud sdk

        :param start_line: **参数解释**：返回日志的起始行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type start_line: str
        :param end_line: **参数解释**：返回日志的结束行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type end_line: str
        :param lines: **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type lines: int
        :param content: **参数解释**：日志内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type content: str
        """
        
        super().__init__()

        self._start_line = None
        self._end_line = None
        self._lines = None
        self._content = None
        self.discriminator = None

        if start_line is not None:
            self.start_line = start_line
        if end_line is not None:
            self.end_line = end_line
        if lines is not None:
            self.lines = lines
        if content is not None:
            self.content = content

    @property
    def start_line(self):
        r"""Gets the start_line of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回日志的起始行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The start_line of this ShowTrainingJobLogsFromAomResponse.
        :rtype: str
        """
        return self._start_line

    @start_line.setter
    def start_line(self, start_line):
        r"""Sets the start_line of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回日志的起始行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param start_line: The start_line of this ShowTrainingJobLogsFromAomResponse.
        :type start_line: str
        """
        self._start_line = start_line

    @property
    def end_line(self):
        r"""Gets the end_line of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回日志的结束行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The end_line of this ShowTrainingJobLogsFromAomResponse.
        :rtype: str
        """
        return self._end_line

    @end_line.setter
    def end_line(self, end_line):
        r"""Sets the end_line of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回日志的结束行号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param end_line: The end_line of this ShowTrainingJobLogsFromAomResponse.
        :type end_line: str
        """
        self._end_line = end_line

    @property
    def lines(self):
        r"""Gets the lines of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The lines of this ShowTrainingJobLogsFromAomResponse.
        :rtype: int
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：返回的日志行数。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param lines: The lines of this ShowTrainingJobLogsFromAomResponse.
        :type lines: int
        """
        self._lines = lines

    @property
    def content(self):
        r"""Gets the content of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：日志内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The content of this ShowTrainingJobLogsFromAomResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowTrainingJobLogsFromAomResponse.

        **参数解释**：日志内容。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param content: The content of this ShowTrainingJobLogsFromAomResponse.
        :type content: str
        """
        self._content = content

    def to_dict(self):
        import warnings
        warnings.warn("ShowTrainingJobLogsFromAomResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTrainingJobLogsFromAomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
