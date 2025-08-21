# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineContentDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_no': 'int',
        'content': 'str'
    }

    attribute_map = {
        'line_no': 'lineNO',
        'content': 'content'
    }

    def __init__(self, line_no=None, content=None):
        r"""LineContentDto

        The model defined in huaweicloud sdk

        :param line_no: **参数解释：** 文件行数
        :type line_no: int
        :param content: **参数解释：** 该行对应内容
        :type content: str
        """
        
        

        self._line_no = None
        self._content = None
        self.discriminator = None

        if line_no is not None:
            self.line_no = line_no
        if content is not None:
            self.content = content

    @property
    def line_no(self):
        r"""Gets the line_no of this LineContentDto.

        **参数解释：** 文件行数

        :return: The line_no of this LineContentDto.
        :rtype: int
        """
        return self._line_no

    @line_no.setter
    def line_no(self, line_no):
        r"""Sets the line_no of this LineContentDto.

        **参数解释：** 文件行数

        :param line_no: The line_no of this LineContentDto.
        :type line_no: int
        """
        self._line_no = line_no

    @property
    def content(self):
        r"""Gets the content of this LineContentDto.

        **参数解释：** 该行对应内容

        :return: The content of this LineContentDto.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this LineContentDto.

        **参数解释：** 该行对应内容

        :param content: The content of this LineContentDto.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, LineContentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
