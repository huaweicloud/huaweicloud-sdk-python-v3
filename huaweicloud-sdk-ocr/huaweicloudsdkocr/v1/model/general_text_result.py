# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTextResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'direction': 'float',
        'words_block_count': 'int',
        'words_block_list': 'list[GeneralTextWordsBlockList]'
    }

    attribute_map = {
        'direction': 'direction',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, direction=None, words_block_count=None, words_block_list=None):
        r"""GeneralTextResult

        The model defined in huaweicloud sdk

        :param direction: 图片朝向，仅当detect_direction为true时，该字段有效。返回图片逆时针旋转角度，值区间为[0， 359],保留四位小数。 当detect_direction为false时，该字段值为 -1。 
        :type direction: float
        :param words_block_count: 识别文字块数目。 
        :type words_block_count: int
        :param words_block_list: 识别文字块列表，输出顺序从左到右，先上后下。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.GeneralTextWordsBlockList`]
        """
        
        

        self._direction = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.direction = direction
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def direction(self):
        r"""Gets the direction of this GeneralTextResult.

        图片朝向，仅当detect_direction为true时，该字段有效。返回图片逆时针旋转角度，值区间为[0， 359],保留四位小数。 当detect_direction为false时，该字段值为 -1。 

        :return: The direction of this GeneralTextResult.
        :rtype: float
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this GeneralTextResult.

        图片朝向，仅当detect_direction为true时，该字段有效。返回图片逆时针旋转角度，值区间为[0， 359],保留四位小数。 当detect_direction为false时，该字段值为 -1。 

        :param direction: The direction of this GeneralTextResult.
        :type direction: float
        """
        self._direction = direction

    @property
    def words_block_count(self):
        r"""Gets the words_block_count of this GeneralTextResult.

        识别文字块数目。 

        :return: The words_block_count of this GeneralTextResult.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        r"""Sets the words_block_count of this GeneralTextResult.

        识别文字块数目。 

        :param words_block_count: The words_block_count of this GeneralTextResult.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        r"""Gets the words_block_list of this GeneralTextResult.

        识别文字块列表，输出顺序从左到右，先上后下。 

        :return: The words_block_list of this GeneralTextResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.GeneralTextWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        r"""Sets the words_block_list of this GeneralTextResult.

        识别文字块列表，输出顺序从左到右，先上后下。 

        :param words_block_list: The words_block_list of this GeneralTextResult.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.GeneralTextWordsBlockList`]
        """
        self._words_block_list = words_block_list

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
        if not isinstance(other, GeneralTextResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
