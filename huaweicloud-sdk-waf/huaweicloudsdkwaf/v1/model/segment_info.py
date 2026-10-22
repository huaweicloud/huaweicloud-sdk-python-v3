# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SegmentInfo:

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
        'category': 'str',
        'position': 'list[int]',
        'lexicon_id': 'str',
        'lexicon_type': 'int'
    }

    attribute_map = {
        'segment': 'segment',
        'category': 'category',
        'position': 'position',
        'lexicon_id': 'lexicon_id',
        'lexicon_type': 'lexicon_type'
    }

    def __init__(self, segment=None, category=None, position=None, lexicon_id=None, lexicon_type=None):
        r"""SegmentInfo

        The model defined in huaweicloud sdk

        :param segment: 命中规则的具体片段
        :type segment: str
        :param category: 命中的规则类别
        :type category: str
        :param position: 敏感词所在位置
        :type position: list[int]
        :param lexicon_id: 命中自定义词库的ID
        :type lexicon_id: str
        :param lexicon_type: 自定义词库是豁免还是违规
        :type lexicon_type: int
        """
        
        

        self._segment = None
        self._category = None
        self._position = None
        self._lexicon_id = None
        self._lexicon_type = None
        self.discriminator = None

        if segment is not None:
            self.segment = segment
        if category is not None:
            self.category = category
        if position is not None:
            self.position = position
        if lexicon_id is not None:
            self.lexicon_id = lexicon_id
        if lexicon_type is not None:
            self.lexicon_type = lexicon_type

    @property
    def segment(self):
        r"""Gets the segment of this SegmentInfo.

        命中规则的具体片段

        :return: The segment of this SegmentInfo.
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        r"""Sets the segment of this SegmentInfo.

        命中规则的具体片段

        :param segment: The segment of this SegmentInfo.
        :type segment: str
        """
        self._segment = segment

    @property
    def category(self):
        r"""Gets the category of this SegmentInfo.

        命中的规则类别

        :return: The category of this SegmentInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SegmentInfo.

        命中的规则类别

        :param category: The category of this SegmentInfo.
        :type category: str
        """
        self._category = category

    @property
    def position(self):
        r"""Gets the position of this SegmentInfo.

        敏感词所在位置

        :return: The position of this SegmentInfo.
        :rtype: list[int]
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this SegmentInfo.

        敏感词所在位置

        :param position: The position of this SegmentInfo.
        :type position: list[int]
        """
        self._position = position

    @property
    def lexicon_id(self):
        r"""Gets the lexicon_id of this SegmentInfo.

        命中自定义词库的ID

        :return: The lexicon_id of this SegmentInfo.
        :rtype: str
        """
        return self._lexicon_id

    @lexicon_id.setter
    def lexicon_id(self, lexicon_id):
        r"""Sets the lexicon_id of this SegmentInfo.

        命中自定义词库的ID

        :param lexicon_id: The lexicon_id of this SegmentInfo.
        :type lexicon_id: str
        """
        self._lexicon_id = lexicon_id

    @property
    def lexicon_type(self):
        r"""Gets the lexicon_type of this SegmentInfo.

        自定义词库是豁免还是违规

        :return: The lexicon_type of this SegmentInfo.
        :rtype: int
        """
        return self._lexicon_type

    @lexicon_type.setter
    def lexicon_type(self, lexicon_type):
        r"""Sets the lexicon_type of this SegmentInfo.

        自定义词库是豁免还是违规

        :param lexicon_type: The lexicon_type of this SegmentInfo.
        :type lexicon_type: int
        """
        self._lexicon_type = lexicon_type

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
        if not isinstance(other, SegmentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
