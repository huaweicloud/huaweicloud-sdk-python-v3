# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartDocumentRecognizerKVBlock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'value': 'str',
        'words_block_count': 'int',
        'words_block_list': 'list[SmartDocumentRecognizerKVWordsBlock]'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'words_block_count': 'words_block_count',
        'words_block_list': 'words_block_list'
    }

    def __init__(self, key=None, value=None, words_block_count=None, words_block_list=None):
        """SmartDocumentRecognizerKVBlock

        The model defined in huaweicloud sdk

        :param key: key-value对（键值对）中的key，例如“姓名：小明”中的“姓名” 
        :type key: str
        :param value: key-value对（键值对）中的value，例如“姓名：小明”中的“小明” 
        :type value: str
        :param words_block_count: 该键值对中所包含的文本框数量。   
        :type words_block_count: int
        :param words_block_list: 文本框识别结果列表。 
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVWordsBlock`]
        """
        
        

        self._key = None
        self._value = None
        self._words_block_count = None
        self._words_block_list = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if words_block_count is not None:
            self.words_block_count = words_block_count
        if words_block_list is not None:
            self.words_block_list = words_block_list

    @property
    def key(self):
        """Gets the key of this SmartDocumentRecognizerKVBlock.

        key-value对（键值对）中的key，例如“姓名：小明”中的“姓名” 

        :return: The key of this SmartDocumentRecognizerKVBlock.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SmartDocumentRecognizerKVBlock.

        key-value对（键值对）中的key，例如“姓名：小明”中的“姓名” 

        :param key: The key of this SmartDocumentRecognizerKVBlock.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this SmartDocumentRecognizerKVBlock.

        key-value对（键值对）中的value，例如“姓名：小明”中的“小明” 

        :return: The value of this SmartDocumentRecognizerKVBlock.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SmartDocumentRecognizerKVBlock.

        key-value对（键值对）中的value，例如“姓名：小明”中的“小明” 

        :param value: The value of this SmartDocumentRecognizerKVBlock.
        :type value: str
        """
        self._value = value

    @property
    def words_block_count(self):
        """Gets the words_block_count of this SmartDocumentRecognizerKVBlock.

        该键值对中所包含的文本框数量。   

        :return: The words_block_count of this SmartDocumentRecognizerKVBlock.
        :rtype: int
        """
        return self._words_block_count

    @words_block_count.setter
    def words_block_count(self, words_block_count):
        """Sets the words_block_count of this SmartDocumentRecognizerKVBlock.

        该键值对中所包含的文本框数量。   

        :param words_block_count: The words_block_count of this SmartDocumentRecognizerKVBlock.
        :type words_block_count: int
        """
        self._words_block_count = words_block_count

    @property
    def words_block_list(self):
        """Gets the words_block_list of this SmartDocumentRecognizerKVBlock.

        文本框识别结果列表。 

        :return: The words_block_list of this SmartDocumentRecognizerKVBlock.
        :rtype: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVWordsBlock`]
        """
        return self._words_block_list

    @words_block_list.setter
    def words_block_list(self, words_block_list):
        """Sets the words_block_list of this SmartDocumentRecognizerKVBlock.

        文本框识别结果列表。 

        :param words_block_list: The words_block_list of this SmartDocumentRecognizerKVBlock.
        :type words_block_list: list[:class:`huaweicloudsdkocr.v1.SmartDocumentRecognizerKVWordsBlock`]
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
        if not isinstance(other, SmartDocumentRecognizerKVBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
