# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectOpt:

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
        'enable': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'enable': 'enable'
    }

    def __init__(self, type=None, enable=None):
        r"""DetectOpt

        The model defined in huaweicloud sdk

        :param type: 检测类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库),supported_language(语言检测，默认开), pii(敏感词检测), abuse(算力滥用检测)
        :type type: str
        :param enable: 是否启用该检测类型
        :type enable: bool
        """
        
        

        self._type = None
        self._enable = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if enable is not None:
            self.enable = enable

    @property
    def type(self):
        r"""Gets the type of this DetectOpt.

        检测类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库),supported_language(语言检测，默认开), pii(敏感词检测), abuse(算力滥用检测)

        :return: The type of this DetectOpt.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DetectOpt.

        检测类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库),supported_language(语言检测，默认开), pii(敏感词检测), abuse(算力滥用检测)

        :param type: The type of this DetectOpt.
        :type type: str
        """
        self._type = type

    @property
    def enable(self):
        r"""Gets the enable of this DetectOpt.

        是否启用该检测类型

        :return: The enable of this DetectOpt.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this DetectOpt.

        是否启用该检测类型

        :param enable: The enable of this DetectOpt.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, DetectOpt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
