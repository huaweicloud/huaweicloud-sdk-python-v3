# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiApiKeyCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_api_key': 'str',
        'alias': 'str'
    }

    attribute_map = {
        'ai_api_key': 'ai_api_key',
        'alias': 'alias'
    }

    def __init__(self, ai_api_key=None, alias=None):
        r"""AiApiKeyCreate

        The model defined in huaweicloud sdk

        :param ai_api_key: AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/&#x3D;特殊字符，长度为8~128个字符。 
        :type ai_api_key: str
        :param alias: AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。
        :type alias: str
        """
        
        

        self._ai_api_key = None
        self._alias = None
        self.discriminator = None

        if ai_api_key is not None:
            self.ai_api_key = ai_api_key
        if alias is not None:
            self.alias = alias

    @property
    def ai_api_key(self):
        r"""Gets the ai_api_key of this AiApiKeyCreate.

        AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/=特殊字符，长度为8~128个字符。 

        :return: The ai_api_key of this AiApiKeyCreate.
        :rtype: str
        """
        return self._ai_api_key

    @ai_api_key.setter
    def ai_api_key(self, ai_api_key):
        r"""Sets the ai_api_key of this AiApiKeyCreate.

        AIAPIKey值，不指定具体值时，由后台自动生成随机字符串。 支持大小写英文字母、数字，以及+-_/=特殊字符，长度为8~128个字符。 

        :param ai_api_key: The ai_api_key of this AiApiKeyCreate.
        :type ai_api_key: str
        """
        self._ai_api_key = ai_api_key

    @property
    def alias(self):
        r"""Gets the alias of this AiApiKeyCreate.

        AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。

        :return: The alias of this AiApiKeyCreate.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this AiApiKeyCreate.

        AIAPIKey的别名。支持大小写字母，数字，下划线，中划线，长度为1~100个字符。

        :param alias: The alias of this AiApiKeyCreate.
        :type alias: str
        """
        self._alias = alias

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
        if not isinstance(other, AiApiKeyCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
