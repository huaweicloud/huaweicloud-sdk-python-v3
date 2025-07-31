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
        'value': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'value': 'value',
        'group_id': 'group_id'
    }

    def __init__(self, type=None, key=None, value=None, group_id=None):
        r"""SaveTtscVocabularyConfigsRequestBody

        The model defined in huaweicloud sdk

        :param type: 支持配置的自定义读法类型。当前读法类型会映射为SSML标签，详见[文本驱动SSML定义](metastudio_02_0038.xml)。  包含如下选项： * CHINESE_G2P：拼音 * PHONETIC_SYMBOL：音标 * CONTINUUM：连读 * ALIAS：别名 * SAY_AS：数字/英文的读法。不同value值有不同的读法，详情如下所示。   数字的读法包括：   - date：读日期   - number：读数字   - figure：读数值   - telephone：读电话    英文的读法包括：   - spell：读字母   - english：读单词
        :type type: str
        :param key: 原始词。
        :type key: str
        :param value: 自定义读法。其中，音标的读法请参考[词典](https://www.youdao.com/)。
        :type value: str
        :param group_id: 分组id
        :type group_id: str
        """
        
        

        self._type = None
        self._key = None
        self._value = None
        self._group_id = None
        self.discriminator = None

        self.type = type
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if group_id is not None:
            self.group_id = group_id

    @property
    def type(self):
        r"""Gets the type of this SaveTtscVocabularyConfigsRequestBody.

        支持配置的自定义读法类型。当前读法类型会映射为SSML标签，详见[文本驱动SSML定义](metastudio_02_0038.xml)。  包含如下选项： * CHINESE_G2P：拼音 * PHONETIC_SYMBOL：音标 * CONTINUUM：连读 * ALIAS：别名 * SAY_AS：数字/英文的读法。不同value值有不同的读法，详情如下所示。   数字的读法包括：   - date：读日期   - number：读数字   - figure：读数值   - telephone：读电话    英文的读法包括：   - spell：读字母   - english：读单词

        :return: The type of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SaveTtscVocabularyConfigsRequestBody.

        支持配置的自定义读法类型。当前读法类型会映射为SSML标签，详见[文本驱动SSML定义](metastudio_02_0038.xml)。  包含如下选项： * CHINESE_G2P：拼音 * PHONETIC_SYMBOL：音标 * CONTINUUM：连读 * ALIAS：别名 * SAY_AS：数字/英文的读法。不同value值有不同的读法，详情如下所示。   数字的读法包括：   - date：读日期   - number：读数字   - figure：读数值   - telephone：读电话    英文的读法包括：   - spell：读字母   - english：读单词

        :param type: The type of this SaveTtscVocabularyConfigsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this SaveTtscVocabularyConfigsRequestBody.

        原始词。

        :return: The key of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this SaveTtscVocabularyConfigsRequestBody.

        原始词。

        :param key: The key of this SaveTtscVocabularyConfigsRequestBody.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this SaveTtscVocabularyConfigsRequestBody.

        自定义读法。其中，音标的读法请参考[词典](https://www.youdao.com/)。

        :return: The value of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SaveTtscVocabularyConfigsRequestBody.

        自定义读法。其中，音标的读法请参考[词典](https://www.youdao.com/)。

        :param value: The value of this SaveTtscVocabularyConfigsRequestBody.
        :type value: str
        """
        self._value = value

    @property
    def group_id(self):
        r"""Gets the group_id of this SaveTtscVocabularyConfigsRequestBody.

        分组id

        :return: The group_id of this SaveTtscVocabularyConfigsRequestBody.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this SaveTtscVocabularyConfigsRequestBody.

        分组id

        :param group_id: The group_id of this SaveTtscVocabularyConfigsRequestBody.
        :type group_id: str
        """
        self._group_id = group_id

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
