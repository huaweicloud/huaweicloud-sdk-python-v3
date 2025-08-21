# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConflictSectionLineDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_code': 'str',
        'type': 'str',
        'old_line': 'int',
        'new_line': 'int',
        'text': 'str',
        'meta_data': 'ConflictSectionLineMetaDataDto',
        'rich_text': 'str',
        'can_receive_suggestion': 'bool'
    }

    attribute_map = {
        'line_code': 'line_code',
        'type': 'type',
        'old_line': 'old_line',
        'new_line': 'new_line',
        'text': 'text',
        'meta_data': 'meta_data',
        'rich_text': 'rich_text',
        'can_receive_suggestion': 'can_receive_suggestion'
    }

    def __init__(self, line_code=None, type=None, old_line=None, new_line=None, text=None, meta_data=None, rich_text=None, can_receive_suggestion=None):
        r"""ConflictSectionLineDto

        The model defined in huaweicloud sdk

        :param line_code: 行
        :type line_code: str
        :param type: 类型
        :type type: str
        :param old_line: 旧行
        :type old_line: int
        :param new_line: 新行
        :type new_line: int
        :param text: 文本
        :type text: str
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkcodehub.v4.ConflictSectionLineMetaDataDto`
        :param rich_text: 富文本
        :type rich_text: str
        :param can_receive_suggestion: 可接受建议
        :type can_receive_suggestion: bool
        """
        
        

        self._line_code = None
        self._type = None
        self._old_line = None
        self._new_line = None
        self._text = None
        self._meta_data = None
        self._rich_text = None
        self._can_receive_suggestion = None
        self.discriminator = None

        if line_code is not None:
            self.line_code = line_code
        if type is not None:
            self.type = type
        if old_line is not None:
            self.old_line = old_line
        if new_line is not None:
            self.new_line = new_line
        if text is not None:
            self.text = text
        if meta_data is not None:
            self.meta_data = meta_data
        if rich_text is not None:
            self.rich_text = rich_text
        if can_receive_suggestion is not None:
            self.can_receive_suggestion = can_receive_suggestion

    @property
    def line_code(self):
        r"""Gets the line_code of this ConflictSectionLineDto.

        行

        :return: The line_code of this ConflictSectionLineDto.
        :rtype: str
        """
        return self._line_code

    @line_code.setter
    def line_code(self, line_code):
        r"""Sets the line_code of this ConflictSectionLineDto.

        行

        :param line_code: The line_code of this ConflictSectionLineDto.
        :type line_code: str
        """
        self._line_code = line_code

    @property
    def type(self):
        r"""Gets the type of this ConflictSectionLineDto.

        类型

        :return: The type of this ConflictSectionLineDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConflictSectionLineDto.

        类型

        :param type: The type of this ConflictSectionLineDto.
        :type type: str
        """
        self._type = type

    @property
    def old_line(self):
        r"""Gets the old_line of this ConflictSectionLineDto.

        旧行

        :return: The old_line of this ConflictSectionLineDto.
        :rtype: int
        """
        return self._old_line

    @old_line.setter
    def old_line(self, old_line):
        r"""Sets the old_line of this ConflictSectionLineDto.

        旧行

        :param old_line: The old_line of this ConflictSectionLineDto.
        :type old_line: int
        """
        self._old_line = old_line

    @property
    def new_line(self):
        r"""Gets the new_line of this ConflictSectionLineDto.

        新行

        :return: The new_line of this ConflictSectionLineDto.
        :rtype: int
        """
        return self._new_line

    @new_line.setter
    def new_line(self, new_line):
        r"""Sets the new_line of this ConflictSectionLineDto.

        新行

        :param new_line: The new_line of this ConflictSectionLineDto.
        :type new_line: int
        """
        self._new_line = new_line

    @property
    def text(self):
        r"""Gets the text of this ConflictSectionLineDto.

        文本

        :return: The text of this ConflictSectionLineDto.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this ConflictSectionLineDto.

        文本

        :param text: The text of this ConflictSectionLineDto.
        :type text: str
        """
        self._text = text

    @property
    def meta_data(self):
        r"""Gets the meta_data of this ConflictSectionLineDto.

        :return: The meta_data of this ConflictSectionLineDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ConflictSectionLineMetaDataDto`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this ConflictSectionLineDto.

        :param meta_data: The meta_data of this ConflictSectionLineDto.
        :type meta_data: :class:`huaweicloudsdkcodehub.v4.ConflictSectionLineMetaDataDto`
        """
        self._meta_data = meta_data

    @property
    def rich_text(self):
        r"""Gets the rich_text of this ConflictSectionLineDto.

        富文本

        :return: The rich_text of this ConflictSectionLineDto.
        :rtype: str
        """
        return self._rich_text

    @rich_text.setter
    def rich_text(self, rich_text):
        r"""Sets the rich_text of this ConflictSectionLineDto.

        富文本

        :param rich_text: The rich_text of this ConflictSectionLineDto.
        :type rich_text: str
        """
        self._rich_text = rich_text

    @property
    def can_receive_suggestion(self):
        r"""Gets the can_receive_suggestion of this ConflictSectionLineDto.

        可接受建议

        :return: The can_receive_suggestion of this ConflictSectionLineDto.
        :rtype: bool
        """
        return self._can_receive_suggestion

    @can_receive_suggestion.setter
    def can_receive_suggestion(self, can_receive_suggestion):
        r"""Sets the can_receive_suggestion of this ConflictSectionLineDto.

        可接受建议

        :param can_receive_suggestion: The can_receive_suggestion of this ConflictSectionLineDto.
        :type can_receive_suggestion: bool
        """
        self._can_receive_suggestion = can_receive_suggestion

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
        if not isinstance(other, ConflictSectionLineDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
