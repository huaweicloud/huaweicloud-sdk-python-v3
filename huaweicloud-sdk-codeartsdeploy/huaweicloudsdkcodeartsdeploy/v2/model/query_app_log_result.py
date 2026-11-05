# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAppLogResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_more': 'bool',
        'text': 'str',
        'offset': 'str',
        'end_offset': 'str'
    }

    attribute_map = {
        'has_more': 'has_more',
        'text': 'text',
        'offset': 'offset',
        'end_offset': 'end_offset'
    }

    def __init__(self, has_more=None, text=None, offset=None, end_offset=None):
        r"""QueryAppLogResult

        The model defined in huaweicloud sdk

        :param has_more: 是否有更多日志信息
        :type has_more: bool
        :param text: 日志信息
        :type text: str
        :param offset: 日志起始偏移量
        :type offset: str
        :param end_offset: 日志末位偏移量，与offset参数配合使用
        :type end_offset: str
        """
        
        

        self._has_more = None
        self._text = None
        self._offset = None
        self._end_offset = None
        self.discriminator = None

        if has_more is not None:
            self.has_more = has_more
        if text is not None:
            self.text = text
        if offset is not None:
            self.offset = offset
        if end_offset is not None:
            self.end_offset = end_offset

    @property
    def has_more(self):
        r"""Gets the has_more of this QueryAppLogResult.

        是否有更多日志信息

        :return: The has_more of this QueryAppLogResult.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        r"""Sets the has_more of this QueryAppLogResult.

        是否有更多日志信息

        :param has_more: The has_more of this QueryAppLogResult.
        :type has_more: bool
        """
        self._has_more = has_more

    @property
    def text(self):
        r"""Gets the text of this QueryAppLogResult.

        日志信息

        :return: The text of this QueryAppLogResult.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this QueryAppLogResult.

        日志信息

        :param text: The text of this QueryAppLogResult.
        :type text: str
        """
        self._text = text

    @property
    def offset(self):
        r"""Gets the offset of this QueryAppLogResult.

        日志起始偏移量

        :return: The offset of this QueryAppLogResult.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryAppLogResult.

        日志起始偏移量

        :param offset: The offset of this QueryAppLogResult.
        :type offset: str
        """
        self._offset = offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this QueryAppLogResult.

        日志末位偏移量，与offset参数配合使用

        :return: The end_offset of this QueryAppLogResult.
        :rtype: str
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this QueryAppLogResult.

        日志末位偏移量，与offset参数配合使用

        :param end_offset: The end_offset of this QueryAppLogResult.
        :type end_offset: str
        """
        self._end_offset = end_offset

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
        if not isinstance(other, QueryAppLogResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
