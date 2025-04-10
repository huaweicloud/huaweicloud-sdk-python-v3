# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DefectFragmentV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_num': 'str',
        'line_content': 'str',
        'start_offset': 'int',
        'end_offset': 'int'
    }

    attribute_map = {
        'line_num': 'line_num',
        'line_content': 'line_content',
        'start_offset': 'start_offset',
        'end_offset': 'end_offset'
    }

    def __init__(self, line_num=None, line_content=None, start_offset=None, end_offset=None):
        r"""DefectFragmentV2

        The model defined in huaweicloud sdk

        :param line_num: 行号
        :type line_num: str
        :param line_content: 该行代码内容
        :type line_content: str
        :param start_offset: 缺陷开始列号
        :type start_offset: int
        :param end_offset: 缺陷结束列号
        :type end_offset: int
        """
        
        

        self._line_num = None
        self._line_content = None
        self._start_offset = None
        self._end_offset = None
        self.discriminator = None

        if line_num is not None:
            self.line_num = line_num
        if line_content is not None:
            self.line_content = line_content
        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset

    @property
    def line_num(self):
        r"""Gets the line_num of this DefectFragmentV2.

        行号

        :return: The line_num of this DefectFragmentV2.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this DefectFragmentV2.

        行号

        :param line_num: The line_num of this DefectFragmentV2.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def line_content(self):
        r"""Gets the line_content of this DefectFragmentV2.

        该行代码内容

        :return: The line_content of this DefectFragmentV2.
        :rtype: str
        """
        return self._line_content

    @line_content.setter
    def line_content(self, line_content):
        r"""Sets the line_content of this DefectFragmentV2.

        该行代码内容

        :param line_content: The line_content of this DefectFragmentV2.
        :type line_content: str
        """
        self._line_content = line_content

    @property
    def start_offset(self):
        r"""Gets the start_offset of this DefectFragmentV2.

        缺陷开始列号

        :return: The start_offset of this DefectFragmentV2.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        r"""Sets the start_offset of this DefectFragmentV2.

        缺陷开始列号

        :param start_offset: The start_offset of this DefectFragmentV2.
        :type start_offset: int
        """
        self._start_offset = start_offset

    @property
    def end_offset(self):
        r"""Gets the end_offset of this DefectFragmentV2.

        缺陷结束列号

        :return: The end_offset of this DefectFragmentV2.
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        r"""Sets the end_offset of this DefectFragmentV2.

        缺陷结束列号

        :param end_offset: The end_offset of this DefectFragmentV2.
        :type end_offset: int
        """
        self._end_offset = end_offset

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
        if not isinstance(other, DefectFragmentV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
