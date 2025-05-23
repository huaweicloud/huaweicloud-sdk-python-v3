# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SegmentResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segment': 'str',
        'glossary_name': 'str',
        'position': 'list[int]'
    }

    attribute_map = {
        'segment': 'segment',
        'glossary_name': 'glossary_name',
        'position': 'position'
    }

    def __init__(self, segment=None, glossary_name=None, position=None):
        r"""SegmentResult

        The model defined in huaweicloud sdk

        :param segment: 命中的风险片段。
        :type segment: str
        :param glossary_name: 命中的自定义词库名称。  命中自定义词库时，才会返回当前字段。
        :type glossary_name: str
        :param position: 命中的风险片段在文本中的位置，起始位置从0开始
        :type position: list[int]
        """
        
        

        self._segment = None
        self._glossary_name = None
        self._position = None
        self.discriminator = None

        if segment is not None:
            self.segment = segment
        if glossary_name is not None:
            self.glossary_name = glossary_name
        if position is not None:
            self.position = position

    @property
    def segment(self):
        r"""Gets the segment of this SegmentResult.

        命中的风险片段。

        :return: The segment of this SegmentResult.
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        r"""Sets the segment of this SegmentResult.

        命中的风险片段。

        :param segment: The segment of this SegmentResult.
        :type segment: str
        """
        self._segment = segment

    @property
    def glossary_name(self):
        r"""Gets the glossary_name of this SegmentResult.

        命中的自定义词库名称。  命中自定义词库时，才会返回当前字段。

        :return: The glossary_name of this SegmentResult.
        :rtype: str
        """
        return self._glossary_name

    @glossary_name.setter
    def glossary_name(self, glossary_name):
        r"""Sets the glossary_name of this SegmentResult.

        命中的自定义词库名称。  命中自定义词库时，才会返回当前字段。

        :param glossary_name: The glossary_name of this SegmentResult.
        :type glossary_name: str
        """
        self._glossary_name = glossary_name

    @property
    def position(self):
        r"""Gets the position of this SegmentResult.

        命中的风险片段在文本中的位置，起始位置从0开始

        :return: The position of this SegmentResult.
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this SegmentResult.

        命中的风险片段在文本中的位置，起始位置从0开始

        :param position: The position of this SegmentResult.
        :type position: list[int]
        """
        self._position = position

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
        if not isinstance(other, SegmentResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
