# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagEntity:

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
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, key=None, value=None):
        """TagEntity

        The model defined in huaweicloud sdk

        :param key: 标签键。  - 不能为空。  - 对于同一个实例，Key值唯一。  [- 长度不超过36个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为1~128个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“&#x3D;”，“*”，“&lt;”，“&gt;”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : &#x3D; + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。
        :type key: str
        :param value: 标签值。  [- 不能为空。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度不超过43个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为0~255个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“&#x3D;”，“*”，“&lt;”，“&gt;”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : &#x3D; + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。
        :type value: str
        """
        
        

        self._key = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def key(self):
        """Gets the key of this TagEntity.

        标签键。  - 不能为空。  - 对于同一个实例，Key值唯一。  [- 长度不超过36个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为1~128个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“=”，“*”，“<”，“>”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : = + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。

        :return: The key of this TagEntity.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this TagEntity.

        标签键。  - 不能为空。  - 对于同一个实例，Key值唯一。  [- 长度不超过36个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为1~128个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“=”，“*”，“<”，“>”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : = + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。

        :param key: The key of this TagEntity.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this TagEntity.

        标签值。  [- 不能为空。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度不超过43个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为0~255个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“=”，“*”，“<”，“>”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : = + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。

        :return: The value of this TagEntity.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TagEntity.

        标签值。  [- 不能为空。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度不超过43个字符。](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 长度为0~255个字符（中文也可以输入128个字符）。](tag:hws,hws_hk)  [- 不能包含“=”，“*”，“<”，“>”，“\\”，“,”，“|”，“/”](tag:cmcc,ctc,g42,hk_g42,hk_tm,hws_eu,hws_ocb,ocb,tm,otc)  [- 由任意语种字母、数字、空格和字符组成，字符仅支持_ . : = + - @](tag:hws,hws_hk)  - 首尾字符不能为空格。

        :param value: The value of this TagEntity.
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
        if not isinstance(other, TagEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
