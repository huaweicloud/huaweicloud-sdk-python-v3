# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DictionaryDelete:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dict_id': 'str',
        'dict_key': 'str',
        'language': 'str'
    }

    attribute_map = {
        'dict_id': 'dict_id',
        'dict_key': 'dict_key',
        'language': 'language'
    }

    def __init__(self, dict_id=None, dict_key=None, language=None):
        r"""DictionaryDelete

        The model defined in huaweicloud sdk

        :param dict_id: 字典id
        :type dict_id: str
        :param dict_key: 字典key
        :type dict_key: str
        :param language: 用户当前语言环境
        :type language: str
        """
        
        

        self._dict_id = None
        self._dict_key = None
        self._language = None
        self.discriminator = None

        self.dict_id = dict_id
        self.dict_key = dict_key
        self.language = language

    @property
    def dict_id(self):
        r"""Gets the dict_id of this DictionaryDelete.

        字典id

        :return: The dict_id of this DictionaryDelete.
        :rtype: str
        """
        return self._dict_id

    @dict_id.setter
    def dict_id(self, dict_id):
        r"""Sets the dict_id of this DictionaryDelete.

        字典id

        :param dict_id: The dict_id of this DictionaryDelete.
        :type dict_id: str
        """
        self._dict_id = dict_id

    @property
    def dict_key(self):
        r"""Gets the dict_key of this DictionaryDelete.

        字典key

        :return: The dict_key of this DictionaryDelete.
        :rtype: str
        """
        return self._dict_key

    @dict_key.setter
    def dict_key(self, dict_key):
        r"""Sets the dict_key of this DictionaryDelete.

        字典key

        :param dict_key: The dict_key of this DictionaryDelete.
        :type dict_key: str
        """
        self._dict_key = dict_key

    @property
    def language(self):
        r"""Gets the language of this DictionaryDelete.

        用户当前语言环境

        :return: The language of this DictionaryDelete.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this DictionaryDelete.

        用户当前语言环境

        :param language: The language of this DictionaryDelete.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, DictionaryDelete):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
