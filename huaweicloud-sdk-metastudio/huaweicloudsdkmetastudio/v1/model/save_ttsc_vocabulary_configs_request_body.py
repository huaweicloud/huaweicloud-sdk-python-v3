# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaveTtscVocabularyConfigsRequestBody:

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
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, type=None, key=None, value=None):
        """SaveTtscVocabularyConfigsRequestBody

        The model defined in huaweicloud sdk

        :param type: TTSS支持配置的词表类型 * CHINESE_G2P:拼音 * PHONETIC_SYMBOL:音标 * CONTINUUM:连读 * ALIAS:别名 * SAY_AS:数字英文读法
        :type type: str
        :param key: 映射键
        :type key: str
        :param value: 映射值
        :type value: str
        """
        
        

        self._type = None
        self._key = None
        self._value = None
        self.discriminator = None

        self.type = type
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def type(self):
        """Gets the type of this SaveTtscVocabularyConfigsRequestBody.

        TTSS支持配置的词表类型 * CHINESE_G2P:拼音 * PHONETIC_SYMBOL:音标 * CONTINUUM:连读 * ALIAS:别名 * SAY_AS:数字英文读法

        :return: The type of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SaveTtscVocabularyConfigsRequestBody.

        TTSS支持配置的词表类型 * CHINESE_G2P:拼音 * PHONETIC_SYMBOL:音标 * CONTINUUM:连读 * ALIAS:别名 * SAY_AS:数字英文读法

        :param type: The type of this SaveTtscVocabularyConfigsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        """Gets the key of this SaveTtscVocabularyConfigsRequestBody.

        映射键

        :return: The key of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SaveTtscVocabularyConfigsRequestBody.

        映射键

        :param key: The key of this SaveTtscVocabularyConfigsRequestBody.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this SaveTtscVocabularyConfigsRequestBody.

        映射值

        :return: The value of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SaveTtscVocabularyConfigsRequestBody.

        映射值

        :param value: The value of this SaveTtscVocabularyConfigsRequestBody.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, SaveTtscVocabularyConfigsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
