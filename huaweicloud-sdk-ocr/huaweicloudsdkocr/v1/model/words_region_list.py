# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WordsRegionList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'words_block_count': 'int',
        'words_block_list': 'list[GeneralTableWordsBlockList]'
    }

    attribute_map = {
        'type': 'type',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, type=None, words_block_count=None, words_block_list=None):
        """WordsRegionList

        The model defined in huaweicloud sdk

        :param type: 文字识别区域类型。 - text：文本识别区域; - table：表格识别区域。 
        :type type: str
        :param words_block_count: 子区域识别文字块数目。 
        :type words_block_count: int
        :param words_block_list: 子区域识别文字块列表，输出顺序从左到右，先上后下。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.GeneralTableWordsBlockList`]
        """
        
        

        self._type = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        self.type = type
        self.words_block_count = words_block_count
        self.words_block_list = words_block_list

    @property
    def type(self):
        """Gets the type of this WordsRegionList.

        文字识别区域类型。 - text：文本识别区域; - table：表格识别区域。 

        :return: The type of this WordsRegionList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WordsRegionList.

        文字识别区域类型。 - text：文本识别区域; - table：表格识别区域。 

        :param type: The type of this WordsRegionList.
        :type type: str
        """
        self._type = type

    @property
    def words_block_count(self):
        """Gets the words_block_count of this WordsRegionList.

        子区域识别文字块数目。 

        :return: The words_block_count of this WordsRegionList.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this WordsRegionList.

        子区域识别文字块数目。 

        :param words_block_count: The words_block_count of this WordsRegionList.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this WordsRegionList.

        子区域识别文字块列表，输出顺序从左到右，先上后下。 

        :return: The words_block_list of this WordsRegionList.
        :rtype: list[:class:`huaweicloudsdkocr.v1.GeneralTableWordsBlockList`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this WordsRegionList.

        子区域识别文字块列表，输出顺序从左到右，先上后下。 

        :param words_block_list: The words_block_list of this WordsRegionList.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.GeneralTableWordsBlockList`]
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
        if not isinstance(other, WordsRegionList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
